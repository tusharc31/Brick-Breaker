import position
import existence
import player

class bricks(position.position,existence.existence):
    def __init__(self,x,y):
        self.height = 2
        self.length = 5
        self.vis = 0
        super().set_position(x,y)

    def blast(self,x,y):
        self.x = -1
        self.y = -1




class level1_brick(bricks):
    def __init__(self,x,y):
        super().__init__(x,y)

class level2_brick(bricks):
    def __init__(self,x,y):
        super().__init__(x,y)

class level3_brick(bricks):
    def __init__(self,x,y):
        super().__init__(x,y)

class non_destructible_brick(bricks):
    def __init__(self,x,y):
        super().__init__(x,y)

class explosive_brick(bricks):
    def __init__(self,x,y):
        super().__init__(x,y)



lvl1_bricks = []
lvl2_bricks = []
lvl3_bricks = []
nond_bricks = []
expl_bricks = []

# Column of level 3 bricks
sample = level3_brick(34,5)
lvl3_bricks.append(sample)
sample = level3_brick(34,6)
lvl3_bricks.append(sample)
sample = level3_brick(34,7)
lvl3_bricks.append(sample)
sample = level3_brick(34,8)
lvl3_bricks.append(sample)
sample = level3_brick(34,9)
lvl3_bricks.append(sample)
sample = level3_brick(34,10)
lvl3_bricks.append(sample)
sample = level3_brick(34,11)
lvl3_bricks.append(sample)
sample = level3_brick(34,12)
lvl3_bricks.append(sample)

# Column of level 2 bricks
sample = level2_brick(40,5)
lvl2_bricks.append(sample)
sample = level2_brick(40,6)
lvl2_bricks.append(sample)
sample = level2_brick(40,7)
lvl2_bricks.append(sample)
sample = level2_brick(40,8)
lvl2_bricks.append(sample)
sample = level2_brick(40,9)
lvl2_bricks.append(sample)
sample = level2_brick(40,10)
lvl2_bricks.append(sample)
sample = level2_brick(40,11)
lvl2_bricks.append(sample)
sample = level2_brick(40,12)
lvl2_bricks.append(sample)

# Column of level 1 bricks
sample = level1_brick(46,5)
lvl1_bricks.append(sample)
sample = level1_brick(46,6)
lvl1_bricks.append(sample)
sample = level1_brick(46,7)
lvl1_bricks.append(sample)
sample = level1_brick(46,8)
lvl1_bricks.append(sample)
sample = level1_brick(46,9)
lvl1_bricks.append(sample)
sample = level1_brick(46,10)
lvl1_bricks.append(sample)
sample = level1_brick(46,11)
lvl1_bricks.append(sample)
sample = level1_brick(46,12)
lvl1_bricks.append(sample)

# Column of non-detructible bricks
sample = non_destructible_brick(58,5)
nond_bricks.append(sample)
sample = non_destructible_brick(58,6)
nond_bricks.append(sample)
sample = non_destructible_brick(58,7)
nond_bricks.append(sample)
sample = non_destructible_brick(58,8)
nond_bricks.append(sample)
sample = non_destructible_brick(58,9)
nond_bricks.append(sample)
sample = non_destructible_brick(58,10)
nond_bricks.append(sample)
sample = non_destructible_brick(58,11)
nond_bricks.append(sample)
sample = non_destructible_brick(58,12)
nond_bricks.append(sample)

# Column of level 1 bricks
sample = level1_brick(70,5)
lvl1_bricks.append(sample)
sample = level1_brick(70,6)
lvl1_bricks.append(sample)
sample = level1_brick(70,7)
lvl1_bricks.append(sample)
sample = level1_brick(70,8)
lvl1_bricks.append(sample)
sample = level1_brick(70,9)
lvl1_bricks.append(sample)
sample = level1_brick(70,10)
lvl1_bricks.append(sample)
sample = level1_brick(70,11)
lvl1_bricks.append(sample)
sample = level1_brick(70,12)
lvl1_bricks.append(sample)

