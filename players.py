class Player:
    def __init__(self, name:str):
        self.health = 100
        self.sword = {}
        self.name = name
        self.alive = True
        self.is_freeze = False
        
    def __add__(self, other):
        if type(other) == Sword:
            self.sword = {'name': other.name, 'damage': other.damage, 'freezing': other.freezing}
            return True
        elif type(other) == Player:
            try:
                other.health -= self.sword['damage']
            except KeyError:
                return False
            
            if other.health <= 0:
                other.alive = False
                other.health = 0
                
            return {'player': other.name, 'damage': self.sword['damage'], 'health': other.health}
                

class Sword:
    def __init__(self, name:str, damage:int, freezing:bool=False) -> None:
        self.name = name
        self.damage = damage
        self.freezing = freezing
    
nikita = Player("Никита")
alik = Player("АЛИК")


dubina = Sword('Дубина переговоров', 110)

#запуск
alik + dubina
alik + nikita
print(nikita.health)

