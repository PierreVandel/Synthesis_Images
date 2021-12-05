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

class GaucheDroite(Courbe): #doiteGD
    
    
    
    def ajouterControle(self, point):
        """ Ajoute un point de controle au Segment """
        if len(self.controles) < 2:
            Courbe.ajouterControle(self, point)
    
    def dessinerPente(self, dessinerPoint, FB, LB, FH, LH, couleur, switching):
        if (FB > FH):
            FB, FH = FH, FB
            LB, LH = LH, LB
        SecondVar = LB
        num = LH - LB
        den = FH - FB
        increment = den - 1
        for FirstVar in range(FB, FH):
            if switching: dessinerPoint((SecondVar, FirstVar), couleur)
            else: dessinerPoint((FirstVar, SecondVar), couleur)
            increment += num
            Q = increment / den
            SecondVar += Q
            increment -= Q * den
    
    def dessinerPoints(self, dessinerPoint):
        """ Dessine le Segment """
        if len(self.controles) == 2:
            #self.dessiner_PenteGauche(dessinerPoint, self.controles[0][0], self.controles[0][1], self.controles[1][0], self.controles[1][1], (255,0,0))
            #self.dessiner_PenteDroite(dessinerPoint, self.controles[0][0], self.controles[0][1], self.controles[1][0], self.controles[1][1], (0,255,0))
            self.dessinerPente(dessinerPoint, self.controles[0][1], self.controles[0][0], self.controles[1][1], self.controles[1][0], (255, 0, 0), True)
            self.dessinerPente(dessinerPoint, self.controles[0][0], self.controles[0][1], self.controles[1][0], self.controles[1][1], (0, 255, 0), False)



class PointMilieu(Courbe):#droitemilieu
    
    def ajouterControle(self, point):
        """ Ajoute un point de controle au Segment 2 """
        if len(self.controles) < 2:
            Courbe.ajouterControle(self, point)
    
    #def boucleDessinPoints(self, dessinerPoint, dF, dL, FB, L, couleur, switching)
    
    def dessinerPoints(self, dessinerPoint):
        
        couleur = self.couleur
        if len(self.controles) == 2:
            xB = self.controles[0][0]
            yB = self.controles[0][1]
            xH = self.controles[1][0]
            yH = self.controles[1][1]
            
            """ Gestion des Cas """
            if xB == xH and yB == yH:
                return
            
            """ Dessine le Segment 2 """
            if (yB > yH):
                xH, xB = xB, xH
                yH, yB = yB, yH
            if (xH >= xB):
                dX = xH - xB
                dY = yH - yB
                if (dX >= dY):
                    y = yB
                    dp = 2 * dY - dX
                    deltaE = 2 * dY
                    deltaNE = 2 * (dY - dX)
                    for x in range(xB,xH):
                        if (dp <= 0):
                            dp += deltaE
                        else:
                            dp += deltaNE
                            y += 1
                        dessinerPoint((x,y), couleur)
                else:
                    x = xB
                    dp = 2 * dX - dY
                    deltaE = 2 * dX
                    deltaNE = 2 * (dX - dY)
                    for y in range(yB,yH):
                        if (dp <= 0):
                            dp += deltaE
                        else:
                            dp += deltaNE
                            x += 1
                        dessinerPoint((x,y), couleur)
            else:
                dX = xB - xH
                dY = yH - yB
                if (dX >= dY):
                    y = yB
                    dp = 2 * dY - dX
                    deltaE = 2 * dY
                    deltaNE = 2 * (dY - dX)
                    for x in range(xB,xH,-1):
                        if (dp <= 0):
                            dp += deltaE
                        else:
                            dp += deltaNE
                            y += 1
                        dessinerPoint((x,y), couleur)
                else:
                    x = xB
                    dp = 2 * dX - dY
                    deltaE = 2 * dX
                    deltaNE = 2 * (dX - dY)
                    for y in range(yB,yH):
                        if (dp <= 0):
                            dp += deltaE
                        else:
                            dp += deltaNE
                            x += -1
                        dessinerPoint((x,y), couleur)

