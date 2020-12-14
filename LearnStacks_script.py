from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []

left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks += [left_stack, middle_stack, right_stack]

#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))

for disk in range(num_disks, 0, -1):
  left_stack.push(disk) 

num_optimal_moves = (2 ** disk) - 1 

print("\nThe fastest you can solve this game is in {0} moves".format(num_optimal_moves))

#Get User Input
def get__input__():
  choices = [stacks.get_name()[0] for stack in stacks]

  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {0} for {1}".format(letter,name))

    user_input = input("")

    if user_input in choices:
      for i in range(len(stacks)):
        return stacks[i]
  
        
#Play the Game
num_user_moves = 0

while(right_stack.get_size() != num_disks):

  print("\n\n\n...Current Stacks...")

  for stack in stacks:
    stack.print_items()

    while True:
      print("\nWhich stack do you want to move from?\n")
      from_stack = stack[i]
      print("\nWhich stack do you want to move to?\n")
      to_stack = stack[i]