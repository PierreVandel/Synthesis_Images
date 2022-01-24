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

### TP 01 #####################################################################


class Segment(Courbe): #doiteGD
    
    
    
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



class Segment2(Courbe):#droitemilieu
    
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

### TP 02 #####################################################################

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
   
    """rempli le triangle de la couleur passee au constructeur"""
    def __init__(self, couleur) :
        Courbe.__init__(self)       
        self.couleur=couleur
        
    def ajouterControle(self, point):
        """ Ajoute un point de controle.
        Ne fait rien si les 3 points existent deja. """
        if len(self.controles) < 3:
            Courbe.ajouterControle(self, point)
        
         
    def tri(self, y1,y2,y3):        
        
        if (y1<=y2) :
            if (y2<=y3) :
                i=0
                j=1
                k=2               
            else :
                if (y1<=y3):
                    i=0
                    j=2
                    k=1   
                else :
                    i=2
                    j=0
                    k=1
        else : #y1>y2
            if (y2>y3) :
                i=2
                j=1
                k=0 
                    
            else :
                if (y3>y1):
                    i=1
                    j=0
                    k=2 
                        
                else :
                    i=1
                    j=2
                    k=0 
        return [i,j,k]
                        
          
                        
                        
    def remplir(self,dessinerPoint):
        
        N=len(self.controles)
        
        #construction du triangle comme cours avec ymin<=ymoy<=ymax
        if (N==3) :
            y1 = self.controles[0][1]
            y2 = self.controles[1][1]
            y3 = self.controles[2][1]
           
            ind=self.tri(y1,y2,y3)
            #trier les 3 points Pmin, Pmoy, Pmax
            Pmin_x=self.controles[ind[0]][0]
            Pmin_y=self.controles[ind[0]][1]
            Pmoy_x=self.controles[ind[1]][0]
            Pmoy_y=self.controles[ind[1]][1]
            Pmax_x=self.controles[ind[2]][0]
            Pmax_y=self.controles[ind[2]][1]
            
            
            
            #2 cas particuliers et 2 config generales
            
           
            dy=Pmax_y-Pmin_y
            dx=Pmax_x-Pmin_x
            if ((dy*(Pmoy_x-Pmin_x)-dx*(Pmoy_y-Pmin_y))<0) : 
                #Pmoy a gauche segment [Pmin,Pmax]
                #config 1 du cours
                if (Pmin_y==Pmoy_y) :   #cas particulier
                    num=Pmax_x-Pmoy_x
                    if (num<=0) :
                        edgeG=Arrete(Pmax_y,Pmoy_x,num,Pmax_y-Pmoy_y,0)
                    else :
                        edgeG=Arrete(Pmax_y,Pmoy_x,num,Pmax_y-Pmoy_y,Pmax_y-Pmoy_y-1)
                        
                    num=Pmax_x-Pmin_x
                    if (num<=0) :
                        edgeD=Arrete(Pmax_y,Pmin_x,num,Pmax_y-Pmin_y,Pmin_y-Pmax_y)
                    else :
                        edgeD=Arrete(Pmax_y,Pmin_x,num,Pmax_y-Pmin_y,-1)
                    
                    y=Pmin_y
                    while (y<Pmax_y):
                        xG=int(edgeG.x)
                        xD=int(edgeD.x)
                        for x in range(xG, xD+1):       
                            dessinerPoint((x,y),self.couleur) 
                        edgeG.mise_a_jour()
                        edgeD.mise_a_jour()
                        y+=1
                        
                    
                    
                else : 
                    #cas general config 1
                    num=Pmoy_x-Pmin_x
                    if (num<=0) :
                        edgeG=Arrete(Pmoy_y,Pmin_x,num,Pmoy_y-Pmin_y,0)
                    else :
                        edgeG=Arrete(Pmoy_y,Pmin_x,num,Pmoy_y-Pmin_y,Pmoy_y-Pmin_y-1)
                        
                    num=Pmax_x-Pmin_x
                    if (num<=0) :
                        edgeD=Arrete(Pmax_y,Pmin_x,num,Pmax_y-Pmin_y,Pmin_y-Pmax_y)
                    else :
                        edgeD=Arrete(Pmax_y,Pmin_x,num,Pmax_y-Pmin_y,-1)
                    
                    y=Pmin_y
                    while (y<Pmoy_y):
                        xG=int(edgeG.x)
                        xD=int(edgeD.x)
                        for x in range(xG, xD+1):  
                            dessinerPoint((x,y),self.couleur) 
                        edgeG.mise_a_jour()
                        edgeD.mise_a_jour()
                        y+=1
                        
                    num=Pmax_x-Pmoy_x
                    if (num<=0) :
                        edgeG=Arrete(Pmax_y,Pmoy_x,num,Pmax_y-Pmoy_y,0)
                    else :
                        edgeG=Arrete(Pmax_y,Pmoy_x,num,Pmax_y-Pmoy_y,Pmax_y-Pmoy_y-1)
                    y=Pmoy_y
                    while (y<Pmax_y):
                        xG=int(edgeG.x)
                        xD=int(edgeD.x)
                        for x in range(xG, xD+1):                                
                            dessinerPoint((x,y),self.couleur)          
                           
                        edgeG.mise_a_jour()
                        edgeD.mise_a_jour()               
                        y+=1       
                
                
            else :
                #Pmoy a droite
                #config 2 du cours
                if (Pmin_y==Pmoy_y) :   #cas particulier
                    num=Pmax_x-Pmin_x
                    if (num<=0) :
                        edgeG=Arrete(Pmax_y,Pmin_x,num,Pmax_y-Pmin_y,0)
                    else :
                        edgeG=Arrete(Pmax_y,Pmin_x,num,Pmax_y-Pmin_y,Pmax_y-Pmin_y-1)
                        
                    num=Pmax_x-Pmoy_x
                    if (num<=0) :
                        edgeD=Arrete(Pmax_y,Pmoy_x,num,Pmax_y-Pmoy_y,Pmoy_y-Pmax_y)
                    else :
                        edgeD=Arrete(Pmax_y,Pmoy_x,num,Pmax_y-Pmoy_y,-1)
                    
                    y=Pmin_y
                    while (y<Pmax_y):
                        xG=int(edgeG.x)
                        xD=int(edgeD.x)
                        for x in range(xG, xD+1):                                
                            dessinerPoint((x,y),self.couleur) 
                        edgeG.mise_a_jour()
                        edgeD.mise_a_jour()
                        y+=1
                        
                else : #cas general config 2
                    num=Pmax_x-Pmin_x
                    if (num<=0) :
                        edgeG=Arrete(Pmax_y,Pmin_x,num,Pmax_y-Pmin_y,0)
                    else :
                        edgeG=Arrete(Pmax_y,Pmin_x,num,Pmax_y-Pmin_y,Pmax_y-Pmin_y-1)
                        
                    num=Pmoy_x-Pmin_x
                    if (num<=0) :
                        edgeD=Arrete(Pmoy_y,Pmin_x,num,Pmoy_y-Pmin_y,Pmin_y-Pmoy_y)
                    else :
                        edgeD=Arrete(Pmoy_y,Pmin_x,num,Pmoy_y-Pmin_y,-1)
                    
                    y=Pmin_y
                    while (y<Pmoy_y):
                        xG=int(edgeG.x)
                        xD=int(edgeD.x)
                        for x in range(xG, xD+1):                                          
                            dessinerPoint((x,y),self.couleur) 
                                   
                        edgeG.mise_a_jour()
                        edgeD.mise_a_jour()
                        y+=1
                        
                    num=Pmax_x-Pmoy_x
                    if (num<=0) :
                        edgeD=Arrete(Pmax_y,Pmoy_x,num,Pmax_y-Pmoy_y,Pmoy_y-Pmax_y)
                    else :
                        edgeD=Arrete(Pmax_y,Pmoy_x,num,Pmax_y-Pmoy_y,-1)
                    y=Pmoy_y
                    while (y<Pmax_y):
                        xG=int(edgeG.x)
                        xD=int(edgeD.x)
                        for x in range(xG, xD+1):                                         
                            dessinerPoint((x,y),self.couleur) 
                    
                        edgeG.mise_a_jour()
                        edgeD.mise_a_jour()               
                        y+=1   