import os
import random

def get_users():

    users = {}

    count = 1
    mouse = "Mouse//"
    keyboard = "Keyboard//"

    mouse_files = os.listdir(mouse)
    key_files = os.listdir(keyboard)

    for i in mouse_files:

        users["User "+str(count)] = []

        if "bot" in i:
            users["User "+str(count)].append(80)
        else:
            users["User "+str(count)].append(10)

        with open(mouse+i) as f:

            lines = f.readlines()

            x = []
            y = []

            for j  in lines:
                x.append(int(j.split(" ")[0]))
                y.append(int(j.split(" ")[1]))

        users["User "+str(count)].append([x, y])

        count = count+1

    count = 1

    for i in key_files:

        with open(keyboard+i) as f:

            lines = f.readlines()

            coordinates = []

            for j in lines:
                splits = j.split(", ")
                for k in range(1, len(splits), 2):
                    coordinates.append(float(splits[k][:-2]))

        users["User "+str(count)].append(coordinates)

        count = count+1

    return users
