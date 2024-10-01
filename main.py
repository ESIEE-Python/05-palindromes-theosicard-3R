#### Fonction secondaire
'''
Ceci est une fichier permettant de tester si une chaine est un palindrome. 
'''

def ispalindrome(p):
    '''
    Cette fonction permet de vérifié si une chaine est in palindrome.
    arg: p --> chaine de caractère.
    return: si vrai --> True 
            si faux --> False
    '''

    #Varibales
    chaine_filtre = ""

    #Liste de caractère à remplacer
    gest_accent = {
                  'é':'e', 'à':'a','è':'e','ê':'e','ë':'e',
                  '!':'','?':'',',':'','ç':'c','ô':'o',
                  }

    table = str.maketrans(gest_accent)

    #Mise en minuscule du text
    p = p.lower().translate(table)

    #Formate la chaine correctement
    for char in p:
        if 'a' <= char <= 'z' or '0' <= char <= '9':
            chaine_filtre += char

    #Retrait des espaces
    p = ''.join(chaine_filtre)

    #inverse la chaine formater
    reverse = p[::-1]

    #Comparaison de la chaine et de la chaine inversé
    if p == reverse:
        return True
    return False

#### Fonction principale
def main():
    '''
    Fonction principal,permettant d'appeler la fonction ispalindrome
    '''
    # vos appels à la fonction secondaire ici
    chaine = "test"
    print(f"{chaine} {ispalindrome(chaine)}")

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
