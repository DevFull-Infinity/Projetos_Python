import pygame 
from pygame.locals import *
from sys import exit
import Back_game
import time



class Game_Front():
	def __init__(self):
		self.window_width = None
		self.window_length = None
		self.window = None
		self.In_window = None
		self.image_chao = None
		self.image_fundo = None
		self.image_nuvens = None
		self.clock = pygame.time.Clock()
		self.image_telaIn_ls = ["tela_inicial/frame1.png","tela_inicial/frame2.png","tela_inicial/frame1.png","tela_inicial/frame2.png","tela_inicial/frame1.png","tela_inicial/frame2.png"]
		self.image_life_ls = ["life/life100.png","life/life80.png","life/life50.png","life/life30.png",
        "life/life20.png","life/life.png"]
		self.image_mage_ls = ["mage_img/stand/frame_1.png","mage_img/stand/frame-2.png","mage_img/stand/frame-3.png","mage_img/stand/frame-4.png",
		"mage_img/walk/frame-1.png","mage_img/walk/frame-2.png","mage_img/walk/frame-3.png","mage_img/atk/frame-1.png","mage_img/atk/frame-2.png",
		"mage_img/atk/frame-3.png","mage_img/atk/frame-4.png","mage_img/atk/frame-5.png"]
		self.image_vampire_ls = []
		self.image_werewolf_ls = ["werewolf_img/stand/frame-01.gif","werewolf_img/stand/frame-02.gif","werewolf_img/stand/frame-03.gif","werewolf_img/stand/frame-04.gif","werewolf_img/stand/frame-05.gif","werewolf_img/stand/frame-06.gif","werewolf_img/stand/frame-07.gif","werewolf_img/stand/frame-08.gif","werewolf_img/stand/frame-09.gif","werewolf_img/stand/frame-10.gif","werewolf_img/walk/frame-11.gif","werewolf_img/walk/frame-12.gif","werewolf_img/walk/frame-13.gif","werewolf_img/walk/frame-14.gif","werewolf_img/walk/frame-15.gif","werewolf_img/walk/frame-16.gif","werewolf_img/walk/frame-17.gif","werewolf_img/walk/frame-18.gif","werewolf_img/walk/frame-19.gif","werewolf_img/walk/frame-20.gif","werewolf_img/walk/frame-21.gif","werewolf_img/walk/frame-22.gif","werewolf_img/walk/frame-23.gif","werewolf_img/walk/frame-24.gif","werewolf_img/walk/frame-25.gif","werewolf_img/walk/frame-26.gif","werewolf_img/walk/frame-27.gif","werewolf_img/atk/frame-01.gif","werewolf_img/atk/frame-11.gif","werewolf_img/atk/frame-12.gif","werewolf_img/atk/frame-28.gif","werewolf_img/atk/frame-29.gif","werewolf_img/atk/frame-30.gif","werewolf_img/atk/frame-36.gif","werewolf_img/atk/frame-40.gif"]
		self.indice_animation = 0
		self.indice_animation_en = 0
		self.x_player = 0
		self.y_player = 350
		self.x_enemy = 570
		self.y_enemy = 350
		self.RANG = None
		self.block_action = 0
		self.command_GUI = None
		self.x_nuvens = 30
	

	def create_game(self,window_width,window_length):
		pygame.init()
		pygame.display.set_caption('RPG GAME')
		

		self.window_width = window_width
		self.window_length = window_length
		self.window = pygame.display.set_mode((self.window_width,self.window_length))
		

		self.image_chao = pygame.image.load('chao.jpg')
		self.image_chao = pygame.transform.scale(self.image_chao,(self.window_width,50))

		self.image_fundo = pygame.image.load('fundo.jpg')
		self.image_fundo = pygame.transform.scale(self.image_fundo,(self.window_width,430))
  
		self.image_nuvens = pygame.image.load('nuvens.png')
		self.image_nuvens = pygame.transform.scale(self.image_nuvens,(300,100))
		return Game_Front.In_windown(self,window_width,window_length)
		

	
	def In_windown(self,window_width,window_length):
		person = 0
	
		while person != "1" and person != "3":
			self.clock.tick(6)
			self.window.fill((0,0,0))

			
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					exit()

				elif event.type == KEYDOWN:
					if event.key == K_1:
						person = "1"
      
					elif event.key == K_3:
						person = "3"
					
						
                
			image_tela1 = pygame.image.load(self.image_telaIn_ls[self.indice_animation])
			image_tela2 = pygame.image.load(self.image_telaIn_ls[self.indice_animation])
			image_tela1 = pygame.transform.scale(image_tela1,(350,400))
			image_tela2 = pygame.transform.scale(image_tela2,(350,400))
   
			image_tela1_M =  pygame.image.load(self.image_mage_ls[0])
			image_tela1_M = pygame.transform.scale(image_tela1_M,(150,200))
			
			image_tela2_W =  pygame.image.load(self.image_werewolf_ls[0])
			image_tela2_W = pygame.transform.scale(image_tela2_W,(150,200))
   
			s = pygame.Surface((185,275), pygame.SRCALPHA) 
			s2 = pygame.Surface((185,275), pygame.SRCALPHA)		
   
			s.fill((128,128,128,128))
			s2.fill((128,128,128,128))


			
			if self.indice_animation == 5:
				self.indice_animation = 0

			self.indice_animation += 1
	
			Game_Front.blit_game(self)
			self.window.blit(image_tela1,(10,50))
			self.window.blit(s, (77,125))
			self.window.blit(image_tela1_M,(100,200))

			self.window.blit(image_tela2,(320,50))
			self.window.blit(s2, (387,125))
			self.window.blit(image_tela2_W,(400,200))

			
			pygame.display.flip()
			pygame.display.update()
   
		return person




	def create_player(self,choose_char,event):
		if choose_char == "1":
			
			if event == "stand":
				if self.indice_animation > 5 and self.indice_animation < 7 or self.indice_animation == 11:
					self.indice_animation = 0

				image_mage = pygame.image.load(self.image_mage_ls[self.indice_animation])
				image_mage = pygame.transform.scale(image_mage,(70,100))
				
				if self.indice_animation == 3:
					self.indice_animation = 0

				self.indice_animation += 1
				return image_mage



			elif event == "walk_next":
				if self.indice_animation < 5:
					self.indice_animation = 4

				image_mage = pygame.image.load(self.image_mage_ls[self.indice_animation])
				image_mage = pygame.transform.scale(image_mage,(70,120))

				
				if self.indice_animation == 6:
					self.indice_animation = 4

				self.indice_animation+=1
				return image_mage


			elif event == "atk":
				
				if self.indice_animation < 7:
					self.indice_animation = 7

				image_mage = pygame.image.load(self.image_mage_ls[self.indice_animation])
				image_mage = pygame.transform.scale(image_mage,(70,120))

				
				if self.indice_animation == 11:
					self.indice_animation = 7

				self.indice_animation+=1
				return image_mage

		elif choose_char == "3":
			
			if event == "stand":
				if self.indice_animation > 5:
					self.indice_animation = 0

				image_werewolf = pygame.image.load(self.image_werewolf_ls[self.indice_animation])
				image_werewolf = pygame.transform.scale(image_werewolf,(100,130))
				
				if self.indice_animation == 5:
					self.indice_animation = 0

				self.indice_animation += 1
				return image_werewolf



			elif event == "walk_next":
				if self.indice_animation < 6:
					self.indice_animation = 6

				print("Andei",self.indice_animation)

				image_werewolf = pygame.image.load(self.image_werewolf_ls[self.indice_animation])
				image_werewolf = pygame.transform.scale(image_werewolf,(100,130))

				
				if self.indice_animation == 27:
					self.indice_animation = 0

				self.indice_animation+=1
				return image_werewolf


			elif event == "atk":
				
				if self.indice_animation < 28:
					self.indice_animation = 28

				image_werewolf = pygame.image.load(self.image_werewolf_ls[self.indice_animation])
				image_werewolf = pygame.transform.scale(image_werewolf,(200,130))

				
				if self.indice_animation == 34:
					self.indice_animation = 0

				self.indice_animation+=1
				return image_werewolf

	def create_enemy(self,choose_char,event):
		if choose_char == "1":
			self.RANG = 300
			if event == "stand":
				if self.indice_animation_en > 5 and self.indice_animation_en < 7 or self.indice_animation_en == 11:
					self.indice_animation_en = 0

				image_mage = pygame.image.load(self.image_mage_ls[self.indice_animation_en])
				image_mage = pygame.transform.flip(image_mage, True, False)
				image_mage = pygame.transform.scale(image_mage,(70,100))
				
				if self.indice_animation_en == 3:
					self.indice_animation_en = 0

				self.indice_animation_en += 1
				return image_mage



			elif event == "walk_next":
				if self.indice_animation_en < 5:
					self.indice_animation_en = 4

				image_mage = pygame.image.load(self.image_mage_ls[self.indice_animation_en])
				image_mage = pygame.transform.flip(image_mage, True, False)
				image_mage = pygame.transform.scale(image_mage,(70,120))

				
				if self.indice_animation_en == 6:
					self.indice_animation_en = 4

				self.indice_animation_en+=1
				return image_mage


			elif event == "atk":
				
				print(self.indice_animation_en)
				if self.indice_animation_en < 7:
					self.indice_animation_en = 7
				print(self.indice_animation_en)

				image_mage = pygame.image.load(self.image_mage_ls[self.indice_animation_en])
				image_mage = image_mage.copy()
				image_mage = pygame.transform.flip(image_mage, True, False)
				image_mage = pygame.transform.scale(image_mage,(70,120))

				
				if self.indice_animation_en == 11:
					self.indice_animation_en = 7

				self.indice_animation_en+=1
				return image_mage


		elif choose_char == "2":
			image_vampire = pygame.image.load(self.image_vampire_ls[self.indice_animation])
			image_vampire = pygame.transform.scale(image_vampire,(70,100))
			return image_vampire

		elif choose_char == "3":
			image_werewolf = pygame.image.load(self.image_werewolf_ls[self.indice_animation])
			image_werewolf = pygame.transform.scale(image_werewolf,(70,100))
			return image_werewolf


	def blit_game(self):
		self.window.blit(self.image_chao, (0,430))
		self.window.blit(self.image_fundo,(0,0))
		self.window.blit(self.image_nuvens,(self.x_nuvens,50))
		self.x_nuvens += 5
		if self.x_nuvens == self.window_width:
			self.x_nuvens = 0
		

	def Enemy_controller_front(self):
		if self.block_action == 1:
      
			if self.RANG >= (self.x_enemy - (self.x_player + 70)):
				a = Game_Front.create_enemy(self,"1",event = "atk")
				self.window.blit(a,(self.x_enemy,self.y_enemy))
				Game_Front.command(self,"1")
				self.block_action = 0
				return True

			if self.RANG < (self.x_enemy - (self.x_player + 70)):
				a = Game_Front.create_enemy(self,"1",event = "walk_next")
				self.window.blit(a,(self.x_enemy,self.y_enemy))
				self.x_enemy -= 10
				Game_Front.command(self,"2")
				self.block_action = 0
	
		else:
			pass


	def Can_I_play(self,block):
		if block == 1:
			return False
		elif block == 0:
			return True


	def Life(self,HP,player):
		
		if player == "player":
			if HP == '':
				pass
			elif HP == 100:
				image_life = pygame.image.load(self.image_life_ls[0])
				image_life = pygame.transform.scale(image_life,(75,25))
				self.window.blit(image_life,(self.x_player,(self.y_player-20)))
			elif HP < 100 and HP >= 80:
				image_life = pygame.image.load(self.image_life_ls[1])
				image_life = pygame.transform.scale(image_life,(75,25))
				self.window.blit(image_life,(self.x_player,(self.y_player-20)))
			elif HP < 80 and HP >= 50:
				image_life = pygame.image.load(self.image_life_ls[2])
				image_life = pygame.transform.scale(image_life,(75,25))
				self.window.blit(image_life,(self.x_player,(self.y_player-20)))
			elif HP < 50 and HP >= 30:
				image_life = pygame.image.load(self.image_life_ls[3])
				image_life = pygame.transform.scale(image_life,(75,25))
				self.window.blit(image_life,(self.x_player,(self.y_player-20)))
			elif HP < 30 and HP >= 20 or HP < 20 and HP > 0:
				image_life = pygame.image.load(self.image_life_ls[4])
				image_life = pygame.transform.scale(image_life,(75,25))
				self.window.blit(image_life,(self.x_player,(self.y_player-20)))
			elif HP <= 0:
				image_life = pygame.image.load(self.image_life_ls[5])
				image_life = pygame.transform.scale(image_life,(75,25))
				self.window.blit(image_life,(self.x_player,(self.y_player-20)))
			else:
				pass

		elif player == "enemy":
			if HP == '':
				pass
			elif HP == 100:
				image_life = pygame.image.load(self.image_life_ls[0])
				image_life = pygame.transform.flip(image_life, True, False)
				image_life = pygame.transform.scale(image_life,(75,25))
				self.window.blit(image_life,(self.x_enemy,(self.y_enemy-20)))
    
			elif HP < 100 and HP >= 80:
				image_life = pygame.image.load(self.image_life_ls[1])
				image_life = pygame.transform.flip(image_life, True, False)
				image_life = pygame.transform.scale(image_life,(75,25))
				self.window.blit(image_life,(self.x_enemy,(self.y_enemy-20)))
    
			elif HP < 80 and HP >= 50:
				image_life = pygame.image.load(self.image_life_ls[2])
				image_life = pygame.transform.flip(image_life, True, False)
				image_life = pygame.transform.scale(image_life,(75,25))
				self.window.blit(image_life,(self.x_enemy,(self.y_enemy-20)))
    
			elif HP < 50 and HP >= 30:
				image_life = pygame.image.load(self.image_life_ls[3])
				image_life = pygame.transform.flip(image_life, True, False)
				image_life = pygame.transform.scale(image_life,(75,25))
				self.window.blit(image_life,(self.x_enemy,(self.y_enemy-20)))
    
			elif HP < 30 and HP >= 20 or HP < 20 and HP > 0:
				image_life = pygame.image.load(self.image_life_ls[4])
				image_life = pygame.transform.flip(image_life, True, False)
				image_life = pygame.transform.scale(image_life,(75,25))
				self.window.blit(image_life,(self.x_enemy,(self.y_enemy-20)))
    
			elif HP <= 0:
				image_life = pygame.image.load(self.image_life_ls[5])
				image_life = pygame.transform.flip(image_life, True, False)
				image_life = pygame.transform.scale(image_life,(75,25))
				self.window.blit(image_life,(self.x_enemy,(self.y_enemy-20)))
    
			else:
				pass


	def GUI(self,command,HP='',HP_en = ''):
		self.command_GUI = command
		HP = HP
	
		
		Game_Front.Life(self,HP,player="player")
		Game_Front.Life(self,HP_en,player="enemy")
  
		'''txt =f'HP:{HP}'                                 
		pygame.font.init()                                
		fontesys = pygame.font.SysFont('arial', 15,pygame.font.Font.bold)           
		txttela = fontesys.render(txt, 1, (255,0,0))  
		self.window.blit(txttela,(self.x_player,(self.y_player-20)))
        '''
		if self.command_GUI == "WIN":
			txt ='WIN!!'                                 
			pygame.font.init()                                
			fonte = pygame.font.get_default_font()

			fontesys = pygame.font.SysFont(fonte, 60)           
			txttela = fontesys.render(txt, 1, (255,0,0))  
			self.window.blit(txttela,(250,30))                

		elif self.command_GUI == "LOSE":
			txt ='DEFEAT'                                 
			pygame.font.init()                                
			fonte = pygame.font.get_default_font()

			fontesys = pygame.font.SysFont(fonte, 60)           
			txttela = fontesys.render(txt, 1, (0,255,0))  
			self.window.blit(txttela,(300,30))                


	def command(self,command):
		return command

	


