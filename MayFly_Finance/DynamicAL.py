class Stock(object):
  #values are prob
  def __init__(self, n, v, w):
    self.name = n
    self.value = v
    self.prices = w
  
  def getName(self):
    return self.name
  
  def getValue(self):
    return self.value
  
  def getCost(self):
    return self.prices

  def density(self):
    return self.getValue()/self.getCost()
  
  def __str__(self):
    return self.name + ': <' + str(self.value) + ', ' + str(self.prices) + '>'

def buildMenu(names, values, prices):
  menu = []
  for i in range(len(values)):
    menu.append(Stock(names[i], values[i], prices[i]))
  return menu

def maxVal_fast(toConsider, avail, memo = {}):
  """Assume toConsider a list of items, avail a weight
  Returns a tuple of the total value of a solution to 0/1 knapsack problem 
  and the items of that solution"""
  if (len(toConsider), avail) in memo:
    return memo[(len(toConsider), avail)]

  elif toConsider == [] or avail == []:
    result = (0, ())
  elif toConsider[0].getCost() > avail:
    #Explore right branch only
    result = maxVal_fast(toConsider[1:], avail)
  else:
    nextItem = toConsider[0]
    #Explore left branch
    withVal, withToTake = maxVal_fast(toConsider[1:],
                                avail - nextItem.getCost())
    withVal += nextItem.getValue()
    #Explore right branch
    withoutVal, withoutToTake = maxVal_fast(toConsider[1:], avail)

    #Choose better branch
    if withVal > withoutVal:
      result = (withVal, withToTake + (nextItem,))
    else:
      result = (withoutVal, withoutToTake)
  memo[(len(toConsider), avail)] = result
  return result
  
def testmaxVal_fast(stocks, maxUnits, printItems = True):
  print('Use search tree to allocate', maxUnits, 'dollars')
  val, taken = maxVal_fast(foods, maxUnits)
  print('Total Value is ', val)
  if printItems:
    for item in taken:
      print('> ', item)