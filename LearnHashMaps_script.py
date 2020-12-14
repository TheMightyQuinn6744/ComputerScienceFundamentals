from linked_list import Node, LinkedList
from blossom_lib import flower_definitions 

class HashMap:
  def __init__(self,array_size):
    self.array_size = array_size 
    self.array = [LinkedList() for i in range(self.array_size)]

  def hash(self,key):
    self.key = key
    hash_code = sum(key.encode())

  def compress(self,hash_code):
    self.hash_code = hash_code 
    return hash_code % self.array_size

  def assign(self,key,value):
    array_index = self.compress(self.hash(key))
    self.array[array_index] = [key,value]

    payload = Node([key,value])
    list_at_index = self.array[array_index]

    for i in list_at_index:
      if key == item[0]:
        item[1] = value
      else:
        return None 

    for i in list_at_array:
      if key == item[0]:
        item[1] = value
      return
      
  def retrieve(self,key):
    self.key = key
    #creates hash code value for array indexing and saves value in array_index
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]

    if payload[0] == key:
      return payload[1]

    else:
      return None

#create instance of the HashMap named blossom
blossom = HashMap(len(flower_definitions))

for flower in flower_definitions:
  blossom.assign(flower[0],flower[1])

print(blossom.retrieve('daisy'))