'''
def loop_game(self):
		while True:
			self.clock.tick(5)
			self.window.fill((0,0,0))


			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					exit()

				elif event.type == KEYDOWN:
					if event.key == K_d and Game_Front.Can_I_play(self,self.block_action):
						self.x_player += 10
						a = Game_Front.create_player(self,"1",event = "walk_next")
						self.window.blit(a,(self.x_player,self.y_player))
						Game_Front.command(self,"2")
						self.block_action = 1
						Game_Front.Enemy_controller_front(self)
						
					elif event.key == K_j and Game_Front.Can_I_play(self,self.block_action):
						a = Game_Front.create_player(self,"1",event = "atk")
						self.window.blit(a,(self.x_player,self.y_player))
						Game_Front.command(self,"1")
						self.block_action = 1
						Game_Front.Enemy_controller_front(self)

					elif event.key == K_z and Game_Front.Can_I_play(self,self.block_action):
						self.window.blit(Game_Front.create_player(self,"1",event = "stand"),(self.x_player,self.y_player))
						self.block_action = 1
						Game_Front.Enemy_controller_front(self)
												

			Game_Front.blit_game(self)
			self.window.blit(Game_Front.create_player(self,"1",event = "stand"),(self.x_player,self.y_player))
			self.window.blit(Game_Front.create_enemy(self,"1",event = "stand"),(self.x_enemy,self.y_enemy))
			Game_Front.GUI(self,self.command_GUI)
			pygame.display.flip()
			pygame.display.update()

'''