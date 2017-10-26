import copy
import random

class SimGame:

  def __init__(self):
    self.game_finished      = False
    self.winner         = -1
    self.player_color   = -1
    self.computer_color = -1
    self.move_counter = 0

    # Graph
    self.nodes = ["A","B","C","D","E","F","G","H"]
    # node -> [[red edges],[blue edges]]
    self.graph = { node : [[],[]] for node in self.nodes }

  # Draw an edge from a to b and b to a
  def add_edge(self, a, b, color,graph):
    graph[a][color].append(b)
    graph[b][color].append(a)

def get_legal_moves(self, color,graph):
  assert color == 0 or color == 1, "invalid color: %d" % color

  valid_list = []
  for node1 in self.nodes:
    for node2 in self.nodes:
      if node1 != node2:
        if self.validate_move(node1, node2, color,graph):#checks if
        #move is valid
          if (node1, node2) not in valid_list:
            valid_list.append((node1, node2))

  return valid_list

  # Determine whether a given move is valid
  def validate_move(self, a, b, color,graph):
    assert color == 0 or color == 1, "invalid color: %d" % color
    assert a in self.nodes, "invalid node a: %s" % a
    assert b in self.nodes, "invalid node b: %s" % b

    # Check if edge already exists
    if a == b: # Check for equality
      return False
    if a in graph[b][0]: # Check if a is a red edge with b
      return False
    if a in graph[b][1]: # Check if a is a blue edge with b
      return False
    if b in graph[a][0]: # Check if b is a red edge with a
      return False
    if b in graph[a][1]: # Check if b is a red edge with a
      return False

    # Check if edge would cause a triangle
    for connected_neighbor in graph[a][color]:
      if b in graph[connected_neighbor][color]:
        return False
    for connected_neighbor in graph[b][color]:
      if a in graph[connected_neighbor][color]:
        assert 0==1, "impossible case definitely should never happen"
        return False

    return True # Edge does not exist, the move is valid





  def pick_move(self, possible_moves):
    # assert len(possible_moves) > 0, "Error, no possible moves"
    # return possible_moves[0]
    cutoff_moves = [5,10,12]
    depths = [2,4,6]
    depth_to_use = 6
    for i in range(len(cutoff_moves)):
        if self.move_counter <= cutoff_moves[i]:
            depth_to_use = depths[i]
            break
    return self.get_move_ab(depth_to_use)

  def alpha_beta_search(self,depth,alpha,beta,color,graph):
    if depth == 0:
      return len(self.get_legal_moves(color,graph))
    if color == self.computer_color:
      v = -float('inf')
      children = self.get_legal_moves(color,graph)
      for child in children:
        new_graph = copy.deepcopy(graph)
        self.add_edge(child[0],child[1],color,new_graph)
        v = max(v,self.alpha_beta_search(depth-1,alpha,beta,not color,\
        new_graph))
        alpha = max(alpha,v)
        if beta <= alpha:
          break
      return v
    else:
      v = float('inf')
      children = self.get_legal_moves(color,graph)
      for child in children:
        new_graph = copy.deepcopy(graph)
        self.add_edge(child[0],child[1],color,new_graph)
        v = min(v,self.alpha_beta_search(depth-1,alpha,beta,not color,\
        new_graph))
        beta = min(beta,v)
        if beta <= alpha:
          break
      return v

  def get_move_ab(self,depth):
    print("depth",depth)
    children = self.get_legal_moves(self.computer_color,self.graph)
    random.shuffle(children)
    ab_values = []
    for child in children:
      ab_values.append(self.alpha_beta_search(depth,-float('inf'),\
      float('inf'),self.player_color,self.graph))
      #want to start alpha beta a level down so we don't have to pass the
      #optimal path back through the tree
      #instead we just return the move that gives the maximum  value
    max_index = max(ab_values)
    print(children[ab_values.index(max_index)])
    return children[ab_values.index(max_index)]


  def make_move(self, color):
    assert color == 0 or color == 1, "invalid color: %d" % color

    possible_moves = self.get_legal_moves(color,self.graph)

    # Check if game is over
    if len(possible_moves) == 0:
      self.game_finished = True
      self.winner = 1 - color

    # Make a move
    move = self.pick_move(possible_moves)
    self.add_edge(move[0], move[1], color, self.graph)

  def get_player_move(self):
    print("Valid Moves for %s: %s", self.player_color, self.get_legal_moves(self.player_color,self.graph))
    move = input("Please enter a move in the form Edge1,Edge2: ")
    move = move.split(",")
    self.move_counter += 1
    while True:
      while not self.validate_move(move[0], move[1], self.player_color, self.graph):
        print("Invalid move, cannot draw edge %s <--> %s for color %s" % (move[0], move[1], "Blue" if self.player_color else "Red"))
        move = input("Please enter a different move in the form Edge1,Edge2: ")
        move = move.split(",")
        continue
      break
    return move[0], move[1]

  def get_player_color(self):
    print("Enter 0 to play as Red, 1 to play as Blue: ", end='', flush=True)
    self.player_color = int(input())
    while (self.player_color != 0) and (self.player_color != 1):
      print("Invalid Input, enter 0 to play as Red, 1 to play as Blue: ", end='', flush=True)
      self.player_color = int(input())
    self.computer_color = 1 - self.player_color
    print("Player Color: %s" % ("Blue" if self.player_color else "Red"))
    print("Computer Color: %s" % ("Blue" if self.computer_color else "Red"))




  def game_loop(self):
    self.get_player_color()

    while not self.game_finished:
      print("Red move")
      if len(self.get_legal_moves(0,self.graph)) == 0:
        print("No valid moves for Red")
        self.winner = 1
        break
      if not self.player_color:
        a, b = self.get_player_move()#ask for player input
        self.add_edge(a, b, self.player_color, self.graph)
      else:
        self.make_move(self.computer_color)#make move for computer

      print("Blue move")
      if len(self.get_legal_moves(1,self.graph)) == 0:
        print("No valid moves for Blue")
        self.winner = 0
        break
      if self.player_color:
        a, b = self.get_player_move()#ask for player input
        self.add_edge(a, b, self.player_color, self.graph)
      else:
        self.make_move(self.computer_color)#make move for computer

    print("Game over. %s wins!" % "Blue" if self.winner else "Red")









s = SimGame()
s.game_loop()
