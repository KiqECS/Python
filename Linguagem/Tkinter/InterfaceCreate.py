from tkinter import *

app=Tk()
app.title("Teste")
app.geometry("500x300")
app.configure(background = "white")

txt = Label(app,text="Olá",bg="yellow",fg="black")
txt.place(x=10,y=20,width=100,height=100)

txt = Label(app,text="Tchau",bg="yellow",fg="black")
txt.pack(ipadx=20,ipady=15,padx=10,pady=10,side="bottom",expand=True,fill=X)
app.mainloop()


