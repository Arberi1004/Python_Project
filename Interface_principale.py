import moteur_de_recherche as P2
import tkinter as tk


root = tk.Tk()
root.title("Spotify Search engine")

frameQuete = tk.Frame(root) 
frameQuete.pack(side=tk.TOP, fill="x", padx=10, pady=10) 


def open_quete1():
     
    text_area.config(state="normal") 
    text_area.delete(1.0,tk.END) 
    text_area.insert(tk.INSERT,P2.quete1(titre1.get(), artiste1.get())) 
    text_area.configure(state='disabled') 


def open_quete2():
     
    text_area.config(state="normal") 
    text_area.delete(1.0,tk.END) 
    text_area.insert(tk.INSERT,P2.quete2(artiste2.get(), pays2.get(), date2.get()))
    text_area.configure(state='disabled')     

def open_quete3():
    text_area.config(state="normal") 
    text_area.delete(1.0,tk.END) 
    text_area.insert(tk.INSERT,P2.quete3(genre3.get(), pays3.get(), date3.get()))
    text_area.configure(state='disabled')   

def open_quete4():
    text_area.config(state="normal") 
    text_area.delete(1.0,tk.END) 
    text_area.insert(tk.INSERT,P2.quete4(artiste4.get()))
    text_area.configure(state='disabled')         
    

#Sous frame pour afficher les formulaires de recherche des quêtes. 1 frame par quête
    

quete1 = tk.Frame(frameQuete, borderwidth=2, highlightthickness=3, highlightbackground="pink", relief=tk.GROOVE)
quete1.pack(side=tk.LEFT, padx=0, pady=1)

quete2 = tk.Frame(frameQuete, borderwidth=2, highlightthickness=3, highlightbackground="pink", relief=tk.GROOVE)
quete2.pack(side=tk.LEFT, padx=0, pady=2)

quete3 = tk.Frame(frameQuete, borderwidth=2, highlightthickness=3, highlightbackground="pink", relief=tk.GROOVE)
quete3.pack(side=tk.LEFT, fill = 'x', padx=0, pady=3)

quete4 = tk.Frame(frameQuete, borderwidth=2, highlightthickness=3, highlightbackground="pink", relief=tk.GROOVE)
quete4.pack(side=tk.LEFT, fill = 'x', padx=0, pady=4)

#Formulaire Quete 1

label = tk.Label(quete1, text="Quête 1")
label.pack()

label = tk.Label(quete1, text="Titre :")
label.pack()
titre1 = tk.Entry(quete1, width=50) 
titre1.pack()

label = tk.Label(quete1, text="Artiste :")
label.pack()
artiste1 = tk.Entry(quete1, width=50) 
artiste1.pack()

button1 = tk.Button(quete1, text= "Recherche", bg='light blue', command=open_quete1)
button1.pack(side='left', fill = 'x', expand = True)

#Formulaire Quete 2

label = tk.Label(quete2, text="Quête 2")
label.pack()

label = tk.Label(quete2, text="Artiste :")
label.pack()
artiste2 = tk.Entry(quete2, width=50)
artiste2.pack()

label = tk.Label(quete2, text="Pays :")
label.pack()
pays2 = tk.Entry(quete2, width=50)
pays2.pack()

label = tk.Label(quete2, text="Date :")
label.pack()
date2 = tk.Entry(quete2, width=50)
date2.pack()
 

button2 = tk.Button(quete2,text= "Recherche", bg='light blue',command=open_quete2)
button2.pack(side='left', fill = 'x', expand = True)

#Formulaire Quete 3

label = tk.Label(quete3, text="Quête 3")
label.pack()

label = tk.Label(quete3, text="Genre :")
label.pack()
genre3 = tk.Entry(quete3, width=50)
genre3.pack()

label = tk.Label(quete3, text="Pays :")
label.pack()
pays3 = tk.Entry(quete3, width=50)
pays3.pack()

label = tk.Label(quete3, text="Date :")
label.pack()
date3 = tk.Entry(quete3, width=50)
date3.pack()

button3 = tk.Button(quete3,text="Recherche", bg = 'light blue',command=open_quete3)
button3.pack(side='left', fill = 'x', expand = True)

#Formulaire Quête 4

label = tk.Label(quete4, text="Quête 4")
label.pack()

label = tk.Label(quete4, text="Artiste :")
label.pack()
artiste4 = tk.Entry(quete4, width=50)
artiste4.pack()


button4 = tk.Button(quete4,text="Recherche", bg= 'light blue', command=open_quete4)
button4.pack(side='left', fill = 'x', expand = True)

#Frame qui nous permettra d'afficher les résultats des recherches

frameRes = tk.Frame(root, borderwidth=2, relief=tk.GROOVE) 
frameRes.pack(side="bottom", fill="x", expand = True )
text_area = tk.Text(frameRes, width = 700,  height = 700) 
text_area.config(state="normal")

text_default = "Résultat des quêtes"
            
text_area.insert(tk.INSERT,text_default)
text_area.configure(state='disabled')
text_area.pack(side=tk.BOTTOM, fill="x", expand=True)    

    
    
root.mainloop()