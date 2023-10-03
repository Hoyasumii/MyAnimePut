"""
Arquivo criado por Alan Reis Anjos no dia 26-2-22 devido a necessidade de separar o back do front end.
Última atualização: 26-2-22
"""

from notion.client import NotionClient # Função Essencial do Projeto

import json # Função para carregar o arquivo JSON

from threading import Thread # Função para criar Threads: Multiprocessamento

class StartProgram(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        
        self.check = False #Vou criar uma variável de check para verificar se os arquivos foram carregados.
        
        with open("Resources/cache.json") as file:
            self.doc = json.load(file)
    
    def run(self):
        self.client = NotionClient(token_v2 = self.doc["token"])
        
        self.page = self.client.get_collection_view(self.doc["page"])
    
        self.check = True #Se self.check for True, a pesquisa pode ser feita.
            
        