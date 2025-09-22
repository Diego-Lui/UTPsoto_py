#Limpieza del CSV
import csv
from datetime import datetime
from pathlib import Path #importo el comando path (busca el lugar del codigo)
from statistics import mean

#Funcion para calcular la temperatura a partir del voltaje
def temperatura_cal(val):
    temp = 18*val - 64
    return  f"{temp:.2f}"

#crear mis variables de rutas para ingreso de archivo y salida de archivo
ROOT=Path(__file__).resolve().parents[1]#busca el lugar donde esta guardado el codigo
IN_FILE=ROOT/"DATA"/"RAW"/"datos_sucios_250_v2.csv" #ruta de ingreso
OUT_FILE=ROOT/"DATA"/"PROCESSED"/"Temperaturas_Procesado.csv" #ruta de salida

with open(IN_FILE,'r',encoding="utf-8", newline="") as fin, \
    open(OUT_FILE, "w", encoding="utf-8", newline="") as fout:
    reader=csv.DictReader(fin,delimiter=';')
    writer=csv.DictWriter(fout,fieldnames=["Timestamp","Voltaje","Temp_C","Alertas"])
    writer.writeheader()
#leer linea por lineal y seleccionar en crudo raw 
    total = kept = 0
    bad_ts = bad_val = 0
    voltajes=[]
    temperaturas = []
    for row in reader:
        total+=1
        ts_raw  = (row.get("timestamp") or "").strip() #toma todos los valores de la columna timestamp
        val_raw = (row.get("value") or "").strip() #toma todos los valores de la columna value
#limpiar datos
        val_raw = val_raw.replace(",", ".")
        val_low = val_raw.lower() #empezar a eliminar valores no existentes
        if val_low in {"", "na", "n/a", "nan", "null", "none", "error"}:
            bad_ts += 1
            continue #salta el comando
        try:
            val = float(val_raw)
        except ValueError:
            bad_ts += 1
            continue  # saltar fila si no es número
#limpieza de datos de tiempo 
        ts_clean = None
        for fmt in ("%Y-%m-%dT%H:%M:%S", "%d/%m/%Y %H:%M:%S"):
            try:
                dt = datetime.strptime(ts_raw, fmt)
                ts_clean = dt.strftime("%Y-%m-%dT%H:%M:%S")
                break
            except ValueError:
                pass
#milisegundo (opcional)
        if ts_clean is None and "T" in ts_raw and len(ts_raw) >= 19:
            try:
                dt = datetime.strptime(ts_raw[:19], "%Y-%m-%dT%H:%M:%S")
                ts_clean = dt.strftime("%Y-%m-%dT%H:%M:%S")
            except ValueError:
                ts_clean = None

        if ts_clean is None:
            bad_ts += 1
            continue  # saltar fila si no pudimos interpretar la fecha
#calcular temperatura
        temp_c = float(temperatura_cal(val))
#sistema de control de temperatura - si temp_c > a 40 Cº entonces lanza una alerta
        if temp_c > 40:
            control = "CUIDADO"
        else:
            control = "OK"
        voltajes.append(val) 
        temperaturas.append(temp_c)  
#grabar datos en writer
        writer.writerow({"Timestamp": ts_clean, "Voltaje": f"{val:.2f}", "Temp_C":f"{temp_c:.2f}","Alertas":control})
        kept += 1 #sume 1 kept, en nuestro caso cambia de fila
        
#KPIs
n=len(voltajes)
if n==0:
    kips={
        "Filas_totales": total,
        "Filas_validas": kept,
        "Descartes_Timestamp": bad_ts,
        "Descartes_valor": bad_val,
        "n": 0,
        "temp_min": None,
        "temp_max": None,
        "temp_prom":None,
        "Alertas": 0
        } # por facilidad usaremos diccionarios
else:
    alertas=sum(t > 40 for t in temperaturas) #estructuras repetitivas simples
    kips={
        "Filas_totales": total,
        "Filas_validas": kept,
        "Descartes_Timestamp": bad_ts,
        "Descartes_valor": bad_val,
        "n": n,
        "temp_min": f"{min(temperaturas):.2f}",
        "temp_max": f"{max(temperaturas):.2f}",
        "temp_prom":f"{mean(temperaturas):.2f}",
        "alertas": alertas,
    }

#salida de pantalla y verificacion de KPIS
print(kips)
