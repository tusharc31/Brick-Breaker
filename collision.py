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
from colorama import Fore, Back, Style


def check_and_adjust():
    flag = 1
    # FOR COLLISION WITH LEVEL 1 BRICKS
    arr = []
    ind = 0
    for k in range(len(bricks.lvl1_bricks)):
        if bricks.lvl1_bricks[k].vis == 0 and flag == 1:
            if ball.game_ball.y_pos + ball.game_ball.y_vel == bricks.lvl1_bricks[k].y_pos and ball.game_ball.x_pos >= bricks.lvl1_bricks[k].x_pos and ball.game_ball.x_pos+1 <= bricks.lvl1_bricks[k].x_pos+6:
                ball.game_ball.reverse_y_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + 1
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos == bricks.lvl1_bricks[k].y_pos and (ball.game_ball.x_pos+ball.game_ball.x_vel-bricks.lvl1_bricks[k].x_pos)*(ball.game_ball.x_pos+ball.game_ball.x_vel+1-bricks.lvl1_bricks[k].x_pos) <= 0:
                ball.game_ball.reverse_x_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + 1
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos == bricks.lvl1_bricks[k].y_pos and ball.game_ball.x_pos+ball.game_ball.x_vel >= bricks.lvl1_bricks[k].x_pos and ball.game_ball.x_pos+ball.game_ball.x_vel+1 <= bricks.lvl1_bricks[k].x_pos+6:
                ball.game_ball.reverse_x_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + 1
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos + ball.game_ball.y_vel == bricks.lvl1_bricks[k].y_pos and ball.game_ball.x_pos+ball.game_ball.x_vel >= bricks.lvl1_bricks[k].x_pos and ball.game_ball.x_pos+ball.game_ball.x_vel+1 <= bricks.lvl1_bricks[k].x_pos+6:
                ball.game_ball.reverse_x_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + 1
                flag = 1

    ind = ind - 1

    while ind >= 0:

        abc = random.randint(0, 15)

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
                ball.game_ball.reverse_y_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + 1
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos == bricks.lvl2_bricks[k].y_pos and (ball.game_ball.x_pos+ball.game_ball.x_vel-bricks.lvl2_bricks[k].x_pos)*(ball.game_ball.x_pos+ball.game_ball.x_vel+1-bricks.lvl2_bricks[k].x_pos) <= 0:
                ball.game_ball.reverse_x_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + 1
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos == bricks.lvl2_bricks[k].y_pos and ball.game_ball.x_pos+ball.game_ball.x_vel >= bricks.lvl2_bricks[k].x_pos and ball.game_ball.x_pos+ball.game_ball.x_vel+1 <= bricks.lvl2_bricks[k].x_pos+6:
                ball.game_ball.reverse_x_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + 1
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos + ball.game_ball.y_vel == bricks.lvl2_bricks[k].y_pos and ball.game_ball.x_pos+ball.game_ball.x_vel >= bricks.lvl2_bricks[k].x_pos and ball.game_ball.x_pos+ball.game_ball.x_vel+1 <= bricks.lvl2_bricks[k].x_pos+6:
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
                ball.game_ball.reverse_y_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + 1
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos == bricks.lvl3_bricks[k].y_pos and (ball.game_ball.x_pos+ball.game_ball.x_vel-bricks.lvl3_bricks[k].x_pos)*(ball.game_ball.x_pos+ball.game_ball.x_vel+1-bricks.lvl3_bricks[k].x_pos) <= 0:
                ball.game_ball.reverse_x_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + 1
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos == bricks.lvl3_bricks[k].y_pos and ball.game_ball.x_pos+ball.game_ball.x_vel >= bricks.lvl3_bricks[k].x_pos and ball.game_ball.x_pos+ball.game_ball.x_vel+1 <= bricks.lvl3_bricks[k].x_pos+6:
                ball.game_ball.reverse_x_vel()
                arr.append(k)
                ind = ind+1
                player.stats.score = player.stats.score + 1
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos + ball.game_ball.y_vel == bricks.lvl3_bricks[k].y_pos and ball.game_ball.x_pos+ball.game_ball.x_vel >= bricks.lvl3_bricks[k].x_pos and ball.game_ball.x_pos+ball.game_ball.x_vel+1 <= bricks.lvl3_bricks[k].x_pos+6:
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

    # FOR COLLISION WITH NON-DESTRUCTIBLE BRICKS
    for k in range(len(bricks.nond_bricks)):
        if bricks.nond_bricks[k].vis == 0 and flag == 1:

            if ball.game_ball.y_pos + ball.game_ball.y_vel == bricks.nond_bricks[k].y_pos and ball.game_ball.x_pos >= bricks.nond_bricks[k].x_pos and ball.game_ball.x_pos+1 <= bricks.nond_bricks[k].x_pos+6:
                ball.game_ball.reverse_y_vel()
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos == bricks.nond_bricks[k].y_pos and (ball.game_ball.x_pos+ball.game_ball.x_vel-bricks.nond_bricks[k].x_pos)*(ball.game_ball.x_pos+ball.game_ball.x_vel+1-bricks.nond_bricks[k].x_pos) <= 0:
                ball.game_ball.reverse_x_vel()
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos == bricks.nond_bricks[k].y_pos and ball.game_ball.x_pos+ball.game_ball.x_vel >= bricks.nond_bricks[k].x_pos and ball.game_ball.x_pos+ball.game_ball.x_vel+1 <= bricks.nond_bricks[k].x_pos+6:
                ball.game_ball.reverse_x_vel()
                flag = 1

            elif ball.game_ball.x_vel != 0 and ball.game_ball.y_pos + ball.game_ball.y_vel == bricks.nond_bricks[k].y_pos and ball.game_ball.x_pos+ball.game_ball.x_vel >= bricks.nond_bricks[k].x_pos and ball.game_ball.x_pos+ball.game_ball.x_vel+1 <= bricks.nond_bricks[k].x_pos+6:
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


    # COLLISION BETWEEN BALL AND SLIDER


    if ball.game_ball.y_pos + ball.game_ball.y_vel == slider.game_slider.y_pos and ball.game_ball.x_pos >= slider.game_slider.x_pos and ball.game_ball.x_pos+1 <= slider.game_slider.x_pos+slider.game_slider.length:
        ball.game_ball.reverse_y_vel()
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

    if player.stats.lives == 0:
        print("SORRY, YOU LOST!\n")
        exit()

    if len(bricks.expl_bricks) + len(bricks.lvl1_bricks) + len(bricks.lvl2_bricks) + len(bricks.lvl3_bricks) == 0:
        bricks.clear_all_bricks()

        if player.stats.level==1:
            player.stats.level==player.stats.level+1
            bricks.display_level2_bricks()
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