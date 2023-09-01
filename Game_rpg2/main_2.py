from Back_game import *
from Front_game import *
from class_personn_2 import *
import pygame

class Game_Full(Game_Controler,Game_Front,PersonClass):
    def __init__(self):
        Game_Controler.__init__(self)
        Game_Front.__init__(self)
        PersonClass.__init__(self)
        #self.game_back = None
        #self.game_front = None
        self.HP_lock = None
        self.HP_lock_en = None
        self.__HP_lock_def = None
        self.__HP_lock_en_def = None
        self.percent_life = None
        self.percent_life_en = None
        self.a = Game_Full.create_game(self,640,480)


    def settings(self):
        Game_Full.choose_person(self,self.a)
        Game_Full.sort_enemys(self)
        
        if str(type(self.jogador)) == "<class 'class_personn_2.WereWolf'>":
            self.y_player = 320
        print(type(self.jogador))
        
        HP_temp = str(self.jogador.HP).split()
        self.HP_lock = HP_temp.copy()
        self.HP_lock = "".join(self.HP_lock)
        
        HP_temp2 = str(self.enemy.HP).split()
        self.HP_lock_en = HP_temp2.copy()
        self.HP_lock_en = "".join(self.HP_lock_en)
        
    def stand(self):
        HP_temp = str(self.HP_lock).split()
        self.__HP_lock_def = HP_temp.copy()
        
        HP_temp2 = str(self.HP_lock_en).split()
        self.__HP_lock_en_def = HP_temp2.copy()
        
        if type(HP_temp) != "<class 'list'>" or type(HP_temp2) != "<class 'list'>":
            self.__HP_lock_def = "".join(self.__HP_lock_def)
            self.__HP_lock_en_def =  "".join(self.__HP_lock_en_def)
            
            self.percent_life = ((self.jogador.HP * 100/100) / int(self.__HP_lock_def))*100
            self.percent_life_en = ((self.enemy.HP * 100/100) / int(self.__HP_lock_en_def))*100
    
            Game_Full.GUI(self,self.command_GUI,HP=self.percent_life,HP_en=self.percent_life_en)
            
            if self.indice_animation > 6 and self.indice_animation < 27:
                self.window.blit(Game_Full.create_player(self,self.a,event = "walk_next"),(self.x_player,self.y_player))
                self.window.blit(Game_Full.create_enemy(self,"1",event = "stand"),(self.x_enemy,self.y_enemy))
                
            elif self.indice_animation > 27:
                self.window.blit(Game_Full.create_player(self,self.a,event = "atk"),(self.x_player,self.y_player))
                self.window.blit(Game_Full.create_enemy(self,"1",event = "stand"),(self.x_enemy,self.y_enemy))
            else:
                self.window.blit(Game_Full.create_player(self,self.a,event = "stand"),(self.x_player,self.y_player))
                self.window.blit(Game_Full.create_enemy(self,"1",event = "stand"),(self.x_enemy,self.y_enemy))
            
        else:   
            if self.indice_animation > 6 and self.indice_animation < 27:
                self.window.blit(Game_Full.create_player(self,self.a,event = "walk_next"),(self.x_player,self.y_player))
                self.window.blit(Game_Full.create_enemy(self,"1",event = "stand"),(self.x_enemy,self.y_enemy))
                Game_Full.GUI(self,self.command_GUI)
                
            elif self.indice_animation > 27:
                self.window.blit(Game_Full.create_player(self,self.a,event = "atk"),(self.x_player,self.y_player))
                self.window.blit(Game_Full.create_enemy(self,"1",event = "stand"),(self.x_enemy,self.y_enemy))
                Game_Full.GUI(self,self.command_GUI)
            else:
                self.window.blit(Game_Full.create_player(self,self.a,event = "stand"),(self.x_player,self.y_player))
                self.window.blit(Game_Full.create_enemy(self,"1",event = "stand"),(self.x_enemy,self.y_enemy))
                Game_Full.GUI(self,self.command_GUI)
    
    def run(self):
        Game_Full.settings(self)
        

        while True:
            self.clock.tick(4)
            self.window.fill((0,0,0))
            print(self.jogador.HP,self.enemy.HP)
            print(self.distance)
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                elif event.type == KEYDOWN:
                    if event.key == K_d and Game_Full.Can_I_play(self,self.block_action):
                        self.x_player += 10
                        a = Game_Full.create_player(self,self.a,event = "walk_next")
                        self.window.blit(a,(self.x_player,self.y_player))
                        Game_Full.command(self,"2")
                        Game_Full.Round(self,player = "player",command="2")
                        self.block_action = 1
                        Game_Full.Enemy_controller(self,Game_Full.Enemy_controller_front(self))
                        
                    elif event.key == K_j and Game_Full.Can_I_play(self,self.block_action) and self.jogador.Can_I_attack(self.distance):
                        a = Game_Full.create_player(self,self.a,event = "atk")
                        self.window.blit(a,(self.x_player,self.y_player))
                        Game_Full.command(self,"1")
                        Game_Full.Round(self,player = "player",command="1")
                        self.block_action = 1
                        Game_Full.Enemy_controller(self,Game_Full.Enemy_controller_front(self))

                    elif event.key == K_z and Game_Full.Can_I_play(self,self.block_action):
                        self.window.blit(Game_Full.create_player(self,self.a,event = "stand"),(self.x_player,self.y_player))
                        self.block_action = 1
                        Game_Full.Enemy_controller(self,Game_Full.Enemy_controller_front(self))
                        
                #if self.block_action == 0:            
                 #   Game_Full.Round(self,player = "player",command = Game_Full.command(self,"4"))
                 #   Game_Full.GUI(self,"PLAY")

                if self.enemy.HP <= 0:
                    if Game_Full.I_Won(self):
                        Game_Full.GUI(self,"WIN")
                    

                    #else:
                    #    self.jogador.HP += int(HP_lock) + int(HP_lock) * 20/100
                    #    self.jogador.ATK += 100
                    #   HP_lock = str(self.jogador.HP)
                    #   Game_Full.sort_enemys(self)

                elif self.enemy.HP < 200 and type(self.enemy) == 'class_personn.WereWolf':
                    self.enemy.ATK += 300

                if Game_Full.Game_Over(self):
                    Game_Full.GUI(self,"LOSE")
                    
                        
                                                

            Game_Full.blit_game(self)
            Game_Full.stand(self)
            pygame.display.flip()
            pygame.display.update()

    


Game_RPG = Game_Full()
Game_RPG.run()

        
            




