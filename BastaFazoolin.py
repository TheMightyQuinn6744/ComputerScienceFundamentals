#create class Franchise
class Franchise:
  #define constructor for class with arguments self, address, menus
  def __init__(self,address,menus):
    #create instance variables for constructor arguments 
    self.address = address 
    self.menus = menus
  #dunder Franchise method for string represintation of address
  def __repr__(self):
    return self.address
  #method available menus returns different menu availability times
  def available_menus(self,time):
    #create empty list menus 
    available_menus = []
    #loop through each item in the instance variable self.menus
    for menu in self.menus:
      #conditional statement for time 
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menus)
        #return the value of the list available menus after loop ends
    return available_menus

#create menu class
class Menu:
  #give menu a constrcutor with 5 params self, name, items, start_time, end_time
  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items 
    self.start_time = start_time 
    self.end_time = end_time
  #string representation for available menus based on time 
  def __repr__(self):
    return self.name + " is available from " + str(self.start_time) + " - " + str(self.end_time)
  #Menu class method that takes the argument purhased items
  def calculate_bill(self, purchased_items):
    #counter variable total price
    total_price = 0
    #iterate through each item in list purchased items  
    for purchased_item in purchased_items:
      #if the item is included in the list of menu items
      if purchased_item in self.items:
        #add the value of each purchased item to the variable total price 
        total_price += self.items[purchased_item]
        #return the value of total price
    return total_price


#create a class called Business
class Business:
  #create constructor that takes name and franchises 
  def __init__(self,name, franchise):
    self.name = name 
    self.franchise = franchise

#brunch menu items object 
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

#bruch menu variable which stores Menu object that calls brunch items + time 
brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)

#early bird menu items object
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

#early bird menu variable which stores Menu object that calls early bird menu items + time 
early_bird_menu = Menu('Early Bird', early_bird_items,1500,1800)

#dinner menu item object
dinner_menu_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

#dinner menu variable which stores Menu object that calls dinner items + time 
dinner_menu = Menu('Dinner',dinner_menu_items,1700,2300)

#kids dinner menu item object
kids_menu_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

#kids menu variable which stores Menu object that calls kid items + time 
kids_menu = Menu('Kids',kids_menu_items,1100,2100)


#menus list that stores list of available menus
menus = [brunch_menu,early_bird_menu,dinner_menu,kids_menu]

#flagship store Franchise instance
flagship_store = Franchise('1232 West End Road', menus)

#new installment Franchise instance
new_installment = Franchise('12 East Mulberry Street',menus)

#basta fazoolin business instance
basta_fazoolin = Business("Basta Fazoolin'with my Heart",[flagship_store, new_installment])

#print(flagship_store.available_menus(1200))

# Arepa 
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Take a' Arepa", arepas_items, 1000, 2000)

arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

arepa = Business("Take a' Arepa", [arepas_place])

print(arepa.franchise[0].menus[0])
