#leer grafo de un archivo
#comprobar que es conexo
#representarlo mediante una matriz de adyacencia

#usar readline conviertiendo a enteros

archivo = open("numeros","r")
matriz = [[0 for i in range(2)] for j in range(4)]
#matrizCeros = [[0 for i in range(3)] for j in range(3)]
for i in range(4):#no me he cargado la primera tupla, la "n" y la "m" vertices y aristas.
    for j in range(2):
        linea = archivo.readline()
        lineaI =int(linea)
        matriz[i][j]= lineaI
        matriz[i][j]= lineaI
print matriz

matrizCeros = []
vector = []
while True:

    line = archivo.readline()
    line = int(line)
    if not line:break





