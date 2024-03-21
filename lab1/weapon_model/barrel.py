from magazine import *

class Barrel:
    def __init__(self, name: str, weapon_type: str, caliber: float):
        self.__name = name
        self.__weapon_type = weapon_type
        self.__caliber = caliber
        self.__cartridges = [] 
        self.__is_cut = False
    
    def __str__(self):
        return f"{self.__weapon_type} barrel. \n \
         Caliber: {self.__caliber}. {'Uncutted' if not self.__is_cut else 'Cutted'}. \n \
            {'Unloaded' if not self.__cartridges else 'Loaded'}"

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
    def caliber(self):
        return self.__caliber
    
    @caliber.setter
    def caliber(self, caliber: float):
        try:
            if not isinstance(caliber, float | int) or caliber < 0:
                raise InvalidAmountInput('Caliber', caliber)
            self.__caliber = caliber
        except InvalidAmountInput as e: 
            print(e)
    
    @property
    def is_cut(self):
        return self.__is_cut
    
    @is_cut.setter
    def is_cut(self, is_cut: bool):
        try:
            if not isinstance(is_cut, bool):
                raise TypeError("\"is_cut\" must be bool value") 
            self.__is_cut = is_cut
        except TypeError as e:
            print(e)
            
    @property
    def cartridges(self):
        return self.__cartridges

    @cartridges.setter
    def cartridges(self, cartridges: List[Cartridge]):
        try:
            if all(isinstance(cartridge, Cartridge) for cartridge in cartridges) == False:
                raise TypeError("Invalid input. The list must be the \"Cartridge\" type")
            self.__cartridges = cartridges
        except (ValueError, TypeError) as e: 
            print(e)


    def load_barrel(self, cartridge: Cartridge):
        if (not isinstance(cartridge, Cartridge) and
             len(self.__cartridges) == 1):
            return
        self.__cartridges.append(cartridge)

    def fire(self):
        self.__cartridges.pop(0)
    
