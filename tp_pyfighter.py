# PyFight!
import random
import math
import sys
import os
import time
from tp_characters_test import *

class Game(object):

    mode_options = {'1':('jan 1','jan ilo'), '2':('jan ilo 1','jan ilo 2'), '3':('jan 1','jan 2')}
    game_mode = '' # Preallocation
    game_mode_choice = '' # Preallocation and Stroage

    character_options = {'1':Berserker, '2':Philosopher, '3':Trickster2}
    move_order = '' # Preallocation

    def __init__(self):
        """ """

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def introduction(self):
        game.clear_screen()
        print """
				_________ _______  _                      _________ _______  _        _______ 
				\__    _/(  ___  )( (    /|      |\     /|\__   __/(  ___  )( \      (  ___  )
				   )  (  | (   ) ||  \  ( |      | )   ( |   ) (   | (   ) || (      | (   ) |
				   |  |  | (___) ||   \ | |      | |   | |   | |   | (___) || |      | (___) |
				   |  |  |  ___  || (\ \) |      | |   | |   | |   |  ___  || |      |  ___  |
				   |  |  | (   ) || | \   |      | |   | |   | |   | (   ) || |      | (   ) |
				|\_)  )  | )   ( || )  \  |      | (___) |   | |   | )   ( || (____/\| )   ( |
				(____/   |/     \||/    )_)      (_______)   )_(   |/     \|(_______/|/     \|
                                                                              					"""
        time.sleep(1)
        game.clear_screen()
    
    def choose_game_mode(self):
        while True:
            self.game_mode_choice = raw_input("sina pali musi e seme: \
                \n1) sina u. jan ilo \
                \n2) jan ilo 1 u. jan ilo 2 \
                \n3) jan 1 u. jan 2 \
                \n0) tawa.\n\n")

            game.clear_screen()

            if self.game_mode_choice == '0':
                sys.exit()
            try:
                self.game_mode = self.mode_options[ self.game_mode_choice ]
                return None
            except KeyError:
                print "ala. wile sina e ike. sina ante e wile sina.\n"
                time.sleep(1)

    def character_selection(self,controller_index):
        while True:
            character_choice = raw_input(self.game_mode[controller_index] + " li wile kepeken:\
                \n1) jan pi pakala nasa\
                \n2) jan pi sona mute\
                \n3) jan pi powe nasa\
                \n4) nasin pi sona ala\
                \n\
                \n0) tawa.\n\n")

            game.clear_screen()

            if character_choice == '0':
                sys.exit()
            elif character_choice == '4':
                character_choice = str (random.randint(1,3))

            try:
                return self.character_options[ character_choice ]
            except KeyError:
                print "ala. wile sina e ike. sina ante e wile sina.\n"
                time.sleep(1)

    def hp_check(self,controller_1, controller_2):
        if controller_1.base_hp <= 0:
            if controller_2.base_hp >0:
                self.clear_screen
                print "jan 2 li kama sewi!"
                sys.exit()
            else:
                self.clear_screen
                print "jan tu li lon sama!!!"
                sys.exit()
        elif controller_2.base_hp <= 0:
            self.clear_screen
            print "jan 1 li kama sewi!"
            sys.exit()
        else:
            pass

    def player_choose_move(self,controller,controller_index):
        while True:
            move_choice = raw_input("o, " + self.game_mode[controller_index] + ", sina wile e seme:\
            \n1)" + controller.move_pool['1'].__doc__ + "\
            \n2)" + controller.move_pool['2'].__doc__ + "\
            \n3)" + controller.move_pool['3'].__doc__ + "\n\n")

            try:
                controller.move = controller.move_pool[move_choice]
                return None
            except KeyError:
                game.clear_screen()
                print "ala. wile sina e ike. sina ante e wile sina.\n"
                time.sleep(1)

    def comp_choose_move(self,controller):
        controller.move = controller.move_pool[ random.choice( ['1','2','3'] )]

    def priority_and_speed_check(self,controller1,controller2):
        if controller1.priority > controller2.priority:
            return True
        elif controller1.priority == controller2.priority:
            if controller1.base_speed > controller2.base_speed:
                return True
            elif controller1.base_speed == controller2.base_speed:
                return bool ( random.choice([0,1]) )
            else:
                return False
        else:
            return False

    def update(self,controller1,controller2):
        print "sijelo pi", self.game_mode[0], ":", str(Player_1.base_hp), "\n", self.game_mode[0], "sona lawa: x " + str(Player_1.mindset_multiplier), "\n"
        print "sijelo pi", self.game_mode[1], ":", str(Player_2.base_hp), "\n", self.game_mode[1], "sona lawa: x " + str(Player_2.mindset_multiplier), "\n"
        print "\n\n"

    def move_collection(self,controller1,controller2):
        if self.game_mode_choice == '1':
            self.update(Player_1,Player_2)
            self.player_choose_move(Player_1,0)
            self.clear_screen()

            self.update(Player_1,Player_2)
            self.comp_choose_move(Player_2)
            self.clear_screen()

        elif self.game_mode_choice == '2':
            self.update(Player_1,Player_2)
            self.comp_choose_move(Player_1)
            self.clear_screen()

            self.update(Player_1,Player_2)
            self.comp_choose_move(Player_2)
            self.clear_screen()

        else:
            self.update(Player_1,Player_2)
            self.player_choose_move(Player_1,0)
            self.clear_screen()

            self.update(Player_1,Player_2)
            self.player_choose_move(Player_2,1)
            self.clear_screen()

    def move_application(self,controller1,controller2):
        if self.priority_and_speed_check(Player_1,Player_2):
            Player_1.move(Player_1,Player_2)
            self.hp_check(Player_1,Player_2)

            Player_2.move(Player_2,Player_1)
            self.hp_check(Player_1,Player_2)
        else:
            Player_2.move(Player_2,Player_1)
            self.hp_check(Player_1,Player_2)

            Player_1.move(Player_1,Player_2)
            self.hp_check(Player_1,Player_2)

game = Game()
game.introduction()
game.choose_game_mode()

( Player_1, Player_2 ) = ( game.character_selection(0)(), game.character_selection(1)() )
while True:
    game.move_collection(Player_1,Player_2)
    game.move_application(Player_1,Player_2)
