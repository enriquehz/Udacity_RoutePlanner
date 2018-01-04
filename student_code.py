import math
from helpers import show_map

def shortest_path(M,start,goal):
    
    set_explored = set()
    final_path = []
    heuristic_values = []
    frontier_values = []
    distances = {}
    
    print("shortest path called")
    
    final_path.append(start)
    set_explored.add(start)
    
    
    ########## MY TESTS ##########
    
    #show_map(M, start, goal)
    
    #print (distance_between_points(M.intersections[start],M.intersections[goal]))
    
    heuristic_values = get_heuristic_value(M, goal)
    #print (heuristic_values)
    
    frontier_values = get_frontier_intersections(start , M.roads)
    distances = adjacent_distances(M.intersections[start], frontier_values, M)
    #print (frontier_values)
    #print (distances)
    
    #print(calculate_h_function (distances, frontier_values, heuristic_values))
    
    
    next_intersection = calculate_h_function (distances, frontier_values, heuristic_values)

    final_path.append(next_intersection)
    ############################
    
    if (next_intersection not in set_explored):
    
        while (goal not in final_path):

            frontier_values = get_frontier_intersections(next_intersection , M.roads)
            distances = adjacent_distances(M.intersections[next_intersection], frontier_values, M)

            next_intersection = calculate_h_function (distances, frontier_values, heuristic_values)

            final_path.append(next_intersection)

        print(final_path)
    return final_path


def distance_between_points(point_1, point_2):
    
    distance_value = 0
    
    distance_value = math.sqrt( (point_2[1] - point_1[1]) ** 2  + (point_2[0] - point_1[0]) ** 2)
    
    return distance_value


# get the value of h (f = g + h) 

def get_heuristic_value (M, goal):
    
    heuristic_values = []
    
    for values in M.intersections:
        heuristic_values.append(distance_between_points(M.intersections[values],M.intersections[goal]))
    
    return heuristic_values


def get_frontier_intersections (current_intersection, roads):
    
    frontier_values = []
    
    frontier_values = roads[current_intersection]
    
    return frontier_values


# get the value of g (f = g + h) 

def adjacent_distances (current_intersection, frontier_values, M):
    
    adj_distance = {}
    
    for key in frontier_values:
        adj_distance[key] = distance_between_points(current_intersection, M.intersections[key])
        
    return adj_distance
       
    
def calculate_h_function (adjacent_distance, frontier_intersections, heuristic_values):
    
    shortest_path = []
    new_acum = 99
    
    for key in adjacent_distance:
        acum = heuristic_values[key] + adjacent_distance[key]
        #print(acum)
        if (new_acum > acum):
            new_acum = acum
            key_value = key
            #set_explored.add(key_value)
 
    #print(key_value)
    #print (new_acum)    
    return key_value
        
     
        
    
    
    