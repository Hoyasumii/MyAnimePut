from notion.client import NotionClient
import json
# V2: Usando arquivos JSON; 14/08/2021
# V2.1: Corrigido Funcionamento do Del; 22/08/2021
# V2.2: Removida necessidade de NotionClient; 03/09/2021
# V2.3: Corrigido Funcionamento de Del; 05/09/2021
# V2.31: Removido Funcionamento.Del; 08/09/2021


def Add(informacoes: dict, page):
    row = page.collection.add_row()
    row.title = informacoes["title"]
    row.opinion = informacoes["infoUSER"]["opinion"]
    row.genres = informacoes["infoMAL"]["genres"]
    row.review = informacoes["infoUSER"]["rewatch"]
    row.favorite = informacoes["infoUSER"]["favorites"]
