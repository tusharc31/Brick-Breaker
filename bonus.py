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
import powerups
import random
from colorama import Fore, Back, Style


def chain_reaction(x, y):

    abc = random.randint(0, 19)

    if abc == 18 or abc == 19:
        bruh = powerups.powerup_fireball(x,y+8)
        powerups.super_power.append(bruh)
    
    if abc == 16 or abc == 17:
        bruh = powerups.powerup_laser(x,y+8)
        powerups.super_power.append(bruh)

    if abc == 14 or abc == 15:
        bruh = powerups.powerup_fastball(x,y+8)
        powerups.super_power.append(bruh)

    if abc == 13 or abc == 12:
        bruh = powerups.powerup_grabball(x,y+8)
        powerups.super_power.append(bruh)

    if abc == 11 or abc == 10:
        bruh = powerups.powerup_shrink(x,y+8)
        powerups.super_power.append(bruh)

    if abc == 9 or abc == 8:
        bruh = powerups.powerup_expand(x,y+8)
        powerups.super_power.append(bruh)

    for k in range(len(bricks.lvl1_bricks)):
        if bricks.lvl1_bricks[k].x_pos == x and bricks.lvl1_bricks[k].y_pos == y:
            bricks.lvl1_bricks[k].vis = 1
            player.stats.score = player.stats.score + 1

    for k in range(len(bricks.lvl2_bricks)):
        if bricks.lvl2_bricks[k].x_pos == x and bricks.lvl2_bricks[k].y_pos == y:
            bricks.lvl2_bricks[k].vis = 1
            player.stats.score = player.stats.score + 2

    for k in range(len(bricks.lvl3_bricks)):
        if bricks.lvl3_bricks[k].x_pos == x and bricks.lvl3_bricks[k].y_pos == y:
            bricks.lvl3_bricks[k].vis = 1
            player.stats.score = player.stats.score + 3

    for k in range(len(bricks.rain_bricks)):
        if bricks.rain_bricks[k].x_pos == x and bricks.rain_bricks[k].y_pos == y:
            bricks.rain_bricks[k].vis = 1
            player.stats.score = player.stats.score + int(time.time()-player.stats.time)%3 + 1

    for k in range(len(bricks.nond_bricks)):
        if bricks.nond_bricks[k].x_pos == x and bricks.nond_bricks[k].y_pos == y:
            bricks.nond_bricks[k].vis = 1
            player.stats.score = player.stats.score + 10

    for k in range(len(bricks.expl_bricks)):
        if bricks.expl_bricks[k].x_pos == x and bricks.expl_bricks[k].y_pos == y:
            bricks.expl_bricks[k].vis = 1
            player.stats.score = player.stats.score + 10

    for k in range(len(bricks.lvl1_bricks)):
        if bricks.lvl1_bricks[k].vis == 0:
            if (bricks.lvl1_bricks[k].x_pos == x+6 or bricks.lvl1_bricks[k].x_pos == x or bricks.lvl1_bricks[k].x_pos == x-6):
                if (bricks.lvl1_bricks[k].y_pos == y+1 or bricks.lvl1_bricks[k].y_pos == y or bricks.lvl1_bricks[k].y_pos == y-1):
                    bricks.lvl1_bricks[k].vis = 1
                    # chain_reaction(
                    #     bricks.lvl1_bricks[k].x_pos, bricks.lvl1_bricks[k].y_pos)

    for k in range(len(bricks.lvl2_bricks)):
        if bricks.lvl2_bricks[k].vis == 0:
            if (bricks.lvl2_bricks[k].x_pos == x+6 or bricks.lvl2_bricks[k].x_pos == x or bricks.lvl2_bricks[k].x_pos == x-6):
                if (bricks.lvl2_bricks[k].y_pos == y+1 or bricks.lvl2_bricks[k].y_pos == y or bricks.lvl2_bricks[k].y_pos == y-1):
                    bricks.lvl2_bricks[k].vis = 1
                    # chain_reaction(
                    #     bricks.lvl2_bricks[k].x_pos, bricks.lvl2_bricks[k].y_pos)

    for k in range(len(bricks.lvl3_bricks)):
        if bricks.lvl3_bricks[k].vis == 0:
            if (bricks.lvl3_bricks[k].x_pos == x+6 or bricks.lvl3_bricks[k].x_pos == x or bricks.lvl3_bricks[k].x_pos == x-6):
                if (bricks.lvl3_bricks[k].y_pos == y+1 or bricks.lvl3_bricks[k].y_pos == y or bricks.lvl3_bricks[k].y_pos == y-1):
                    bricks.lvl3_bricks[k].vis = 1
                    # chain_reaction(
                    #     bricks.lvl3_bricks[k].x_pos, bricks.lvl3_bricks[k].y_pos)

    for k in range(len(bricks.rain_bricks)):
        if bricks.rain_bricks[k].vis == 0:
            if (bricks.rain_bricks[k].x_pos == x+6 or bricks.rain_bricks[k].x_pos == x or bricks.rain_bricks[k].x_pos == x-6):
                if (bricks.rain_bricks[k].y_pos == y+1 or bricks.rain_bricks[k].y_pos == y or bricks.rain_bricks[k].y_pos == y-1):
                    bricks.rain_bricks[k].vis = 1
                    # chain_reaction(
                    #     bricks.rain_bricks[k].x_pos, bricks.rain_bricks[k].y_pos)

    for k in range(len(bricks.nond_bricks)):
        if bricks.nond_bricks[k].vis == 0:
            if (bricks.nond_bricks[k].x_pos == x+6 or bricks.nond_bricks[k].x_pos == x or bricks.nond_bricks[k].x_pos == x-6):
                if (bricks.nond_bricks[k].y_pos == y+1 or bricks.nond_bricks[k].y_pos == y or bricks.nond_bricks[k].y_pos == y-1):
                    bricks.nond_bricks[k].vis = 1
                    # chain_reaction(
                    #     bricks.nond_bricks[k].x_pos, bricks.nond_bricks[k].y_pos)

    for k in range(len(bricks.expl_bricks)):
        if bricks.expl_bricks[k].vis == 0:
            if (bricks.expl_bricks[k].x_pos == x+6 or bricks.expl_bricks[k].x_pos == x or bricks.expl_bricks[k].x_pos == x-6):
                if (bricks.expl_bricks[k].y_pos == y+1 or bricks.expl_bricks[k].y_pos == y or bricks.expl_bricks[k].y_pos == y-1):
                    chain_reaction(
                        bricks.expl_bricks[k].x_pos, bricks.expl_bricks[k].y_pos)
