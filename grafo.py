class Vertice:

  pass
  #def __init__(self, nome):
  #self.nome = nome


class Aresta:

  def __init__(self, partida, chegada):
    self.partida = partida
    self.chegada = chegada
    self.Coordenada = (self.partida, self.chegada)


class Grafo:

  def __init__(self, n):
    self.arestas = []
    self.vertices = [Vertice() for i in range(n)]

  def addVertice(self, vertice):
    self.vertices.append(vertice)

  def addAresta(self, partida, chegada):
    self.arestas.append(Aresta(partida, chegada))

  def removerAresta(self, a):
    self.vertices.remove(a)

  def removerVertice(self, v):
    g.vertices.remove(v)

  def numAresta(self):
    return len(self.arestas)

  def numVertices(self):
    return len(self.vertices)

  def matrizAdjacencia(self):
    nVertice = self.numVertices()
    indice = {}
    #criar dicionario
    #criar um for para listar a posicao dos vertices
    self.matriz = [[0] * nVertice for _ in range(nVertice)]
    for (posicao, ponto) in enumerate(self.vertices):
      indice[ponto] = posicao
    for ares in self.arestas:
      vP = ares.partida
      vC = ares.chegada
      #dicionario = {'ponto1':'linha1','ponto2':'linha2'}
      iP = indice[vP]
      iC = indice[vC]
      if (iP == iC):
        self.matriz[iP][iC] = 2
      else:
        self.matriz[iC][iP] = 1
        self.matriz[iP][iC] = 1

    return self.matriz

  def PrintGrafo(self, Aresta, Vertice):
    print("Array de aresta: ", self.arestas, ", ", "")
    print("\nArray de vertices", self.vertices, ", ")


'''    
    def ListaAdjacencia():

    def GrauVertice(self, arestas):
        self.arestas = arestas

    def GrauMedioGrafo():
    
    def BuscaProf():
    
    def BuscaLargura():'''
''''''
g = Grafo(4)
v1, v2, v3, v4 = g.vertices[0], g.vertices[1], g.vertices[2], g.vertices[3]
g.addAresta(v1, v2)
g.addAresta(v1, v3)
g.addAresta(v2, v4)
g.addAresta(v3, v4)
print(g.numAresta())

print(g.matrizAdjacencia())
