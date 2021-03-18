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
    ball.game_ball = ball.ball(random.randint(slider.game_slider.x_pos, slider.game_slider.x_pos+slider.game_slider.length),33)


def display_and_input():
    c = input_to()

    for k in range(len(c)):

        if c[k] == 'Q' or c[k] == 'q':
            exit()

        if c[k] == 'A' or c[k] == 'a':
            if player.stats.status == 'A':
                if slider.game_slider.x_pos >= 10:
                    slider.game_slider.x_pos = slider.game_slider.x_pos - 10
                else:
                    slider.game_slider.x_pos = 0

            else:
                if slider.game_slider.x_pos >= 10:
                    slider.game_slider.x_pos = slider.game_slider.x_pos - 10
                    ball.game_ball.x_pos = ball.game_ball.x_pos - 10

        if c[k] == 'D' or c[k] == 'd':
            if player.stats.status == 'A':
                if slider.game_slider.x_pos + slider.game_slider.length + 10 < 120:
                    slider.game_slider.x_pos = slider.game_slider.x_pos + 10
                else:
                    slider.game_slider.x_pos = 120-slider.game_slider.length
            else:
                if slider.game_slider.x_pos + slider.game_slider.length + 10 < 120:
                    slider.game_slider.x_pos = slider.game_slider.x_pos + 10
                    ball.game_ball.x_pos = ball.game_ball.x_pos + 10

        if c[k] == ' ' and player.stats.status == 'P':
            player.stats.status = 'A'

        if c[k] == 'L' or c[k] == 'l':
            bricks.clear_all_bricks()

            if player.stats.level==1:
                player.stats.level==player.stats.level+1
                bricks.level2_brick()
                powerups.delete_super_power
                slider.slider.length = 40
                slider.slider.x_pos = 25
                slider.slider.y_pos = 34
                ball.ball.x_vel = 2
                ball.ball.y_vel = -1
                ball.ball.x_pos = 30
                ball.ball.y_pos = 33
                

            if player.stats.level==2:
                player.stats.level==player.stats.level+1
                bricks.display_level3_bricks()
                powerups.delete_super_power
                slider.slider.length = 40
                slider.slider.x_pos = 25
                slider.slider.y_pos = 34
                ball.ball.x_vel = 2
                ball.ball.y_vel = -1
                ball.ball.x_pos = 30
                ball.ball.y_pos = 33

            if player.stats.level==3:
                powerups.delete_super_power
                print("CONGRATS, YOU WON!\n")
                exit()


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
                        str = str + Back.GREEN + " "
                        j = j+1
                    obj = 1
                j = j-1

            if ball.game_ball.x_pos == j and ball.game_ball.y_pos == i:
                str = str + Fore.GREEN + "🔴"
                j = j+1
                obj = 1

            for k in range(len(powerups.super_power)):
                if powerups.super_power[k].x_pos == j and powerups.super_power[k].y_pos == i:
                    str = str + Fore.GREEN + powerups.super_power[k].image
                    obj = 1

            for k in range(len(bricks.lvl1_bricks)):
                if bricks.lvl1_bricks[k].x_pos == j and bricks.lvl1_bricks[k].y_pos == i and bricks.lvl1_bricks[k].vis == 0:
                    str = str + Back.WHITE + Fore.BLACK + "______"
                    obj = 1
                    j = j+5

            for k in range(len(bricks.lvl2_bricks)):
                if bricks.lvl2_bricks[k].x_pos == j and bricks.lvl2_bricks[k].y_pos == i and bricks.lvl2_bricks[k].vis == 0:
                    str = str + Back.BLUE + Fore.BLACK + "______"
                    obj = 1
                    j = j+5

            for k in range(len(bricks.lvl3_bricks)):
                if bricks.lvl3_bricks[k].x_pos == j and bricks.lvl3_bricks[k].y_pos == i and bricks.lvl3_bricks[k].vis == 0:
                    str = str + Back.YELLOW + Fore.BLACK + "______"
                    obj = 1
                    j = j+5

            for k in range(len(bricks.nond_bricks)):
                if bricks.nond_bricks[k].x_pos == j and bricks.nond_bricks[k].y_pos == i and bricks.nond_bricks[k].vis == 0:
                    str = str + Back.RED + Fore.BLACK + "______"
                    obj = 1
                    j = j+5

            for k in range(len(bricks.expl_bricks)):
                if bricks.expl_bricks[k].x_pos == j and bricks.expl_bricks[k].y_pos == i and bricks.expl_bricks[k].vis == 0:
                    str = str + Back.MAGENTA + Fore.BLACK + "______"
                    obj = 1
                    j = j+5

            if obj == 0:
                str = str + Back.BLACK + " "

            j = j+1

        str = str + '\n'
        i = i+1

    subprocess.call("clear")
    print()
    print(" SCORE = ", player.stats.score, "         LIVES REMAINING = ", player.stats.lives,
          "         TIME PLAYED = ", int(time.time()-player.stats.time), "seconds", "         LEVEL = ", player.stats.level)
    print()
    print(str)
    print()
    print(" PRESS SPACE TO RELEASE THE BALL")
    print(" MOVE YOUR PADDLE - PRESS A TO MOVE LEFT AND D TO MOVE RIGHT")
    print(" TO QUIT, PRESS Q")
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
    return c