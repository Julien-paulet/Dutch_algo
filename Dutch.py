#!/usr/bin/env python
# coding: utf-8

# In[15]:


import random
import time
import sys

# Classe qui définit un jeu de cartes
class JeuDeCartes:
    def __init__(self):
        # Un jeu possède des cartes de 4 couleurs
        self.paquet = []
        for couleur in ["carreau", "coeur", "pique", "trèfle"]:                         # Pour chaque couleur
            for valeur in list(range(2,11)):                                            # Pour chaque carte numérique
                carte = Carte(couleur, valeur)                                          # Crée l'objet
                self.paquet.append(carte)                                               # Et l'insère dans le paquet
                self.paquet.append(carte) #On joue ici avec deux paquets
            for (nom, valeur) in {"as": 14, "valet": 11, "dame": 12, "roi": 13}.items(): # Pour chaque carte "nommée"
                carte = Carte(couleur, valeur, nom)                                     # Crée l'objet
                self.paquet.append(carte)                                               # Et l'insère dans le paquet
                self.paquet.append(carte)
        self.melange()                                                                  # Mélange automatiquement le paquet
        self.position = 0
        #self.paquetPourDistribue = self.paquet.copy()

    def melange(self):              # Méthode qui
        random.shuffle(self.paquet) # mélange le paquet
        return self.paquet          # et le retourne

    #def choisitCarte(self, paquet=None):         # Méthode qui permet de tirer une carte au hasard
        #carte = ""
        #if (len(self.paquet) > 0):  # s'il en reste au moins une
        #    carte = self.paquet.pop(0)
        #return carte

    def __iter__(self):
        return iter(self.paquet)

    def __next__(self):
        carte = self.paquet[self.position]
        self.position += 1
        return carte

# Classe qui définit les cartes à jouer
class Carte:
    def __init__(self, couleur, valeur, nom=None):
        if not nom: nom = valeur
        self.couleur, self.valeur, self.nom = couleur, int(valeur), nom
    def __str__(self):
        mapping = {"carreau": "♦", "coeur": "♥", "pique": "♠", "trèfle": "♣"}
        return f"{mapping[self.couleur]} {self.nom}"
    def __repr__(self):
        return f"{self.couleur}.{self.nom}"

class Jeu:
    # Constructeur de la classe
    def __init__(self, nbJoueurs=2):
        self.jeu = JeuDeCartes()                   # Instancie le jeu de cartes
        self.nbJoueurs = [] #Pas utile pour le moment, mais il faudra voir ce point
        self.mains = {}
        self.paquet = self.jeu.paquet
        for i in range(nbJoueurs):                 # Pour chaque joueur
            self.mains["joueur" + str(i + 1)] = [] # Crée une main
        self.distribue()                           # Distribue les cartes

    # Méthode qui permet de distribuer les cartes aux joueurs
    def distribue(self):
        nbCartesParJoueur = 4                  # Récupère le nombre de cartes à distribuer en fonction du nombre de joueurs
        for joueur in self.mains:                                  # Pour chaque joueur
            for i in range(nbCartesParJoueur):
                self.mains[joueur].append(self.choisitCarte()) # Pioche les cartes et crée sa main
            
                
    def choisitCarte(self, paquet=None):         # Méthode qui permet de tirer une carte au hasard
        carte = ""
        if (len(self.paquet) > 0):  # s'il en reste au moins une
            carte = self.paquet.pop(0)
        return carte    
    
    def joue(self):                # Méthode à créer obligatoirement
        raise NotImplementedError  # chez les classes filles


# In[16]:


class backend():
    def get_id_card():
        for players in id_players:      #Pour chaque joueur
            for card in players.mains:  #Pour chaque carte dans la main
                id_ = [players, card]   #L'id = le joueur et la carte 
                
#Fonction à revoir et surtout à implémenter dans le tour de jeu et dans la défausse
#En effet les cartes changent en permanence dans le jeu. Il faut que l'id suive

#Pas sur de l'utilité de la fonction, voir avec Adou


# In[21]:


class Dutch(Jeu):    
        # Méthode qui initialise le jeu
    def joue(self):
        deck_pose = []
        
        while len(self.mains) > 1:#Si les joueurs ont encore des cartes
            for joueur in self.mains.items(): #Chaque joueur va faire un tour
                self.tour_de_jeu(joueur[0]) 
                for joueur_ in self.mains.items():
                    self.defausse(joueur_[0], deck_pose)
        print('Fin de la manche') #Si quelqu'un n'a plus de carte alors la manche est finie
        #Il faudra ensuite compté les points si quelqu'un n'a plus de carte
        
    
    def tour_de_jeu(self, joueur):
        print("C'est au joueur :", joueur, "de jouer")
        la_pose = []
        print('La main:', self.mains[joueur])
        pioche_ou_prend = input('pioche ou prend:') #Demande à l'utilisateur s'il pioche ou s'il prend une carte du tas
        if pioche_ou_prend == 'pioche': #Si l'utilisateur pioche
            carte_ = self.choisitCarte() #Alors il prend la carte du dessus du jeu
        
        elif pioche_ou_prend == 'prend': #S'il décide de prendre du jeu pose
            carte_ = deck_pose.pop(0) #Alors il prend la carte du dessus du jeu pose
        
        print("Voici la carte :", carte_)
        ou_mettre_carte = input('Ou mettre la carte:') #user input pour savoir ou mettre la carte
        
        la_pose = self.mains[joueur][int(ou_mettre_carte)]
        self.mains[joueur][int(ou_mettre_carte)] = carte_
        
        deck_pose = la_pose
        print('Deck de pose:', deck_pose)
        ## Reste à gérer les effets, sinon le tour du joueur est fait
        print('La main:', self.mains[joueur])
     
    def use_effect(la_pose):
        if la_pose == 'queen': #Si la carte posée est une reine
            voir_carte = input('Quelle carte voir:') #Le user donne la carte qu'il veut voir
            return carte[voir_carte] #Return la carte demandée 
        ## Fonction à revoir ##
        
    def defausse(self, joueur, deck_pose):
        print("C'est au joueur :", joueur, "de se défausser")
        
        joueur_se_defausse = input('Est-ce que tu te défausses:') #Le joueur décide s'il se défausse ou non
        
        if joueur_se_defausse == 'non':
            pass
        elif joueur_se_defausse == 'oui':
            carte_defausse = input('Position de la carte à défausser:') #Le joueur décide de quelle carte défausser
            carte_defausse_value = self.mains[joueur][int(carte_defausse)]
            if carte_defausse_value == deck_pose: #Faire attention ici check tout et pas seulement la valeur de la carte
                del self.mains[joueur][carte_defausse]
                deck_pose = carte_defausse_value
            else:
                print("Ce n'est pas la bonne carte, tu en prends une en pénalité")
                self.mains[joueur].append(self.JeuDeCartes().choisitCarte())
                print("Voici ta nouvelle main:", self.mains[joueur])


# # Test du jeu

# In[ ]:


#game = Dutch()
#game.joue()


# In[ ]:




