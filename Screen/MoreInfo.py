from tkinter import *
from tkinter.ttk import Button
from tkinter.messagebox import showerror

from PIL import Image, ImageTk
from os import startfile

import Functions.Integration as Integration
import Functions.Treatments as Treatments

from Functions.WidgetsBuilder import LabelB, FrameB

from threading import Thread

class MoreInfo:
    def __init__(self, content, informacoes: dict):
        """
        ~ Exemplo de Funcionamento de informacoes:
            * {"title": titulo,
            "infoMAL": {
                "season": season, 
                "studio": studio, 
                "score": {"score": pontuacao, "users": usuarios}, 
                "statistics": [ranking, popularidade, membros], 
                "genres": generos, "image": imagem}
                },
            "infoUSER": {
                "opinion": opinion, 
                "rewatch": rewatch
                }, 
            "link": link}
        """
        
        self.screen = Toplevel()
        self.screen.withdraw()
        self.screen.iconbitmap("Resources/icon.ico")
        self.screen.resizable(False, False)
        
        # region Treatments
        informacoes["title"] = Treatments.TitleTreatment(informacoes["title"])
        
        generos = str(str(informacoes["infoMAL"]["genres"]).replace("'", "")[1:-1])
        generos = Treatments.GenreTreatment(generos)
        
        studio = Treatments.StudioTreatment(informacoes['infoMAL']['studio'])
        # endregion
        
        IMG = ImageTk.PhotoImage(Image.open(informacoes["infoMAL"]["image"]))
        
        # region Top
        self.FrameTop = Frame(self.screen, bg="#e1e7f5")
        self.FrameTop.pack(fill=X)

        LabelB(self.FrameTop, informacoes["title"], 12, weight="bold", mode=False).pack(padx=5, pady=5, anchor=W, side=LEFT)
        
        # endregion
        
        Frame(self.screen, background="#1d439b").pack(fill=X)
        
        # region Mid
        self.FrameMid = Frame(self.screen, bg="white")
        self.FrameMid.pack(fill="x")

        # region MidLeft
        self.FrameMidLeft = Frame(self.FrameMid, bg="white")
        self.FrameMidLeft.grid(row=0, column=0)
        
        image = Label(self.FrameMidLeft, image=IMG, background="black", highlightthickness = 0, bd = 0)
        image.bind("<Button-3>", lambda event: startfile(informacoes['link']))
        image.pack(padx=(5, 0), pady=5)
        # endregion

        # region MidRight
        self.FrameMidRight = Frame(self.FrameMid, bg="white")
        self.FrameMidRight.grid(row=0, column=1, sticky="ns")
        
        # region Informações do MyAnimeList
        self.FrameMAL = FrameB(self.FrameMidRight)
        self.FrameMAL.pack(padx=5, pady=5, fill=BOTH, side=TOP)

        self.FrameMAL_Score = FrameB(self.FrameMAL, False)
        self.FrameMAL_Score.grid(row=0, column=0, padx=5, pady=5)
        
        Label(self.FrameMAL_Score, text="SCORE", background="#2e51a2", foreground="white", font="Tahoma 7 bold").grid(row=0, column=0, ipadx=10)
        
        LabelB(self.FrameMAL_Score, informacoes['infoMAL']['score']['score'], 17, weight="bold").grid(row=1, column=0)
        LabelB(self.FrameMAL_Score, informacoes['infoMAL']['score']['users'], 7).grid(row=2, column=0)
        
        Frame(self.FrameMAL, background="#d8d8d8").grid(row=0, column=1, sticky="ns", pady=5, padx=(0, 5))
        
        LabelB(self.FrameMAL, informacoes['infoMAL']['season'], 10).grid(row=0, column=2)
        
        Frame(self.FrameMAL, background="#d8d8d8", height=20).grid(row=0, column=3, pady=5, padx=5)
        
        if len(studio) > 15 * (studio.count("\n") + 1):
            SIZE = 8
        else:
            SIZE = 10
        
        LabelB(self.FrameMAL, studio, SIZE, mode=False).grid(row=0, column=4, padx=(0, 5))
        # endregion
        
        # region Ranking e Button
        # FrameMidRightMid: Sim, eu não tive outra ideia de nome...
        self.FrameMRM = FrameB(self.FrameMidRight)
        self.FrameMRM.pack(padx=5, pady=(0, 5), fill=BOTH)
        
        LabelB(self.FrameMRM, "Ranked", 11).grid(row=0, column=0, padx=(5, 0))
        LabelB(self.FrameMRM, informacoes['infoMAL']['statistics'][0], 11, "#323232", "bold").grid(row=0, column=1)
        
        self.SeparatorFrame = Frame(self.FrameMRM, height=20, bg="#d8d8d8")
        self.SeparatorFrame.grid(row=0, column=2, padx=5)
        
        LabelB(self.FrameMRM, "Popularity", 11).grid(row=0, column=3)
        LabelB(self.FrameMRM, informacoes['infoMAL']['statistics'][1], 11, "#323232", "bold").grid(row=0, column=4, padx=(0, 5))
        
        self.FrameButton = FrameB(self.FrameMRM, False)
        self.FrameButton.grid(row=1, columnspan=5, sticky="nswe", padx=5, pady=(0, 5))
        
        Button(self.FrameButton, text="Adicionar na Lista", command=lambda: self.TitleAppend(informacoes, content)).pack(fill=BOTH, expand=True)
        # endregion
        
        # region Informações do Usuário
        self.FrameInfo = Frame(self.FrameMidRight, background="white")
        self.FrameInfo.pack(padx=5, pady=(0, 5), fill=BOTH)
        
        # region Gêneros
        self.FrameGeneros = FrameB(self.FrameInfo, False)
        self.FrameGeneros.grid(row=0, sticky="w")
        
        LabelB(self.FrameGeneros, "Gêneros", 12, weight="bold", foreground="#444444").grid(row=0, column=0, sticky="w", padx=(5, 0))
        Frame(self.FrameGeneros, background="#ebebeb").grid(row=0, column=1, sticky="wns", padx=5)
        LabelB(self.FrameGeneros, generos, 10, mode=False).grid(row=0, column=2, sticky="we")
        # endregion
        
        Frame(self.FrameInfo, bg="#bebebe").grid(row=1, sticky="we", pady=5)
        
        # region Frame infoUSER
        LabelB(self.FrameInfo, f"Opinião Pessoal: {informacoes['infoUSER']['opinion']}", 12, "#444444", "bold").grid(row=2, sticky="w", padx=5)
        
        Frame(self.FrameInfo, bg="#bebebe").grid(row=3, sticky="we", pady=5)
        
        LabelB(self.FrameInfo, f"Assistiria Novamente? {self.ShowBool(informacoes['infoUSER']['rewatch'])}", 12, "#444444", "bold").grid(row=4, sticky="w", padx=5)
        
        Frame(self.FrameInfo, bg="#bebebe").grid(row=5, sticky="we", pady=5)
        
        LabelB(self.FrameInfo, f"Favoritos? {self.ShowBool(informacoes['infoUSER']['favorites'])}", 12, "#444444", "bold").grid(row=6, sticky="w", padx=5)
        
        self.lastFrame = Frame(self.FrameInfo, bg="#bebebe")
        self.lastFrame.grid(row=7, sticky="we", pady=(5, 0))
        # endregion
        
        # endregion
        
        # endregion
        
        # endregion
        
        # region Soluções de Esoaçamento
        self.screen.update()
        
        # Para Pegar o Tamanho da Imgem
        self.IMGSize = self.GetIMGSize(informacoes)
        
        self.FrameMAL_width = self.FrameMAL.winfo_width()
        Frame(self.FrameButton, width=self.FrameMAL_width - 10, height=0, background="#f6f6f6").pack()
        
        Frame(self.FrameMRM, width=0, height=self.IMGSize['h'] - (self.FrameMAL.winfo_height() + self.FrameInfo.winfo_height() + 10 + 3)).grid(column=5, row=0, rowspan=2)
        
        self.FrameButton.config(height=self.FrameMRM.winfo_height() - (self.SeparatorFrame.winfo_height() - 10))
        
        self.lastFrame.config(width=self.FrameMAL.winfo_width())
        # endregion
        self.screen.deiconify()
        self.screen.mainloop()
    
    def ShowBool(self, var: bool):
        if var == True:
            return "✔"
        else:
            return "❌"
    
    def GetIMGSize(self, informacoes):
        arquivo = informacoes['infoMAL']['image']

        with Image.open(arquivo) as img:
            width, height = img.size

        return {"w": width, "h": height}
    
    def TitleAppend(self, info, content):
        try:
            Thread(target = Integration.Add, args = (info, content.page)).start()
            self.screen.destroy()
        except AttributeError:
            showerror("Erro", "Não foi possível adicionar a lista.\nVerifique se o seu token está correto.")