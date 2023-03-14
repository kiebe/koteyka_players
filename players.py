from random import random
class Player:
    def __init__(self, name:str):
        self.health = 1000 # Здоровье персонажа
        self.sword = {} # Свойства меча персонажа
        self.name = name # Имя персонажа
        self.alive = True # Жив ли персонаж
        
    def __add__(self, other): # <Персонаж> + <что-либо>
        """
        self:
            Наш персонаж, персонаж который наносит урон
            
        other: 
            Персонаж, которому наносим урон
            Оружие, характеристики которого добавляем к персонажу
        
        return:
            True если добавилось оружие
            Свойства персонажа которого мы дамажим
            None в других случаях
            
        """
        if type(other) == Sword: # Если мы прибавляем оружие, то добавляем его характеристики к персонажу
            sword = other
            self.sword = {'name': sword.name, 
                          'damage': sword.damage,
                          'enchantments': sword.enchantments,
                          'crit_rate': sword.crit_rate,
                          'crit_dmg': sword.crit_dmg,
                          }
            
            return True # Всё успешно, возвращаем True
        
        elif type(other) == Player:  # Если мы прибавляем <персонажа> (<персонаж> + <персонаж>)
            if not self.sword: # Если у нас нету меча
                return
            sword = self.sword # Меч
            damage = sword['damage'] # Стандартный урон нашего меча не учитывая крит
            if random() <= sword['crit_rate']: # Если кританул
                damage += damage * sword['crit_dmg'] # Увеличиваем урон на (урон * крит урон)
                
            other.health -= int(damage) # Вычитаем из здоровья урон оружия

            if other.health <= 0: # Если здоровье меньше или 0
                other.alive = False # Теперь мы не живы
                other.health = 0 # Если хп было бы меньше чем 0, то стало бы 0 (чтобы хп не было отрицательным)
                
            return {'player': other.name,
                    'damage': self.sword['damage'],
                    'health': other.health}
                
class Sword:
    def __init__(self, name:str, damage:int, crit_rate:float, crit_dmg:float, enchantments=None, level:int=1) -> None:
        self.name = name                 # Имя оружия
        self.damage = damage - 1         # Урон оружия по умолчанию
        self.enchantments = enchantments # Зачарования на оружии
        self.crit_rate = crit_rate       # Шанс критического попадания
        self.crit_dmg = crit_dmg         # На сколько раз увеличится урон при крит попадании (damage+damage*crit_dmg)
        self._level = 0               # Уровень оружия (чем выше тем выше урон)
        
        self._can_level_up = True # Можно ли улучшать оружие (нельзя если уровень = 90)
        
        self.level_up(level)
    def level_up(self, amount:int=1): # Повысить уровень оружия
        if not self._can_level_up: 
            return
        self._level += amount
        if self._level >= 90: # Уровень не может быть выше 90 лвл
            self._level = 90  
            self._can_level_up = False
            return
        self.damage += amount
        
    
nikita = Player("Никита")
alik = Player("АЛИК")


dubina = Sword('Дубина переговоров', 100, 0.5, 0.7)

#запуск
alik + dubina
alik + nikita
print(nikita.health)

