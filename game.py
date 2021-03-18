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
import render
import powerups
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

while (True):
    powerups.disable_powerup()
    c = render.display_and_input()
    if player.stats.status == 'A':
        collision.check_and_adjust()
    if c:
        time.sleep(display_file.refresh_rate)