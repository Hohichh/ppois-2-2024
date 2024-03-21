import unittest   # The test framework
from gunshop import *
from player import *
from barrel import *

class Test_CartrdigeClass(unittest.TestCase):
    def setUp(self):
        self.exampleCart = Cartridge('Glock 19', 9, 'handgun', 10)
    
    def test_NameGetSet(self):
        self.assertEqual(self.exampleCart.name, 'Glock 19')
        self.exampleCart.name = 'newname'
        self.assertEqual(self.exampleCart.name, 'newname')

    def test_CaliberGetSet(self):
        self.assertEqual(self.exampleCart.caliber, 9)
        self.exampleCart.caliber = 9.5
        self.assertEqual(self.exampleCart.caliber, 9.5)
    
    def test_WeaponTypeGetSet(self):
        self.assertEqual(self.exampleCart.weapon_type, 'handgun')
        self.exampleCart.weapon_type = 'rifle'
        self.assertEqual(self.exampleCart.weapon_type, 'rifle')
    
    def test_PriceGetSet(self):
        self.assertEqual(self.exampleCart.price, 10)
        self.exampleCart.price = 15
        self.assertEqual(self.exampleCart.price, 15)

class Test_MagazineClass(unittest.TestCase):
    def setUp(self):
        self.exMagazine = Magazine('Colt M1877','handgun', 6, 5)
        self.exCartridge = Cartridge('Colt M1877', 5, 'handgun', 14)

    def test_GetSetCapacity(self):
        self.assertEqual(self.exMagazine.capacity, 6)
        self.exMagazine.capacity = 7
        self.assertEqual(self.exMagazine.capacity, 7)
    
    def test_GetSetCartridges(self):
        self.assertEqual(self.exMagazine.empty, True)
        self.assertEqual(self.exMagazine.cartridges, [])
        cartridges = [self.exCartridge]*6 
        self.exMagazine.cartridges = cartridges
        self.assertEqual(self.exMagazine.cartridges, cartridges)
        self.assertEqual(self.exMagazine.empty, False)

    def test_LoadCartridge(self):
        self.assertEqual(self.exMagazine.empty, True)
        self.assertEqual(self.exMagazine.cartridges, [])
        self.exMagazine.load_cartridge(self.exCartridge)
        self.assertEqual(self.exMagazine.empty, False)
        self.assertEqual(self.exMagazine.cartridges[0], self.exCartridge)

class Test_AimClass(unittest.TestCase):
    def setUp(self):
        self.exAim = Aim('Barret M82','rifle', 'optical', 3)
    
    def test_GetSetAimType(self):
        self.assertEqual(self.exAim.aim_type, 'optical')
        self.exAim.aim_type = 'mechanical'
        self.assertEqual(self.exAim.aim_type, 'mechanical')
        self.assertEqual(self.exAim.magnification, 0)
    
    def test_GetSetMagnification(self):
        self.assertEqual(self.exAim.magnification, 3)
        self.exAim.magnification = 1.5
        self.assertEqual(self.exAim.magnification, 1.5)
    
    def test_AimRotation(self):
        self.assertEqual(self.exAim.angle, 0)
        self.exAim.rotate(30)
        self.assertEqual(self.exAim.angle, 30)

class Test_BarrelClass(unittest.TestCase):
    def setUp(self):
        self.exBarrel = Barrel('AK-74','machine gun', 5.45)
        self.exCartridge = Cartridge('AK-74', 5.45, 'machine gun', 0.11)

    def test_LoadBarrel(self):
        self.assertEqual(self.exBarrel.cartridges, [])
        self.exBarrel.load_barrel(self.exCartridge)
        self.assertEqual(self.exBarrel.cartridges[0], self.exCartridge)
    
    def test_Fire(self):
        self.assertEqual(self.exBarrel.cartridges, [])
        self.exBarrel.load_barrel(self.exCartridge)
        self.assertEqual(self.exBarrel.cartridges[0], self.exCartridge)
        self.exBarrel.fire()
        self.assertEqual(self.exBarrel.cartridges, [])
    
    def test_GetSetIsCut(self):
        self.assertEqual(self.exBarrel.is_cut, False)
        self.exBarrel.is_cut = True
        self.assertEqual(self.exBarrel.is_cut, True)
        
