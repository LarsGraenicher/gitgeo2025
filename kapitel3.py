# --- Player, Character, Class


class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.character_class.setupCharacter(self)
        self.level= 1
        self.health =100
        self.attack_power=10
        self.defense= 10

    def setHealth(self, health):
        self.health=health


    def attack(self):
        print("Huaa")

    def take_damage(self, amount):
        self.health -=amount
        if self.health <=0:
            print(f"{self.name} ist verstorben")


class PlayerCharacter(Character):
    def __init__(self, name, character_class, player):
        super().__init__(name, character_class)
        self.player=player
        self.inventory=[]

class NpcCharacter(Character):
    def __init__(self, name, character_class):
        super().__init__(name, character_class)
        self.dropList=[]

class CharacterClass:
    def __init__(self, className):
        self.className=className
    
    def setupCharacter(character):
        print("Abstract class no function")

class WarriorClass(CharacterClass):
    def __init__(self):
        super().__init__("Warrior")

    def setupCharacter(self, character):
        print(type(character))
        character.setHealth(200)

class MageClass(CharacterClass):
    def __init__(self):
        super().__init__("Mage")

c1=NpcCharacter("Horst", WarriorClass())
p1=PlayerCharacter("Hansli", MageClass(), "Player1")

p1.take_damage(1000)

