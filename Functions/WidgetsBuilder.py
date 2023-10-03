from tkinter import *

from tkinter.ttk import Label as Lb

from tkinter.font import Font


def LabelB(master, content: str, size: int, foreground="black", weight="normal", mode=True):
        """
        * Label Builder
            * O intuito de criação de facilitar a Criação de Label's Personalizados
            
            * Instruções:
                * Durante a Criação, existem apenas 3 tipos de variáveis que são obrigatórias para o funcionamento:
                    * master: Tela onde o Label será Criado
                    * content: Conteúdo de Texto do Label
                    * size: Tamanho da Fonte
                
                * Existem também casos onde o usuário precise de mais opções, como o weight e o foreground. Para isso, basta especificá-los
                
                * Existe também o mode, que existe para o programa criar o tkinter.Label ou o tkinter.ttk.Label.
                    * mode is True: tkinter.Label
                    * mode is False: tkinter.ttk.Label
            
            * Criado por Alan Reis no dia 04/09/2021 
        """

        font = Font(
            family ="Tahoma",
            size = size,
            weight = weight,
            )
        
        if mode == True:
            return Label(master, text=content, font=font, background=master.cget("background"), foreground=foreground)
        else:
            return Lb(master, text=content, font=font, background=master.cget("background"), foreground=foreground)

def FrameB(master, mode=True):
    # True para Criação de um Frame Master; False para criação de uma pseudo Frame
    if mode:
        return Frame(master,  bg="#f6f6f6", highlightbackground="#ebebeb", highlightthickness=1)
    else:
        return Frame(master, bg=master.cget("background"))