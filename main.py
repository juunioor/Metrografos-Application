"""
32092921 | MATHEUS HENRIQUE DA SILVA APOSTULO
32095971 | VALDIR LOPES JUNIOR
"""

from grafoMatriz import Grafo
# Classe para auxiliar nas ligações das arestas do grafo
class Aresta:
  def __init__(self,a1,a2,peso):
    self.aresta1 = a1
    self.aresta2 = a2
    self.peso = peso
 
# Lista global com todos os nomes, o tamanho da lista vai iniciar o grafo
estacoes = []
#Lista global de arestas que vai ajudar a popular o grafo
arestas_lista = []
# Controle do carregamento do item "a"
controle_carregamento = True

# MENU
while True:
  print("+----------------------------------------+")
  print("|            METRÔGRAFOS                 |")
  print("+----------------------------------------+")
  print("| 1:  Ler dados do arquivo.              |")
  print("| 2:  Gravar os dados no arquivo.        |")
  print("| 3:  Inserir vértice.                   |")
  print("| 4:  Inserir aresta.                    |")
  print("| 5:  Remover vértice.                   |")
  print("| 6:  Remover aresta.                    |")
  print("| 7:  Menor caminho entre duas estações. |")
  print("| 8:  Mostrar conexidade do grafo.       |")
  print("| 9:  Mostrar conteúdo do arquivo.       |")
  print("| 10: Mostrar grafo.                     |")
  print("| 11: Exibir adjacências de um vértice.  |")
  print("| 12: Exibir objetivos da ODS do projeto.|")
  print("| 13: Encerrar a aplicação.              |")
  print("+----------------------------------------+\n")

  opcao = int(input("Escolha uma opção: "))

  match opcao:
    case 1:
      if controle_carregamento:
        # a) Ler dados do arquivo grafo.txt;
        with open("grafo.txt", "r") as grf:
            lines = grf.readlines()
            for i, line in enumerate(lines): # i: percorre linhas txt, line: conteúdo da linha
              match i: 
                case 0:
                  tipo_grafo = line
                case 1:
                  tamanho_inicial = line
                case _:
                  if '"' in line: # Vértice com rótulo
                    # Fazendo o split para pegar apenas o rótulo e jogar na lista global 
                    line_splitada = line.split('"')
                    line_splitada = line_splitada[1]
                    estacoes.append(line_splitada)
                    
                  else: # Arestas e ligações
                    # splitando linhas arestas e guardando dados em variáveis
                    arestas_txt_split = line.split(", ")
                    #print(arestas_txt_split)
                    
                    a_1 = arestas_txt_split[0]
                    a_2 = arestas_txt_split[1]
                    peso = arestas_txt_split[2]
                    #print(f"a1: {a_1}, a2:{a_2}, peso: {peso}")
                    
                    # instanciando arestas e atribuindo os atributos
                    aresta_obj = Aresta(a_1, a_2, int(peso))         
                    arestas_lista.append(aresta_obj)
                    
        
        #CRIANDO GRAFO
        grafo = Grafo(len(estacoes)) # instancia pelo tamanho do vetor grafo 
  
        # Inserindo vértices no grafo com a lista criada anteriormente
        for nome_estacao in estacoes:  
          grafo.insereV_txt(nome_estacao)
  
        # Inserindo arestas no grafo  
        for aresta in arestas_lista:
          grafo.insereA(aresta.aresta1, aresta.aresta2, aresta.peso)      
        #Fechando o arquivo txt
        grf.close()

        # Mostrando informações iniciais e atestando que o grafo foi instanciado
        tamanho_vertices_split = tamanho_inicial.split("\n")
        print(f"Grafo criado com {tamanho_vertices_split[0]} vértices e {len(arestas_lista)} arestas!")
        
        # Mudando variável de controle para não entrar mais nessa opção
        controle_carregamento = False
           
      else: # Caso o arquivo já tenha sido carregado
        print("O ARQUIVO TXT JÁ FOI CARRREGADO NO GRAFO!")
        
    case 2:
      if controle_carregamento == False: 
        # Chama o método de gravar dados
        grafo.gravarDados()
      else:
        print("Por favor, leia os dados do arquivo (1) antes de selecionar outras opções!")
      
    case 3:
      if controle_carregamento == False:
        inserir_vertice = input("Insira um nome pra o vértice que você deseja inserir: ")
        grafo.insereV(inserir_vertice.upper())
      else:
        print("Por favor, leia os dados do arquivo (1) antes de selecionar outras opções!")
        
    case 4:
      if controle_carregamento == False:
        v1 = input("Diga o primeiro vértice que irá ter adjacência:")
        v2 = input("Diga o segundo vértice que irá ser adjacente ao anterior:")
        peso = int(input("Digite o peso da adjacência entre os vértices inseridos:"))
        grafo.insereA(v1.upper(), v2.upper(), peso)
      else:
        print("Por favor, leia os dados do arquivo (1) antes de selecionar outras opções!")
        
    case 5:
      if controle_carregamento == False:
        remover_vertice = input("Insira um nome do vértice que você deseja remover: ")
        grafo.removeV(remover_vertice.upper())
      else:
        print("Por favor, leia os dados do arquivo (1) antes de selecionar essa opção!")
        
    case 6:
      if controle_carregamento == False:
        a1 = input("Diga um vértice que você quer remover uma aresta:")
        a2 = input("Diga um vértice adjacente ao vértice anterior para remover a aresta:")
        grafo.removeA(a1.upper(), a2.upper())  
      else:
        print("Por favor, leia os dados do arquivo (1) antes de selecionar essa opção!")

    case 7:
      if controle_carregamento == False:
        v1 = input("Diga o vértice origem: ")
        v2 = input("Diga o vértice destino: ")
        grafo.menor_caminho(v1.upper(),v2.upper())
      else:
        print("Por favor, leia os dados do arquivo (1) antes de selecionar essa opção!")  
      
    case 8:
      if controle_carregamento == False:
        grafo.conexidade()
      else:
        print("Por favor, leia os dados do arquivo (1) antes de selecionar essa opção!")
        
    case 9:  
      print("Mostrando o conteúdo do arquivo:\n")
      with open("grafo.txt", "r") as conteudo:
          lines = conteudo.read()
          print(lines)
      print("\nConteúdo exibido!")

      conteudo.close()
      
    case 10:
      if controle_carregamento == False:
        grafo.show()
      else:
        print("Por favor, leia os dados do arquivo (1) antes de selecionar essa opção!")

    case 11:
      if controle_carregamento == False:
        vertice = input("Diga o vértice que você deseja exibir as adjacências:")
        grafo.mostrarAdjacenciaVertice(vertice.upper())
      else:
        print("Por favor, leia os dados do arquivo (1) antes de selecionar essa opção!")
        
    case 12:
      print("+-------------------------------------------------------+")
      print("|                 OBJETIVOS DA ODS:                     |")
      print("+-------------------------------------------------------+")
      print("| ODS 8 - Trabalho Decente e Crescimento Econômico:     |")
      print("| (a)	Emprego e produtividade                         |")
      print("| (b)	Economia local                                  |")
      print("|                                                       |")
      print("| ODS 9 - Indústria, Inovação e Infraestrutura:         |")
      print("| (a)	Eficiência do transporte público:               |")
      print("| (b)	Inovação tecnológica                            |")
      print("| (c)	Sustentabilidade                                |")
      print("|                                                       |")
      print("| ODS 16 - Paz, Justiça e Instituições Eficazes:        |")
      print("| (a)	Segurança no transporte                         |")
      print("| (b)	Eficiência e transparência                      |")
      print("|                                                       |")
      print("|   * PARA MAIS INFORMAÇÕES CONSULTE A DOCUMENTAÇÃO! *  |")
      print("|   *    github.com/matheusapostulo/metrografos      *  |")
      print("+-------------------------------------------------------+\n")
  



    case 13:
      print("Aplicação encerrada!")
      break
      
    case _:
      print("ERRO! ENTRADA INVÁLIDA!")
  print("\n")