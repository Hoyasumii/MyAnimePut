def TitleTreatment(title: str):
    # VALOR MÁXIMO DE CARACTERES = 50

    title = title.split()

    word = ""

    cont = 1

    for x in title:
        contBackup = cont
        if len(word + x) >= 55 * cont and len(x) > 2:
            word += "\n"
            cont += 1
            
        if contBackup < cont:
            word += f"{x}"
        else:
            word += f" {x}"

    return word[1:]

def GenreTreatment(genres: str) -> str:
    genresFormat = ""
    linha = ""
    
    for genre in genres.split(", "):
        if len(linha + genre) >= 25:
            genresFormat += "\n"
            linha = ""
        
        genresFormat += f"{genre}, "
        linha += f"{genre}, "
    
    return genresFormat[:-2]
            
    
def StudioTreatment(studio: str):
    quandidadeStudios = studio.count(", ")
    posicao = []
    
    for x in range(quandidadeStudios):
        posicao.append(studio.index(", ", quandidadeStudios+1))
    
    studio  = studio.split(", ")
    
    for x in range(len(studio)):
        if x > 0:
            studio[x] = f"\n{studio[x]}"
        studio[x] += ","
    
    studio[-1] = studio[-1][:-1]
    
    string = "".join(studio)

    return string