import numpy as np
from collections import deque

naosei = 0


class DadosBuscaLargura:

  def __init__(self, cor, d, pi):
    self.cor = cor
    self.d = d
    self.pi = pi
    self.inicial = 0
    self.final = 0


class Vertice:

  def __init__(self, nome):
    self.nome = nome


class Aresta:

  def __init__(self, partida, chegada, nome):
    self.partida = partida
    self.chegada = chegada
    self.coordenada = (self.partida, self.chegada)
    self.nome = nome

  def arExtremidade(self, vertice):
    return self.partida == vertice or self.chegada == vertice

  def oposto(self, vertice):
    if self.partida == vertice:
      return self.chegada
    return self.partida


class Grafo:

  def __init__(self, n):
    self.arestas = []
    self.vertices = [Vertice(f"v{i+1}") for i in range(n)]

  def addVertice(self, vertice):
    self.vertices.append(vertice)

  def addAresta(self, partida, chegada, nome):
    self.arestas.append(Aresta(partida, chegada, nome))

  def removerAresta(self, A):
    for i in A:
      self.removerAresta(A)

  def removerVertice(self, v):
    self.vertices.remove(v)
    #remover as arestas incidentes ao vertice chamando a funcao arestas incidentes
    self.removerAresta(self.arestasIncidentes(v))

  def arestasIncidentes(self, v):
    return [a for a in self.arestas if a.arExtremidade(v)]

  def numAresta(self):
    return len(self.arestas)

  def numVertices(self):
    return len(self.vertices)

  def listAdjacencia(self):
    self.lista = {v.nome: [] for v in self.vertices}
    for aresta in self.arestas:
      u, v = aresta.partida.nome, aresta.chegada.nome
      self.lista[u].append((v, aresta.nome))
      self.lista[v].append((u, aresta.nome))

    return self.lista

  def matrizAdjacencia(self):
    nVertice = self.numVertices()
    indice = {}
    self.matriz = [[0] * nVertice for _ in range(nVertice)]
    for (posicao, ponto) in enumerate(self.vertices):
      indice[ponto] = posicao
    for ares in self.arestas:
      vP = ares.partida
      vC = ares.chegada
      iP = indice[vP]
      iC = indice[vC]
      if (iP == iC):
        self.matriz[iP][iC] += 1
      else:
        self.matriz[iC][iP] = 1
        self.matriz[iP][iC] = 1

    return self.matriz

  def grauVertice(self, vertice):
    self.grau = []
    for aresta in self.arestas:
      if (aresta.arExtremidade(vertice)):
        self.grau.append(aresta)
    return len(self.grau)

  def grauMedioGrafo(self):
    total_graus = 0
    for vertice in self.vertices:
      grau_vertice = self.grauVertice(vertice)
      total_graus += grau_vertice
    grau_medio = total_graus / len(self.vertices)
    return grau_medio

  def MatrizIncidencia(self):
    indice = {}
    nVertice = self.numVertices()
    nAresta = self.numAresta()
    self.matriz = np.zeros((nVertice, nAresta))
    #zerar matriz
    for (posicao, ponto) in enumerate(self.vertices):
      indice[ponto] = posicao

    for (j, ares) in enumerate(self.arestas):
      vP = ares.partida
      vC = ares.chegada
      #dicionario = {'ponto1':'linha1','ponto2':'linha2'}
      iP = indice[vP]
      iC = indice[vC]
      if (iP == iC):
        self.matriz[iP][j] = 2
      else:
        self.matriz[iP][j] = 1
        self.matriz[iC][j] = 1
    return self.matriz

  def adjacentes(self, v):
    adj = []
    for edge in self.arestas:
      if edge.arExtremidade(v):
        adj.append(edge.oposto(v))
    return adj

  def BuscaLargura(self, raiz):
    mapa = dict()
    for u in self.vertices:
      if u != raiz:
        mapa[u] = DadosBuscaLargura("BRANCO", 100000, None)

    mapa[raiz] = DadosBuscaLargura("CINZENTO", 0, None)

    fila = deque([raiz])

    while len(fila) > 0:
      u = fila.popleft()
      um = mapa[u]
      for v in self.adjacentes(u):
        vm = mapa[v]
        if vm.cor == "BRANCO":
          vm.cor = "CINZENTO"
          vm.d = um.d + 1
          vm.pi = u
          fila.append(v)
      um.cor = "PRETO"
    return mapa

  def BuscaProfundidade(self):
    mapa = dict()
    for u in self.vertices:
      mapa[u] = DadosBuscaLargura("BRANCO", 0, None)
    self.inicial = 0
    for u in self.vertices:
      um = mapa[u]
      if um.cor == "BRANCO":
        self.BuscaProfVisit(um)
    return mapa

  def BuscaProfVisit(self, u):
    self.inicial += 1
    u.d = self.inicial
    u.cor = "CINZENTO"
    for v in self.adjacentes(u):
      if v.cor == "BRANCO":
        v.pi = u
        self.BuscaProfVisit(v)
    u.cor = "PRETO"
    self.inicial += 1
    u.final = self.inicial


g = Grafo(7)
v1, v2, v3, v4, v5, v6, v7 = g.vertices[0], g.vertices[1], g.vertices[
  2], g.vertices[3], g.vertices[4], g.vertices[5], g.vertices[6]
g.addAresta(v1, v2, "aresta 0")
g.addAresta(v1, v4, "Aresta 1")
g.addAresta(v2, v3, "Aresta 2")
g.addAresta(v2, v4, "Aresta 3")
g.addAresta(v3, v4, "Aresta 4")
g.addAresta(v4, v5, "Aresta 5")
g.addAresta(v5, v6, "Aresta 6")
g.addAresta(v6, v7, "Aresta 7")
print("------------------------------------------------")
for i in g.matrizAdjacencia():
  print(i)
print("------------------------------------------------")
print(g.MatrizIncidencia())
print("------------------------------------------------")
for x in g.vertices:
  naosei += 1
  print(f"V{naosei}:", g.grauVertice(x))
print("------------------------------------------------")
print(f"Grau Medio: {g.grauMedioGrafo()}")
print("------------------------------------------------")
for vertice, adjacencias in g.listAdjacencia().items():
  print(f"{vertice}: ", end="")
  for adjacente, aresta in adjacencias:
    print(f"{adjacente} ({aresta})", end=" ")
  print()
print("------------------------------------------------")
<<<<<<< HEAD
for x, y in g.BuscaLargura(v1).items():
=======
for x, y in g.BuscaLargura(v1).items():
>>>>>>> ff9295e1b3d076b14b46c25e6fb4cc91a36bedff
  print("Vertice: ", x.nome, "Cor:", y.cor, "Distancia:", y.d)
print("------------------------------------------------")
for x, y in g.BuscaProfundidade().items():
  print("Vertice: ", x.nome, "Cor:", y.cor, "Tempo Incial:", y.inicial,
        "Tempo Final", y.final)
<<<<<<< HEAD
print("------------------------------------------------")
=======
print("------------------------------------------------")
>>>>>>> ff9295e1b3d076b14b46c25e6fb4cc91a36bedff
