class Vertice:
    def __init__(self, nome):
        self.nome = nome

class Aresta:
    def __init__(self, partida, chegada):
        self.partida = partida
        self.chegada = chegada

class Grafo:
    def __init__(self):
        self.arestas = []
        self.vertices = []
        self.numVertices = 0
        self.numArestas = 0

    def addVertice(self, vertice):
        self.vertices.append(vertice)
        self.numVertices += 1

    def addAresta(self, partida, chegada):
        self.arestas.append(Aresta(partida,chegada))
        #self.numArestas += 1

    def matrizAdjacencia(self):
        self.dicionario = {}
        
        #criar dicionario
        #criar um for para listar a posicao dos vertices
        self.matriz = [[0]*self.numVertices for _ in range(self.numVertices)]
        '''
        for x in self.arestas:
            vP = x.getPartida().getId()
            vC = x.getChegada().getId()
            self.matriz[vP][vC] += 1
            if vP != vC:
                self.matriz[vC][vP] += 1
        '''
        return self.matriz
g = Grafo()
g.addVertice(Vertice('v1'))
g.addVertice(Vertice('v2'))
g.addVertice(Vertice('v3'))
g.addVertice(Vertice('v4'))
g.addAresta(Aresta(g.getVertice(0),g.getVertice(1)))
g.addAresta(Aresta(g.getVertice(0),g.getVertice(1)))
g.addAresta(Aresta(g.getVertice(1),g.getVertice(2)))
g.addAresta(Aresta(g.getVertice(0),g.getVertice(3)))
g.addAresta(Aresta(g.getVertice(2),g.getVertice(3)))
g.addAresta(Aresta(g.getVertice(2),g.getVertice(3)))
g.addAresta(Aresta(g.getVertice(0),g.getVertice(0)))
for x in g.matrizAdjacencia():
    print(*x)

dicionario={
    'vertice1': '1',    
    'vertice2': '2',
    'vertice3': '3',
}
dicionario.pop('vertice1')
print(dicionario)