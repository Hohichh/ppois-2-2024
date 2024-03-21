from trigger import *
from aim import *

class Weapon:
    def __init__(self, name: str, weapon_type: str, 
                 magazine: Magazine=None, aim: Aim=None, barrel: Barrel=None, price: float=2):
        self.__name = name
        self.__weapon_type = weapon_type
        self.__magazine = magazine
        self.__aim = aim
        self.__barrel = barrel
        self.__trigger = Trigger()
        self.__grime = 0
        self.__price = price
    
    def __str__(self):
        return f"\n{self.__weapon_type} {self.__name}. \n Caliber: {self.__magazine.caliber}\
            Magazine capacity: {self.__magazine.capacity}. \
            \n Aim: {self.__aim.aim_type}, \
            {self.__aim.magnification if self.__aim.aim_type == 'optical' else ''}"

    def __compatibility(self):
        if self.__name != self.__magazine.name != self.__barrel.name != self.__aim.name:
            raise Incompatibility(self, self.__magazine, self.__barrel, self.__aim)

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def weapon_type(self):
        return self.__weapon_type
    
    @weapon_type.setter
    def weapon_type(self, weapon_type: str):
        try:
            if weapon_type not in VALID_WEAPON_TYPES:
                raise ListMismatch(weapon_type, VALID_WEAPON_TYPES)
            self.__weapon_type = weapon_type
        except ListMismatch as e:
            print(e)

    @property
    def magazine(self):
        return self.__magazine

    @magazine.setter
    def magazine(self, magazine: Magazine):
        try:
            if not isinstance(magazine, Magazine):
                raise TypeError("magazine must be Magazine type")
            self.__magazine = magazine
        except TypeError as e:
            print(e)
    
    @property
    def aim(self):
        return self.__aim

    @aim.setter
    def aim(self, aim: Aim):
        try:
            if not isinstance(aim, Aim):
                raise TypeError("magazine must be Magazine type")
            self.__aim = aim
        except TypeError as e:
            print(e)

    @property
    def barrel(self):
        return self.__barrel

    @barrel.setter
    def barrel(self, barrel: Barrel):
        try:
            if not isinstance(barrel, Barrel):
                raise TypeError("Barrel must be barrel type")
            self.__barrel = barrel
        except TypeError as e:
            print(e)

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price: float):
        try: 
            if not isinstance(price, float):
                raise InvalidAmountInput('price', price)
            self.__price = price
        except InvalidAmountInput as e:
            print(e)

    @property
    def grime(self):
        return self.__grime

    def reload(self, cartridges: List[Cartridge]):
        if not cartridges:
            print("Your ammo ran out")
            return
        i = 0
        while len(self.__magazine.cartridges) < self.__magazine.capacity:
            self.__magazine.load_cartridge(cartridges.pop(-i))
            i+=1
    
    def unload(self):
        self.__magazine.unload()

    def take_aim(self, rotation_angle: float):
        try:
            if self.__aim == None:
                raise TypeError("No aim")
            self.__aim.rotate(rotation_angle)
        except TypeError as e:
            print(e)       

    def shoot(self):
        try: 
            if self.__grime >= 1:
                raise Dirty
            if self.__magazine == None or self.__barrel == None:
                raise TypeError("Missing weapon parts")
            self.__compatibility()
            self.__trigger.pull(self.__magazine, self.__barrel)
            self.__grime += 0.1
        except (Dirty, Incompatibility, TypeError) as e:
            print(e)

    def maintenance(self, operation: int):
        if operation == 1:
            self.__grime = 0
        if operation == 2:
            self.__barrel.is_cut = True 

    def safe_storage(self) -> bool:
        return self.__magazine.empty

