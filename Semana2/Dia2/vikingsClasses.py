
# Soldier

class Soldier:
    
    def __init__(self, health, strength):
        
        self.health = health
        self.strength = strength
    
    def attack(self):
        
        return self.strength
    
    def receiveDamage(self, damage):
        
        self.health = self.health - damage

# Viking

class Viking(Soldier):
    def __init__(self, health, strength, name):
        super().__init__(health, strength)
        self.name = name
    
    def receiveDamage(self, damage):
        return super().receiveDamage(damage)

    def battleCry():
        

# Saxon
class Saxon:
    pass


# War
class War:
    pass
