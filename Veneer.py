class Art:
  def __init__(self,artist,title,medium,year,owner):
    self.artist = artist 
    self.title = title 
    self.medium = medium 
    self.year = year
    self.owner = owner 

  def __repr__(self):
    return '%s. "%s". %s, %s. %s, %s.' % (self.artist,  self.title, self.medium, self.year,self.owner.name, self.owner.location)

class Marketplace:
  def __init__(self,listings):
    self.listings = []

  def add_listing(self,new_listing):
    self.listings.append(new_listing)

  def remove_listing(self, delete_listing):
    self.listings.remove(delete_listing)

  def show_listings(self):
    for listing in self.listings:
      print(listing)

#print(girl_with_mandolin)

#Veneer = Marketplace()
#Veener.show_listings()

class Client:
  def __init__(self,name,location,is_museum):
    self.name = name 
    self.location = location 
    self.is_museum = is_museum

  def sell_artwork(self,artwork,price):
    self.artwork = artwork 
    self.price = price
    if artwork.owner == self:
      new_listing = Listing(artwork,price,self)
      veneer.add_listing(new_listing)


edytta = Client("Edytta Halprit",location = None,is_museum = False )

girl_with_mandolin = Art("Picasso,Pablo","Girl with a Mandolin (Fanny Tellier)",1910,"oil on canvas",edytta)

print(girl_with_mandolin)

moma = Client("The MOMA","New York",is_museum = True)

class Listing:
  def __init__(self,art,price,seller):
    self.art = art 
    self.price = price 
    self.seller = seller 

  def __repr__(self):
    return '%s %s' % (self.art, self.price)

edytta.sell_artwork(girl_with_mandolin, "$6M(USD)")
  
veneer.show_listings()
