class Human :
  #Constructor
  def __init__(self, nm,wt = 0): #self refers to the object name
    self.no_of_hands = 2
    self.weight = wt
    self.name = nm
  def breathe(self):
    print(self.name + " is Breathing")


  def set_height(self, h):
    self.height = h

  def get_height(self):
    return self.height

  def set_age(self, a):
    self.age = a

  def get_age(self):
    return self.age

zach = Human("Zach", 5)
print(zach.no_of_hands, zach.weight)
zach.breathe()
zach.set_height(6)
zach.set_age(13) 
print( zach.get_height() )

after_5 = zach.get_age() + 5#age after 5 years

zach.set_age(after_5)

print(zach.get_age())

a = []

#first method
'''
for i in range(10):
    n = int(input("Enter a number: "))
    a.append(n)
'''

#second method
'''
info = list (map ( int, input("Enter the numbers: ").split(",") ))
print(info)

n = int(input("Enter the number you want to search in the list: "))

if n in info:
    for i in range(len(info)):
        if n == info[i]:
            print("{} found at {}".format(n, i+1))
'''

#binary search
#information must always be arranged! (increasing or decreasing order)

info = list (map ( int, input("Enter the numbers: ").split() ))
n = int(input("Enter the value you want to search: "))

start = 0
end = len(info) - 1
flag = False
while start <= end:
    mid = start+end//2
    if info[mid] == n:
        print("{} found at {}".format(n, mid+1))
        flag = True
        break
    elif n > info[mid]:
        start = mid+1
    elif n < info[mid]:
        end = mid-1

if flag == False:
    print("Value not present")