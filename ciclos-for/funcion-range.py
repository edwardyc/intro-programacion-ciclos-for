"""
sintaxis funcion range():

range([inicio], fin, [paso])
- el inicio es 0 por defecto, si no se indica
- el paso es 1 por defecto, si no se indica

- la funcion range() genera una serie de numero enteros entre el inicio y el fin-1 con incremento dado por el paso
"""

# caso 1: range(fin)

print(list(range(10))) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(list(range(101))) # 0, 1, 2, ..., 100
print(list(range(31))) # 0, 1, ..., 32 