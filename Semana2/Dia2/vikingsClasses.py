
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
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if Soldier.health != 0:
            return str(self.name) + 'has received ' + str(damage) + ' points of damage'
        else: 
            return str(self.name) + 'has died in act of combat '
        
    def battleCry(self):
        return  "Odin Owns You All!"
        

# Saxon
class Saxon:
    pass


# War
class War:
    pass
