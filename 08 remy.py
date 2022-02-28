#################################
#ülesanne 08

class Auto:
    automark='teadmata'
    aasta=0
    hind=0
    
    def kuvaMark (self):
        print(self.automark)
    
        
    def lisaMark(self,x):
        self.automark = x
        
        
        
minu=Auto()
minu.lisaMark("Audi")

minu.kuvaMark()