from getchunix import *
from alarmexception import *
import display_file
import signal
import copy
import sys
import time
import bricks
import colorama
import slider
import ball
import time
import subprocess
import player
import time
import collision
import random
import powerups
import bullet
import boss
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
screen = display_file.display()

getch = GetchUnix()

def alarmHandler(signum, frame):
    raise AlarmException


def input_to(timeout=display_file.refresh_rate):
    signal.signal(signal.SIGALRM, alarmHandler)
    # signal.alarm(timeout)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        text = getch()
        signal.alarm(0)
        signal.setitimer(signal.ITIMER_REAL, 0)
        return text
    except AlarmException:
        signal.setitimer(signal.ITIMER_REAL, 0)
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ""

def reset ():
    player.stats.status = 'P'
    slider.game_slider = slider.slider(random.randint(0,50),34)
    ball.game_ball = ball.ball(random.randint(slider.game_slider.x_pos, slider.game_slider.x_pos+slider.game_slider.length-2),33)
    slider.game_slider.state=0
    powerups.super_power = []
    bullet.game_bullet = []

def display_and_input():
    # c = input_to()

    # for k in range(len(c)):

    #     if c[k] == 'Q' or c[k] == 'q':
    #         exit()

    #     if c[k] == 'A' or c[k] == 'a':
    #         if player.stats.status == 'A':
    #             if slider.game_slider.x_pos >= 10:
    #                 slider.game_slider.x_pos = slider.game_slider.x_pos - 10
                    
    #                 if player.stats.level==3:
    #                     if bricks.nond_bricks[5].x_pos>=6:# and slider.game_slider.x_pos>0:
    #                         for k1 in range(len(bricks.nond_bricks)):
    #                             if bricks.nond_bricks[k1].y_pos!=12:
    #                                 bricks.nond_bricks[k1].x_pos = bricks.nond_bricks[k1].x_pos - 6
                
    #             else:

    #                 if player.stats.level==3:
    #                     if bricks.nond_bricks[5].x_pos>=6:# and slider.game_slider.x_pos>0:
    #                         for k1 in range(len(bricks.nond_bricks)):
    #                             if bricks.nond_bricks[k1].y_pos!=12:
    #                                 bricks.nond_bricks[k1].x_pos = bricks.nond_bricks[k1].x_pos - 6

    #                 slider.game_slider.x_pos = 0

    #         else:
    #             if slider.game_slider.x_pos >= 10:
    #                 slider.game_slider.x_pos = slider.game_slider.x_pos - 10
    #                 ball.game_ball.x_pos = ball.game_ball.x_pos - 10
                    
    #                 if player.stats.level==3:
    #                     if bricks.nond_bricks[5].x_pos>=6:# and slider.game_slider.x_pos>0:
    #                         for k1 in range(len(bricks.nond_bricks)):
    #                             if bricks.nond_bricks[k1].y_pos!=12:
    #                                 bricks.nond_bricks[k1].x_pos = bricks.nond_bricks[k1].x_pos - 6

    #     if c[k] == 'D' or c[k] == 'd':
    #         if player.stats.status == 'A':
    #             if slider.game_slider.x_pos + slider.game_slider.length + 10 < 120:
    #                 slider.game_slider.x_pos = slider.game_slider.x_pos + 10
                    
    #                 if player.stats.level==3:
    #                     if bricks.nond_bricks[10].x_pos+6<=114:# and slider.game_slider.x_pos + slider.game_slider.length < 120:
    #                         for k1 in range(len(bricks.nond_bricks)):
    #                             if bricks.nond_bricks[k1].y_pos!=12:
    #                                 bricks.nond_bricks[k1].x_pos = bricks.nond_bricks[k1].x_pos + 6
                
    #             else:

    #                 if player.stats.level==3:
    #                     if bricks.nond_bricks[10].x_pos+6<=114:# and slider.game_slider.x_pos + slider.game_slider.length < 120:
    #                         for k1 in range(len(bricks.nond_bricks)):
    #                             if bricks.nond_bricks[k1].y_pos!=12:
    #                                 bricks.nond_bricks[k1].x_pos = bricks.nond_bricks[k1].x_pos + 6

    #                 slider.game_slider.x_pos = 120-slider.game_slider.length

            
    #         else:
    #             if slider.game_slider.x_pos + slider.game_slider.length + 10 < 120:
                    
    #                 if player.stats.level==3:
    #                     if bricks.nond_bricks[10].x_pos+6<=114:# and slider.game_slider.x_pos + slider.game_slider.length < 120:
    #                         for k1 in range(len(bricks.nond_bricks)):
    #                             if bricks.nond_bricks[k1].y_pos!=12:
    #                                 bricks.nond_bricks[k1].x_pos = bricks.nond_bricks[k1].x_pos + 6
                    
    #                 slider.game_slider.x_pos = slider.game_slider.x_pos + 10
    #                 ball.game_ball.x_pos = ball.game_ball.x_pos + 10

    #     if c[k] == ' ' and player.stats.status == 'P':
    #         player.stats.status = 'A'

    #     if c[k] == 'L' or c[k] == 'l':
    #         bricks.lvl1_bricks = []
    #         bricks.lvl2_bricks = []
    #         bricks.lvl3_bricks = []
    #         bricks.nond_bricks = []
    #         bricks.expl_bricks = []
    #         bricks.rain_bricks = []
    #         bullet.game_bullet = []
    #         bricks.clear_all_bricks()
    #         slider.game_slider.state=0
    #         bullet.game_bullet = []

    #         if player.stats.level==1:
    #             player.stats.status = 'P'
    #             player.stats.level=2
    #             bricks.display_level2_brick()
    #             powerups.super_power = []
    #             slider.game_slider.length = 40
    #             slider.game_slider.x_pos = 20
    #             slider.game_slider.y_pos = 34
    #             ball.game_ball.x_vel = -2
    #             ball.game_ball.y_vel = -1
    #             ball.game_ball.x_pos = 25
    #             ball.game_ball.y_pos = 33
                

    #         elif player.stats.level==2:
    #             player.stats.status = 'P'
    #             player.stats.level=3
    #             bricks.display_level3_brick()
    #             powerups.super_power = []
    #             slider.game_slider.length = 40
    #             slider.game_slider.x_pos = 40
    #             slider.game_slider.y_pos = 34
    #             ball.game_ball.x_vel = 2
    #             ball.game_ball.y_vel = -1
    #             ball.game_ball.x_pos = 70
    #             ball.game_ball.y_pos = 33

    #         elif player.stats.level==3:
    #             player.stats.status == 'P'
    #             powerups.super_power = []
    #             print("CONGRATS, YOU WON!\n")
    #             exit()


    i = 0
    j = 0
    str = ''

    while i < (screen.display_height):
        j = 0

        while j < (screen.display_length):

            obj = 0

            if slider.game_slider.x_pos == j and slider.game_slider.y_pos == i:
                for k in range(slider.game_slider.length):
                    if (j<120):
                        if slider.game_slider.state==0:
                            str = str + Back.LIGHTGREEN_EX + " "
                        else:
                            str = str + Back.LIGHTRED_EX + " "
                        j = j+1
                    obj = 1
                j = j-1

            if ball.game_ball.x_pos == j and ball.game_ball.y_pos == i:
                str = str + Fore.GREEN + "🔴"
                j = j+1
                obj = 1

            for k in range(len(powerups.super_power)):
                if powerups.super_power[k].x_pos == j and powerups.super_power[k].y_pos == i:
                    str = str + Fore.LIGHTGREEN_EX + powerups.super_power[k].image
                    obj = 1

            for k in range(len(bricks.lvl1_bricks)):
                if bricks.lvl1_bricks[k].x_pos == j and bricks.lvl1_bricks[k].y_pos == i and bricks.lvl1_bricks[k].vis == 0:
                    str = str + Back.LIGHTWHITE_EX + Fore.BLACK + "______"
                    obj = 1
                    j = j+5

            for k in range(len(bricks.lvl2_bricks)):
                if bricks.lvl2_bricks[k].x_pos == j and bricks.lvl2_bricks[k].y_pos == i and bricks.lvl2_bricks[k].vis == 0:
                    str = str + Back.LIGHTBLUE_EX + Fore.BLACK + "______"
                    obj = 1
                    j = j+5

            for k in range(len(bricks.lvl3_bricks)):
                if bricks.lvl3_bricks[k].x_pos == j and bricks.lvl3_bricks[k].y_pos == i and bricks.lvl3_bricks[k].vis == 0:
                    str = str + Back.LIGHTYELLOW_EX + Fore.BLACK + "______"
                    obj = 1
                    j = j+5

            if player.stats.level<3:
                for k in range(len(bricks.nond_bricks)):
                    if bricks.nond_bricks[k].x_pos == j and bricks.nond_bricks[k].y_pos == i and bricks.nond_bricks[k].vis == 0:
                        str = str + Back.LIGHTRED_EX + Fore.BLACK + "______"
                        obj = 1
                        j = j+5

            else:
                for k in range(len(bricks.nond_bricks)):
                    if bricks.nond_bricks[k].x_pos == j and bricks.nond_bricks[k].y_pos == i and bricks.nond_bricks[k].y_pos ==12 and bricks.nond_bricks[k].vis == 0:
                        str = str + Back.LIGHTRED_EX + Fore.BLACK + "______"
                        obj = 1
                        j = j+5

                    elif bricks.nond_bricks[k].x_pos == j and bricks.nond_bricks[k].y_pos == i and bricks.nond_bricks[k].vis == 0:
                        str = str + Back.LIGHTWHITE_EX + Fore.BLACK + "  " + Back.RED + Fore.BLACK + "  " + Back.LIGHTWHITE_EX + Fore.BLACK + "  "
                        obj = 1
                        j = j+5

            for k in range(len(bricks.expl_bricks)):
                if bricks.expl_bricks[k].x_pos == j and bricks.expl_bricks[k].y_pos == i and bricks.expl_bricks[k].vis == 0:
                    str = str + Back.LIGHTMAGENTA_EX + Fore.BLACK + "______"
                    obj = 1
                    j = j+5

            for k in range(len(bricks.rain_bricks)):
                if bricks.rain_bricks[k].x_pos == j and bricks.rain_bricks[k].y_pos == i and bricks.rain_bricks[k].vis == 0:
                    if int(time.time()-player.stats.time)%3 == 0:
                        str = str + Back.LIGHTWHITE_EX + Fore.BLACK + "______"
                        obj = 1
                        j = j+5
                    elif int(time.time()-player.stats.time)%3 == 1:
                        str = str + Back.LIGHTBLUE_EX + Fore.BLACK + "______"
                        obj = 1
                        j = j+5
                    elif int(time.time()-player.stats.time)%3 == 2:
                        str = str + Back.LIGHTYELLOW_EX + Fore.BLACK + "______"
                        obj = 1
                        j = j+5

            for k in range(len(bullet.game_bullet)):
                if bullet.game_bullet[k].x_pos == j and bullet.game_bullet[k].y_pos == i:
                    str = str + Back.LIGHTRED_EX + Fore.RED + " " #▲
                    obj = 1
                    j = j
            
            if obj == 0:
                str = str + Back.BLACK + " "

            j = j+1

        str = str + '\n'
        i = i+1


    subprocess.call("clear")
    print()
    print(" SCORE = ", player.stats.score, "     LIVES REMAINING = ", player.stats.lives,
          "     TIME PLAYED = ", int(time.time()-player.stats.time), "seconds", "     LEVEL = ", player.stats.level,
          "     LASERS TIME = ", max(slider.game_slider.remain,0))
    print()
    if player.stats.level<3:
        print(" Boss lives = You're too noob to face the boss yet!")
    if player.stats.level==3:
        health_bar = ''
        for abc in range(boss.game_boss.lives-1):
            health_bar = health_bar + Back.LIGHTRED_EX + " "
        print(" Boss health = ", health_bar)
    print()
    print(str)
    print()
    print(" PRESS SPACE TO RELEASE THE BALL")
    print(" MOVE YOUR PADDLE - PRESS A TO MOVE LEFT AND D TO MOVE RIGHT")
    print(" TO QUIT, PRESS Q")
    print(" TO JUMP TO NEXT LEVE, PRESS L")
    print()
    str = Back.WHITE + "            "
    print(str, "LEVEL-1 BRICKS")
    str = Back.BLUE + "            "
    print(str, "LEVEL-2 BRICKS")
    str = Back.YELLOW + "            "
    print(str, "LEVEL-3 BRICKS")
    str = Back.RED + "            "
    print(str, "NON-DESTRUCTIBLE BRICKS")
    str = Back.MAGENTA + "            "
    print(str, "EXPLOSIVE BRICKS")
    print()
    # print(display_file.refresh_rate)
    if player.stats.lives == 0:
        print("SORRY, YOU LOST!\n")
        exit()

    c = input_to()

    for k in range(len(c)):

        if c[k] == 'Q' or c[k] == 'q':
            exit()

        if c[k] == 'A' or c[k] == 'a':
            if player.stats.status == 'A':
                if slider.game_slider.x_pos >= 10:
                    slider.game_slider.x_pos = slider.game_slider.x_pos - 10
                    
                    if player.stats.level==3:
                        if bricks.nond_bricks[5].x_pos>=6:# and slider.game_slider.x_pos>0:
                            for k1 in range(len(bricks.nond_bricks)):
                                if bricks.nond_bricks[k1].y_pos!=12:
                                    bricks.nond_bricks[k1].x_pos = bricks.nond_bricks[k1].x_pos - 6
                
                else:

                    if player.stats.level==3:
                        if bricks.nond_bricks[5].x_pos>=6:# and slider.game_slider.x_pos>0:
                            for k1 in range(len(bricks.nond_bricks)):
                                if bricks.nond_bricks[k1].y_pos!=12:
                                    bricks.nond_bricks[k1].x_pos = bricks.nond_bricks[k1].x_pos - 6

                    slider.game_slider.x_pos = 0

            else:
                if slider.game_slider.x_pos >= 10:
                    slider.game_slider.x_pos = slider.game_slider.x_pos - 10
                    ball.game_ball.x_pos = ball.game_ball.x_pos - 10
                    
                    if player.stats.level==3:
                        if bricks.nond_bricks[5].x_pos>=6:# and slider.game_slider.x_pos>0:
                            for k1 in range(len(bricks.nond_bricks)):
                                if bricks.nond_bricks[k1].y_pos!=12:
                                    bricks.nond_bricks[k1].x_pos = bricks.nond_bricks[k1].x_pos - 6

        if c[k] == 'D' or c[k] == 'd':
            if player.stats.status == 'A':
                if slider.game_slider.x_pos + slider.game_slider.length + 10 < 120:
                    slider.game_slider.x_pos = slider.game_slider.x_pos + 10
                    
                    if player.stats.level==3:
                        if bricks.nond_bricks[10].x_pos+6<=114:# and slider.game_slider.x_pos + slider.game_slider.length < 120:
                            for k1 in range(len(bricks.nond_bricks)):
                                if bricks.nond_bricks[k1].y_pos!=12:
                                    bricks.nond_bricks[k1].x_pos = bricks.nond_bricks[k1].x_pos + 6
                
                else:

                    if player.stats.level==3:
                        if bricks.nond_bricks[10].x_pos+6<=114:# and slider.game_slider.x_pos + slider.game_slider.length < 120:
                            for k1 in range(len(bricks.nond_bricks)):
                                if bricks.nond_bricks[k1].y_pos!=12:
                                    bricks.nond_bricks[k1].x_pos = bricks.nond_bricks[k1].x_pos + 6

                    slider.game_slider.x_pos = 120-slider.game_slider.length

            
            else:
                if slider.game_slider.x_pos + slider.game_slider.length + 10 < 120:
                    
                    if player.stats.level==3:
                        if bricks.nond_bricks[10].x_pos+6<=114:# and slider.game_slider.x_pos + slider.game_slider.length < 120:
                            for k1 in range(len(bricks.nond_bricks)):
                                if bricks.nond_bricks[k1].y_pos!=12:
                                    bricks.nond_bricks[k1].x_pos = bricks.nond_bricks[k1].x_pos + 6
                    
                    slider.game_slider.x_pos = slider.game_slider.x_pos + 10
                    ball.game_ball.x_pos = ball.game_ball.x_pos + 10

        if c[k] == ' ' and player.stats.status == 'P':
            player.stats.status = 'A'

        if c[k] == 'L' or c[k] == 'l':
            bricks.lvl1_bricks = []
            bricks.lvl2_bricks = []
            bricks.lvl3_bricks = []
            bricks.nond_bricks = []
            bricks.expl_bricks = []
            bricks.rain_bricks = []
            bullet.game_bullet = []
            bricks.clear_all_bricks()
            slider.game_slider.state=0
            bullet.game_bullet = []

            if player.stats.level==1:
                player.stats.status = 'P'
                player.stats.level=2
                bricks.display_level2_brick()
                powerups.super_power = []
                slider.game_slider.length = 40
                slider.game_slider.x_pos = 20
                slider.game_slider.y_pos = 34
                ball.game_ball.x_vel = -2
                ball.game_ball.y_vel = -1
                ball.game_ball.x_pos = 25
                ball.game_ball.y_pos = 33
                

            elif player.stats.level==2:
                player.stats.status = 'P'
                player.stats.level=3
                bricks.display_level3_brick()
                powerups.super_power = []
                slider.game_slider.length = 40
                slider.game_slider.x_pos = 40
                slider.game_slider.y_pos = 34
                ball.game_ball.x_vel = 2
                ball.game_ball.y_vel = -1
                ball.game_ball.x_pos = 70
                ball.game_ball.y_pos = 33

            elif player.stats.level==3:
                player.stats.status == 'P'
                powerups.super_power = []
                print("CONGRATS, YOU WON!\n")
                exit()


    # i = 0
    # j = 0
    # str = ''
    return c