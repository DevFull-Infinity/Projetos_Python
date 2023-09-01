from class_personn_2 import *
from Front_game import *
import random

class Game_Controler:
    def __init__(self):
        self.ListaClass = [Mage(),Rogue_vampire(),WereWolf()]
        self.jogador = None
        self.enemy = None
        self.distance = 500
        self.won_round = 0
        self.choose_class = None

    def choose_person(self,choose_class):
        
        if choose_class == "1":
            self.jogador = Mage()
            print("a")
           

        elif choose_class == "2":
            self.jogador = Rogue_vampire()
            

        elif choose_class == "3":
            self.jogador = WereWolf()



    def sort_enemys(self):
        if self.ListaClass == []:
            return False
        
        else:
            self.enemy = Mage()
            #self.enemy = random.choice(self.ListaClass)  
            #self.ListaClass.remove(self.enemy)



    def Round(self,player,command):
        if player == "player":
            if command == "1": #and self.jogador.Can_I_attack(distance = self.distance):
                dano = (self.jogador.ATK + random.randint(0,50)) - (self.enemy.DEF + random.randint(0,50))

                if dano < 0:
                    dano = 0

                self.enemy.HP -= dano
                
                dano = 0
            
            elif command == "2":
                self.distance -= 10
                

            elif command == "3":
                if self.jogador.Can_I_walk():
                    self.distance += 10
                    
            elif command == "4":
                pass

                
        elif player == "enemy":
            if command == "1":
                dano = (self.enemy.ATK + random.randint(0,50)) - (self.jogador.DEF + random.randint(0,50))

                if dano < 0:
                    dano = 0

                self.jogador.HP -= dano
                dano = 0
            
            elif command == "2":
                self.distance -= 10
        
            elif command == "3":
                if self.enemy.Can_I_walk():
                    self.distance += 10
                    

    def Enemy_controller(self,ATK):
        if self.distance > self.enemy.RANG:
            Game_Controler.Round(self,player = "enemy", command = "2")

        elif self.distance <= self.enemy.RANG and ATK == True:
            Game_Controler.Round(self,player = "enemy", command = "1")


    def Game_Over(self):
        if self.jogador.HP <= 0:
            return True

    def I_Won(self):
        self.won_round += 1
        if self.won_round == 1:
            return True

    

    



        

