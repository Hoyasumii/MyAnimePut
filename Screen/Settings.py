import json, os

from tkinter import ttk
from tkinter import *

from tkinter.messagebox import *

from Functions.WidgetsBuilder import *

class Settings:
    def __init__(self, master):
        self.master = master
        
        #region JsonFile
        with open("Resources/cache.json", 'r') as file:
            self.doc = json.load(file)
        #endregion
        
        self.screen = Toplevel()
        
        #region FrameTop
        self.FrameTop = Frame(self.screen, background="#e1e7f5")
        self.FrameTop.pack(fill="x")
        
        LabelB(self.FrameTop, "Configurações", 12, weight="bold", mode=False).pack(padx=5, pady=(5, 0), side="left")
        Frame(self.screen, background="#1d439b").pack(fill=X)
        #endregion
        
        #region FrameToken
        self.FrameToken = FrameB(self.screen)
        self.FrameToken.pack(padx=5, pady=5, fill=BOTH, side=TOP)
        
        LabelB(self.FrameToken, "Token", 8, weight="bold", mode=False).grid(row=0, column=0, padx=5, pady=(2, 3), sticky="w")
        
        self.entryToken = Entry(self.FrameToken, width=50, font=("Tahoma", 10), border=False)
        self.entryToken.grid(row=1, columnspan=5, padx=5, pady=(0, 5))
        
        self.entryToken.insert(0, self.doc["token"])
        self.entryToken.configure(state="readonly")
        self.phE_token = self.entryToken.bind("<Button-1>", self.PlaceHolder1)#TODO: Adicionar Função
        #endregion
        
        #region FramePage
        self.FramePage = FrameB(self.screen)
        self.FramePage.pack(padx=5, pady=(0, 5), fill=BOTH, side=TOP)
        
        LabelB(self.FramePage, "Page", 8, weight="bold", mode=False).grid(row=0, column=0, padx=5, pady=(2, 3), sticky="w")
        
        self.entryPage = Entry(self.FramePage, width=50, font=("Tahoma", 10), border=False)
        self.entryPage.grid(row=1, columnspan=5, padx=5, pady=(0, 5))
        
        self.entryPage.insert(0, self.doc["page"])
        self.entryPage.configure(state="readonly")
        self.phE_page = self.entryPage.bind("<Button-1>", self.PlaceHolder2)#TODO: Adicionar Função
        #endregion
        
        ttk.Button(self.screen, text="Salvar Alterações", command=lambda: self.Update()).pack(fill=X)
        
        self.ScreenProperties()
        
    def ScreenProperties(self):
        self.screen.iconbitmap("Resources/icon.ico")
        
        self.screen.configure(background="#ffffff")
        
        self.screen.title("MyAnimePut - Configurações")
        
        self.screen.resizable(False, False)
        
        self.screen.mainloop()
        
    def PlaceHolder1(self, event):
        self.entryToken.configure(state="normal")
        self.entryToken.unbind("<Button-1>", self.phE_token)
    
    def PlaceHolder2(self, event):
        self.entryPage.configure(state="normal")
        self.entryPage.unbind("<Button-1>", self.phE_page)
        
    def Update(self):
        self.doc["token"] = self.entryToken.get()
        self.doc['page'] = self.entryPage.get()
        
        with open("Resources/cache.json", 'w') as file:
            json.dump(self.doc, file, indent=4)
        
        showinfo("Sucesso", "Alterações salvas com sucesso!")
        
        self.close()
        self.master.destroy()
        
    def close(self):
        for x in os.listdir():
            if ".jpg" in x:
                os.remove(x)
            if '.png' in x:
                os.remove(x)

        self.screen.destroy()
            
        
