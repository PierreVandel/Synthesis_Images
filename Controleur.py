import Modele


### TP 04 #####################################################################

# Creation de Vecteur entre 2 Points
def Vecteur(p1, p2):
    if len(p1) == 3 and len(p2) == 3:
        res = [0,0,0]
        for ii in range(3):
            res[ii] = p2[ii] - p1[ii]
        return res

# Produit Scalaire de 2 Vecteurs
def ProdScal(v1, v2):
    if len(v1) == 3 and len(v2) == 3:
        res = 0
        for ii in range(3):
            res += v1[ii] * v2[ii]
        return res

# Produit Vectoriel de 2 Vecteurs
def ProdVec(v1, v2):
    if len(v1) == 3 and len(v2) == 3:
        res = [0,0,0]
        for ii in range(3):
            res[ii] = v1[(ii + 1) % 3] * v2[(ii + 2) % 3] - v2[(ii + 1) % 3] * v1[(ii + 2) % 3]
        return res

# Vecteur Normee
def Normed(v1):
    if len(v1) == 3:
        somme = 0
        for ii in range(3):
            somme += pow(v1[ii], 2)
        val = 1/pow(somme, .5)
        res = [v1[0]*val, v1[1]*val, v1[2]*val]
        return res

########################################################################

class ControleurCourbes(object):
    """ Gere un ensemble de courbes. """
    def __init__(self):
        self.courbes = []
        self.scene = [] #sert pour l affichage des scenes (donnees importees)
        ### TP 05 #####################################################################
        self.zbuffer=[] #une instance du ZBuffer
       
    def ajouterCourbe(self, courbe):
        """ Ajoute une courbe supplementaire.  """
        self.courbes.append(courbe) 

    def dessiner(self, dessinerControle, dessinerPoint, enabled):
        """ Dessine les courbes. """
        # dessine les point de la courbe
        for courbe in self.courbes:
            courbe.dessinerPoints(dessinerPoint)
        #reset zbuffer to MAX
        if self.zbuffer:
            for courbe in self.courbes:
                if type(courbe) == Modele.TriangleRempliZBuffer :
                    self.zbuffer.reset_zbuffer()
                    break;
        
        #si la courbe peut etre remplie
        for courbe in self.courbes:
            if type(courbe) != Modele.TriangleRempliZBuffer :
                courbe.remplir(dessinerPoint)
            else :
                courbe.remplir(dessinerPoint, self.zbuffer, self.scene)

          
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
    
### TP 05 #####################################################################    
    def initzbuffer(self):
        self.zbuffer=Modele.ZBuffer()
        return self.zbuffer.alloc_init_zbuffer
########################################################################
    
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

### TP 01 #####################################################################

    
    def nouveauSegment(self): #DroiteGauche
        """ Ajoute un nouveau segment initialement vide.
        Retourne une fonction permettant d'ajouter les points de controle. """
        segment = Modele.Segment()
        self.ajouterCourbe(segment)
        return segment.ajouterControle
   
    def nouveauSegment2(self, col): #pointmilieu
        """ Ajoute un nouveau segment 2 initialement vide.
        Retourne une fonction permettant d'ajouter les points de controle. """
        segment2 = Modele.Segment2(col)
        self.ajouterCourbe(segment2)
        return segment2.ajouterControle

### TP 02 #####################################################################


    def nouveauTriangleRempli(self, col):
        """ Ajoute un nouveau Triangle Rempli initialement vide.
        Retourne une fonction permettant d'ajouter les points de controle. """
        triangleRempli = Modele.TriangleRempli(col)
        self.ajouterCourbe(triangleRempli)
        return triangleRempli.ajouterControle

