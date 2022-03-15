class Stock(object):
  def __init__(self, n, v, w):
    self.name = n
    self.values = v
    self.prices = w

  def getName(self):
    return self.name

  def getValue(self):
    return self.values

  def getCost(self):
    return self.prices

  def density(self):
    return self.getValue()/self.getCost()

  def __str__(self):
    return (self.name + ': <' + str(round(self.values,3)) + ', ' + str(round(self.prices,1)) + '$' + '>')

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
  import numpy as np
  choosen = []
  print('Use search tree to allocate ' + str(maxUnits) + '$')
  val, taken = maxVal_fast(stocks, maxUnits)
  m = len(taken)
  print('Total Values are ' + str(round(val,1)))
  if printItems:
    for item in taken:
      choosen.append(item.getName())
      print('> ', item)
  return choosen

def greedy(items, maxCost, keyFunction):
  itemsCopy = sorted(items, key = keyFunction, reverse = True).copy()
  result = []
  totalValue, totalCost = float(0), float(0)
  for i in range(len(itemsCopy)):
    if (totalCost + itemsCopy[i].getCost()) <= maxCost:
      result.append(itemsCopy[i])
      totalCost += itemsCopy[i].getCost()
      totalValue += itemsCopy[i].getValue()
  return result, totalValue

def testGreedy(items, constraint, keyFunction):
  taken, val = greedy(items, constraint, keyFunction)
  print('Total value of items taken = ', val)
  for item in taken:
    print(' > ', item)
def testGreedys(stocks, maxUnits):
  print('use greedy by density to allocate', maxUnits, 'dolalrs')
  testGreedy(stocks, maxUnits, Stock.density)