class PersonClass:
    def __init__(self):
        self.HP = 0
        self.ATK = 0
        self.DEF = 0
        self.RANG = 0
        self.walk = 0
        


    def Can_I_attack(self,distance):
        if self.RANG >= distance:  
            return True
        else:
            return False
    
    def Can_I_walk(self):
        if self.walk == 1: 
            self.walk = 0
            return False

        elif self.walk == 0:
            self.walk +=1
            return True

    def I_Won(self):
        self.won_round += 1
        if self.won_round == 3:
            return True
        else:
            return False
        
        


class Mage(PersonClass):
    def __init__(self):
        super().__init__()
        self.HP = 500
        self.ATK = 500
        self.DEF = 100
        self.RANG = 300

    
class Rogue_vampire(PersonClass):
    def __init__(self):
        super().__init__()
        self.HP = 800
        self.ATK = 200
        self.DEF = 300
        self.RANG = 100


class WereWolf(PersonClass):
    def __init__(self):
        super().__init__()
        self.HP = 2000
        self.ATK = 200
        self.DEF = 500
        self.RANG = 100







