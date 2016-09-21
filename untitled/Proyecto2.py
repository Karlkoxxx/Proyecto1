#averiguar si el grafo tiene dependencias ciclicas

archivo = open("numeros2","r")

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

for i in range(vertices):
    matriz.append([False] * vertices)
print matriz

while True:
    a = archivo.readline()
    b = archivo.readline()
    if not a:break
    a = int(a)
    b = int(b)
    print a
    print b
    matriz[a][b]=True

archivo.close()
print matriz


