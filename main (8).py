#yo. this is a harry potter spell inspired project. in this project you can enter a spell name(incantation) into the code ting and it will return with its  name(its english name), effect, and what light source it emits. EX: user enters: Aguamenti, and the code returns: name: Water-Making Spell, effect: Conjures water, light: Icy blue.


#im focused on the schedule project rn so i havent exactly fine tunned this project
import csv
#has an attribute called "data" that stores the value of the node and "next_node" that points to the next node in the list. has methods to initialize the node, and return its string  
class Node:
  def __init__(self, data):
    self.data = data
    self.next_node = None

  def __repr__(self):
    return str(self.data)

#has an attribute called "head" that points to the first node in the list and "num_of_nodes" that stores the number of nodes in the list. has methods to insert nodes at the start, end, or after a given node in the list, and to traverse the list. also has methods to return the number of nodes in the list.
class LinkedList:
  def __init__(self):
    self.head = None
    self.num_of_nodes = 0

  def __iter__(self):
    node = self.head
    while node is not None:
      yield node
      node = node.next_node

  def get_num_of_nodes(self):
    return self.num_of_nodes

  def insert_at_start(self, data):
    self.num_of_nodes += 1
    new_node = Node(data)
    new_node.next_node = self.head
    self.head = new_node

  def insert_at_end(self, data):
    self.num_of_nodes += 1
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      temp_node = self.head
      while temp_node.next_node is not None:
        temp_node = temp_node.next_node
      temp_node.next_node = new_node

  def insert_after(self, node, data):
    self.num_of_nodes += 1
    new_node = Node(data)
    temp_node = self.head
    while temp_node is not None and temp_node.data != node:
      temp_node = temp_node.next_node
    if temp_node is None:
      return
    new_node.next_node = temp_node.next_node
    temp_node.next_node = new_node

  # Same as iter but prints out every node
  def traverse(self):
    current_node = self.head
    while current_node is not None:
      print(current_node)
      current_node = current_node.next_node

  def __repr__(self):
    list = []
    temp_node = self.head
    while temp_node is not None:
      list.append(temp_node.data)
      temp_node = temp_node.next_node
    return str(list)

#has attributes called "data" that stores the value of the node, "left_node" that points to the left child of the node, "right_node" that points to the right child of the node, and "parent" that points to the parent of the node. initializes the node and returns its string
class bst_node:
  # creates a new node and sets the next node to be none
  def __init__(self, data, parent=None):
    self.data = data
    self.left_node = None
    self.right_node = None
    self.parent = None

  # returns the string representation of the node
  def __repr__(self):
    return str(self.data)


    
#has an attribute that points to the root node of the tree. has methods to insert nodes into the tree, traverse the tree in order, find the minimum and maximum value in the tree, and search for a node in the tree.
class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, data):
    if self.root is None:
      self.root = bst_node(data)
    else:
      self.insert_node(data, self.root)

  def insert_node(self, data, node):
    if data.incantation.lower() < node.data.incantation.lower():
      if node.left_node is not None:
        self.insert_node(data, node.left_node)
      else:
        node.left_node = bst_node(data, node)
    else:
      if node.right_node is not None:
        self.insert_node(data, node.right_node)
      else:
        node.right_node = bst_node(data, node)

  def traverse(self):
    if self.root is not None:
      self.traverse_in_order(self.root)

  def get_min(self):
    temp = self.root
    while temp.left_node is not None:
      temp = temp.left_node
    return temp

  def get_max(self):
    temp = self.root
    while temp.right_node is not None:
      temp = temp.right_node
    return temp

  def search(self, data, root):
    if data == root.data.num:
      return root
    elif data < root.data.num:
      return self.search(data, root.left_node)
    else:
      return self.search(data, root.right_node)


#It has a constructor that initializes the head_node and num_of_nodes as None and 0. It also has several methods such as push, pop, and peak.
class Stack:
  
  def __init__(self):
    self.head_node = None
    self.num_of_nodes = 0
    
  def __iter__(self):
    node = self.head_node
    while node is not None:
      yield node
      node = node.next

  def stack_num_of_nodes(self):
    return self.num_of_nodes
    
  def push(self, data):
    self.num_of_nodes += 1
    new_node = Node(data)
    if self.head_node is None:
      self.head_node = new_node
    else:
      new_node.next_node = self.head_node
      self.head_node = new_node

  def pop(self):
    self.num_of_nodes -= 1
    remove = self.head_node
    self.head_node = self.head_node.next_node
    return remove.data
    
  def peak(self, i):
    temp_node = self.head_node
    if self.num_of_nodes > i:
      for x in range(i):
        temp_node = temp_node.next_node
      return temp_node.data



