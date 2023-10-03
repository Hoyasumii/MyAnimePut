"""
Arquivo criado por Alan Reis Anjos no dia 26-2-22 devido a necessidade de separar o back do front end.
Última atualização: 26-2-22
"""

from tkinter import * # Função Gráfica pt.1
from tkinter.ttk import * # Função Gráfica pt.2
from tkinter import Frame, IntVar, DISABLED, NORMAL, END # Função Gráfica pt.3: Apenas para Substituir algumas coisas do Tkinter.tkk

from tkinter.font import Font # Função para carregar a Fonte pt.1

import pyglet # Função para carregar a Fonte pt.2
import os

from threading import Thread

import Functions.GenSearch as GenSearch # Função de Pesquisa

from Screen.MoreInfo import MoreInfo # Função para Executar a Janela MoreInfo
from Screen.Settings import Settings

class MainScreen:
    def __init__(self, content):
        self.screen = Tk() # Construtor da Janela
        
        self.content = content # Função Inicial do Programa
        
        #region Carregamento da Fonte
        pyglet.font.add_file('Resources/font.ttf')
        self.TitleFont = Font(family='AGRevueCyr Roman Medium', size=25)
        #endregion
        
        #region FrameTop
        self.FrameTop = Frame(self.screen, bg="#2e51a2")
        self.FrameTop.grid(row=0, sticky='we')
        
        self.logo = Label(self.FrameTop, text="MyAnimePut", font=self.TitleFont, background="#2e51a2", foreground="#ffffff")
        self.settingsButton = self.logo.bind("<Button-3>", self.ConfigButton)
        self.logo.pack(pady=(5, 0))
        
        #region PlaceHolder
        self.entry = Entry(self.FrameTop, background="#2e51a2")
        self.entry.insert(0, "Pesquise aqui o Título")
        self.entry.configure(state=DISABLED)
        self.click = self.entry.bind("<Button-1>", self.PlaceHolderEffect)
        self.entry.pack(padx=5, pady=5, fill="x")
        #endregion

        Frame(self.FrameTop, bg="#1d439b", height=1).pack(fill="x")
        
        #region Configurações Widgets
        self.style = Style()
        self.style.configure('Black.TCheckbutton', foreground='black', background='white')
        #endregion
        #endregion
        
        #region FrameMid
        self.opinioes = ['Péssimo', 'Ruim', '?', 'Regular', 'Bom', 'Muito Bom', 'Excelente']
        self.opinioes.reverse() # Apenas para alterar a ordem que a lista será exibida
        
        self.FrameMid = Frame(self.screen, background='white')
        self.FrameMid.grid(row=1, sticky='we', pady=5)
        
        self.LabelOpinion = Label(self.FrameMid, text='Minha Opinião', background='white')
        self.LabelOpinion.grid(row=0, column=0, sticky='e', padx=5)
        
        self.ComboboxOpinion = Combobox(self.FrameMid, values=self.opinioes, state='readonly', width=10)
        self.ComboboxOpinion.current(3) # Valor Padrão
        self.ComboboxOpinion.grid(row=0, column=1, sticky='w')
        
        self.rewatch = IntVar()
        self.CheckbuttonRewatch = Checkbutton(self.FrameMid, text='Assistiria Novamente?', variable=self.rewatch, style='Black.TCheckbutton')
        self.CheckbuttonRewatch.grid(row=0, column=2, padx=5)
        
        self.favorites = IntVar()
        self.checkButtonFavorites = Checkbutton(self.FrameMid, text="Favoritos?", offvalue=0, onvalue=1,
                                                variable=self.favorites, style="Black.TCheckbutton")
        self.checkButtonFavorites.grid(row=0, column=3, padx=(0, 5))
        #endregion
        
        #region Button
        self.button = Button(self.screen, text='Pesquisar', command=lambda: self.SearchButton())
        self.button.grid(row=2, sticky='we')
        
        self.ScreenProperties()
    
    def ScreenProperties(self):
        self.screen.configure(background="#ffffff")
        
        self.screen.iconbitmap("Resources/icon.ico") # Ícone da Janela
        
        self.screen.title("MyAnimePut") # Nome da Janela
        
        self.screen.resizable(False, False) # Não deixa Redimensionar a Janela
        
        self.screen.protocol("WM_DELETE_WINDOW", self.close) # Função de Fechamento da Janela
        
        self.screen.mainloop()
        
    def PlaceHolderEffect(self, event):
        self.entry.configure(state=NORMAL)
        self.entry.delete(0, END)
        self.entry.unbind("<Button-1>", self.click)
        
    def SearchButton(self):
        if self.entry.get() != "Pesquise aqui o Título":
            
            try:
                
                self.link = GenSearch.search(self.entry.get())
                self.informacoes = GenSearch.collect(self.link)
                
                self.informacoes["infoUSER"] = {"opinion": self.ComboboxOpinion.get(), 
                                                "rewatch": bool(self.rewatch.get()), 
                                                "favorites": bool(self.favorites.get())} # Adições do Usuário
                
                self.informacoes["link"] = str(self.link).split("&")[0].split("%")[0]
                
                MoreInfo(self.content, self.informacoes)
                
            except:
                pass
                    
    def ConfigButton(self, event):
        Settings(self.screen)
    
    def close(self):
        for x in os.listdir():
            if ".jpg" in x:
                os.remove(x)
            if '.png' in x:
                os.remove(x)

        self.screen.destroy()