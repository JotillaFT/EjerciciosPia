import random
from itertools import combinations

radios = {
"kone": set({"ID", "NV", "UT"}),
"ktwo": set({"WA", "ID", "MT"}),
"kthree": set({"OR", "NV", "CA"}),
"kfour": set({"NV", "UT"}),
"kfive": set({"CA", "AZ"}),
"ksix": set({"NM", "TX", "OK"}),
"kseven": set({"OK", "KS", "CO"}),
"keight": set({"KS", "CO", "NE"}),
"knine": set({"NE", "SD", "WY"}),
"kten": set({"ND", "IA"}),
"keleven": set({"MN", "MO", "AR"}),
"ktwelve": set({"LA"}),
"kthirteen": set({"MO", "AR"}),
}
'''
def busqueda_global(radios):
    max_estados = -float('inf')
    estacion_max = ''
    for estacion, estados in radios.items():
        if len(estados) > max_estados:
            max_estados = len(estados)
            estacion_max = estacion
'''

def maximo_global(radios):
    todos_estados = set().union(*radios.values())
    n = len(radios)
    estaciones = list(radios.keys())
    
    for k in range(1, n+1):
        for combo in combinations(estaciones, k):
            cubiertos = set()
            for estacion in combo:
                cubiertos.update(radios[estacion])
            if cubiertos == todos_estados:
                return list(combo)
    return []

def minimo_local(radios):
    estados_por_cubrir = set()
    for estados in radios.values():
        estados_por_cubrir.update(estados)
    
    estaciones_seleccionadas = []
    
    while estados_por_cubrir:
        mejor_estacion = None
        max_cobertura = 0
        
        for estacion, estados in radios.items():
            cobertura_actual = len(estados & estados_por_cubrir)
            if cobertura_actual > max_cobertura:
                max_cobertura = cobertura_actual
                mejor_estacion = estacion
                
        if mejor_estacion:
            estaciones_seleccionadas.append(mejor_estacion)
            estados_por_cubrir -= radios[mejor_estacion]
    
    return estaciones_seleccionadas

if __name__ == "__main__":
    lista_radios_global = maximo_global(radios)
    lista_radios_local = minimo_local(radios)
    print(lista_radios_global)
    print(lista_radios_local)