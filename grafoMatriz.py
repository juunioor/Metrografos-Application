"""
32092921 | MATHEUS HENRIQUE DA SILVA APOSTULO
32095971 | VALDIR LOPES JUNIOR
"""

from math import inf
import os
from copy import deepcopy # Usado nos métodos de cópia de lista. Opções 2 e 4!
from pilha import Pilha

infinito = inf

class Grafo:
  TAM_MAX_DEFAULT = 100  # qtde de vértices máxima default

  # construtor da classe grafo
  def __init__(self, n=TAM_MAX_DEFAULT):
    self.n = n  # número de vértices
    self.m = 0  # número de arestas
    # matriz de adjacência
    self.adj = [[infinito for i in range(n)] for j in range(n)]
    self.nomes_vertices = [] #Lista com nomes dos vértices, manipulação vai ser feita aqui  
            
  # Atribui nome a um número de vértice
  def atribuiVertice(self, nome_vertice, numero_vertice):
    self.nomes_vertices[numero_vertice] = nome_vertice

  #Percorre a lista de nomes e retorna a posição que o nome está
  def getPosicaoNome(self, nome_vertice):
    for i in range(len(self.nomes_vertices)): 
      if self.nomes_vertices[i] == nome_vertice:
        return i
       
    return -1

  def insereV_txt(self, nome_vertice): # Esse método é o usado para a leitura do txt apenas
    self.nomes_vertices.append(nome_vertice)  

  # b) Gravar dados no arquivo grafo.txt;
  def gravarDados(self):
    # Apaga o arquivo pois o grafo pode estar totalmente diferenre do original
    os.remove("grafo.txt")
    # Abre o arquivo 
    with open("grafo.txt", "w") as grf_r:
      # Laço que escreve os VÉRTICES EXISTENTES NO GRAFO
      for i in range(len(self.nomes_vertices)+2):# percorre linhas txt, line: conteúdo da linha
        match i: 
          case 0:
            grf_r.write("2\n")
          case 1:
            grf_r.write(f"{str(self.n)}\n")
          case _:
            string_vertice = f'{i-1} "{self.nomes_vertices[i-2]}"\n'
            grf_r.write(string_vertice)
      # Laço para percorrer a matriz principal para pegar as arestas 
      # Utilizaremos um matriz cópia auxiliar e iremos setando infinito no contrário da posição([i][j] -> [j][i])
      matriz_aux = deepcopy(self.adj) # usando lib copy para criar uma cópia
      for i in range(self.n):
        for j in range(self.n):
          if matriz_aux[i][j] != infinito: # verifica se não é infinito
            # Guarda os nomes dos vértice pela posição e também o peso
            vertice_i = self.nomes_vertices[i]
            vertice_j = self.nomes_vertices[j]
            peso = self.adj[i][j]
            string_aresta = f'{vertice_i}, {vertice_j}, {peso}\n'
            grf_r.write(string_aresta)
            # Agora iremos setar infinito na posição inversa para não pegarmos a mesma relação
            matriz_aux[j][i] = infinito

      #print(f"ASSIM FICOU A MATRIZ AUX: {matriz_aux}")      
      #print(f"ASSIM FICOU A LISTA ADJ: {self.adj}")  
      grf_r.close()

  
  # c) Insere vértice na lista que representa o grafo. Irá inserir na última posição, não fará diferença na lógica geral pois pesquisamos por nomes para fazer as operações dos métodos
  def insereV(self, nome_vertice): 
    # Se o vértice não existe, adiciona à última posição da lista de nomes e aumenta o tamanho de vértices do grafo
    if nome_vertice not in self.nomes_vertices:
      # Copia a matriz antiga para futuras operações no método
      matriz_copia = deepcopy(self.adj)
      # Add à lista de nomes de vértices
      self.nomes_vertices.append(nome_vertice)
      self.n += 1
      # Resetaremos a matriz do grafo com o novo tamanho 
      self.adj = [[infinito for i in range(self.n)] for j in range(self.n)]
      # Repaseremos os dados anteriores para a lista nova (somente onde tinha aresta) 
      for i in range(len(matriz_copia)):
        for j in range(len(matriz_copia)):
          if matriz_copia[i][j] != infinito:
            self.adj[i][j] = matriz_copia[i][j]
    
    else:
      print("ESSE VÉRTICE JÁ EXISTE NO GRAFO! Tente outro da próxima vez!")
      

  # d) Insere uma aresta no Grafo tal que v é adjacente a w (pega a posição pelo nome). Não precisamos saber a posição, apenas o nome para poder ligar dois vértices.
  def insereA(self, vertice_i, vertice_j, peso):
    if peso > 0:
      pos_i = self.getPosicaoNome(vertice_i)
      pos_j = self.getPosicaoNome(vertice_j)
      if pos_i != -1 and pos_j != -1:
        if self.adj[pos_i][pos_j] == infinito and self.adj[pos_j][pos_i] == infinito:
          self.adj[pos_i][pos_j] = peso
          self.adj[pos_j][pos_i] = peso
          self.m += 1  # atualiza qtd arestas
        elif self.adj[pos_i][pos_j] != infinito and self.adj[pos_j][pos_i] != infinito: # Atualizar com um novo peso caso já tenha um peso, condicional para n mudar qtd aresta
          self.adj[pos_i][pos_j] = peso
          self.adj[pos_j][pos_i] = peso
      else:
        print("Algum dos vértices digitados não existe!\n")
    else:
      print("Insira um peso positivo maior que 0!")
      
   # e) Método para remover vértice do grafo ND
  def removeV(self, vertice):
    if vertice in self.nomes_vertices:
      posicao_vertice = self.getPosicaoNome(vertice)
      # Removendo as arestas com todos os outros vértices primeiro antes de apagar as posições do vetor
      for i in range(self.n):
        vertice_2 = self.nomes_vertices[i] # variável que pega todos os nomes dos vértices existentes na lista de nomes
        self.removeA(vertice,vertice_2) # remove as ligações existentes com os outros vértices        
      # Atualiza a matriz (removendo os elementos)
      del self.adj[posicao_vertice] # Apaga o vértice 
      self.n -= 1 # Atualiza a quantidade de vértices  
      #Atualizando as colunas desalocando o espaço do antigo vértice
      for i in range(self.n):        
        del self.adj[i][posicao_vertice]

      # Apagando o vértice da lista de nomes 
      del self.nomes_vertices[posicao_vertice]
    else:
      print("Vértice não existente no grafo!")

  # f) remove uma aresta v->w do Grafo utiliza nome para achar a posição
  def removeA(self, vertice_i, vertice_j):
    pos_i = self.getPosicaoNome(vertice_i)
    pos_j = self.getPosicaoNome(vertice_j)
    if pos_i != -1 and pos_j != -1:
      # testa se temos a aresta
      if self.adj[pos_i][pos_j] != infinito and self.adj[pos_j][pos_i] != infinito:
        self.adj[pos_i][pos_j] = infinito
        self.adj[pos_j][pos_i] = infinito
        self.m -= 1
      # atualiza qtd arestas
    else:
      print("\nUm dos vértices digitados não existe!\n")

  # g) Verifica se o grafo é conexo ou não-conexo
  #PERGUNTAR PRO PROF SE PRECISA DO VERTICE INICIAL
  def adjacenciasVertice(self, n, nosMarcados):
    vetorAdjacencias = []
    for i in range(self.n): #percorre linhas
      if self.adj[n][i] != infinito and i not in nosMarcados: # se o não estiver marcado e é adjacente a n 
        vetorAdjacencias.append(i)
    return vetorAdjacencias 

  def adjacenciasV(self, n):
    vetorAdjacencias = []
    for i in range(self.n): #percorre linhas
      if self.adj[n][i] != infinito: # se é adjacente a n 
        vetorAdjacencias.append(i)
    return vetorAdjacencias
    
    
  def conexidade(self):
    verticeInicio = 0
    # Cria a pilha e array de nós marcados e contador para marcar os nós visitados
    quantidade_visitados = 0
    nosMarcados = []
    pilha = Pilha()
    # Visita o Nó
    #print(f"Nó inicial visitado: {verticeInicio}")
    quantidade_visitados += 1
    # Marca o nó inicial
    nosMarcados.append(verticeInicio)
    # Empilha o nó
    pilha.push(verticeInicio)

    while not pilha.isEmpty():
      n = pilha.pop()
      #print("Pilha está assim = ", pilha)

      adjacentesDeN = self.adjacenciasVertice(n, nosMarcados)
      #print(f"adjacentes de {n} = ", adjacentesDeN)
      
      while len(adjacentesDeN) > 0: # Roda em todos os adjacentes de "n" que ainda não foram marcados
        #print("Nó m visitado = ", chr((adjacentesDeN[0]+1) + 96))
        quantidade_visitados += 1 # incrementa visitados
        pilha.push(n)
        #print("n colocado na pilha = ", pilha)
        nosMarcados.append(adjacentesDeN[0]) # "m é marcado = ", nosMarcados)
        n = adjacentesDeN[0] #"Troca o valor de n para m (n <- m(atribuição)) = ", n, "\n")
        adjacentesDeN = self.adjacenciasVertice(n, nosMarcados)

    '''
    # mostrando Percurso em profundidade
    print("O percurso em profundidade foi:", end = " ")
    for i in nosMarcados:
      print(i, end = " ")
    print("\n\n")
    '''
    
    # Tendo o percurso em profundidade, poderemos verificar a conexidade
    print(f"Quantitidade de vértices = {self.n}")
    print(f"Quantidade de vértices visitados no percurso = {quantidade_visitados}\n")
    # Verifica se o grafo é conexo ou não 
    if(self.n == quantidade_visitados):
      print("O grafo é conexo!\n\n")
    else:
      print("O grafo é não conexo!\n\n")
  
  # h) Menor caminho entre dois vértices utilizando o algoritmo de Dijkstra
  def menor_caminho(self, v1, v2):
    # Recebe os vértices em nome e descobre se índice
    indice_v1 = self.getPosicaoNome(v1)
    indice_v2 = self.getPosicaoNome(v2)

    #print(f"indice 1 = {indice_v1}, indice 2 = {indice_v2}")
    if indice_v1 == -1 or indice_v2 == -1:
      print("\nAlguma vértice digitado não existe!")
    else:
      #print("Continua a lógica")
      # Criando o array d(distancias)
      d = [infinito] * self.n
      #print(d)

      # Atribuindo 0 no array d(distancias) na posição do indice de v1
      d[indice_v1] = 0

      # Criando array A(abertos), F(fechados), S(sucessores), k e rot(rotas)
      A = [i for i in range(0, self.n)]
      #print("A = ", A)
      F = [] # começa vazio
      S = [indice_v1] #começa S com o vértice inicial
      k = 0
      rot = [-1 for i in range(0, self.n)] #inicializando rot

      while len(A) != 0: #mudar aqui
        k += 1 
        distanciasA = []
        indices = []

        for i in A:
          distanciasA.append(d[i])
          indices.append(i)

        r = indices[distanciasA.index(min(distanciasA))]
        F.append(r)
        A.remove(r)

        S = list(set(A) & set(self.adjacenciasV(r)))

        for i in S:
          p = min(d[i], d[r] + self.adj[r][i])
          if p < d[i]:
            d[i] = p
            rot[i] = r
        
    
      #print("Terminou o algoritmo!")
      print(f"\nA seguir, temos a rota com o menor tempo entre {v1} e {v2}:\n")
      #Vetor = [i for i in range(0, self.n)]
      #print("Vetor", Vetor)
      #print("ROT:", rot)
      #print("Distancias:", d)
      
      # Vamos pegar a rota que devemos fazer
      rota = []
      indice_aux = indice_v2
      while indice_aux != indice_v1:
        vertice_visitar = rot[indice_aux]
        rota.append(vertice_visitar)
        indice_aux = vertice_visitar
      
      # Vamos inverter a ordem para simular o caminho real a partir de v1
      rota_invertida = rota[::-1]
      rota_invertida.append(indice_v2) # Adicionamos o v2 ao array de rotas tmb, pois é o destino e não entrou no laço
      #print("Essa é a rota invertida: ", rota_invertida)
  
      # Agora, iremos exibir quanto é a distância entre todos os vértice da partida ao destino
      for i in range(len(rota_invertida)-1):
        #print("i = ",i, "i + 1 = ", i+1)
        print(f"{self.adj[rota_invertida[i]][rota_invertida[i+1]]} min | {self.nomes_vertices[rota_invertida[i]]} ( ) -> ( ) {self.nomes_vertices[rota_invertida[i+1]]}\n")
  
      # Por último, iremos printar o tempo total do percurso de acordo com o que foi calculado no algoritmo
      print(f"\n{ d[indice_v2]} min | TEMPO TOTAL DO PERCURSO")
  
    
  
  # Método para exibir as adjacências apenas de um vértice
  def mostrarAdjacenciaVertice(self, vertice):
    #Vamos pesquisar se o vértice existe na nossa lista de estacoes
    if vertice in self.nomes_vertices:
      # Agora, iremos pegar a posição do vértice na matriz e percorrer apenas na linha da matriz referente a ele
      posicao_vertice = self.getPosicaoNome(vertice)
      print(f"\nADJACÊNCIAS NO VÉRTICE '{vertice}': ")
      for i in range(self.n):
        if self.adj[posicao_vertice][i] != infinito:
          print(f"{self.adj[posicao_vertice][i]} min | {self.nomes_vertices[posicao_vertice]} ( ) -> ( ) {self.nomes_vertices[i]}")
    else:
      print("VÉRTICE NÃO EXISTENTE NO GRAFO")
    
    
    
  
  # Exibe de forma reduzida devido a grande quantidade de vértices
  def show(self):
    print(f"\n n: {self.n:2d} ", end="")
    print(f"m: {self.m:2d}\n")
    for i in range(self.n):
      print(f"ESTAMOS NO VÉRTICE '{self.nomes_vertices[i]}': ")
      for w in range(self.n):
        if self.adj[i][w] != infinito:
          print(f"{self.adj[i][w]} min | {self.nomes_vertices[i]} ( ) -> ( ) {self.nomes_vertices[w]}")
      print("\n")
    print("fim da impressao do grafo.\n\n")