class Arrete():
     def __init__(self, yhaut1=0, x1=0, num1=0, den1=0, inc1=0):
         self.yhaut = yhaut1
         self.x = x1
         self.num = num1
         self.den = den1
         self.inc = inc1
    
     def mise_a_jour(self):
         self.inc += self.num
         Q = self.inc / self.den
         self.x += Q
         self.inc -= Q * self.den


class TriangleRempli(Courbe):
    """remplir le triangle de la couleur passee au constructeur"""
     
    def __init__(self, couleur):
        Courbe.__init__(self, (0,0,0), couleur)
    
    def ajouterControle(self, point):
        """ Ajoute un point de controle.
        Ne fait rien si les 3 points existent deja."""
        if len(self.controles) < 3:
            Courbe.ajouterControle(self, point)
 
    def remplir(self,dessinerPoint):
        if len(self.controles) == 3:
            """implémentez, commencez par trier les points Pmin, Pmoy, Pmax"""
             
            Pmax = [0, 1]
            Pmoy = [0, 1]
            Pmin = [0, 1]
            

            
            if (self.controles[0][1] >= self.controles[1][1]) and (self.controles[0][1] >= self.controles[2][1]):
                Pmax = self.controles[0]
                if self.controles[1][1] >= self.controles[2][1]:
                    Pmoy = self.controles[1]
                    Pmin = self.controles[2]
                else:
                    Pmoy = self.controles[2]
                    Pmin = self.controles[1]
            elif (self.controles[1][1] >= self.controles[0][1]) and (self.controles[1][1] >= self.controles[2][1]):
                Pmax = self.controles[1]
                if self.controles[0][1] >= self.controles[2][1]:
                    Pmoy = self.controles[0]
                    Pmin = self.controles[2]
                else:
                    Pmoy = self.controles[2]
                    Pmin = self.controles[0]
            else:
                Pmax = self.controles[2]
                if self.controles[0][1] >= self.controles[1][1]:
                    Pmoy = self.controles[0]
                    Pmin = self.controles[1]
                else:
                    Pmoy = self.controles[1]
                    Pmin = self.controles[0]
                    
            print("Pmin : ", Pmin)
            print("Pmoy : ", Pmoy)
            print("Pmax : ", Pmax)
                         
            dx = Pmax[0] - Pmin[0]
            dy = Pmax[1] - Pmin[1]
             
             #Utilisation cartésiènne de l'équation cartésienne de droite
            F = dy*(Pmoy[0] - Pmax[0]) - dx * (Pmoy[1] - Pmax[1])
             
            if(F < 0):
                #Pmoy se trouve à gauche du segment Pmax/Pmin, orienté de Pmax vers Pmin
                if(Pmin[1] < Pmoy[1]):
                    #Cas général
                    y = Pmin[1]
                    
                    num = Pmoy[0] - Pmin[0]
                    den = Pmoy[1] - Pmin[1]
                    
                    if(num > 0):
                        inc = den - 1
                    else:
                        inc = 0
                    
                    AAGauche = Arrete(Pmoy[1], Pmin[0], num, den, inc)
                    
                    num = Pmax[0] - Pmin[0]
                    den = Pmax[1] - Pmin[1]
                    
                    if(num > 0):
                        inc = -1
                    else:
                        inc = - den
                    
                    AADroite = Arrete(Pmax[1], Pmin[0], num, den, inc)
                    
                    while(y < Pmoy[1]):
                        for i in range(int(AAGauche.x), int(AADroite.x)):
                            dessinerPoint((i,y), self.brush)
                        AAGauche.mise_a_jour()
                        AADroite.mise_a_jour()
                        y+=1
                            
                    num = Pmax[0] - Pmoy[0]
                    den = Pmax[1] - Pmoy[1]
                    
                    if(num > 0):
                        inc = den - 1
                    else:
                        inc = 0
                    
                    AAGauche = Arrete(Pmax[1], Pmoy[0], num, den, inc)
                    
                    while y < Pmax[1]:
                        for i in range(int(AAGauche.x), int(AADroite.x)):
                            dessinerPoint((i,y), self.brush)
                        AAGauche.mise_a_jour()
                        AADroite.mise_a_jour()
                        y+=1
                        
                else: #if(Pmin[1] == Pmoy[1])
                    #cas particulier
                    y = Pmin[1]
                    
                    num = Pmax[0] - Pmoy[0]
                    den = Pmax[1] - Pmoy[1]
                    
                    if(num > 0):
                        inc = den - 1
                    else:
                        inc = 0
                    
                    AAGauche = Arrete(Pmax[1], Pmoy[0], num, den, inc)
                    
                    num = Pmax[0] - Pmin[0]
                    den = Pmax[1] - Pmin[1]
                    
                    if(num > 0):
                        inc = -1
                    else:
                        inc = - den
                    
                    AADroite = Arrete(Pmax[1], Pmin[0], num, den, inc)
                    
                    while(y < Pmax[1]):
                        for i in range(int(AAGauche.x), int(AADroite.x)):
                            dessinerPoint((i,y), self.brush)
                        AAGauche.mise_a_jour()
                        AADroite.mise_a_jour()
                        y+=1
            elif(F > 0):
                    #Pmoy se trouve à droite du segment Pmax/Pmin, orienté de Pmax vers Pmin
                    if(Pmin[1] < Pmoy[1]):
                        #Cas général
                        y = Pmin[1]
                        
                        num = Pmax[0] - Pmin[0]
                        den = Pmax[1] - Pmin[1]
                        
                        if(num > 0):
                            inc = den - 1
                        else:
                            inc = 0
                        
                        AAGauche = Arrete(Pmax[1], Pmin[0], num, den, inc)
                        
                        num = Pmoy[0] - Pmin[0]
                        den = Pmoy[1] - Pmin[1]
                        
                        if(num > 0):
                            inc = -1
                        else:
                            inc = - den
                        
                        AADroite = Arrete(Pmoy[1], Pmin[0], num, den, inc)
                        
                        while(y < Pmoy[1]):
                            for i in range(int(AAGauche.x), int(AADroite.x)):
                                dessinerPoint((i,y), self.brush)
                            AAGauche.mise_a_jour()
                            AADroite.mise_a_jour()
                            y+=1
                                
                        num = Pmax[0] - Pmoy[0]
                        den = Pmax[1] - Pmoy[1]
                        
                        if(num > 0):
                            inc = -1
                        else:
                            inc = - den
                        
                        AADroite = Arrete(Pmax[1], Pmoy[0], num, den, inc)
                        
                        while y < Pmax[1]:
                            for i in range(int(AAGauche.x), int(AADroite.x)):
                                dessinerPoint((i,y), self.brush)
                            AAGauche.mise_a_jour()
                            AADroite.mise_a_jour()
                            y+=1
                            
                    else: #if(Pmin[1] == Pmoy[1])
                        #cas particulier
                        y = Pmin[1]
                        
                        num = Pmax[0] - Pmin[0]
                        den = Pmax[1] - Pmin[1]
                        
                        if(num > 0):
                            inc = den - 1
                        else:
                            inc = 0
                        
                        AAGauche = Arrete(Pmax[1], Pmin[0], num, den, inc)
                        
                        num = Pmax[0] - Pmoy[0]
                        den = Pmax[1] - Pmoy[1]
                        
                        if(num > 0):
                            inc = -1
                        else:
                            inc = - den
                        
                        AADroite = Arrete(Pmax[1], Pmoy[0], num, den, inc)
                        
                        while(y < Pmax[1]):
                            for i in range(int(AAGauche.x), int(AADroite.x)):
                                dessinerPoint((i,y), self.brush)
                            AAGauche.mise_a_jour()
                            AADroite.mise_a_jour()
                            y+=1






