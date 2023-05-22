class Node:
  def __init__(self, compatibility, items):
    self.compatibility = compatibility
    self.items = items

def branch_and_bounds(C, n, k):
    c_min = 100
    i_min = 100
    j_min = 100
    N = []
    for element in range(n):
      N.append(element)

    for element in C:
        element_min = min(element)
        if element_min < c_min:
            c_min = element_min
            i_min = C.index(element)
            j_min = element.index(c_min)

    node = Node(c_min, [i_min, j_min])
    queue = [node]
    explored = []
    record = Node(100, [100, 100])
    iteration = 0
    while len(queue) > 0:
      iteration += 1
      Vcurrent = queue.pop(0)
      diff_indexes = difference(N, Vcurrent.items)
      children = []
      for index in diff_indexes:
        c = Vcurrent.compatibility
        for item in Vcurrent.items:
          c += C[item][index]
        child = []
        child = find_child(Vcurrent, index)
        children.append(Node(c, child))
      children = difference(children, explored)
      if len(children) > 0:
        if len(Vcurrent.items) + 1 == k:
          child_min = min(children, key = condition)
          if child_min.compatibility < record.compatibility:
            record = child_min
            queue = update_queue(queue, record)
          explored = explored + children
        else:
          for child in children:
            if child.compatibility < record.compatibility:
              queue.append(child)
          queue.sort(key=condition)
      explored.append(Vcurrent)
    
    
    return record.items          

def find_child(Vcurrent, index):
  temp = Vcurrent.items.copy()
  temp.append(index)
  temp.sort()
  return temp

def print_list(l):
  for item in l:
    print(item.items)
    print(item.compatibility)

def update_queue(queue, record):
  temp = []
  for item in queue:
    if(item.compatibility < record.compatibility):
      temp.append(item)
  return temp

def condition(node):
  return node.compatibility

def difference(a, b):
  temp = []
  for element in a:
    if element not in b:
      temp.append(element)
  return temp