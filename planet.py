import sys
from Graph import *
import numpy as np

# check number of stations
def check_station_num(n):
    if n < 1 or n > 200:
        print('Stations are out of range')
        sys.exit()
        
# check coordinates
def check_coordenates(coordenates):
    if not (len(coordenates) == 3):
        print('Number of coordinates are wrong')
        sys.exit()
    for i in range(len(coordenates)):
        if not (coordenates[i] >= -10000 and coordenates[i] <= 10000):
            print('One or more coordenates are out of range')
            sys.exit()


def planet(file_input):
    
    text = open(file_input).read().split('\n')
    line = text[0].split()
    
    earth=[0.00, 0.00, 0.00]
    # get zearth coordenates
    zearth = [float(a) for a in line]
    check_coordenates(zearth)
    station_num = int(text[1])
    check_station_num(station_num)
    station_list = []
    station_list.append(earth)
    station_list.append(zearth)
    
    #stations coordinates
    for line in text[2:]:
        l = line.split()
        station = [float(a) for a in l]
        check_coordenates(station)
        station_list.append(station)
    
    # construction of the graph with origin and end point
    graph = Graph(station_num +2)
    
    def get_distance(x, y):
        distance = ((x[0] - y[0])**2 + (x[1] - y[1])**2 + (x[2] - y[2])**2)**0.5
        return distance
    
    # creating the graph with the weight and edges of the nodes
    for i,n1 in enumerate(station_list):
        for j,n2 in enumerate(station_list): 
            if (i > j) and (i != j):
                weight = get_distance(n1, n2)
                graph.add_edge(i, j, weight)
    
    res = graph.find_MST()
    
    path = graph.find_shortest_path(0, 1, res)
    
    max_weight = graph.get_max_weight(path)
    
    print('OUTPUT -> ', np.round(max_weight, 2))
    
planet('planet_test1.txt')
planet('planet_test2.txt')
