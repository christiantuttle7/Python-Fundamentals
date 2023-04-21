class Player:

    def __init__(self, hp=10, damage = 2):
        self.hp = hp
        self.damage = damage
    
    def take_damage(self, enemy):
        self.hp -= enemy.damage
    def hit(self, enemy):
        enemy.hp -= self.damage
    def __str__(self):
        return f"HP = {self.hp}, Damage = {self.damage}"

corin = Player(50,10)
morty = Player(10,2)

morty.hit(corin)
print(corin, morty)
morty.take_damage(corin)
print(corin, morty)
