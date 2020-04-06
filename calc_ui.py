import tkinter as tk

class App:
    def __init__(self,main,name):
        self.master = main
        self.master.title(name)
        self.master["background"] = "grey"                 
        self.topFrame = tk.Frame(self.master)
        self.topFrame["background"] = "red"
        self.topFrame.pack(fill=tk.BOTH,expand=1)
        self.topFrame.pack()

    def add_main_label(self,msg):
        self.label = tk.Label(self.topFrame,text=msg)
        self.label["background"] = "yellow"
        #self.label.pack()
        self.label.grid(row=0 ,column=0)

    def add_button(self,name,rrr=None,ccc=None):
        self.button=tk.Button(self.topFrame)
        self.button["text"]=name
        self.button["background"]="green"
        #self.button.place(x=75,y=50)
        #self.button.pack()
        self.button.grid(row=rrr ,column=ccc)
        #self.button.bind("<Button-1>",self.echoname)
        self.button.bind("<Button-1>",self.readinput)
        

    def echoname(self,event):
        print(event.widget["text"])

    def add_input(self):
        self.inp=tk.Entry(self.topFrame)
        self.inp.grid(row=0,column=1)
        self.inp.bind("<Return>",self.readinput)

    def readinput(self,event):
        print(self.inp.get())


root=tk.Tk()
CalcApp=App(root,"Calculator")
CalcApp.add_main_label("This is my calculator")
CalcApp.add_button("OK",1,2)
CalcApp.add_button("NOT OK",5,7)
#CalcApp.add_button("OK")
CalcApp.add_input()
root.mainloop()
