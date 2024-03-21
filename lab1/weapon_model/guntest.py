from weapon import *

def guntest(weapon: Weapon, cartridges: List[Cartridge]):
    while True:
        print(f""" 
        Choose an action with weapon: 
              1 - take aim
              2 - shoot
              3 - reload
              4 - unload
              5 - clean
              6 - cut the barrel
              7 - view detail information
              8 - exit
        """)
        choise = int(input("Enter the number"))
        match choise:
            case 1:
                angle = input("Enter rotation angle: ")
                weapon.take_aim(angle)
            case 2:
                weapon.shoot()
                print(weapon.grime)
            case 3:
                print('reloading...')
                weapon.reload(cartridges)
            case 4:
                print('your weapon is unload')
                weapon.unload()
            case 5:
                print('your weapon is clean now')
                weapon.maintenance(1)
            case 6:
                print('your weapon has cut barrel')
                weapon.maintenance(2)
            case 7:
                print(weapon)
                print(weapon.magazine)
                print(weapon.barrel)
                print(weapon.aim)
            case 8:
                if weapon.safe_storage() == False:
                    print("unload a gun first!")
                else:
                    return
            case _:
                print("Enter the number from 1 to 8!")