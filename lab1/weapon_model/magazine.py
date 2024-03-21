from cartridge import *
from typing import List

class Magazine:
    def __init__(self, name: str, weapon_type: str, capacity: int, caliber: float, 
                 cartridges: List[Cartridge]=None):
        self.__name = name
        self.__capacity = capacity
        self.__weapon_type = weapon_type
        self.__caliber = caliber
        self.__cartridges = cartridges if cartridges else []
        self.__empty = not cartridges

    def __str__(self):
        if self.__empty == True:
            return f"{self.__weapon_type} magazine with capacity {self.__capacity}. \n \
            Empty."
        else: 
            return f"{self.__weapon_type} magazine with capacity {self.__capacity}. \n \
            {len(self.__cartridges)}/{self.__capacity}"

    def __compatibility(self):
        if all(self.__name == cartridge.name for cartridge in self.__cartridges) == False:
            raise TypeError(f"Incorrect cartridge type!")

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def empty(self):
        return self.__empty

    def __update_empty(self):
        self.__empty = not self.__cartridges

    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, capacity: int):
        try:
            if not isinstance(capacity, int) or capacity < 0:
                raise InvalidAmountInput('Capacity', capacity)
            self.__capacity = capacity
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
    def cartridges(self):
        return self.__cartridges
    
    @cartridges.setter
    def cartridges(self, cartridges: List[Cartridge]):
        try:
            if all(isinstance(cartridge, Cartridge) for cartridge in cartridges) == False:
                raise TypeError("Invalid input. The list must be the \"Cartridge\" type")
            if len(cartridges) > self.__capacity:
                raise ValueError("Cartridges amount exceeds the magazine capacity")
            self.__compatibility()
            self.__cartridges = cartridges
            self.__update_empty()
        except (ValueError, TypeError) as e: 
            print(e) 
    
    def load_cartridge(self, cartridge: Cartridge):
        try:
            if not isinstance(cartridge, Cartridge):
                raise TypeError("Invalid Input. Loaded item must be a \"Cartridge\" type.")
            if self.__name != cartridge.name:
                raise ValueError("Weapon type mismatch")
            if len(self.__cartridges) == self.capacity:
                return
            self.__cartridges.append(cartridge)
            self.__update_empty()
        except (TypeError,ValueError) as e:
            print(e) 
    
    def unload(self):
        self.__cartridges.clear()
        self.__update_empty()

    def cartridge_feed(self) -> Cartridge:
        if self.__cartridges:
            out = self.__cartridges.pop(-1)
            self.__update_empty()
            return out
        else:
            self.__update_empty()
            return None 
