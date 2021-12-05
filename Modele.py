class Courbe(object):
    """ Classe generique definissant une courbe. """
    
    def __init__(self, _couleur = (0,0,0), _brush = (255,0,0)):
        self.controles = []
        self.couleur = _couleur
        self.brush = _brush

    def dessinerControles(self, dessinerControle):
        """ Dessine les points de controle de la courbe. """
        for controle in self.controles:
            dessinerControle(controle)

    def dessinerPoints(self, dessinerPoint):
        """ Dessine la courbe. Methode a redefinir dans les classes derivees. """
        pass

    def ajouterControle(self, point):
        """ Ajoute un point de controle. """
        #print point
        self.controles.append(point)
        
    def remplir(self,dessinerPoint):
        """ remplir une courbe fermee : triangle"""
        pass



class Horizontale(Courbe):
    """ Definit une horizontale. Derive de Courbe. """                  
                
    def ajouterControle(self, point):
        """ Ajoute un point de controle a l'horizontale.
        Ne fait rien si les 2 points existent deja. """
        if len(self.controles) < 2:
            Courbe.ajouterControle(self, point)

    def dessinerPoints(self, dessinerPoint):
        """ Dessine la courbe. Redefinit la methode de la classe mere. """
        if len(self.controles) == 2 :
            x1 = self.controles[0][0]
            x2 = self.controles[1][0]
            y = self.controles[0][1]
            xMin = min(x1, x2)
            xMax = max(x1, x2)
            for x in range(xMin, xMax):
                dessinerPoint((x, y), self.couleur)

class Verticale(Courbe):
    """ Definit une Verticale. Derive de Courbe. """                  
                
    def ajouterControle(self, point):
        """ Ajoute un point de controle a l'horizontale.
        Ne fait rien si les 2 points existent deja. """
        if len(self.controles) < 2:
            Courbe.ajouterControle(self, point)

    def dessinerPoints(self, dessinerPoint):
        """ Dessine la courbe. Redefinit la methode de la classe mere. """
        if len(self.controles) == 2 :
            y1 = self.controles[0][1]
            y2 = self.controles[1][1]
            x = self.controles[0][0]
            yMin = min(y1, y2)
            yMax = max(y1, y2)
            for y in range(yMin, yMax):
                dessinerPoint((x, y),self.couleur)


#Parcours segment à gauche
class DiagGauche(Courbe):
    #Definit une DIAGONAL. Derive de Courbe       

                
    def ajouterControle(self, point):
        #Ajoute un point de controle a l'horizontale.
        #Ne fait rien si les 2 points existent deja.
        if len(self.controles) < 2:
            Courbe.ajouterControle(self, point)

    def dessinerPoints(self, dessinerPoint):
        #Dessine la courbe. Redefinit la methode de la classe mere.
        if len(self.controles) == 2 :
            y1 = self.controles[0][1]
            y2 = self.controles[1][1]
            x1 = self.controles[0][0]
            x2 = self.controles[1][0]
            if(y1 < y2):
                ybas = y1
                xbas = x1
                yhaut = y2
                xhaut = x2
            else :
                ybas = y2
                xbas = x2
                yhaut = y1
                xhaut = x1
            

            x = xbas
            num = xhaut - xbas
            den = yhaut - ybas
            if num > 0:
                increment = den - 1
            if num <= 0:
                increment = 0
            
            
            for y in range(ybas, yhaut):
                dessinerPoint((x,y),(255,0,0))
                increment += num
                Q = increment/den
                x += Q
                increment -= Q * den
                y+=1
         