# Column of level 2 bricks
sample = level2_brick(76,5)
lvl2_bricks.append(sample)
sample = level2_brick(76,6)
lvl2_bricks.append(sample)
sample = level2_brick(76,7)
lvl2_bricks.append(sample)
sample = level2_brick(76,8)
lvl2_bricks.append(sample)
sample = level2_brick(76,9)
lvl2_bricks.append(sample)
sample = level2_brick(76,10)
lvl2_bricks.append(sample)
sample = level2_brick(76,11)
lvl2_bricks.append(sample)
sample = level2_brick(76,12)
lvl2_bricks.append(sample)

# Column of level 3 bricks
sample = level3_brick(82,5)
lvl3_bricks.append(sample)
sample = level3_brick(82,6)
lvl3_bricks.append(sample)
sample = level3_brick(82,7)
lvl3_bricks.append(sample)
sample = level3_brick(82,8)
lvl3_bricks.append(sample)
sample = level3_brick(82,9)
lvl3_bricks.append(sample)
sample = level3_brick(82,10)
lvl3_bricks.append(sample)
sample = level3_brick(82,11)
lvl3_bricks.append(sample)
sample = level3_brick(82,12)
lvl3_bricks.append(sample)

#Column 1 including explosive bricks
sample = explosive_brick(0,5)
expl_bricks.append(sample)
sample = level1_brick(0,6)
lvl1_bricks.append(sample)
sample = level2_brick(0,7)
lvl2_bricks.append(sample)
sample = non_destructible_brick(0,8)
nond_bricks.append(sample)
sample = non_destructible_brick(0,9)
nond_bricks.append(sample)
sample = level2_brick(0,10)
lvl2_bricks.append(sample)
sample = level1_brick(0,11)
lvl1_bricks.append(sample)
sample = explosive_brick(0,12)
expl_bricks.append(sample)

#Column 2 including explosive bricks
sample = non_destructible_brick(6,5)
nond_bricks.append(sample)
sample = explosive_brick(6,6)
expl_bricks.append(sample)
sample = level1_brick(6,7)
lvl1_bricks.append(sample)
sample = level2_brick(6,8)
lvl2_bricks.append(sample)
sample = level2_brick(6,9)
lvl2_bricks.append(sample)
sample = level1_brick(6,10)
lvl1_bricks.append(sample)
sample = explosive_brick(6,11)
expl_bricks.append(sample)
sample = non_destructible_brick(6,12)
nond_bricks.append(sample)

#Column 3 including explosive bricks
sample = non_destructible_brick(108,5)
nond_bricks.append(sample)
sample = explosive_brick(108,6)
expl_bricks.append(sample)
sample = level1_brick(108,7)
lvl1_bricks.append(sample)
sample = level2_brick(108,8)
lvl2_bricks.append(sample)
sample = level2_brick(108,9)
lvl2_bricks.append(sample)
sample = level1_brick(108,10)
lvl1_bricks.append(sample)
sample = explosive_brick(108,11)
expl_bricks.append(sample)
sample = non_destructible_brick(108,12)
nond_bricks.append(sample)

#Column 4 including explosive bricks
sample = explosive_brick(114,5)
expl_bricks.append(sample)
sample = level1_brick(114,6)
lvl1_bricks.append(sample)
sample = level2_brick(114,7)
lvl2_bricks.append(sample)
sample = non_destructible_brick(114,8)
nond_bricks.append(sample)
sample = non_destructible_brick(114,9)
nond_bricks.append(sample)
sample = level2_brick(114,10)
lvl2_bricks.append(sample)
sample = level1_brick(114,11)
lvl1_bricks.append(sample)
sample = explosive_brick(114,12)
expl_bricks.append(sample)

# lvl1_bricks = []
# lvl2_bricks = []
# lvl3_bricks = []
# nond_bricks = []
# expl_bricks = []

