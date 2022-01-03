from tkinter import *
import numpy as np

c = ["#3B2E8C", "#5D4AD9","#222340", "#1A1A1A", "#F2F2F2"] #paleta de cores // color pallete
app = Tk()
app.title("Register1.0")
app.geometry("220x340")
app.configure(background= c[0])

def aplicar():
    nome = Vname.get()
    email = Email.get()
    telefone = tel.get()
    observacao = OBS.get("1.0", "end")
    arr1 = nome+', '+email+', '+telefone+', '+observacao
    try:
        name_arq = "register.txt"
        arquivo = open(name_arq, 'a')
        arquivo.writelines(arr1)
    except FileNotFoundError:
        arquivo = open(name_arq, 'w+')
        arquivo.writelines(arr1)
    arquivo.close()
    

Label(app, text ="NAME", background =c[4], foreground = c[3], anchor = W).place(x =10, y =10, width = 100, height = 20)
Vname = Entry(app)
Vname.place(x=10, y = 30, width = 200, height =20)

Label(app, text ="E-mail", background =c[4], foreground = c[3], anchor = W).place(x =10, y =60, width = 100, height = 20)
Email = Entry(app)
Email.place(x=10, y = 80, width = 200, height =20)

Label(app, text ="TELEPHONE", background =c[4], foreground = c[3], anchor = W).place(x =10, y =110, width = 100, height = 20)
tel = Entry(app)
tel.place(x=10, y = 130, width = 200, height =20)

Label(app, text ="NOTE", background =c[4], foreground =c[3], anchor = W).place(x =10, y =160, width = 100, height = 20)
OBS = Text(app)
OBS.place(x=10, y = 180, width = 200, height =120)

botao = Button(app,height = 20, width = 20, text = "REGISTER", command = aplicar)
botao.place(x = 10, y=300, width = 200, height = 20)

app.mainloop()
