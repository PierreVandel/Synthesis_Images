import Modele

class ControleurCourbes(object):
    """ Gere un ensemble de courbes. """
    def __init__(self):
        self.courbes = []
       
    def ajouterCourbe(self, courbe):
        """ Ajoute une courbe supplementaire.  """
        self.courbes.append(courbe) 

    def dessiner(self, dessinerControle, dessinerPoint, enabled):
        """ Dessine les courbes. """
        # dessine les point de la courbe
        for courbe in self.courbes:
            courbe.dessinerPoints(dessinerPoint)
        
        #si la courbe peut etre remplie
        for courbe in self.courbes:
                courbe.remplir(dessinerPoint)

          
        # dessine les point de controle
        if enabled:
            for courbe in self.courbes:
                courbe.dessinerControles(dessinerControle)


    def deplacerControle(self, ic, ip, point):
        """ Deplace le point de controle a l'indice ip de la courbe a l'indice ic. """
        self.courbes[ic].controles[ip] = point
        
    def selectionnerControle(self, point):
        """ Trouve un point de controle proche d'un point donne. """
        xp, yp = point
        for ic in range(len(self.courbes)):
            for ip in range(len(self.courbes[ic].controles)):
                xc, yc = self.courbes[ic].controles[ip]
                if abs(xc-xp)<4 and abs(yc-yp)<4 :
                    return lambda p : self.deplacerControle(ic, ip, p)
        return None
    
    def nouvelleHorizontale(self):
        """ Ajoute une nouvelle horizontale initialement vide. 
        Retourne une fonction permettant d'ajouter les points de controle. """
        horizontale = Modele.Horizontale()
        self.ajouterCourbe(horizontale)
        return horizontale.ajouterControle
    
    def nouvelleVerticale(self):
        """ Ajoute une nouvelle verticale initialement vide. 
        Retourne une fonction permettant d'ajouter les points de controle. """
        verticale = Modele.Verticale()
        self.ajouterCourbe(verticale)
        return verticale.ajouterControle
    
    def nouvelleDiagonalPGD(self):
        """ Ajoute une nouvelle diagonale initialement vide. 
        Retourne une fonction permettant d'ajouter les points de controle. """
        diagonaleGauche = Modele.DiagGauche()
        self.ajouterCourbe(diagonaleGauche)
        return diagonaleGauche.ajouterControle
        diagonaleDroite = Modele.DiagDroite()
        self.ajouterCourbe(diagonaleDroite)
        return diagonaleDroite.ajouterControle
    
    def nouvelleDiagonalPointMilieu(self, color):
        """ Ajoute une nouvelle diagonale initialement vide. 
        Retourne une fonction permettant d'ajouter les points de controle. """
        diagonale = Modele.DiagPointMilieu(color)
        self.ajouterCourbe(diagonale)
        return diagonale.ajouterControle
    
    

    
   
