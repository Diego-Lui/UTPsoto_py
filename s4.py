from pathlib import Path  #importo el comando path (busca el lugar del codigo)

ROOT = Path(__file__).resolve().parents[0]  # sube desde src/ a la raíz del proyecto
TXT = ROOT / "archivo" / "mediciones_basico.txt"

valores = []
with open(TXT, 'r', encoding="utf-8") as f:
    for linea in f:
        s=linea.strip()
        if not s or s.startswith('#'):
            continue
        if not s or s .startswith('!'):
            continue
        s =  s.replace(',', '.') #reemplaza las comas por puntos
        try:
            valores.append(float(s))
        except ValueError:
            pass

Vmayor=[]
Vmenor=[]
for v in valores:
    if v > 5:
        Vmayor.append(v)
    else:
        Vmenor.append(v)
print(Vmayor)
print(Vmenor)

print(len(Vmayor))
print(len(Vmenor))