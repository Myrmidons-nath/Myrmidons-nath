
print("application pour calculer diverse aires, volumes et perimetre")
boucle = True

#rectangle/pave droits debut

def rectangle():
    rectangle_demande = input("que voulez vous calculer(aire ou perimetre) ??")
    
    if rectangle_demande == "aire" :
        aire_rectangle()
        
    
    if rectangle_demande == "perimetre" :
        perimetre_rectangle()


def perimetre_rectangle():
    perimetre_rectangle_longueur_cotés_A = int(input("quelle est le nombre de centimetre du coté A ? ?"))
    perimetre_rectangle_longueur_cotés_B = int(input("quelle est le nombre de centimetre du coté B ? ?"))
    resultat_perimetre_rectangle = perimetre_rectangle_longueur_cotés_A + perimetre_rectangle_longueur_cotés_B
    resultat_perimetre_rectangle *= 2
    print("l'aire de ton rectangle est de ", resultat_perimetre_rectangle , "cm")
    
def aire_rectangle():
    aire_rectangle_longueur_cotés_A = int(input("quelle est le nombre de centimetre du coté A ? ?"))
    aire_rectangle_longueur_cotés_B = int(input("quelle est le nombre de centimetre du coté B ? ?"))
    resultat_aire_rectangle = aire_rectangle_longueur_cotés_A * aire_rectangle_longueur_cotés_B
    print("l'aire de ton rectangle est de ", resultat_aire_rectangle, "cm²")
    
    
def volume_pave_droits():
    volume_pave_droit_longueur_largeur = int(input("quelle est le nombre de centimetre de la largeur"))
    volume_pave_droit_longueur_longeur = int(input("quelle est le nombre de centimetre de la longeur"))
    volume_pave_droit_longueur_hauteur = int(input("quelle est le nombre de centimetre de la hauteur"))
    resultat_volume_pave_droits = volume_pave_droit_longueur_largeur * volume_pave_droit_longueur_longeur * volume_pave_droit_longueur_hauteur
    print("le volume de ton carré es de ", resultat_volume_pave_droits, "cm3")    
    
    
#rectangle/pave droits fin




#cubes/carre debut
def volume_cubes():
    volume_carre_longueur_cotés = int(input("quelle est le nombre de centimetre par arrêtes ?"))
    resultat_volume_carre = volume_carre_longueur_cotés * volume_carre_longueur_cotés * volume_carre_longueur_cotés
    print("le volume de ton carré es de ", resultat_volume_carre, "cm3")

def perimetre_carre():
    perimetre_carre_longueur_cotés = int(input("quelle est le nombre de centimetre par cotés ?"))
    resultat_perimetre_carre = perimetre_carre_longueur_cotés * 4
    print("le perimetre de ton carré es de ", resultat_perimetre_carre, "cm")    
    


def aire_carre():
    aire_carre_longueur_cotés = int(input("quelle est le nombre de centimetre par cotés ?"))
    resultat_aire_carre = aire_carre_longueur_cotés * aire_carre_longueur_cotés 
    print("l'aire de ton carré es de ", resultat_aire_carre, "cm²")
    
    
def carre():
    carre_demande = input("que voulez vous calculer(aire ou perimetre) ??")
    
    if carre_demande == "aire" :
        aire_carre()
        
    
    if carre_demande == "perimetre" :
        perimetre_carre()
        
#cubes/carre fin        
        
        


while boucle == True :
    demande_figure_geometrique = input("quelle est la figure geometrique que tu veux calculer (carre, cubes/rectangle, pave droits/ triangle, pyramides / cercle, cylindre, sphere/)? (sortie)  :")
    if demande_figure_geometrique == "carre":
        carre()
        break
    if demande_figure_geometrique == "cubes" :
        volume_cubes()
        break
    if demande_figure_geometrique == "rectangle" :
        rectangle()
        break
    if demande_figure_geometrique == "sortie" :
        print("au revoir")
        break
    if demande_figure_geometrique == "pave droits" :
        volume_pave_droits()
        break
    
