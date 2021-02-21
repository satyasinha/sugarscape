import random

class turtle:
  def __init__(self, maxX, maxY):
    self.x = random.randint(0, maxX)
    self.y = random.randint(0, maxY) 

class sugar:
  def __init__(self, maxX, maxY):
    self.x = random.randint(0, maxX)
    self.y = random.randint(0, maxY)

class environment:
  def __init__(self, gridSize):
    self.turtles = []
    self.sugars = []
    self.width = gridSize
    self.height = gridSize

  def initEnvironment(self, numTurtles, numSugars):
    # make sugars
    for s in range(numSugars):
      s = sugar(self.width, self.height)
      self.sugars.append(s)

    # make a list of turtles
    for t in range(numTurtles):
      t = turtle(self.width, self.height)
      self.turtles.append(t)    

  def tick(self):
    return self