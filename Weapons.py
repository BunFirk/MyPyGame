
import random
class Weapon:
    def __init__(self, name: str, damage: int, critMin: int, critMax: int, weight: int, defence: int):
        self.name = name
        self.critMin = critMin
        self.critMax = critMax
        self.damage = damage
        self.weight = weight
        self.degradation = 50
        self.procDeration = 200
        
        
    def critDamage(self):
        self.damage = self.damage * random.randint(self.critMin, self.critMax)
        return self.damage
    
    def degactionControl(self):
        return (self.degradation * self.procDeration) // 100
        
class Sword(Weapon):
    def __init__(self, name: str, damage: int, critMin: int, critMax: int, weight: int, deterioration: int):
        super().__init__(name, damage, critMin, critMax, weight, deterioration)
    def attack(self):
        self.degradation -= 1
        print(f"{self.name} наносит {self.critDamage()}.")
        print(f"Износ {self.name}: {self.degactionControl()}%")


sword = Sword("Мой мечь", 5, 1, 5, 7, 100)
sword.attack()
sword.attack()
"""
a = 200
proc = 50

res = (a * proc) / 100
print(res)  # Выведет 50
"""