#Parcours segment à droite
class DiagDroite(Courbe):
    #Definit une DIAGONAL. Derive de Courbe       

                
    def ajouterControle(self, point):
        #Ajoute un point de controle a l'horizontale.
        #Ne fait rien si les 2 points existent deja.
        if len(self.controles) < 2:
            Courbe.ajouterControle(self, point)

    def dessinerPoints(self, dessinerPoint):
        #Dessine la courbe. Redefinit la methode de la classe mere.
        if len(self.controles) == 2 :
            y1 = self.controles[0][1]
            y2 = self.controles[1][1]
            x1 = self.controles[0][0]
            x2 = self.controles[1][0]
            if(y1 < y2):
                ybas = y1
                xbas = x1
                yhaut = y2
                xhaut = x2
            else :
                ybas = y2
                xbas = x2
                yhaut = y1
                xhaut = x1
            

            x = xbas
            num = xhaut - xbas
            den = yhaut - ybas
            if num > 0:
                increment = -1
            if num <= 0:
                increment = -den
            
            
            for y in range(ybas, yhaut):
                dessinerPoint((x,y),(0,255,0))
                increment += num
                Q = increment/den
                x += Q
                increment -= Q * den
                y+=1

#point milieu
class DiagPointMilieu(Courbe):
    #Definit une DIAGONAL. Derive de Courbe       

                
    def ajouterControle(self, point):
        #Ajoute un point de controle a l'horizontale.
        #Ne fait rien si les 2 points existent deja.
        if len(self.controles) < 2:
            Courbe.ajouterControle(self, point)

    def dessinerPoints(self, dessinerPoint):
        #Dessine la courbe. Redefinit la methode de la classe mere.
        if len(self.controles) == 2 :
            y1 = self.controles[0][1]
            y2 = self.controles[1][1]
            x1 = self.controles[0][0]
            x2 = self.controles[1][0]
            if(y1 < y2):
                ybas = y1
                xbas = x1
                yhaut = y2
                xhaut = x2
            else :
                ybas = y2
                xbas = x2
                yhaut = y1
                xhaut = x1
            

            x = xbas
            y = ybas
            
            if xhaut >= xbas :
                dx = xhaut - xbas
                dy = yhaut - ybas

                if dx >= dy :
                    dp = 2*dy - dx
                    deltaE = 2*dy
                    deltaNE =2*(dy - dx)
                    
                    dessinerPoint((x,y),self.couleur)
                    while x < xhaut:                
                        if dp <= 0 :        #On choisi le point E
                            dp += deltaE    #nouveau dp
                            x+=1            #calcul xp+1
                                            #yp+1 = yp
                        else :              #On choisi le point E
                            dp += deltaNE   #nouveau dp
                            x+=1            #calcul xp+1
                            y+=1            #calcul yp+1
                        dessinerPoint((x,y),self.couleur)
                    
                if dx < dy :
                    dp = 2 * dx - dy
                    deltaE = 2 * dx
                    deltaNE = 2 * (dx - dy)
                
                    dessinerPoint((x,y),self.couleur)
                    while y < yhaut:                
                        if dp <= 0 :        #On choisi le point E
                            dp += deltaE    #nouveau dp
                            y+=1            
                                            
                        else :              #On choisi le point E
                            dp += deltaNE   #nouveau dp
                            x+=1            
                            y+=1            
                        dessinerPoint((x,y),self.couleur)
                
            if xhaut < xbas:
                dx = xbas - xhaut
                dy = yhaut - ybas
                
                if dx >= dy :
                    dp= 2*dy - dx
                    deltaE = 2 * dy
                    deltaNE = 2*(dy - dx)
                    
                    dessinerPoint((x,y),self.couleur)
                    while x >= xhaut:                
                        if dp <= 0 :        #On choisi le point E
                            dp += deltaE    #nouveau dp
                            x-=1            
                                            
                        else :              #On choisi le point E
                            dp += deltaNE   #nouveau dp
                            x-=1            
                            y+=1            
                        dessinerPoint((x,y),self.couleur)
                    
                if dx < dy :
                    dp = 2*dx - dy
                    deltaE = 2*dx
                    deltaNE = 2 * (dx - dy)
                    
                    dessinerPoint((x,y),self.couleur)
                    while y < yhaut:                
                        if dp <= 0 :        #On choisi le point E
                            dp += deltaE    #nouveau dp
                            y+=1            
                                            
                        else :              #On choisi le point E
                            dp += deltaNE   #nouveau dp
                            x-=1            
                            y+=1            
                        dessinerPoint((x,y),self.couleur)
                    
                
                




