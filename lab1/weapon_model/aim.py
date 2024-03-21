from valid_values import *
from exceptions import *

class Aim:
    def __init__(self, name: str, weapon_type: str, aim_type: str, magnification: float=0):
        self.__name = name
        self.__weapon_type = weapon_type
        self.__aim_type = aim_type
        self.__magnification = magnification
        self.__angle = 0
    
    def __str__(self):
        return f"{self.__weapon_type} {self.__aim_type} aim. \n Magnification: {self.__magnification}.\n \
        rotation angle: {self.__angle}"

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
    def aim_type(self):
        return self.__aim_type
    
    @aim_type.setter
    def aim_type(self, aim_type: str):
        try:
            if aim_type not in VALID_AIM_TYPES:
                raise ListMismatch(aim_type, VALID_AIM_TYPES)
            self.__aim_type = aim_type
            if aim_type != 'optical':
                self.__magnification = 0
        except ListMismatch as e:
            print(e)

    @property
    def magnification(self):
        return self.__magnification
    
    @magnification.setter
    def magnification(self, magnification: float):
        try:
            if self.__aim_type != 'optical':
                raise ValueError("You should change the aim type, to set magnification.")
            self.__magnification = magnification 
        except ValueError as e:
            print(e)
    
    @property
    def angle(self):
        return self.__angle
    
    def rotate(self, delta: float):
        try:
            delta_angle = float(delta)   
            self.__angle += delta_angle
            self.__angle %= 360
        except TypeError as e:
            print(e)