def clear_all_bricks():
    global lvl1_bricks
    global lvl2_bricks
    global lvl3_bricks
    global nond_bricks
    global expl_bricks
    lvl1_bricks = []
    lvl2_bricks = []
    lvl3_bricks = []
    nond_bricks = []
    expl_bricks = []



def level2_brick():

    global lvl1_bricks
    global lvl2_bricks
    global lvl3_bricks
    global nond_bricks
    global expl_bricks

    sample = level3_brick(34,5)
    lvl3_bricks.append(sample)
    sample = level3_brick(34,6)
    lvl3_bricks.append(sample)
    sample = level3_brick(34,7)
    lvl3_bricks.append(sample)
    sample = level3_brick(34,8)
    lvl3_bricks.append(sample)
    sample = level3_brick(34,9)
    lvl3_bricks.append(sample)
    sample = level3_brick(34,10)
    lvl3_bricks.append(sample)
    sample = level3_brick(34,11)
    lvl3_bricks.append(sample)
    sample = level3_brick(34,12)
    lvl3_bricks.append(sample)

    # # Column of level 2 bricks
    # sample = level2_brick(40,5)
    # lvl2_bricks.append(sample)
    # sample = level2_brick(40,6)
    # lvl2_bricks.append(sample)
    # sample = level2_brick(40,7)
    # lvl2_bricks.append(sample)
    # sample = level2_brick(40,8)
    # lvl2_bricks.append(sample)
    # sample = level2_brick(40,9)
    # lvl2_bricks.append(sample)
    # sample = level2_brick(40,10)
    # lvl2_bricks.append(sample)
    # sample = level2_brick(40,11)
    # lvl2_bricks.append(sample)
    # sample = level2_brick(40,12)
    # lvl2_bricks.append(sample)

    # Column of level 1 bricks
    sample = level1_brick(46,5)
    lvl1_bricks.append(sample)
    sample = level1_brick(46,6)
    lvl1_bricks.append(sample)
    sample = level1_brick(46,7)
    lvl1_bricks.append(sample)
    sample = level1_brick(46,8)
    lvl1_bricks.append(sample)
    sample = level1_brick(46,9)
    lvl1_bricks.append(sample)
    sample = level1_brick(46,10)
    lvl1_bricks.append(sample)
    sample = level1_brick(46,11)
    lvl1_bricks.append(sample)
    sample = level1_brick(46,12)
    lvl1_bricks.append(sample)

    # Column of non-detructible bricks
    sample = non_destructible_brick(58,5)
    nond_bricks.append(sample)
    sample = non_destructible_brick(58,6)
    nond_bricks.append(sample)
    sample = non_destructible_brick(58,7)
    nond_bricks.append(sample)
    sample = non_destructible_brick(58,8)
    nond_bricks.append(sample)
    sample = non_destructible_brick(58,9)
    nond_bricks.append(sample)
    sample = non_destructible_brick(58,10)
    nond_bricks.append(sample)
    sample = non_destructible_brick(58,11)
    nond_bricks.append(sample)
    sample = non_destructible_brick(58,12)
    nond_bricks.append(sample)

    # Column of level 1 bricks
    sample = level1_brick(70,5)
    lvl1_bricks.append(sample)
    sample = level1_brick(70,6)
    lvl1_bricks.append(sample)
    sample = level1_brick(70,7)
    lvl1_bricks.append(sample)
    sample = level1_brick(70,8)
    lvl1_bricks.append(sample)
    sample = level1_brick(70,9)
    lvl1_bricks.append(sample)
    sample = level1_brick(70,10)
    lvl1_bricks.append(sample)
    sample = level1_brick(70,11)
    lvl1_bricks.append(sample)
    sample = level1_brick(70,12)
    lvl1_bricks.append(sample)

    # # Column of level 2 bricks
    # sample = level2_brick(76,5)
    # lvl2_bricks.append(sample)
    # sample = level2_brick(76,6)
    # lvl2_bricks.append(sample)
    # sample = level2_brick(76,7)
    # lvl2_bricks.append(sample)
    # sample = level2_brick(76,8)
    # lvl2_bricks.append(sample)
    # sample = level2_brick(76,9)
    # lvl2_bricks.append(sample)
    # sample = level2_brick(76,10)
    # lvl2_bricks.append(sample)
    # sample = level2_brick(76,11)
    # lvl2_bricks.append(sample)
    # sample = level2_brick(76,12)
    # lvl2_bricks.append(sample)

    # Column of level 3 bricks
    sample = level3_brick(82,5)
    lvl3_bricks.append(sample)
    sample = level3_brick(82,6)
    lvl3_bricks.append(sample)
    sample = level3_brick(82,7)
    lvl3_bricks.append(sample)
    sample = level3_brick(82,8)
    lvl3_bricks.append(sample)
    sample = level3_brick(82,9)
    lvl3_bricks.append(sample)
    sample = level3_brick(82,10)
    lvl3_bricks.append(sample)
    sample = level3_brick(82,11)
    lvl3_bricks.append(sample)
    sample = level3_brick(82,12)
    lvl3_bricks.append(sample)

    #Column 1 including explosive bricks
    sample = explosive_brick(0,5)
    expl_bricks.append(sample)
    sample = level1_brick(0,6)
    lvl1_bricks.append(sample)
    sample = level2_brick(0,7)
    lvl2_bricks.append(sample)
    sample = non_destructible_brick(0,8)
    nond_bricks.append(sample)
    sample = non_destructible_brick(0,9)
    nond_bricks.append(sample)
    sample = level2_brick(0,10)
    lvl2_bricks.append(sample)
    sample = level1_brick(0,11)
    lvl1_bricks.append(sample)
    sample = explosive_brick(0,12)
    expl_bricks.append(sample)

    #Column 2 including explosive bricks
    sample = non_destructible_brick(6,5)
    nond_bricks.append(sample)
    sample = explosive_brick(6,6)
    expl_bricks.append(sample)
    sample = level1_brick(6,7)
    lvl1_bricks.append(sample)
    sample = level2_brick(6,8)
    lvl2_bricks.append(sample)
    sample = level2_brick(6,9)
    lvl2_bricks.append(sample)
    sample = level1_brick(6,10)
    lvl1_bricks.append(sample)
    sample = explosive_brick(6,11)
    expl_bricks.append(sample)
    sample = non_destructible_brick(6,12)
    nond_bricks.append(sample)

    #Column 3 including explosive bricks
    sample = non_destructible_brick(108,5)
    nond_bricks.append(sample)
    sample = explosive_brick(108,6)
    expl_bricks.append(sample)
    sample = level1_brick(108,7)
    lvl1_bricks.append(sample)
    sample = level2_brick(108,8)
    lvl2_bricks.append(sample)
    sample = level2_brick(108,9)
    lvl2_bricks.append(sample)
    sample = level1_brick(108,10)
    lvl1_bricks.append(sample)
    sample = explosive_brick(108,11)
    expl_bricks.append(sample)
    sample = non_destructible_brick(108,12)
    nond_bricks.append(sample)

    #Column 4 including explosive bricks
    sample = explosive_brick(114,5)
    expl_bricks.append(sample)
    sample = level1_brick(114,6)
    lvl1_bricks.append(sample)
    sample = level2_brick(114,7)
    lvl2_bricks.append(sample)
    sample = non_destructible_brick(114,8)
    nond_bricks.append(sample)
    sample = non_destructible_brick(114,9)
    nond_bricks.append(sample)
    sample = level2_brick(114,10)
    lvl2_bricks.append(sample)
    sample = level1_brick(114,11)
    lvl1_bricks.append(sample)
    sample = explosive_brick(114,12)
    expl_bricks.append(sample)