### TP 03 #####################################################################
    
    """ Read Scene Process. """
    def readScene(self, larg, haut, method):
        import Import_scene
        from tkinter import filedialog
        
        donnees = Import_scene.Donnees_scene("ressources/scenes/Donnees_scene.sce")
        self.scene = donnees
        d = self.scene.d #distance de la camera a l ecran
        
        fic = "fic"
        indcptobj = -1
        while len(fic) > 0 : #tant que des fichiers objets selectionnes
            fic = filedialog.askopenfilename \
            (title="Inserer l objet:", initialdir="ressources/scenes", filetypes = [("Fichiers Objets","*.obj")]) 
            if len(fic) > 0 :
                indcptobj += 1
                donnees.ajoute_objet(fic,indcptobj)             
            
                self.scene = donnees     

                #mettre objet  dans repere camera avec  translation differente de l objet Diamant et changement axes y<->z
                listesommetsdansreperecamera = []
                for som in  self.scene.listeobjets[indcptobj].listesommets :
                    if self.scene.listeobjets[indcptobj].nomobj == "Diamant" :
                        tx=150
                        ty=150
                        tz=2.2*d
                    elif self.scene.listeobjets[indcptobj].nomobj == "Cube" :
                        tx=350
                        ty=100
                        tz=2*d
                    else :
                        tx=200
                        ty=0
                        tz=1.8*d
                    
                    
                    yp=som[2]+ty
                    xp=-som[1]+tx
                    zp=som[0]+tz
                    
                    listesommetsdansreperecamera.append((xp,yp,zp))
                    
                method(indcptobj, d, larg, haut, listesommetsdansreperecamera)
    
    
    
    """ Method of Wireframe. """
    def methodSceneFildefer(self, indcptobj, d, larg, haut, listesommetsdansreperecamera):
        listeprojete = []
        # Projection perspective des sommets 3D du polyedre exprimes dans le repere camera:  
        for pt in listesommetsdansreperecamera:
            ptSx = pt[0] * d / pt[2]
            ptSy = pt[1] * d / pt[2]
            ptSx += larg / 2
            ptSy -= (haut + 1) / 2 - 1
            ptSy *= -1
            listeprojete.append([round(ptSx), round(ptSy)])
 
    
        i=-1 
        #Pour chaque triangle du polyedre : construction des 3 segments par algo point milieu.
        # Ajout des courbes et des points de controle.
        for tr in self.scene.listeobjets[indcptobj].listeindicestriangle :
            i += 1
            for ii in range(len(tr)):
                seg = Modele.Segment2(self.scene.listeobjets[indcptobj].listecouleurs[i])
                seg.ajouterControle(listeprojete[tr[ii] - 1])
                seg.ajouterControle(listeprojete[tr[(ii + 1) % len(tr)] - 1])
                self.courbes.append(seg)
    
    
    
    """ Create a new Wireframe Scene. """
    def nouvelleSceneFildefer(self, larg, haut):
        
        self.readScene(larg, haut, \
        (lambda io, d, l, h, ls: \
         self.methodSceneFildefer(io, d, l, h, ls)))

### TP 04 #####################################################################
    
    """ Painter's Method. """
    def methodScenePeintre(self, indcptobj, d, larg, haut, listesommetsdansreperecamera):
        listeprojete = []
        # Projection perspective des sommets 3D du polyedre exprimes dans le repere camera:  
        for pt in listesommetsdansreperecamera:
            ptSx = pt[0] * d / pt[2]
            ptSy = pt[1] * d / pt[2]
            ptSx += larg / 2
            ptSy -= (haut + 1) / 2 - 1
            ptSy *= -1
            listeprojete.append([round(ptSx), round(ptSy)])
 
    
        i=-1 
        #Pour chaque triangle du polyedre : construction des 3 segments par algo point milieu.
        # Ajout des courbes et des points de controle.
        for tr in self.scene.listeobjets[indcptobj].listeindicestriangle :
            i += 1
            ###########################
            
            #triVn = ProdVec(Vecteur(listesommetsdansreperecamera[tr[0] - 1], listesommetsdansreperecamera[tr[2] - 1]), \
                            #Vecteur(listesommetsdansreperecamera[tr[0] - 1], listesommetsdansreperecamera[tr[1] - 1]))
            #if ProdScal(Normed(triVn), Normed(Vecteur(listesommetsdansreperecamera[tr[0] - 1], [0,0,0]))) <= 0:
                #continue
            ###########################
            #Remplissage d'une face de l'objet grâce au TriangleRempli
            tri = Modele.TriangleRempli(self.scene.listeobjets[indcptobj].listecouleurs[i])
            # Ajout des courbes et des points de controle oour chaque triangle
            for jj in range(len(tr)):
                tri.ajouterControle(listeprojete[tr[jj] - 1])
            self.courbes.append(tri)
    
    
    
    """ Create new Painter's Scene. """
    def nouvelleScenePeintre(self, larg, haut):
        
        self.readScene(larg, haut, \
                       (lambda io, d, l, h, ls: \
                        self.methodScenePeintre(io, d, l, h, ls)))

