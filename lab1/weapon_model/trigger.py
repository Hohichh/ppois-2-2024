from magazine import *
from barrel import *

class Trigger:
    def pull(self, magazine: Magazine, barrel: Barrel):
        if magazine.empty == True:
            print("Unloaded. Can't shoot")
        else:
            print("Piu!!")
            barrel.load_barrel(magazine.cartridge_feed()) 
            barrel.fire()