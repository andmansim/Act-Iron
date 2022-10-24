
import random
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
        if self.health != 0:
            return str(self.name) + ' has received ' + str(damage) + ' points of damage'
        else: 
            return str(self.name) + ' has died in act of combat'
        
    def battleCry(self):
        return  "Odin Owns You All!"
        

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health != 0:
            return  'A Saxon has received ' + str(damage) + ' points of damage'
        else: 
            return 'A Saxon has died in combat'


# War
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        self.v = random.choice(self.vikingArmy)
        self.s = random.choice(self.saxonArmy)

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        
        resultado = self.s.receiveDamage(self.v.strength)
        if self.s.health == 0:
            self.saxonArmy.remove(self.s)
        return resultado
    
    def saxonAttack(self):
        
        resultado = self.v.receiveDamage(self.s.strength)
        if self.v.health == 0:
            self.vikingArmy.remove(self.v)
        return resultado
        
            
        
    def showStatus(self):
        if len(self.saxonArmy) == 0:
           return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."