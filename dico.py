from tkinter import *
from time import *
import wikipedia
fenetre = Tk()
fenetre.title("dico")
fenetre.geometry('700x500')
fenetre.configure(bg='#9FEAA7')
v = StringVar()   #importation de la zone de saisie StringVar
e = Entry(fenetre, textvariable=v, width=50, fg="black")
e.pack()    #insertion de la zone de saisie
Button(fenetre, text="Annuler", command = fenetre.destroy).pack()
def reponse():
    
    wikipedia.set_lang("fr")
    
    champ_label = Label(fenetre, text= wikipedia.summary(e.get(), sentences=1)).pack()  #Insertion des Labels
Button(fenetre, text="Valider", command=reponse).pack() #Bouton qui verifie que le mot de passe est bon
fenetre.mainloop()