# It has a constructor that initializes the head_node, rear_node, and num_of_nodes as None, None, and 0. It also has several methods such as enqueue, dequeue, and traverse. The traverse method prints out every node in the queue.
class Queue:

  def __init__(self):
    self.head_node = None
    self.num_of_nodes = 0
    self.rear_node = None
      
  def __iter__(self):
    temp = self.head_node
    while temp is not None:
      yield temp
      temp = temp.next_node

  def get_num_of_nodes(self):
    return self.num_of_nodes

  def traverse(self):
    current_node = self.head_node  
    while current_node is not None:
      print(current_node)
      current_node = current_node.next_node
      
  def enqueue(self, data):
    self.num_of_nodes += 1
    new_node = Node(data)
    if self.head_node is None:
      self.head_node = new_node
    elif self.rear_node is None:
      self.rear_node = new_node
    else:
      self.rear_node.next_node = new_node
      self.rear_node = new_node

  def dequeue(self):
    if self.head_node is None:
      return None
    self.num_of_nodes -= 1
    temp_node = self.head_node
    self.head_node = temp_node.next_node
    if self.head_node is None:
      self.rear_node = None
    return temp_node.data

  #def __repr__(self):
    #return f"Queue: {list(self)}"

  def __repr__(self):
    nodes = []
    temp = self.head_node
    while temp is not None:
      nodes.append(str(temp.data))
      temp = temp.next_node
    return "Queue: ".join(nodes)






class Wizard:
  hogwarts_students = LinkedList()

  #
  def __init__(self, house, year):
    self.house = house
    self.year = year
    #self.upcoming_matches = Queue()
    self.spell_log = Stack()
    Wizard.hogwarts_students.add(self)
    
  #
  def __repr__(self):
    if self.light == "":
      return "name: " + self.name + ", effect: " + self.effect + ", light: no info for Light"
    else:
      return "name: " + self.name + ", effect: " + self.effect + ", light: " + self.light


  def print_spell_history(self, n):
    if n > self.spell_log.num_of_nodes:
      n = self.spell_log.num_of_nodes
    for i in range(n):
      print(self.spell_log.peak(i))

  #def add_match(quidditch_match):
    #self.upcoming_matches.enqueue(quidditch_match)

  


class Spell:
  all_spells_bst = BinarySearchTree()
  
  
  def __init__(self, ID, incantation, name, effect, light):
    self.ID = ID
    self.incantation = incantation
    self.name = name
    self.effect = effect
    self.light = light
    Spell.all_spells_bst.insert(self)

  def __repr__(self):
    if self.light == "":
      return "name: " + self.name + ", effect: " + self.effect + ", light: no info for Light"
    else:
      return "name: " + self.name + ", effect: " + self.effect + ", light: " + self.light

  @classmethod
  def import_spells(cls, filename: str):
    with open(filename, "r") as f:
      reader = csv.DictReader(f)
      items = list(reader)
    for item in items:
      Spell(
        ID = item.get('Spell ID'),
        incantation = item.get('Incantation'),
        name = item.get('Spell Name'),
        effect = item.get('Effect'), 
        light = item.get('Light'),
        )

class QuidditchMatch:
  upcoming_games = Queue()
  def __init__(self, game_date, opponent):
     self.game_date = game_date
     self.opponent = opponent
     QuidditchMatch.upcoming_games.enqueue(self)

  def __repr__(self):
    return f"Your next match will be on {self.game_date} against {self.opponent}"

     
     
class Line:
  all_spells_qu = Queue()
  
  def __init__(self, recent_user, first_user):
    
    self.recent_user = recent_user
    self.first_user = first_user
    Line.all_spells_qu.enqueue(self)

  
  def __repr__(self):
    return "most recent user: " + self.recent_user + ", first ever user: " + self.first_user

if __name__=="__main__":
  
  Spell.import_spells("Spells.csv")
  ticket1 = Line("Jacky", "Bob")
  print(Spell.all_spells_bst.get_min())
  print(Spell.all_spells_bst.get_max())
  print(Line.all_spells_qu.dequeue())
  Line.all_spells_qu.traverse()
  
  match1 = QuidditchMatch('2023-04-21', 'Slytherin')
  match2 = QuidditchMatch('2023-03-11', 'Gryffindor')
  match3 = QuidditchMatch('2023-02-01', 'Hufflepuff')
  
  QuidditchMatch.upcoming_games.traverse()
  QuidditchMatch.upcoming_games.dequeue()
    
  
  