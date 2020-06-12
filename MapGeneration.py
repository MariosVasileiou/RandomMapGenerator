import numpy as np
import random as r
import matplotlib.pyplot as plt

# =========================== Variable Declaration ===========================

# Map size (Rectangle)
size = 100
# TODO Obstacle percentage
o_per = 40
current_o_per = 0
current_o_sum = 0
# Robotic System size (Rectangle)
robot_size = 3

# Empty Map
map = np.zeros((size, size))

# Minimum Obstacle size
minim = 3

# === Maximum Obstacle size ===

# Rectangle
rect_m_size = 11
# Vertical Parallelogram
vPar_x_m_size = 61
vPar_y_m_size = 3
# Horizontal Parallelogram
hPar_x_m_size = 3
hPar_y_m_size = 61
# Parallelogram x, y minimum difference
p_min = 10

# List of obstacles
obs_list = []

boarder_width = 2
minimum_se_distance = 30

# =========================== Random Obstacle creation ===========================

# Initial point
# todo set Initial point (different value or..)

# goal point
# todo set goal point (different value or..)


# Rectangle
def rectangle():
    while True:
        s = r.randrange(minim, rect_m_size + 1, 2)

        x = r.randrange(s // 2, (size-1) - s // 2)
        y = r.randrange(s // 2, (size-1) - s // 2)

        if available(x, y, s, s):
            break


# Vertical Parallelogram
def v_parallelogram():
    while True:
        sx = r.randrange(vPar_y_m_size + p_min, vPar_x_m_size + 1, 2)
        sy = r.randrange(1, vPar_y_m_size + 1, 2)

        x = r.randrange(sx // 2, (size-1) - sx // 2)
        y = r.randrange(sy // 2, (size-1) - sy // 2)

        if available(x, y, sx, sy):
            break


# Horizontal Parallelogram
def h_parallelogram():
    while True:
        sy = r.randrange(hPar_x_m_size + p_min, hPar_y_m_size + 1, 2)
        sx = r.randrange(1, hPar_x_m_size + 1, 2)

        x = r.randrange(sx // 2, (size-1) - sx // 2)
        y = r.randrange(sy // 2, (size-1) - sy // 2)

        if available(x, y, sx, sy):
            break


# =========================== Class for the Obstacle List ===========================

class Obstacle:
    def __init__(self, x, y, sx, sy):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy


# =========================== Class for the Obstacle List ===========================


class Map:
    def __init__(self, map, start, end):
        self.map = map
        # start and end points
        self.start = start
        self.end = end


# =========================== Check Availability ===========================

def available(x, y, sx, sy):
    for k in obs_list:
        # if it is below or above the obstacle
        if (k.x + k.sx // 2 + robot_size) < (x - sx // 2) or (k.x - k.sx // 2 - robot_size) > (x + sx // 2):
            continue
        # if it is right or left of the obstacle
        elif (k.y + k.sy // 2 + robot_size) < (y - sy // 2) or (k.y - k.sy // 2 - robot_size) > (y + sy // 2):
            continue
        else:
            return False
    # If it leaves the for loop it means that it can be placed
    # Adds the obstacle to the list and returns true
    obs_list.append(Obstacle(x, y, sx, sy))

    for i in range(x - sx // 2, x + sx // 2 + 1):
        for j in range(y - sy // 2, y + sy // 2 + 1):
            map[i][j] = 1

    global current_o_sum
    current_o_sum = current_o_sum + sx * sy

    return True


# =========================== Map initialize Obstacle fill ===========================

# Creates a boarder
def init_fill():
    global boarder_width
    for i in range(0, size):
        for j in range(0, boarder_width):
            map[i][j] = 1
            map[j][i] = 1
            map[(size-1) - j][i] = 1
            map[i][(size-1) - j] = 1

    global current_o_sum
    current_o_sum = current_o_sum + size * boarder_width * 4


x_s = 0
y_s = 0
x_g = 0
y_g = 0


# for the boarders
def init_doors():
    bezels_input_length = 11
    bezels_output_length = 5
    bezels_width = 2

    global x_s
    global y_s
    global x_g
    global y_g

    # xy_start
    x_s = r.randrange(0, size, (size-1))  # x_s is 0 or 99
    y_s = r.randrange(0 + bezels_input_length // 2, 100 - bezels_input_length // 2)

    # xy_goal
    x_g = (size-1) - x_s
    y_g = r.randrange(0 + bezels_output_length // 2, 100 - bezels_output_length // 2)

    # Entrance
    b = bool(r.getrandbits(1))
    if b:
        # Up or down
        for i in range((x_s // (size-1)) * (x_s - bezels_width + 1), bezels_width + (x_s // (size-1)) * (x_s - bezels_width + 1)):
            for j in range(y_s - bezels_input_length // 2, y_s + bezels_input_length // 2 + 1):
                map[i][j] = 0
        obs_list.append(Obstacle(x_s, y_s, bezels_width, bezels_input_length))
        # print("Input , Up/Down : x=", x_s, "y=", y_s, "x_len=", bezels_width, "y_len=", bezels_input_length)
        print("x_s=", x_s, "y_s=", y_s)
    else:
        # Left or Right
        for i in range((x_s // (size-1)) * (x_s - bezels_width + 1), bezels_width + (x_s // (size-1)) * (x_s - bezels_width + 1)):
            for j in range(y_s - bezels_input_length // 2, y_s + bezels_input_length // 2 + 1):
                map[j][i] = 0
        obs_list.append(Obstacle(y_s, x_s, bezels_input_length, bezels_width))
        # print("Input , Left/ Right : x=", y_s, "y=", x_s, "x_len=", bezels_input_length, "y_len=", bezels_width)
        temp = x_s
        x_s = y_s
        y_s = temp
        print("x_s=", x_s, "y_s=", y_s)


    # Exit
    b = bool(r.getrandbits(1))  # This defines the orientation of the doors
    if b:
        # Up or down
        for i in range((x_g // (size-1)) * (x_g - bezels_width + 1), bezels_width + (x_g // (size-1)) * (x_g - bezels_width + 1)):
            for j in range(y_g - bezels_output_length // 2, y_g + bezels_output_length // 2 + 1):
                map[i][j] = 0
        obs_list.append(Obstacle(x_g, y_g, bezels_width, bezels_output_length))
        # print("Input , Up/Down : x=", x_g, "y=", y_g, "x_len=", bezels_width, "y_len=", bezels_output_length)
        print("x_g=", x_g, "y_g=", y_g)
    else:
        # Left or Right
        for i in range((x_g // (size-1)) * (x_g - bezels_width + 1), bezels_width + (x_g // (size-1)) * (x_g - bezels_width + 1)):
            for j in range(y_g - bezels_output_length // 2, y_g + bezels_output_length // 2 + 1):
                map[j][i] = 0
        obs_list.append(Obstacle(y_g, x_g, bezels_output_length, bezels_width))
        # print("Input , Left/ Right : x=", y_g, "y=", x_g, "x_len=", bezels_output_length, "y_len=", bezels_width)
        temp = x_s
        x_s = y_s
        y_s = temp
        print("x_g=", x_g, "y_g=", y_g)


# Initialization of Start, End points
def init_se():
    global x_s
    global y_s
    global x_g
    global y_g

    # xy_start
    x_s = r.randrange(boarder_width, (size-1) - boarder_width)
    y_s = r.randrange(boarder_width, (size-1) - boarder_width)

    # xy_goal
    while True:
        x_g = r.randrange(boarder_width, (size-1) - boarder_width)
        y_g = r.randrange(boarder_width, (size-1) - boarder_width)
        if (abs(x_s - x_g) + abs(y_s - y_g) >= minimum_se_distance):
            break;

    # size of point = 1s
    obs_list.append(Obstacle(x_s, y_s, 1, 1))
    obs_list.append(Obstacle(x_g, y_g, 1, 1))
    print("x_s=", x_s, "y_s=", y_s)
    print("x_g=", x_g, "y_g=", y_g)


startL = [[0, 0]]
endL = [[0, 0]]


def init_mult_se(n_points):

    global startL
    global endL
    startL = [[0 for x in range(2)] for y in range(n_points)]
    endL = [[0 for x in range(2)] for y in range(n_points)]

    for i in range(0, n_points):
        # xy_start
        startL[i][0] = r.randrange(boarder_width, (size - 1) - boarder_width)
        startL[i][1] = r.randrange(boarder_width, (size - 1) - boarder_width)

        # xy_goal
        while True:
            endL[i][0] = r.randrange(boarder_width, (size - 1) - boarder_width)
            endL[i][1] = r.randrange(boarder_width, (size - 1) - boarder_width)
            if (abs(startL[i][0] - endL[i][0]) + abs(startL[i][1] - endL[i][1]) >= minimum_se_distance):
                break;

        # size of point = 1s
        obs_list.append(Obstacle(startL[i][0], startL[i][1], 1, 1))
        obs_list.append(Obstacle(endL[i][0], endL[i][1], 1, 1))

    print(startL)
    print(endL)


# =========================== Return Map ===========================

def getMap(n_points):
    global map
    global obs_list
    global current_o_per
    global current_o_sum

    map = np.zeros((size, size))
    obs_list = []
    current_o_per = 0
    current_o_sum = 0

    func_list = [rectangle, v_parallelogram, h_parallelogram]
    init_fill()

    init_mult_se(n_points)



    for i in range(0, 50):
        r.choice(func_list)()  # Runs a random function

    a = Map(map, startL, endL)

    return a

    #plt.imshow(a.map, cmap='binary');
    #plt.show()


# =========================== Main Function ===========================

def main():
    func_list = [rectangle, v_parallelogram, h_parallelogram]

    init_fill()

    init_doors()

    global map
    global obs_list
    while True:
        # print(obs_list[0].x)
        # print(obs_list[1].x)
        for i in range(0, 50):
            r.choice(func_list)()  # Runs a random function
        global current_o_per
        global current_o_sum
        current_o_per = int(100 * current_o_sum / (size ** 2))
        print("Obstacle persentage", current_o_per, "%")

        sum = 0
        for i in range(0, size):
            for j in range(0, size):
                if map[i][j] == 1:
                    sum = sum + 1

        print("the real percentage is:", 100 * sum / (size ** 2), "%")

        plt.imshow(map, cmap='binary');
        plt.show()

        # Next Map
        print("Next Map")
        map = np.zeros((size, size))
        obs_list = []
        current_o_per = 0
        current_o_sum = 0
        init_fill()
        init_doors()


# getMap()
if __name__ == '__main__':
    main()