### TP 05 ##################################################################### 


    """ Method of ZBuffer Scene. """
    def methodSceneZBuffer(self, indcptobj, d, larg, haut, listesommetsdansreperecamera):
        
        listeprojete = []
        # Projection perspective des sommets 3D du polyedre exprimes dans le repere camera: 
        for pt in listesommetsdansreperecamera:
            ptSx = pt[0] * d / pt[2]
            ptSy = pt[1] * d / pt[2]
            listeprojete.append([round(ptSx), round(ptSy)])
    
        i=-1 
	    # Pour chaque triangle du polyedre : construction des 3 segments par algo point milieu.
        # Ajout des courbes et des points de controle.
        for tr in self.scene.listeobjets[indcptobj].listeindicestriangle :
            i += 1
            # Algorithme Peintre avec BONUS
            triVn = ProdVec(Vecteur(listesommetsdansreperecamera[tr[0] - 1], listesommetsdansreperecamera[tr[2] - 1]), \
                            Vecteur(listesommetsdansreperecamera[tr[0] - 1], listesommetsdansreperecamera[tr[1] - 1]))
            if ProdScal(Normed(triVn), Normed(Vecteur(listesommetsdansreperecamera[tr[0] - 1], [0,0,0]))) <= 0:
                continue
            #triVn est donc la normale à la facette qui correspond au triangle : tr (produit vectoriel de deux vecteurs du triangle)
            # Construction facette
            fac = Modele.Facette()
            P1= listesommetsdansreperecamera[tr[0]-1]
            P2= listesommetsdansreperecamera[tr[1]-1]
            P3= listesommetsdansreperecamera[tr[2]-1]
                    
            fac.sommets.append(P1)
            fac.sommets.append(P2)
            fac.sommets.append(P3)
            
            #equation du plan du triangle
            A=(P2[1]-P1[1])*(P3[2]-P1[2])-((P2[2]-P1[2])*(P3[1]-P1[1]))
            B=-((P2[0]-P1[0])*(P3[2]-P1[2])-((P2[2]-P1[2])*(P3[0]-P1[0])))
            C=(P2[0]-P1[0])*(P3[1]-P1[1])-((P2[1]-P1[1])*(P3[0]-P1[0]))
            D=-A*P1[0]-B*P1[1]-C*P1[2]
            
            fac.normaleetplan=[A,B,C,D]
            fac.couleur=self.scene.listeobjets[indcptobj].listecouleurs[i]

            # Creation Triangle
            tri = Modele.TriangleRempliZBuffer(self.scene.listeobjets[indcptobj].listecouleurs[i])
            for jj in range(3):
                tri.ajouterControle(listeprojete[tr[jj] - 1])
            tri.ajouterfacette(fac)
            self.courbes.append(tri)
    
    
    
    """ Create new ZBuffer Scene. """
    def nouvelleSceneZBuffer(self):
        
        self.readScene(0, 0, \
                       (lambda io, d, l, h, ls: \
                        self.methodSceneZBuffer(io, d, l, h, ls)))
