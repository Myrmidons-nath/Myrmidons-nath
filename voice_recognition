
import pyttsx3 
import webbrowser
import time
import speech_recognition as sr  


#variable necaissaire modules----------------------------------------
r  = sr.Recognizer()

#creations des variables principals---------------------------------
boucle = True

commandes = """les commandes sont les suivantes : 
- internet (pour ouvrir une fenetre internet)
- dicteur (pour se faire dicter un texte)
- bye (pour fermer le programme)
- créateur (pour avoir des infos sur mon créateur)
"""


boucle_principal = True 

variable_choix_principal = """ > vous voulez le logiciel en textuel ou en reconaissance vocal(t/r); 
    la reconaissance vocal peut potentiellement  disfonctionner à cause de votre connexion internet,
    si vous utilisez la reconaissance vocal veuillez parler distinctement et n'enchainer pas la commande plusieur fois 
     > """

#fonctions principals------------------------------------------------

def assistant_voix(sortie):
    if sortie != None:
        voix = pyttsx3.init()
        voix.say(sortie)
        voix.runAndWait()



assistant_voix("bonjour, je m'appelle Flhavwère")



def createur():
    time.sleep
    assistant_voix("j'ai été créer par nathan, un codeur en python")
    assistant_voix("voulez-vous contacter mon créateur ? ")
    contacter_createur = input(" >> ")
    if contacter_createur == "oui":
        assistant_voix("voici son serveur discorde , il es proprio et s'appelle nathan dev")
        print("https://discord.gg/fbRZhrFQdF")
    elif contacter_createur == "non":
        assistant_voix("tres bien")
def internet():
    time.sleep(0.5)
    assistant_voix("une fenetre s'est ouverte")
    webbrowser.open_new("http://google.com")
    
def youtube():
    time.sleep(0.5)
    assistant_voix("une fenetre s'est ouverte")
    webbrowser.open_new("https://www.youtube.com")

def bye():
    assistant_voix("d'accord je me déconnecte .")
    
def ecole_direct():
    time.sleep(0.5)
    assistant_voix("une fenetre s'est ouverte")
    webbrowser.open_new("https://www.ecoledirecte.com/")

def heure():
    print(time.ctime())
    assistant_voix(time.ctime())

def sinon():
    assistant_voix("desoler, je n'ai pas compris la commande que vous avez fais, veuillez respecter les noms des commandes")
    assistant_voix("si vous voulez des infos sur les commandes, tapez aide")

def dicteur():
    time.sleep(0.5)
    assistant_voix("tres bon choix, veuillez saisir votre texte")
    time.sleep(0.3)
    texte_a_dicter = input(" >> ")
    assistant_voix(texte_a_dicter)

def discution():
    assistant_voix("salut a toi")
    assistant_voix("je suis desoler mon createur ne ma pas confectionner pour une discution mais pour des fonctions pratiques")

def secret():
    print("nathan es fier de toi, tu as debloquer une fonction special, tape mtn > 789456474745454747474544")
    while boucle:
        demande_principal = input(" >> ")
        if demande_principal == "789456474745454747474544":
            azertyuiopmlkjhgfdsqwxcvbn()
            break

def aide():
    print(commandes)

def azertyuiopmlkjhgfdsqwxcvbn():
    print("dis 'la vie c'est comme une boite de chocolat, on ne sait jamais sur quoi on va tomber' a mon createur")

def boucle_t():
    while boucle :
        
        time.sleep(0.5)
        demande_principal = input(" > ")
        if demande_principal == "aide":
            aide()
            continue
        if demande_principal == "dicteur" :
            dicteur()
            continue
        if demande_principal == "internet" :
            internet()
            continue
        if demande_principal == "bye" :
            break
        if demande_principal == "créateur":
            createur()
            continue
        if demande_principal == "youtube":
            youtube()
            continue
        if demande_principal == "ecole_direct" or demande_principal == "ecoledirect":
            ecole_direct()
            continue
        if demande_principal == "heure":
            heure()
            continue
        if demande_principal == "salut" or demande_principal == "boujour" or demande_principal == "yo" or demande_principal == "wesh":
            discution()
            continue
        if demande_principal == "nathancreateurazerty134":
            secret()
            continue
        else:
            sinon()
            continue
            
def boucle_r():
    while boucle :
            time.sleep(0.5)
            with sr.Microphone() as source:
                print("Dites quelque chose")
                audio = r.listen(source)
            try:

                demande_principal = r.recognize_google(audio, language="fr-FR")
                print(" >" + demande_principal)
                if demande_principal == "aide":
                    aide()
                    continue
                if demande_principal == "dicteur" :
                    dicteur()
                    continue
                if demande_principal == "internet" :
                    internet()
                    continue
                if demande_principal == "bye" :
                    bye()
                    break
                if demande_principal == "créateur":
                    createur()
                    continue
                if demande_principal == "youtube":
                    youtube()
                    continue
                if demande_principal == "ecole_direct" or demande_principal == "ecoledirect":
                    ecole_direct()
                    continue
                if demande_principal == "heure":
                    heure()
                    continue
                if demande_principal == "salut" or demande_principal == "boujour" or demande_principal == "yo" or demande_principal == "wesh":
                    discution()
                    continue
                if demande_principal == "nathancreateurazerty134":
                    secret()
                    continue
                else:
                    sinon()
                    break
            except sr.UnknownValueError:
                print("L'audio n'as pas été compris")
            except sr.RequestError as e:
                print("Le service Google Speech API ne fonctionne plus" + format(e))


while boucle_principal :
    choix_principal = input(variable_choix_principal) 
    if choix_principal == "r": 
        boucle_r()
        break
    if choix_principal == "t":
        boucle_t()
        break
    else:
        print()

