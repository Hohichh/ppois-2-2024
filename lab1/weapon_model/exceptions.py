#класс для обработки исключений типа ValueError и TypeError -
#незможность преобразования str в int/float; 
#а также когда input_value < 0
class InvalidAmountInput(Exception):
    def __init__(self, attribute_name:str, input_value):
        self.input_value = input_value
        self.attribute_name = attribute_name
    def __str__(self):
        return f"Invalid input value: {self.input_value}. \n \
             {self.attribute_name} must be a positive number."

#класс для обработки исключений ValueError, 
#случай когда значение не соответствует установленным спискам:
#VALID_WEAPON_TYPES , VALID_INTENDED_USE
class ListMismatch(Exception):
    def __init__(self, input_value, values_list:set):
        self.input_value = input_value
        self.values_list = values_list
    def __str__(self):
        return f"Invalid type: {self.input_value} \n \
            Allow types are: \n {self.values_list}"
#класс для обработки исключения, когда пистолет загразнился    
class Dirty(Exception):
    def __str__(self):
        return "Clean your gun!"

class Incompatibility(Exception):
    def __init__(self, weapon, magazine, barrel, aim):
        self.__weapon = weapon
        self.__maazine = magazine
        self.__barrel = barrel
        self.__aim = aim

    def __str__(self):
        return f"Error: incompatibility of parts! Weapon: {self.__weapon.name}\n \
            Magazine for {self.__maazine.neme}, \n \
            Barrel for {self.__barrel.name} \n \
            Aim for {self.__aim.name}"