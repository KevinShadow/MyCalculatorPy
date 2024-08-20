from tkinter import *

class Calco(Tk):
    def  __init__(self):
    	Tk.__init__(self)
    	self.title("Ma Calculatrice")
    	self.geometry("300x300")
    	self.entre=StringVar(value="")
    	self.l=Entry(self, textvariable=self.entre)
    	self.l.grid(row=0, columnspan=4)
    	self.initial()
    def initial(self):
    	touch=["1","2","3","4","5","6","7","8","9","0","(",")","-","+","*","/","c","="]
    	self.position(touch)
    def position(self,touch):
    #c pour colone et r pour ligne
    	c=0
    	r=1
    	for i in range(len(touch)):
    		self.p=Button(self, text=touch[i],command=lambda valeur=touch[i]:self.merci(valeur))
    		self.p.grid(row=r, column=c)
    		c=c+1
    		print(r,c)
    		if c > 3:
    			c=0
    			r=r+1
    			
    def merci(self, t):	
    	if t == "=":
    		self.evluexp()
    	if t == "c":
    		self.entre.set("")
    	if t in ["1","2","3","4","5","6","7","8","9","0","-","+","*","/","(",")"]:
    		self.ecrit(t)
    		
    def ecrit(self,t):
    	self.d=self.l.get()
    	self.entre.set(self.d+t)
    	
    def evluexp(self):
    	expression = self.l.get()
    	try:
    		resultat = eval(expression)
    		self.entre.set(resultat)
    	except Exception as e:
    		self.entre.set("erreur")
if __name__ == "__main__":
    fen = Calco()
    fen.mainloop()
