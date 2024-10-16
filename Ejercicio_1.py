'''Crear un Detector de palíndromos. Un palíndromo es una palabra o frase que se lee igual
de derecho y del revés Ej anita lava la tina, neuquen, etc'''

pal = str(input('Ingrese una palabra: ')).lower().strip()

# Verifica si la palabra es igual a su versión invertida (palíndromo)
if pal == pal[::-1]:  # 'pal[::-1]' invierte la palabra
    print(f'{pal} es un palindromo')
else:
    print(f'{pal} No es un palindromo')
