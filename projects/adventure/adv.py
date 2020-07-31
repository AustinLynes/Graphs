from room import Room
from player import Player
from world import World
from util import Queue
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()


# Fill this out with directions to walk
# traversal_path = ['n', 'n']

# create a function that can walk the entirerty of the load_graph
# the graph will need to know where to start.. and what rooms it can
# traverse...
# by holding onto the paths that have been traversed and the visited rooms
# we can look through the entire graph recursively
def walk(start, rooms, paths=None, visited=None):
    # on the first pass set the visited rooms to an empty list
    if visited == None:
        visited = []
    # same with the paths
    if paths == None:
        paths = {}
    # save the currrent rooms id for later lookup
    _id = start.id

    # if the id is not currently in our path
    if _id not in paths.keys():
        # add it to the visited
        visited.append(_id)
        # and create a position in our paths dict to hold it
        paths[_id] = {}
        # get all directions from the current room
        directions = start.get_exits()
        
        # for each of the avalable directions
        for dir in directions:
            # update the corrisponding room with its 
            # directions
            paths[_id].update({dir:start.get_room_in_direction(dir).id})
        
        # randomize the directions
        random.shuffle(directions)

        # for each direction avalable
        for dir in directions:
            # copy the room that this room points to based 
            # on the current direction
            _room = start.get_room_in_direction(dir)
            
            # walk to the correct room, knowing 
            # our visited, paths, and all rooms avalable
            walk(_room, rooms, paths, visited)
        
        # when our path fills up
        if len(paths)== len(rooms):
            # we are finished
            # return the paths and the visited rooms
            return paths, visited

# using breadth-first-search
# we can get the path from start to end of each of the 
# rooms we visit
def bfs(start, next, paths):
    # save the visited as a set
    visited = set()
    # create a Queue to handle Rooms
    room_q = Queue()
    # create a Queue to handle the directions
    dir_q  = Queue()

    # initalize the rooms queue with the first room
    room_q.enqueue([start])
    # initalize the directions queue... 
    # empty because we have not moved
    dir_q.enqueue([])

    # while the rooms queue has a room in it
    while room_q.size() > 0: 
        # grab the vertices path from the queue
        v_path = room_q.dequeue()
        # grab the directions path from the queue
        d_path = dir_q.dequeue()
        
        # the current vertex is the last one 
        v = v_path[-1]
        # if the vertex we grabbed is not in the visited list
        if v not in visited:
            # then add it
            visited.add(v)
            # and if the current vertex is the next 
            if v == next:
                # return the path created
                return d_path

            # for each direction in the current 
            # vertex path
            for dir in paths[v]:
                # copy the queues
                _path = v_path.copy()
                _dir_path = d_path.copy()

                # append the currently looked at
                # vertex && direction to the copied path
                _path.append(paths[v][dir])
                _dir_path.append(dir)
                
                # add the new data to be processed
                room_q.enqueue(_path)
                dir_q.enqueue(_dir_path)

traversal_path = []

# add the Player to the start room
player = Player(world.starting_room)

# walk the graph.. and save the
# the walked rooms --> rooms
# the visited rooms --> visited
rooms, visited = walk(world.starting_room, room_graph)

# for each entry in that has been visited
for i in range(len(visited)-1):
    # save the path it took to walk to that point
    path = bfs(visited[i], visited[i+1], rooms)
    # add it to our traversal_path 
    traversal_path.extend(path)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
