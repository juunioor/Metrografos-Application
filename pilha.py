"""
32092921 | MATHEUS HENRIQUE DA SILVA APOSTULO
32095971 | VALDIR LOPES JUNIOR
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 18:53:01 2023

@author: icalc
"""
class Pilha:
    TAM_DEFAULT = 1100
    def __init__(self, tamanho=TAM_DEFAULT):
        self.pilha = list(range(tamanho))
        self.topoPilha = -1
        
   	#Verifica se a pilha
   	#está vazia
    def isEmpty(self):
   		return self.topoPilha == -1
  
    # Verifica se a pilha está
    # cheia
    def isFull(self):
        return self.topoPilha == (len(self.pilha) - 1)
       
  	# insere um elemento e 
   	# no topo da pilha
    def push(self, e):
        if not self.isFull():
            self.topoPilha+=1
            self.pilha[self.topoPilha] = e 
        else: 
            print("overflow - Estouro de Pilha")
         
    # remove um elemento 
   	# do topo da pilha
    def pop(self):
        if not self.isEmpty(): 
            e = self.pilha[self.topoPilha]
            self.topoPilha-=1 
            return e 
        else:
            print("Underflow - Esvaziamento de Pilha") 
            return -1;

   	# Retorna o elemento que está
   	# no topo da pilha
    def topo(self):
        if not self.isEmpty():
            return self.pilha[self.topoPilha]
        else:
            print("Underlow - Esvaziamento de Pilha") 
            return -1

   	# obtém o total de elementos 
   	# armazenados na Pilha
    def totalElementos(self):
        return self.topoPilha+1
   	