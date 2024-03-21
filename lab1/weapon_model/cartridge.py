from exceptions import *
from valid_values import *

class Cartridge:
    def __init__(self, name:str, caliber: float, weapon_type: str, price: float=0.1): 
        self.__name = name
        self.__caliber = caliber
        self.__weapon_type = weapon_type
        self.__price = price

    def __str__(self):
        return f"Cartridges for {self.__name} \n Caliber: {self.__caliber}"
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price: float):
        try:
            if not isinstance(price, float | int):
                raise InvalidAmountInput('price', price)
            self.__price = price
        except InvalidAmountInput as e:
            print(e)