class Test_WeaponClass(unittest.TestCase):
    def setUp(self):
        self.Rem_870_aim = Aim('Remington 870','shotgun', 'mechanical')
        self.Rem_870_magazine = Magazine('Remington 870','shotgun', 5, 12)
        self.Rem_870_barrel = Barrel('Remington 870','shotgun', 12)
        self.Rem_870 = Weapon('Remington 870', 'shotgun', self.Rem_870_magazine,
                               self.Rem_870_aim, self.Rem_870_barrel, 180)
        self.Rem_cart = Cartridge('Remington 870', 12, 'shotgun', 0.12)
        self.rem_pack = [self.Rem_cart] * 30

    def test_Reload(self):
        self.assertEqual(self.Rem_870.magazine.cartridges, [])
        self.Rem_870.reload(self.rem_pack)
        self.assertEqual(len(self.Rem_870.magazine.cartridges), self.Rem_870.magazine.capacity)
    
    def test_unload(self):
        self.Rem_870.reload(self.rem_pack)
        self.assertEqual(len(self.Rem_870.magazine.cartridges), self.Rem_870.magazine.capacity)
        self.Rem_870.unload()
        self.assertEqual(len(self.Rem_870.magazine.cartridges), 0)
    
    def test_take_aim(self):
        self.assertEqual(self.Rem_870.aim.angle, 0)
        self.Rem_870.take_aim(45)
        self.assertEqual(self.Rem_870.aim.angle, 45)
    
    def test_shoot(self):
        self.Rem_870.reload(self.rem_pack)
        self.assertEqual(len(self.Rem_870.magazine.cartridges), self.Rem_870.magazine.capacity)
        self.Rem_870.shoot()
        self.assertEqual(len(self.Rem_870.magazine.cartridges), self.Rem_870.magazine.capacity-1)
        self.Rem_870.shoot()
        self.assertEqual(len(self.Rem_870.magazine.cartridges), self.Rem_870.magazine.capacity-2)

    def test_maintenance(self):
        self.assertEqual(self.Rem_870.barrel.is_cut, False)
        self.Rem_870.maintenance(2)
        self.assertEqual(self.Rem_870.barrel.is_cut, True)

        self.Rem_870.reload(self.rem_pack)
        self.Rem_870.shoot()
        self.Rem_870.shoot()
        self.Rem_870.shoot()
        self.assertEqual(round(self.Rem_870.grime, 1), 0.3)
        self.Rem_870.maintenance(1)
        self.assertEqual(self.Rem_870.grime, 0)
    
    def test_safe_storage(self):
        self.Rem_870.reload(self.rem_pack)
        self.assertEqual(self.Rem_870.safe_storage(), False)
        self.Rem_870.unload()
        self.assertEqual(self.Rem_870.safe_storage(), True)

class Test_Gunshop_Player(unittest.TestCase):
    def setUp(self):
        self.Rem_870_aim = Aim('Remington 870','shotgun', 'mechanical')
        self.Rem_870_magazine = Magazine('Remington 870','shotgun', 5, 12)
        self.Rem_870_barrel = Barrel('Remington 870','shotgun', 12)
        self.Rem_870 = Weapon('Remington 870', 'shotgun', self.Rem_870_magazine, 
                              self.Rem_870_aim, self.Rem_870_barrel, 180)
        self.Rem_cart = Cartridge('Remington 870', 12, 'shotgun', 0.12)
        self.rem_pack = [self.Rem_cart] * 30

        self.gunshop = Gunshop()
        self.gunshop.add_weapon(self.Rem_870, self.Rem_870.weapon_type)
        self.gunshop.add_cartridges(self.rem_pack, self.rem_pack[0].weapon_type)
        self.player = Player('Player')

    def test_buysell_weapon(self):
        name = 'Remington 870'
        purchase = self.gunshop.sell_weapon(self.gunshop.find_weapon(name))
        self.player.buy_weapon(purchase)
        self.assertEqual(len(self.gunshop._Gunshop__weapons['shotgun']), 0)
        self.assertEqual(self.player._Player__weapons['shotgun'][0], purchase)

        purchase = self.player.sell_weapon(self.player.find_weapon(name))
        self.gunshop.buy_weapon(purchase)
        self.assertEqual(len(self.player._Player__weapons['shotgun']), 0)
        self.assertEqual(self.gunshop._Gunshop__weapons['shotgun'][0], purchase)
    
    def test_buysell_cartridge(self):
        name = 'Remington 870'
        purchase = self.gunshop.sell_cartridges(self.gunshop.find_cartridges(name))
        self.player.buy_cartridges(purchase)
        self.assertEqual(len(self.gunshop._Gunshop__cartridges['shotgun']), 0)
        self.assertEqual(self.player._Player__cartridges['shotgun'][0], purchase)

        purchase = self.player.sell_cartridges(self.player.find_cartridges(name))
        self.gunshop.buy_cartridges(purchase)
        self.assertEqual(len(self.player._Player__cartridges['shotgun']), 0)
        self.assertEqual(self.gunshop._Gunshop__cartridges['shotgun'][0], purchase)

if __name__ == '__main__':
    unittest.main()