class Vecteur():
    def __init__(self,x=0,y=0,z=0):
        self.vx=x
        self.vy=y
        self.vz=z
        
    
    def __add__(self,v):
        vres=Vecteur()
        vres.vx=self.vx+v.vx
        vres.vy=self.vy+v.vy
        vres.vz=self.vz+v.vz
        return vres
    
    def __sub__(self,v):
        vres=Vecteur()
        vres.vx=self.vx-v.vx
        vres.vy=self.vy-v.vy
        vres.vz=self.vz-v.vz
        return vres
    
    def __mul__(self,v):    #produit scalaire
        return  self.vx*v.vx+self.vy*v.vy+self.vz*v.vz
    
    def dot(self,v):
        vres=Vecteur()
        vres.vx=self.vy*v.vz - self.vz*v.vy
        vres.vy=-(self.vx*v.vz-self.vz*v.vx)
        vres.vz=self.vx*v.vy-self.vy*v.vx
        return vres
    
    def __rmul__(self,k):
        vres=Vecteur()
        vres.vx=self.vx*k
        vres.vy=self.vy*k
        vres.vz=self.vz*k
        return vres
    
    def norm(self):
        import math
        return math.sqrt(self.vx*self.vx+self.vy*self.vy+self.vz*self.vz)
    
    def normer(self):
        val=1/self.norm()
        self=val*self
        return self
    
    def debug(self):
        print(self.vx, " ", self.vy, " ", self.vz)
    
    