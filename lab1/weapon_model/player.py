from weapon import *

class Player:
    def __init__(self, name, budget=10000000):
        self.name = name
        self.__weapons = {
            'handgun': [],
            'machine gun': [],
            'shotgun': [],
            'rifle': []
        }
        self.__cartridges = {
            'handgun': [],
            'machine gun': [],
            'shotgun': [],
            'rifle': []
        }
        self.__budget = budget

    @property 
    def budget(self):
        return self.__budget

    def buy_weapon(self, weapon: Weapon):
        try:
            if not isinstance(weapon, Weapon):
                raise TypeError("\'weapon\' must be a Weapon type.")
            if weapon.weapon_type in self.__weapons:
                self.__weapons[weapon.weapon_type].append(weapon)
                self.__budget -= weapon.price
            else:
                raise ValueError(f"Unkwon weapon type {weapon.weapon_type}")
        except (TypeError, ValueError) as e:
            print(e)

    def buy_cartridges(self, cartridges: List[Cartridge]):
        try:
            if all(isinstance(cartridge, Cartridge) for cartridge in cartridges) == False:
                raise TypeError("\'cartridges\' must be a Cartridge type.")
            weapon_type = cartridges[0].weapon_type
            if weapon_type in self.__cartridges:
                self.__cartridges[weapon_type].append(cartridges)
                total_price = sum(cartridge.price for cartridge in cartridges)
                self.__budget -= total_price
            else:
                raise ValueError(f"Unkwon weapon type {weapon_type}")
        except (TypeError, ValueError) as e:
            print(e)

    def sell_weapon(self, weapon: Weapon) -> Weapon:
        try:
            if not isinstance(weapon, Weapon):
                raise TypeError("\'weapon\' must be a Weapon type.")
            if weapon.weapon_type in self.__weapons:
                if weapon in self.__weapons[weapon.weapon_type]:
                    sold_weapon = weapon
                    self.__budget += weapon.price
                    self.__weapons[weapon.weapon_type].remove(weapon)
                    return sold_weapon
                else: 
                    raise ValueError("This weapon is out of stock")
            else:
                raise ValueError(f"Unkwon weapon type {weapon.weapon_type}")
        except (TypeError, ValueError) as e:
            print(e)
            return None

    def sell_cartridges(self, cartridges: List[Cartridge]) -> List[Cartridge]:
        try:
            if all(isinstance(cartridge, Cartridge) for cartridge in cartridges) == False:
                raise TypeError("\'cartridges\' must be a Cartridge type.")
            weapon_type = cartridges[0].weapon_type
            if weapon_type in self.__cartridges:
                if cartridges in self.__cartridges[weapon_type]:
                    sold_cartridges = cartridges
                    total_price = sum(cartridge.price for cartridge in cartridges)
                    self.__budget += total_price
                    self.__cartridges[weapon_type].remove(cartridges) 
                    return sold_cartridges
                else:
                    raise ValueError("This cartridges is out of stock")
            else:
                raise ValueError(f"Unkwon weapon type {weapon_type}")
        except (TypeError, ValueError) as e:
            print(e)
            return None
    

    def show_inventory(self):
        print("\nInventory:\n")
        for weapon_type, weapons in self.__weapons.items():
            print(f"\n {weapon_type.capitalize()}: ")
            for weapon in weapons:
                print(weapon)
        for weapon_type, cartridges in self.__cartridges.items():
            print(f"\n {weapon_type.capitalize()}: ")
            if cartridges: 
                first_cartridge = cartridges[0][0] 
                print(f"Сartridges for {weapon_type}: {first_cartridge}")
    
    def find_weapon(self, name: str) -> Weapon:
        try:
            for weapon_list in self.__weapons.values():
                for weapon in weapon_list:
                    if weapon.name == name: 
                        return weapon
            raise ValueError(f"Weapon with name '{name}' not found.")
        except ValueError as e:
            print(e)

    def find_cartridges(self, cartridge_name: str) -> List[str]:
        try: 
            for weapon_type, cartridge_pack in self.__cartridges.items():
                for cartridges in cartridge_pack:
                    if cartridges and cartridges[0].name == cartridge_name: 
                        return cartridges
            raise ValueError(f"Cartridges with first cartridge name '{cartridge_name}' not found.")
        except ValueError as e:
            print(e)
            return None