#I've based my code in the wikipedia A* pseudocode: 
# https://en.wikipedia.org/wiki/A*_search_algorithm


import math

def shortest_path(M, start, goal):
    
    points = M.intersections 
    #print(points)
    roads = M.roads
    #print(roads)
    
    closed_set = set()
    opened_set = set([start])
    node_number = len(points)
    
    came_from = {}
    
    g_Score = []
    f_Score = []
    
    for nodes in range(node_number):
        g_Score.append(999)
        f_Score.append(999)
        
    g_Score[start] = 0.0    
    f_Score[start] = distance_between_points(start, goal, points)
    
    connected_nodes = roads[start]
    
    while (len(opened_set) != 0 ):
        
        current_node = find_lowest_f (opened_set, f_Score) 
        
        if (current_node == goal):
            print ("Path Finded")
            
            print(reconstruct_path(came_from, current_node))
            return reconstruct_path(came_from, current_node)
            
        opened_set.remove(current_node)
        closed_set.add(current_node)
        
        neighbors_nodes = roads[current_node]
        
        for neighbor in neighbors_nodes:
            if neighbor in closed_set:
                continue
            
            if neighbor not in opened_set:
                opened_set.add(neighbor)
            
            tentative_g_Score = g_Score[current_node] + distance_between_points(current_node, neighbor, points)
    
            if tentative_g_Score >= g_Score[neighbor]:
                continue
            
            came_from[neighbor] = current_node
            g_Score[neighbor] = tentative_g_Score
            f_Score[neighbor] = g_Score[neighbor] + distance_between_points(neighbor, goal, points)

    return None



    #print (g_Score)
    #print (f_Score)
    
    
def reconstruct_path(came_from, current_node):
    total_path = [current_node]
    
    while (current_node in came_from.keys()):
        current_node = came_from[current_node]
        total_path.append(current_node)
    
    reversed_total_path = total_path[::-1]
    
    return reversed_total_path
    
    
    
def find_lowest_f(opened_set, f_Score):

    next_node = 0
    new_acum = 99999
    
    for node in opened_set:
        acum = f_Score[node] 
        if (new_acum > acum):
            new_acum = acum
            next_node = node
           
    return next_node



def distance_between_points(start, goal, points):
    x1, y1 = points[start]
    #print("x1: ", x1)
    #print("y1: ", y1)
    x2, y2 = points[goal]
    #print("x2: ", x2)
    #print("y2:", y2)    
    
    distance_value = math.sqrt( (x2 - x1) ** 2  + (y2 - y1) ** 2)
    
    return distance_value

