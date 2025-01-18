class Treenode:
  def __init__(self,data):
      self.data = data
      self.leftchild = None
      self.rightchild = None


def insertnode(root,data):
  if root == None:
      return Treenode(data)
  else:
      if data < root.data:
          root.leftchild = insertnode(root.leftchild,data)
      else:
          root.rightchild = insertnode(root.rightchild,data)
  return root

def preordertraversal(node):
  if node != None:
      print(node.data,end = " ")
      preordertraversal(node.leftchild)
      preordertraversal(node.rightchild)

def inordertraversal(node):
  if node != None:
      inordertraversal(node.leftchild)
      print(node.data,end = " ")
      inordertraversal(node.rightchild)

def postordertraversal(node):
  if node != None:
      postordertraversal(node.leftchild)
      postordertraversal(node.rightchild)
      print(node.data,end = " ")

def search(node, key):
  print("Searching")
  if node.data == key:
      return node
  elif node.data < key and node.rightchild is not None:
      return search(node.rightchild, key)
  elif node.data > key and node.leftchild is not None:
      return search(node.leftchild, key)
  else:
      return -1
def delete(root,key):
  if root is None:
      return root
  if key < root.data:
      root.leftchild = delete(root.leftchild,key)
  elif key > root.data:
      root.rightchild = delete(root.rightchild,key)
  else:
      if root.leftchild is None:
          tmp = root.rightchild
          root = None
          return tmp
      elif root.rightchild is None:
          tmp = root.leftchild
          root = None
          return tmp
      else:
          tmp = inordersuccesor(root)
          print("Hello",tmp.data)
          t = root.data
          root.data = tmp.data
          tmp.data = t
          root.rightchild = delete(root.rightchild,tmp.data)
def inordersuccesor(root):
  current = root
  while current.leftchild is not None:
      current = current.leftchild
  return current
elements = int(input("How many elements would you like to add?: "))
tree = None
for i in range(elements):
  valuenode = int(input("Enter the value of the node: "))
  tree = insertnode(tree,valuenode)

preordertraversal(tree)

searchinput = int(input("What value are you searching for?: "))
found = search(tree, searchinput)

if found == -1:
  print("Value is not in the list")
else:
  print("Found item")