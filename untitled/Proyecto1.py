#hacer que funcione con mas de un grafo...la c, la primera linea del archivo
#refactorizar en funciones y hacer un for sobre el numero de grafos

def recorrer_componente(origen,visitados):
    visitados[origen]=True
    for ady in range(vertices):
        if (matriz[origen][ady])!= 0:
            if(not visitados[ady]):
                recorrer_componente(ady,visitados)

def recorrer_grafo():
    for i in range(vertices):
        if (not visitados[i]):
            recorrer_componente(i,visitados)


archivo = open("numerosNoConex","r")

grafos = archivo.readline()
vertices = archivo.readline()
aristas = archivo.readline()

print "numero de grafos: " + grafos
print "numero de vertices: " + vertices
print "numero de artistas: " + aristas

grafos = int(grafos)
vertices = int(vertices)
aristas = int(aristas)

matriz = []
visitados = []

visitados = [False] * vertices
for i in range(vertices):
    matriz.append([False] * vertices)
print matriz
print visitados

while True:
    a = archivo.readline()
    b = archivo.readline()
    if not a:break
    a = int(a)
    b = int(b)
    print a
    print b
    matriz[a][b]=True
    matriz[b][a]=True
print matriz
recorrer_grafo()
print visitados
archivo.close()




