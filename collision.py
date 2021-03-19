# Uncomment os.system("aplay tick_low.mp3 &") for sound 
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
import bonus
import render
import powerups
import random
import bullet
import os
import boss
from colorama import Fore, Back, Style


def check_and_adjust():

    # if player.details_of_player.level<3:
        
    flag = 1
    # FOR COLLISION WITH LEVEL 1 BRICKS
    arr = []
    ind = 0
    for k in range(len(bricks.lvl1_bricks)):
        if bricks.lvl1_bricks[k].vis == 0 and flag == 1:
            if ball.game_ball.y_pos + ball.game_ball.y_vel == bricks.lvl1_bricks[k].y_pos and ball.game_ball.x_pos >= bricks.lvl1_bricks[k].x_pos and ball.game_ball.x_pos+1 <= bricks.lvl1_bricks[k].x_pos+6:
                if ball.game_ball.state>0:
                    bonus.chain_reaction(
                    bricks.lvl1_bricks[k].x_pos, bricks.lvl1_bricks[k].y_pos)
                ##os.system("aplay tick_low.mp3 &")
                ball.game_ball.reverse_y_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + 1
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos == bricks.lvl1_bricks[k].y_pos and (ball.game_ball.x_pos+ball.game_ball.x_vel-bricks.lvl1_bricks[k].x_pos)*(ball.game_ball.x_pos+ball.game_ball.x_vel+1-bricks.lvl1_bricks[k].x_pos) <= 0:
                if ball.game_ball.state>0:
                    bonus.chain_reaction(
                    bricks.lvl1_bricks[k].x_pos, bricks.lvl1_bricks[k].y_pos)
                ##os.system("aplay tick_low.mp3 &")
                ball.game_ball.reverse_x_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + 1
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos == bricks.lvl1_bricks[k].y_pos and ball.game_ball.x_pos+ball.game_ball.x_vel >= bricks.lvl1_bricks[k].x_pos and ball.game_ball.x_pos+ball.game_ball.x_vel+1 <= bricks.lvl1_bricks[k].x_pos+6:
                if ball.game_ball.state>0:
                    bonus.chain_reaction(
                    bricks.lvl1_bricks[k].x_pos, bricks.lvl1_bricks[k].y_pos)
                ##os.system("aplay tick_low.mp3 &")
                ball.game_ball.reverse_x_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + 1
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos + ball.game_ball.y_vel == bricks.lvl1_bricks[k].y_pos and ball.game_ball.x_pos+ball.game_ball.x_vel >= bricks.lvl1_bricks[k].x_pos and ball.game_ball.x_pos+ball.game_ball.x_vel+1 <= bricks.lvl1_bricks[k].x_pos+6:
                if ball.game_ball.state>0:
                    bonus.chain_reaction(
                    bricks.lvl1_bricks[k].x_pos, bricks.lvl1_bricks[k].y_pos)
                ##os.system("aplay tick_low.mp3 &")
                ball.game_ball.reverse_x_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + 1
                flag = 1

    ind = ind - 1

    while ind >= 0:

        abc = random.randint(0, 19)
        # abc=19

        if abc == 18 or abc == 19:
            bruh = powerups.powerup_fireball(
                bricks.lvl1_bricks[arr[ind]].x_pos, bricks.lvl1_bricks[arr[ind]].y_pos+8)
            powerups.super_power.append(bruh)

        if abc == 16 or abc == 17:
            bruh = powerups.powerup_laser(
                bricks.lvl1_bricks[arr[ind]].x_pos, bricks.lvl1_bricks[arr[ind]].y_pos+8)
            powerups.super_power.append(bruh)

        if abc == 14 or abc == 15:
            bruh = powerups.powerup_fastball(
                bricks.lvl1_bricks[arr[ind]].x_pos, bricks.lvl1_bricks[arr[ind]].y_pos+8)
            powerups.super_power.append(bruh)

        if abc == 13 or abc == 12:
            bruh = powerups.powerup_grabball(
                bricks.lvl1_bricks[arr[ind]].x_pos, bricks.lvl1_bricks[arr[ind]].y_pos+8)
            powerups.super_power.append(bruh)

        if abc == 11 or abc == 10:
            bruh = powerups.powerup_shrink(
                bricks.lvl1_bricks[arr[ind]].x_pos, bricks.lvl1_bricks[arr[ind]].y_pos+8)
            powerups.super_power.append(bruh)

        if abc == 9 or abc == 8:
            bruh = powerups.powerup_expand(
                bricks.lvl1_bricks[arr[ind]].x_pos, bricks.lvl1_bricks[arr[ind]].y_pos+8)
            powerups.super_power.append(bruh)

        bricks.lvl1_bricks.pop(arr[ind])
        ind = ind - 1

    # FOR COLLISION WITH LEVEL 2 BRICKS
    arr = []
    ind = 0
    for k in range(len(bricks.lvl2_bricks)):
        if bricks.lvl2_bricks[k].vis == 0 and flag == 1:
            if ball.game_ball.y_pos + ball.game_ball.y_vel == bricks.lvl2_bricks[k].y_pos and ball.game_ball.x_pos >= bricks.lvl2_bricks[k].x_pos and ball.game_ball.x_pos+1 <= bricks.lvl2_bricks[k].x_pos+6:
                if ball.game_ball.state>0:
                    bonus.chain_reaction(
                    bricks.lvl2_bricks[k].x_pos, bricks.lvl2_bricks[k].y_pos)
                ##os.system("aplay tick_low.mp3 &")
                ball.game_ball.reverse_y_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + 1
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos == bricks.lvl2_bricks[k].y_pos and (ball.game_ball.x_pos+ball.game_ball.x_vel-bricks.lvl2_bricks[k].x_pos)*(ball.game_ball.x_pos+ball.game_ball.x_vel+1-bricks.lvl2_bricks[k].x_pos) <= 0:
                if ball.game_ball.state>0:
                    bonus.chain_reaction(
                    bricks.lvl2_bricks[k].x_pos, bricks.lvl2_bricks[k].y_pos)
                ##os.system("aplay tick_low.mp3 &")
                ball.game_ball.reverse_x_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + 1
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos == bricks.lvl2_bricks[k].y_pos and ball.game_ball.x_pos+ball.game_ball.x_vel >= bricks.lvl2_bricks[k].x_pos and ball.game_ball.x_pos+ball.game_ball.x_vel+1 <= bricks.lvl2_bricks[k].x_pos+6:
                if ball.game_ball.state>0:
                    bonus.chain_reaction(
                    bricks.lvl2_bricks[k].x_pos, bricks.lvl2_bricks[k].y_pos)
                ##os.system("aplay tick_low.mp3 &")
                ball.game_ball.reverse_x_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + 1
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos + ball.game_ball.y_vel == bricks.lvl2_bricks[k].y_pos and ball.game_ball.x_pos+ball.game_ball.x_vel >= bricks.lvl2_bricks[k].x_pos and ball.game_ball.x_pos+ball.game_ball.x_vel+1 <= bricks.lvl2_bricks[k].x_pos+6:
                if ball.game_ball.state>0:
                    bonus.chain_reaction(
                    bricks.lvl2_bricks[k].x_pos, bricks.lvl2_bricks[k].y_pos)
                ##os.system("aplay tick_low.mp3 &")
                ball.game_ball.reverse_x_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + 1
                flag = 1

    ind = ind - 1
    while ind >= 0:
        bricks.lvl1_bricks.append(bricks.lvl2_bricks[arr[ind]])
        bricks.lvl2_bricks.pop(arr[ind])
        ind = ind - 1

    # FOR COLLISION WITH LEVEL 3 BRICKS
    arr = []
    ind = 0
    for k in range(len(bricks.lvl3_bricks)):
        if bricks.lvl3_bricks[k].vis == 0 and flag == 1:

            if ball.game_ball.y_pos + ball.game_ball.y_vel == bricks.lvl3_bricks[k].y_pos and ball.game_ball.x_pos >= bricks.lvl3_bricks[k].x_pos and ball.game_ball.x_pos+1 <= bricks.lvl3_bricks[k].x_pos+6:
                if ball.game_ball.state>0:
                    bonus.chain_reaction(
                    bricks.lvl3_bricks[k].x_pos, bricks.lvl3_bricks[k].y_pos)
                ##os.system("aplay tick_low.mp3 &")
                ball.game_ball.reverse_y_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + 1
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos == bricks.lvl3_bricks[k].y_pos and (ball.game_ball.x_pos+ball.game_ball.x_vel-bricks.lvl3_bricks[k].x_pos)*(ball.game_ball.x_pos+ball.game_ball.x_vel+1-bricks.lvl3_bricks[k].x_pos) <= 0:
                if ball.game_ball.state>0:
                    bonus.chain_reaction(
                    bricks.lvl3_bricks[k].x_pos, bricks.lvl3_bricks[k].y_pos)
                #os.system("aplay tick_low.mp3 &")
                ball.game_ball.reverse_x_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + 1
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos == bricks.lvl3_bricks[k].y_pos and ball.game_ball.x_pos+ball.game_ball.x_vel >= bricks.lvl3_bricks[k].x_pos and ball.game_ball.x_pos+ball.game_ball.x_vel+1 <= bricks.lvl3_bricks[k].x_pos+6:
                if ball.game_ball.state>0:
                    bonus.chain_reaction(
                    bricks.lvl3_bricks[k].x_pos, bricks.lvl3_bricks[k].y_pos)
                ##os.system("aplay tick_low.mp3 &")
                ball.game_ball.reverse_x_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + 1
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos + ball.game_ball.y_vel == bricks.lvl3_bricks[k].y_pos and ball.game_ball.x_pos+ball.game_ball.x_vel >= bricks.lvl3_bricks[k].x_pos and ball.game_ball.x_pos+ball.game_ball.x_vel+1 <= bricks.lvl3_bricks[k].x_pos+6:
                if ball.game_ball.state>0:
                    bonus.chain_reaction(
                    bricks.lvl3_bricks[k].x_pos, bricks.lvl3_bricks[k].y_pos)
                ##os.system("aplay tick_low.mp3 &")
                ball.game_ball.reverse_x_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + 1
                flag = 1

    ind = ind - 1

    while ind >= 0:
        bricks.lvl2_bricks.append(bricks.lvl3_bricks[arr[ind]])
        bricks.lvl3_bricks.pop(arr[ind])
        ind = ind - 1

    ###################################################################
    # # FOR COLLISION WITH RAIN BRICKS
    arr = []
    ind = 0
    for k in range(len(bricks.rain_bricks)):
        if bricks.rain_bricks[k].vis == 0 and flag == 1:
            if ball.game_ball.y_pos + ball.game_ball.y_vel == bricks.rain_bricks[k].y_pos and ball.game_ball.x_pos >= bricks.rain_bricks[k].x_pos and ball.game_ball.x_pos+1 <= bricks.rain_bricks[k].x_pos+6:
                if ball.game_ball.state>0:
                    bonus.chain_reaction(
                    bricks.rain_bricks[k].x_pos, bricks.rain_bricks[k].y_pos)
                ##os.system("aplay tick_low.mp3 &")
                ball.game_ball.reverse_y_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + int(time.time()-player.stats.time)%3 + 1
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos == bricks.rain_bricks[k].y_pos and (ball.game_ball.x_pos+ball.game_ball.x_vel-bricks.rain_bricks[k].x_pos)*(ball.game_ball.x_pos+ball.game_ball.x_vel+1-bricks.rain_bricks[k].x_pos) <= 0:
                if ball.game_ball.state>0:
                    bonus.chain_reaction(
                    bricks.rain_bricks[k].x_pos, bricks.rain_bricks[k].y_pos)
                ##os.system("aplay tick_low.mp3 &")
                ball.game_ball.reverse_x_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + int(time.time()-player.stats.time)%3 + 1
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos == bricks.rain_bricks[k].y_pos and ball.game_ball.x_pos+ball.game_ball.x_vel >= bricks.rain_bricks[k].x_pos and ball.game_ball.x_pos+ball.game_ball.x_vel+1 <= bricks.rain_bricks[k].x_pos+6:
                if ball.game_ball.state>0:
                    bonus.chain_reaction(
                    bricks.rain_bricks[k].x_pos, bricks.rain_bricks[k].y_pos)
                ##os.system("aplay tick_low.mp3 &")
                ball.game_ball.reverse_x_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + int(time.time()-player.stats.time)%3 + 1
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos + ball.game_ball.y_vel == bricks.rain_bricks[k].y_pos and ball.game_ball.x_pos+ball.game_ball.x_vel >= bricks.rain_bricks[k].x_pos and ball.game_ball.x_pos+ball.game_ball.x_vel+1 <= bricks.rain_bricks[k].x_pos+6:
                if ball.game_ball.state>0:
                    bonus.chain_reaction(
                    bricks.rain_bricks[k].x_pos, bricks.rain_bricks[k].y_pos)
                ##os.system("aplay tick_low.mp3 &")
                ball.game_ball.reverse_x_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + int(time.time()-player.stats.time)%3 + 1
                flag = 1

    ind = ind - 1

    while ind >= 0:

        if int(time.time()-player.stats.time)%3 == 1:
            bricks.lvl1_bricks.append(bricks.rain_bricks[arr[ind]])
        
        elif int(time.time()-player.stats.time)%3 == 2:
            bricks.lvl2_bricks.append(bricks.rain_bricks[arr[ind]])

        bricks.rain_bricks.pop(arr[ind])
        ind = ind - 1

    #############################################################

    # FOR COLLISION WITH NON-DESTRUCTIBLE BRICKS
    for k in range(len(bricks.nond_bricks)):
        if bricks.nond_bricks[k].vis == 0 and flag == 1:

            if ball.game_ball.y_pos + ball.game_ball.y_vel == bricks.nond_bricks[k].y_pos and ball.game_ball.x_pos >= bricks.nond_bricks[k].x_pos and ball.game_ball.x_pos+1 <= bricks.nond_bricks[k].x_pos+6:
                if ball.game_ball.state>0:
                    bonus.chain_reaction(
                    bricks.nond_bricks[k].x_pos, bricks.nond_bricks[k].y_pos)
                
                if player.stats.level==3:
                    boss.game_boss.lives=boss.game_boss.lives-1
                
                ##os.system("aplay tick_low.mp3 &")
                ball.game_ball.reverse_y_vel()
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos == bricks.nond_bricks[k].y_pos and (ball.game_ball.x_pos+ball.game_ball.x_vel-bricks.nond_bricks[k].x_pos)*(ball.game_ball.x_pos+ball.game_ball.x_vel+1-bricks.nond_bricks[k].x_pos) <= 0:
                if ball.game_ball.state>0:
                    bonus.chain_reaction(
                    bricks.nond_bricks[k].x_pos, bricks.nond_bricks[k].y_pos)

                if player.stats.level==3:
                    boss.game_boss.lives=boss.game_boss.lives-1

                ##os.system("aplay tick_low.mp3 &")
                ball.game_ball.reverse_x_vel()
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos == bricks.nond_bricks[k].y_pos and ball.game_ball.x_pos+ball.game_ball.x_vel >= bricks.nond_bricks[k].x_pos and ball.game_ball.x_pos+ball.game_ball.x_vel+1 <= bricks.nond_bricks[k].x_pos+6:
                if ball.game_ball.state>0:
                    bonus.chain_reaction(
                    bricks.nond_bricks[k].x_pos, bricks.nond_bricks[k].y_pos)

                if player.stats.level==3:
                    boss.game_boss.lives=boss.game_boss.lives-1

                ##os.system("aplay tick_low.mp3 &")
                ball.game_ball.reverse_x_vel()
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos + ball.game_ball.y_vel == bricks.nond_bricks[k].y_pos and ball.game_ball.x_pos+ball.game_ball.x_vel >= bricks.nond_bricks[k].x_pos and ball.game_ball.x_pos+ball.game_ball.x_vel+1 <= bricks.nond_bricks[k].x_pos+6:
                if ball.game_ball.state>0:
                    bonus.chain_reaction(
                    bricks.nond_bricks[k].x_pos, bricks.nond_bricks[k].y_pos)
                
                if player.stats.level==3:
                    boss.game_boss.lives=boss.game_boss.lives-1

                ##os.system("aplay tick_low.mp3 &")
                ball.game_ball.reverse_x_vel()
                flag = 1

    # FOR COLLISION WITH EXPLODING BRICKS
    for k in range(len(bricks.expl_bricks)):
        if bricks.expl_bricks[k].vis == 0 and flag == 1:

            if ball.game_ball.y_pos + ball.game_ball.y_vel == bricks.expl_bricks[k].y_pos and ball.game_ball.x_pos >= bricks.expl_bricks[k].x_pos and ball.game_ball.x_pos+1 <= bricks.expl_bricks[k].x_pos+6:
                ball.game_ball.reverse_y_vel()
                flag = 1
                bonus.chain_reaction(
                    bricks.expl_bricks[k].x_pos, bricks.expl_bricks[k].y_pos)

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos == bricks.expl_bricks[k].y_pos and (ball.game_ball.x_pos+ball.game_ball.x_vel-bricks.expl_bricks[k].x_pos)*(ball.game_ball.x_pos+ball.game_ball.x_vel+1-bricks.expl_bricks[k].x_pos) <= 0:
                ball.game_ball.reverse_x_vel()
                flag = 1
                bonus.chain_reaction(
                    bricks.expl_bricks[k].x_pos, bricks.expl_bricks[k].y_pos)

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos == bricks.expl_bricks[k].y_pos and ball.game_ball.x_pos+ball.game_ball.x_vel >= bricks.expl_bricks[k].x_pos and ball.game_ball.x_pos+ball.game_ball.x_vel+1 <= bricks.expl_bricks[k].x_pos+6:
                ball.game_ball.reverse_x_vel()
                flag = 1
                bonus.chain_reaction(
                    bricks.expl_bricks[k].x_pos, bricks.expl_bricks[k].y_pos)

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos + ball.game_ball.y_vel == bricks.expl_bricks[k].y_pos and ball.game_ball.x_pos+ball.game_ball.x_vel >= bricks.expl_bricks[k].x_pos and ball.game_ball.x_pos+ball.game_ball.x_vel+1 <= bricks.expl_bricks[k].x_pos+6:
                ball.game_ball.reverse_x_vel()
                flag = 1
                bonus.chain_reaction(
                    bricks.expl_bricks[k].x_pos, bricks.expl_bricks[k].y_pos)



    ###########################################################################################################################

    # FOR COLLISION WITH LEVEL 1 BRICKS
    arr = []
    ind = 0
    for k in range(len(bricks.lvl1_bricks)):
        if bricks.lvl1_bricks[k].vis == 0 and flag == 1:

            lol = len(bullet.game_bullet)
            lol = lol-1
            
            while lol>=0:
                if bullet.game_bullet[lol].y_pos-1 == bricks.lvl1_bricks[k].y_pos and bullet.game_bullet[lol].x_pos>=bricks.lvl1_bricks[k].x_pos and bullet.game_bullet[lol].x_pos+1<=bricks.lvl1_bricks[k].x_pos+6:
                    arr.append(k)
                    ind = ind+1
                    bullet.game_bullet.pop(lol)
                    player.stats.score = player.stats.score + 1
                lol=lol-1

    ind = ind - 1

    while ind >= 0:

        abc = random.randint(0, 19)
        # abc=19

        if abc == 18 or abc == 19:
            bruh = powerups.powerup_fireball(
                bricks.lvl1_bricks[arr[ind]].x_pos, bricks.lvl1_bricks[arr[ind]].y_pos+8)
            powerups.super_power.append(bruh)

        if abc == 16 or abc == 17:
            bruh = powerups.powerup_laser(
                bricks.lvl1_bricks[arr[ind]].x_pos, bricks.lvl1_bricks[arr[ind]].y_pos+8)
            powerups.super_power.append(bruh)

        if abc == 14 or abc == 15:
            bruh = powerups.powerup_fastball(
                bricks.lvl1_bricks[arr[ind]].x_pos, bricks.lvl1_bricks[arr[ind]].y_pos+8)
            powerups.super_power.append(bruh)

        if abc == 13 or abc == 12:
            bruh = powerups.powerup_grabball(
                bricks.lvl1_bricks[arr[ind]].x_pos, bricks.lvl1_bricks[arr[ind]].y_pos+8)
            powerups.super_power.append(bruh)

        if abc == 11 or abc == 10:
            bruh = powerups.powerup_shrink(
                bricks.lvl1_bricks[arr[ind]].x_pos, bricks.lvl1_bricks[arr[ind]].y_pos+8)
            powerups.super_power.append(bruh)

        if abc == 9 or abc == 8:
            bruh = powerups.powerup_expand(
                bricks.lvl1_bricks[arr[ind]].x_pos, bricks.lvl1_bricks[arr[ind]].y_pos+8)
            powerups.super_power.append(bruh)

        bricks.lvl1_bricks.pop(arr[ind])
        ind = ind - 1


    ############ FOR BULLET AND LEVEL 2 BRICKS

    arr = []
    ind = 0
    for k in range(len(bricks.lvl2_bricks)):
        if bricks.lvl2_bricks[k].vis == 0 and flag == 1:
            
            lol = len(bullet.game_bullet)
            lol = lol-1
            
            while lol>=0:
                if bullet.game_bullet[lol].y_pos-1 == bricks.lvl2_bricks[k].y_pos and bullet.game_bullet[lol].x_pos>=bricks.lvl2_bricks[k].x_pos and bullet.game_bullet[lol].x_pos+1<=bricks.lvl2_bricks[k].x_pos+6:
                    arr.append(k)
                    ind = ind+1
                    bullet.game_bullet.pop(lol)
                    player.stats.score = player.stats.score + 1
                lol=lol-1

    ind = ind - 1

    while ind >= 0:
        bricks.lvl1_bricks.append(bricks.lvl2_bricks[arr[ind]])
        bricks.lvl2_bricks.pop(arr[ind])
        ind = ind - 1

    ########### BULLET AND LEVEL 3
    arr = []
    ind = 0
    for k in range(len(bricks.lvl3_bricks)):
        if bricks.lvl3_bricks[k].vis == 0 and flag == 1:
            
            lol = len(bullet.game_bullet)
            lol = lol-1
            
            while lol>=0:
                if bullet.game_bullet[lol].y_pos-1 == bricks.lvl3_bricks[k].y_pos and bullet.game_bullet[lol].x_pos>=bricks.lvl3_bricks[k].x_pos and bullet.game_bullet[lol].x_pos+1<=bricks.lvl3_bricks[k].x_pos+6:
                    arr.append(k)
                    ind = ind+1
                    bullet.game_bullet.pop(lol)
                    player.stats.score = player.stats.score + 1
                lol=lol-1

    ind = ind - 1

    while ind >= 0:
        bricks.lvl2_bricks.append(bricks.lvl3_bricks[arr[ind]])
        bricks.lvl3_bricks.pop(arr[ind])
        ind = ind - 1

    

    # FOR BULLET AND NON-DESTRUCTIBLE BRICKS
    for k in range(len(bricks.nond_bricks)):
        if bricks.nond_bricks[k].vis == 0 and flag == 1:

            lol = len(bullet.game_bullet)
            lol = lol-1
            
            while lol>=0:
                if bullet.game_bullet[lol].y_pos-1 == bricks.nond_bricks[k].y_pos and bullet.game_bullet[lol].x_pos>=bricks.nond_bricks[k].x_pos and bullet.game_bullet[lol].x_pos+1<=bricks.nond_bricks[k].x_pos+6:
                    bullet.game_bullet.pop(lol)
                    player.stats.score = player.stats.score + 1
                lol=lol-1


    ####### FOR BULLET AND RAINBOW
    arr = []
    ind = 0
    for k in range(len(bricks.rain_bricks)):
        if bricks.rain_bricks[k].vis == 0 and flag == 1:

            lol = len(bullet.game_bullet)
            lol = lol-1
            
            while lol>=0:
                if bullet.game_bullet[lol].y_pos-1 == bricks.rain_bricks[k].y_pos and bullet.game_bullet[lol].x_pos>=bricks.rain_bricks[k].x_pos and bullet.game_bullet[lol].x_pos+1<=bricks.rain_bricks[k].x_pos+6:
                    arr.append(k)
                    ind = ind+1
                    bullet.game_bullet.pop(lol)
                    player.stats.score = player.stats.score + int(time.time()-player.stats.time)%3 + 1
                lol=lol-1

    ind = ind - 1

    while ind >= 0:

        if int(time.time()-player.stats.time)%3 == 1:
            bricks.lvl1_bricks.append(bricks.rain_bricks[arr[ind]])
        
        elif int(time.time()-player.stats.time)%3 == 2:
            bricks.lvl2_bricks.append(bricks.rain_bricks[arr[ind]])

        bricks.rain_bricks.pop(arr[ind])
        ind = ind - 1


    # FOR COLLISION WITH EXPLODING BRICKS
    for k in range(len(bricks.expl_bricks)):
        if bricks.expl_bricks[k].vis == 0 and flag == 1:

            lol = len(bullet.game_bullet)
            lol = lol-1
            
            while lol>=0:
                if bullet.game_bullet[lol].y_pos-1 == bricks.expl_bricks[k].y_pos and bullet.game_bullet[lol].x_pos>=bricks.expl_bricks[k].x_pos and bullet.game_bullet[lol].x_pos+1<=bricks.expl_bricks[k].x_pos+6:
                    bullet.game_bullet.pop(lol)
                    bonus.chain_reaction(
                    bricks.expl_bricks[k].x_pos, bricks.expl_bricks[k].y_pos)
                lol=lol-1

            # if ball.game_ball.y_pos + ball.game_ball.y_vel == bricks.expl_bricks[k].y_pos and ball.game_ball.x_pos >= bricks.expl_bricks[k].x_pos and ball.game_ball.x_pos+1 <= bricks.expl_bricks[k].x_pos+6:
            #     ball.game_ball.reverse_y_vel()
            #     flag = 1
            #     bonus.chain_reaction(
            #         bricks.expl_bricks[k].x_pos, bricks.expl_bricks[k].y_pos)

            # elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos == bricks.expl_bricks[k].y_pos and (ball.game_ball.x_pos+ball.game_ball.x_vel-bricks.expl_bricks[k].x_pos)*(ball.game_ball.x_pos+ball.game_ball.x_vel+1-bricks.expl_bricks[k].x_pos) <= 0:
            #     ball.game_ball.reverse_x_vel()
            #     flag = 1
            #     bonus.chain_reaction(
            #         bricks.expl_bricks[k].x_pos, bricks.expl_bricks[k].y_pos)

            # elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos == bricks.expl_bricks[k].y_pos and ball.game_ball.x_pos+ball.game_ball.x_vel >= bricks.expl_bricks[k].x_pos and ball.game_ball.x_pos+ball.game_ball.x_vel+1 <= bricks.expl_bricks[k].x_pos+6:
            #     ball.game_ball.reverse_x_vel()
            #     flag = 1
            #     bonus.chain_reaction(
            #         bricks.expl_bricks[k].x_pos, bricks.expl_bricks[k].y_pos)

            # elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos + ball.game_ball.y_vel == bricks.expl_bricks[k].y_pos and ball.game_ball.x_pos+ball.game_ball.x_vel >= bricks.expl_bricks[k].x_pos and ball.game_ball.x_pos+ball.game_ball.x_vel+1 <= bricks.expl_bricks[k].x_pos+6:
            #     ball.game_ball.reverse_x_vel()
            #     flag = 1
            #     bonus.chain_reaction(
            #         bricks.expl_bricks[k].x_pos, bricks.expl_bricks[k].y_pos)



    ###########################################################################################################################


    # COLLISION BETWEEN BALL AND SLIDER


    if ball.game_ball.y_pos + ball.game_ball.y_vel == slider.game_slider.y_pos and ball.game_ball.x_pos >= slider.game_slider.x_pos and ball.game_ball.x_pos+1 <= slider.game_slider.x_pos+slider.game_slider.length:
        ball.game_ball.reverse_y_vel()

        if int(time.time()-player.stats.time)>=10 and player.stats.level<3:

            for k in range(len(bricks.lvl1_bricks)):
                bricks.lvl1_bricks[k].y_pos = bricks.lvl1_bricks[k].y_pos+1
                if bricks.lvl1_bricks[k].y_pos == 34:
                    print("SORRY, YOU LOST!\n")
                    exit()

            for k in range(len(bricks.lvl2_bricks)):
                bricks.lvl2_bricks[k].y_pos = bricks.lvl2_bricks[k].y_pos+1
                if bricks.lvl2_bricks[k].y_pos == 34:
                    print("SORRY, YOU LOST!\n")
                    exit()

            for k in range(len(bricks.lvl3_bricks)):
                bricks.lvl3_bricks[k].y_pos = bricks.lvl3_bricks[k].y_pos+1
                if bricks.lvl3_bricks[k].y_pos == 34:
                    print("SORRY, YOU LOST!\n")
                    exit()

            for k in range(len(bricks.nond_bricks)):
                bricks.nond_bricks[k].y_pos = bricks.nond_bricks[k].y_pos+1
                if bricks.nond_bricks[k].y_pos == 34:
                    print("SORRY, YOU LOST!\n")
                    exit()

            for k in range(len(bricks.expl_bricks)):
                bricks.expl_bricks[k].y_pos = bricks.expl_bricks[k].y_pos+1
                if bricks.expl_bricks[k].y_pos == 34:
                    print("SORRY, YOU LOST!\n")
                    exit()

            for k in range(len(bricks.rain_bricks)):
                bricks.rain_bricks[k].y_pos = bricks.rain_bricks[k].y_pos+1
                if bricks.rain_bricks[k].y_pos == 34:
                    print("SORRY, YOU LOST!\n")
                    exit()
        
        
        if ball.game_ball.x_pos <= slider.game_slider.x_pos+slider.game_slider.length/5:
            ball.game_ball.x_vel = -2
        elif ball.game_ball.x_pos <= slider.game_slider.x_pos+2*slider.game_slider.length/5:
            ball.game_ball.x_vel = -1
        elif ball.game_ball.x_pos <= slider.game_slider.x_pos+3*slider.game_slider.length/5:
            ball.game_ball.x_vel = 0
        elif ball.game_ball.x_pos <= slider.game_slider.x_pos+4*slider.game_slider.length/5:
            ball.game_ball.x_vel = 1
        elif ball.game_ball.x_pos <= slider.game_slider.x_pos+5*slider.game_slider.length/5:
            ball.game_ball.x_vel = 2
        if ball.game_ball.grab_status == 1:
            player.stats.status = 'P'
            ball.game_ball.y_pos = slider.game_slider.y_pos

    # FOR COLLISION WITH VERTICAL WALLS

    if ball.game_ball.x_pos + ball.game_ball.x_vel + 1 < 120 and ball.game_ball.x_pos + ball.game_ball.x_vel > 0:
        ball.game_ball.x_pos = ball.game_ball.x_pos + ball.game_ball.x_vel

    else:
        ball.game_ball.reverse_x_vel()
        ball.game_ball.x_pos = ball.game_ball.x_pos + ball.game_ball.x_vel

    ##################### FOR POWERUPS ########################

    for k in range(len(powerups.super_power)):
        powerups.super_power[k].y_pos = powerups.super_power[k].y_pos + 1

    for k in range(len(powerups.super_power)):
        if powerups.super_power[k].y_pos + 1 == slider.game_slider.y_pos and powerups.super_power[k].x_pos >= slider.game_slider.x_pos and powerups.super_power[k].x_pos+1 <= slider.game_slider.x_pos+slider.game_slider.length:
            powerups.super_power[k].time_of_activation = time.time()
            powerups.super_power[k].used = 1
            powerups.super_power[k].image = ' '
            powerups.super_power[k].activate()

    if slider.game_slider.state > 0:
        slider.game_slider.remain = int(10+slider.game_slider.start-time.time())
        if time.time()-slider.game_slider.shoot>2:
            sample = bullet.bullet(slider.game_slider.x_pos,slider.game_slider.y_pos)
            bullet.game_bullet.append(sample)
            sample = bullet.bullet(slider.game_slider.x_pos-1+slider.game_slider.length,slider.game_slider.y_pos)
            bullet.game_bullet.append(sample)
            slider.game_slider.shoot = time.time()

    if player.stats.level==3:
        if time.time()-slider.game_slider.shoot>4:
            sample = bullet.bullet(bricks.nond_bricks[5].x_pos,bricks.nond_bricks[5].y_pos+1)
            bullet.game_bullet.append(sample)
            sample = bullet.bullet(bricks.nond_bricks[10].x_pos-1+6,bricks.nond_bricks[10].y_pos+1)
            bullet.game_bullet.append(sample)
            slider.game_slider.shoot = time.time()

    if player.stats.level<3:
        for k in range(len(bullet.game_bullet)):
            bullet.game_bullet[k].y_pos=bullet.game_bullet[k].y_pos-1

    else:
        k=len(bullet.game_bullet)-1
        
        while k>=0:
            bullet.game_bullet[k].y_pos=bullet.game_bullet[k].y_pos+1

            if bullet.game_bullet[k].y_pos == 34 and bullet.game_bullet[k].x_pos>=slider.game_slider.x_pos and bullet.game_bullet[k].x_pos+1<=slider.game_slider.x_pos+slider.game_slider.length:
                player.stats.lives = player.stats.lives-1
                bullet.game_bullet.pop(k)

            k = k-1


    # FOR COLLISION WITH HORIZONTAL WALL

    if ball.game_ball.y_pos + ball.game_ball.y_vel + 1 > 0 and ball.game_ball.y_pos + ball.game_ball.y_vel < 35:
        ball.game_ball.y_pos = ball.game_ball.y_pos + ball.game_ball.y_vel

    elif ball.game_ball.y_pos + ball.game_ball.y_vel + 1 <= 0:
        ball.game_ball.reverse_y_vel()
        ball.game_ball.y_pos = ball.game_ball.y_pos + ball.game_ball.y_vel

    else:
        player.stats.lives = player.stats.lives - 1
        k = len(powerups.super_power)-1
        while k >= 0:
            if powerups.super_power[k].used == 1:
                powerups.super_power[k].deactivate()
            powerups.super_power.pop(k)
            k = k-1

        render.reset()

    # if player.stats.lives == 0:
    #     print("SORRY, YOU LOST!\n")
    #     exit()

    rem_bricks_cnt = 0
    
    for k in range(len(bricks.lvl1_bricks)):
        if bricks.lvl1_bricks[k].vis==0:
            rem_bricks_cnt=rem_bricks_cnt+1

    for k in range(len(bricks.lvl2_bricks)):
        if bricks.lvl2_bricks[k].vis==0:
            rem_bricks_cnt=rem_bricks_cnt+1

    for k in range(len(bricks.lvl3_bricks)):
        if bricks.lvl3_bricks[k].vis==0:
            rem_bricks_cnt=rem_bricks_cnt+1

    for k in range(len(bricks.expl_bricks)):
        if bricks.expl_bricks[k].vis==0:
            rem_bricks_cnt=rem_bricks_cnt+1

    for k in range(len(bricks.rain_bricks)):
        if bricks.rain_bricks[k].vis==0:
            rem_bricks_cnt=rem_bricks_cnt+1

    if player.stats.level == 3 and boss.game_boss.lives>0:
        rem_bricks_cnt=1

    if rem_bricks_cnt == 0:
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