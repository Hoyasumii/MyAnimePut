from requests import get
from bs4 import BeautifulSoup
#v2.6 - (08/09/2021)

def search(title: str):
    """
    * GenSearch.search, feito por Alan Reis
    * Para que serve essa função?
        * Serve Para Pegar o Link do anime atavés do Google.
        * Por quê a Função usa o Google ao invés do próprio motor de busca do MyAnimeList?
            * Porque o motor de busca do MyAnimeList não é tão eficiente quanto o do Google.
    * Para fazê-la funcionar, basta chamar GenSearch.search("<Coloque Aqui seu Título>")
    """
    
    title = title.replace(" ", "+").lower()
    
    link = get(f"https://www.google.com.br/search?q={title}+anime+myanimelist")
    soup = BeautifulSoup(link.text, features="html.parser")
    pesquisa = list(soup.findAll("a", href=True))

    for x in range(len(pesquisa)):
        pesquisa[x] = str(pesquisa[x]["href"])[7:]

    lista = []

    for x in pesquisa:
        if "https://myanimelist.net/anime/" in x:
            lista.append(x)

    print(lista)
    return lista[0]

def collect(link: str):
    """
    * GenSearch.collect, feito por Alan Reis
    * Para que serve essa função?
        * Serve Para coletar dados de dentro do link que fora adquirido em GenSearch.search
    """
    
    link = get(link)
    soup = BeautifulSoup(link.text, features="html.parser")

    # region Coisas Fundamentais
    try:
        titulo = soup.find("h1", class_="title-name h1_bold_none").text
    except:
        titulo = soup.find(itemprop="name").text

    # region infoMAL
    try:
        season = soup.find(class_="information season").text
    except:
        season = soup.find(class_="information type").text

    studio = str(soup.find(class_="information studio author").text).replace("            ", "")

    ScoreGet = soup.find(class_="fl-l score")

    pontuacao = ScoreGet.text

    usuarios = ScoreGet["data-user"]

    ranking = str(soup.find(class_="numbers ranked").text).split()[1]
    popularidade = str(soup.find(class_="numbers popularity").text).split()[1]
    membros = str(soup.find(class_="numbers members").text).split()[1]

    generos = list(soup.findAll(itemprop="genre"))

    for x in range(len(generos)):
        generos[x] = generos[x].text

    imagem = soup.find(itemprop="image")['data-src']
    nomeImagem = str(imagem).split("/")[-1]
    ArquivoImagem = open(nomeImagem, "wb")
    
    response = get(imagem)
    ArquivoImagem.write(response.content)
    ArquivoImagem.close()
    # endregion
    # endregion

    variavel = {"title": titulo, 
                "infoMAL": {
                    "season": season, 
                    "studio": studio, 
                    "score": {"score": pontuacao, "users": usuarios}, 
                    "statistics": [ranking, popularidade, membros], 
                    "genres": generos, 
                    "image": nomeImagem}
                }
    # [titulo, pontuacao, generos, imagem]
    return variavel
