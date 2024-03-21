from gunshop import *
from player import Player
from guntest import guntest
from saves import *
def main():
    player = None
    gunshop = None

    if load_state('gunshop.pkl') != None:
        player, gunshop = load_state('gunshop.pkl') 
    
    if player is None or gunshop is None:
        glock_aim = Aim('Glock 19','handgun', 'machanical')
        glock_magazine = Magazine('Glock 19','handgun', 15, 9)
        glock_barrel = Barrel('Glock 19', 'handgun', 9)
        glock = Weapon('Glock 19', 'handgun', glock_magazine, glock_aim, glock_barrel, 100)
        gl_cart = Cartridge('Glock 19', 9, 'handgun', 0.1)
        gl_pack = [gl_cart] * 50

        ak_74_aim = Aim('AK-74','machine gun', 'mechanical')
        ak_74_magazine = Magazine('AK-74','machine gun', 30, 5.45)
        ak_74_barrel = Barrel('AK-74','machine gun', 5.45)
        ak_74 = Weapon('AK-74', 'machine gun', ak_74_magazine, ak_74_aim, ak_74_barrel, 200)
        ak_74_cart = Cartridge('AK-74', 5.45, 'machine gun', 0.11)
        ak_pack = [ak_74_cart] * 100

        Rem_870_aim = Aim('Remington 870','shotgun', 'mechanical')
        Rem_870_magazine = Magazine('Remington 870','shotgun', 5, 12)
        Rem_870_barrel = Barrel('Remington 870','shotgun', 12)
        Rem_870 = Weapon('Remington 870', 'shotgun', Rem_870_magazine, Rem_870_aim, Rem_870_barrel, 180)
        Rem_cart = Cartridge('Remington 870', 12, 'shotgun', 0.12)
        rem_pack = [Rem_cart] * 30

        B_M82_aim = Aim('Barret M82','rifle', 'optical', 10)
        B_M82_magazine = Magazine('Barret M82','rifle', 10, 12.7)
        B_M82_barrel = Barrel('Barret M82','rifle', 12.7)
        b_M82 = Weapon('Barret M82', 'rifle', B_M82_magazine, B_M82_aim, B_M82_barrel)
        m82_cart = Cartridge('Barret M82', 12.7, 'rifle', 0.13)
        m82_pack = [m82_cart] * 30

        gunshop = Gunshop()
        gunshop.add_weapon(glock, glock.weapon_type)
        gunshop.add_cartridges(gl_pack, gl_pack[0].weapon_type)
        gunshop.add_weapon(ak_74, ak_74.weapon_type)
        gunshop.add_cartridges(ak_pack, ak_pack[0].weapon_type)
        gunshop.add_weapon(Rem_870, Rem_870.weapon_type)
        gunshop.add_cartridges(rem_pack, rem_pack[0].weapon_type)
        gunshop.add_weapon(b_M82, b_M82.weapon_type)
        gunshop.add_cartridges(m82_pack, m82_pack[0].weapon_type)

        player = Player('Player')
        print(f"\n Hello, {player.name}. You are at the gunshop.")
        player.name = input("\nEnter your name: ")

    while True:
        print(f"""Choose an action, {player.name}:
            1 - View the assortment
            2 - View your inventory
            3 - Test a weapon
            4 - Buy a weapon
            5 - Sell your weapon
            6 - Buy cartridges
            7 - Sell cartridges
            8 - Check your wallet
            9 - Save
            10 - Exit
            """)
        choise = int(input("Enter the number: "))
        match choise:
            case 1:
                gunshop.show_assortment()
            case 2:
                player.show_inventory()
            case 3:
                name = input("Enter weapon name: ")
                weapon = gunshop.find_weapon(name)
                cartridges = gunshop.find_cartridges(name)
                guntest(weapon, cartridges)
            case 4: 
                name = input("Enter weapon name: ")
                purchase = gunshop.sell_weapon(gunshop.find_weapon(name))
                player.buy_weapon(purchase)
            case 5:
                name = input("Enter weapon name: ")
                purchase = player.sell_weapon(player.find_weapon(name))
                gunshop.buy_weapon(purchase)
            case 6: 
                name = input("Enter weapon name: ") 
                purchase = gunshop.sell_cartridges(gunshop.find_cartridges(name))
                player.buy_cartridges(purchase)
            case 7: 
                name = input("Enter weapon name: ")
                purchase = player.sell_cartridges(player.find_cartridges(name))
                gunshop.buy_cartridges(purchase)
            case 8:
                print(f"\nYour budjet: {player.budget}")
            case 9:
                save_state(player, gunshop, 'gunshop.pkl')
            case 10:
                print(f"Bye, {player.name}")
                break
            case _:
                print("Enter the number from 1 to 10!")
    
    
    
    
if __name__ == "__main__":
    main()