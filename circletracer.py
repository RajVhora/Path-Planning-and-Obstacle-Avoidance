# Algorithm
# Accept all points and obstacles
# Start with first point..
# Check if path from first point to second lies through any circle(obstacle)
# if not go straight
# else
#   Make a list of obstacles..
#   go to intersection of first obst and line
#   grace circle until second intersection point
#   go straight again until next circle and line intersection (repeat from 6)
# (You must get till end by this and repeat this for all start-end pairs)

import pygame
import math
import sys
import random
from math import *
from pygame import *
from CircletraceSolver import Solver

blue = 0, 0, 255
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 0
cyan = 0, 180, 105
maroon = 119, 27, 7

obst1 = [325, 300, 50]
obst2 = [435, 300, 25]
obst3 = [575, 250, 50]
obst4 = [600, 400, 45]
obst = [obst1, obst2, obst3, obst4]
path = []
gr = 10     #Grace Radius variables

screen = pygame.display.set_mode((900, 600))


def init_obstacles():  # Later run in for loop
    for q in obst:
        pygame.draw.circle(screen, green, q[0:2], q[2]+gr, 0)
        pygame.draw.circle(screen, maroon, q[0:2], q[2], 0)
        q[2] = q[2] + 10
        

def reset():
    screen.fill((240, 240, 0))
    init_obstacles()
    pygame.display.update()
    print("resetting")


def dist_between(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

def sortedobstacles(obstacles, start):
    distances = []
    for o in obstacles:
        d = dist_between(o, start)
        distances.append(d)
    distances1 = sorted(distances)
    sl = []
    for i in range(0, len(obstacles)):
        sl.append(obstacles[distances.index(distances1[i])])
    return sl


def f(p,q,x1,y1,x2,y2):
	t = ((y1-q)*(y2-y1)+(x2-x1)*(x1-p))*((y2-q)*(y2-y1)+(x2-x1)*(x2-p))
	if t<0:
		return True
	else:
		return False

def inmypath(obst,s,e):
	trouble = []
	for o in obst:
		if(f(o[0],o[1],s[0],s[1],e[0],e[1]) == False):
			print(o,"NOT OBSTACLE")
		else :
			distance = ((e[1]-s[1])*o[0] - (e[0]-s[0])*o[1] + e[0]*s[1] - e[1]*s[0])/dist_between(s,e)
			if(abs(distance)<o[2]):
				print(o,"As OBSTACLE")
				trouble.append(o)
	return trouble

def findpath(start, end):
    global obst,gr
    sol = Solver()
    obstacles = inmypath(obst, start, end)
    path = [start]
    if len(obstacles) > 0:
        obstacles = sortedobstacles(obstacles, start)
        for i in obstacles:
            dangle = floor(acos((i[2] - gr)/i[2])*180/pi)
            temp = sol.Solver(i, path[-1], end,dangle)
            path = path + temp
    path.append(end)
    path = refine(path,obstacles)
    if len(obstacles) == 0:
        path.append(end)
    return path

def lastpt(path,obstacles,start):
    for i in path[::-1]:
        thisisgood = True
        obst = inmypath(obstacles,start,i)
        for j in obstacles:
            if j in obst:
                thisisgood = False
                break
        if thisisgood:
            return i

def refine(path,obstacles):
    refinedpath = [path[0]]
    startpt = path[0]
    startptidx = 0
    while(startpt is not path[-1]):
        lastpoint = lastpt(path[startptidx:],obstacles,refinedpath[-1])
        refinedpath.append(lastpoint)
        startpt = lastpoint
        startptidx = path.index(startpt)
    return refinedpath


screen.fill((240, 240, 0))
init_obstacles()
pygame.display.update()

goalset = 0
destiny = []
n = int(input("Enter the number of waypoints to visit:"))
while True:
    while goalset < n:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = event.pos
                print(position)
                destiny.append(position)
                if goalset == 0:
                    start = position
                pygame.draw.circle(screen, red, position, 6, 0)
                pygame.display.update()
                goalset += 1
            if event.type == pygame.QUIT:
                pygame.quit()
    for i in range(0, len(destiny)-1):
        path = findpath(destiny[i], destiny[i+1])
        print(path)
        for i in range(len(path)-1):
            pygame.draw.line(screen, cyan, path[i], path[i+1])
            pygame.display.update()
    goalset = 0
    destiny = []
