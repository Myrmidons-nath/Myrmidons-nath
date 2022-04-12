"""
chiffrer
"""
liste=['a','b','c','d','e','f','g','h','i','j','k','m','n','l','o','p','q','r','s','t','u','v','w','x','y','z']
for x in range(len(liste)):    #Dédouble la liste
    liste.append(liste[x])


message = input("message a chiffrer : ")

a = 0
while a < 27 :
    clef = int(a)  #on précise le type, sinon Python le considère comme un string
    def chiffrage_lettre(lettre,liste,clef):
        for i in range(len(liste)):
            if lettre==' ':       #au cas ou il y a un espace
                return ' '
            elif liste[i]==lettre:
                return str(liste[i+clef])
        return '?'  #en cas de caractère inconnu
    message_chiffré = str()
    for lettre in message:
        message_chiffré += chiffrage_lettre(lettre,liste,clef)
    print(message_chiffré)
    a+=1


