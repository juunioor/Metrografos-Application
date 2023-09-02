from bs4 import BeautifulSoup

class Estacao:
  def __init__(self, id, nome):
    self.id_estacao = id
    self.nome_estacao = nome
    self.estacoes = []

estacoes = []

# Abrindo o arquivo xml
with open("graph_biIyXIgpeHrnXudk.xml", "r") as f:
  data = f.read()

# Vamos pegar o ID e nomes das estações 
Bs_data = BeautifulSoup(data, "xml") 

# Todas instâncias da tag node
b_node = Bs_data.find_all('node')

# Percorrendo todas as tags, já populando a lista das estações e escrevendo os vértices no arquivo
with open("grafo.txt", "w") as grf:
  contador_v = 1
  for node in b_node:
    tag = node
    id = tag['id']
    nome_estacao = tag['mainText']
    estacao_obj = Estacao(id, nome_estacao)
    estacoes.append(estacao_obj)
    string = f'{contador_v} "{nome_estacao.upper()}"\n'
    grf.write(string)
    contador_v += 1
    
  # Todas instâncias da tag edge (onde estão as arestas)
  b_edge = Bs_data.find_all('edge')
  
  # Percorrendo todas as tags edge arestas e salvando em um arquivo
  for edge in b_edge:
    tag = edge
    source = tag['source']
    target = tag['target']
    peso = tag['weight']

    #print(f"id source da linha: {source}, id target da linha: {target}, peso da linha {peso}")
    
    for i in estacoes:
      if i.id_estacao ==  source:
        source_nome = i.nome_estacao         
      elif i.id_estacao == target:
        target_nome = i.nome_estacao

    string_arq = f"{source_nome.upper()}, {target_nome.upper()}, {peso}\n"
    grf.write(string_arq)
    #print(f'nome source:{source_nome}, nome target: {target_nome}, peso: {peso}')

# Fechando arquivos
f.close()
grf.close()