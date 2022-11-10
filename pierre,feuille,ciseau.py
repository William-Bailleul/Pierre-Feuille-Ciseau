#DEBUT
#On admet une fonction random qui retourne un chiffre aléatoire entre 0 et 2
#On admet une fonction input qui recupere le saisi d'un joueur lors de son execution
#On définit une fonction PierreFeuilleCiseau qui prend en argument nombrePartiePourGagner(le nombre de round pour gagner la partie)(!!! un nombre impair !!!)
    #On initialise la variable scoreOrdinateur à 0
    #On initialise la variable scoreJoueur à 0
    #Tant que scoreOrdinateur OU scoreJoueur est différent de nombrePartiePourGagner
        #Alors on assigne a choixOrdinateur le retour de l'execution de la fonction random
        #Alors on assigne a choixJoueur le retour de l'execution de la fonction input (avec la question "feuille, pierre ou ciseau ?")
        #Si le retour de l'execution de la fonction input est "pierre"
            #Alors la variable choixJoueur prend la valeur 0
        #OU SINON le retour de l'execution de la fonction input est "feuille"
            #Alors la variable choixJoueur prend la valeur 1
        #OU SINON le retour de l'execution de la fonction input est "ciseau"
            #Alors la variable choixJoueur prend la valeur 2
        #Si la valeur de choixOrdinateur est différente de valeur de choixJoueur
            #Si choixOrdinateur est égal à 0 
                #Si choixJoueur est égal à 1
                    #Alors incrementer de 1 scoreJoueur
                #Si choixJoueur est égal à 2
                    #Alors ajouter 1 à scoreOrdinateur
            #Si choixOrdinateur est égal à 1
                #Si choixJoueur est égal à 0
                    #Alors incrementer de 1 scoreOrdinateur
                #Si choixJoueur est égal à 2
                    #Alors incrementer de 1 scoreJoueur
            #Si choixOrdinateur est égal à 2 
                #Si choixJoueur est égal à 0
                    #Alors incrementer de 1 scoreJoueur
                #Si choixJoueur est égal à 1
                    #Alors incrementer de 1 scoreOrdinateur
    #Si scoreOrdinateur est égal nombrePartiePourGagner
        #Alors on afficher un message de défaite
    #Sinon
        #Alors on affiche un message de victoire
#FIN