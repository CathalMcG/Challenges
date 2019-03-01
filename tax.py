# Given a list of tuples (category, amount), return a function
# which will give a breakdown of a given amount by the same
# proportion as the list of tuples.

# This can be used to approximate how much of your tax money
# was spent on what in a given year.

def createTaxCalculator(breakdown):
  total = sum([amount for (category, amount) in breakdown])
  proportions = [(category, amount/total) for (category, amount) in breakdown]
  def calculateTaxBreakdown(amount):
    return [(category, proportion*amount) for (category, proportion) in proportions]
  return calculateTaxBreakdown

spendingBreakdown2018 = [
  ("Social Protection", 20.4),
  ("Health", 16.0),
  ("Education", 10.2),
  ("Justice", 2.7),
  ("Agriculture", 1.5),
  ("Debt", 10.8),
  ("Transport", 2.1),
  ("Other", 10.2)
]

taxCalculator2018 = createTaxCalculator(spendingBreakdown2018)

def report(amount, calculator):
  my2018Breakdown = sorted(calculator(amount), key=lambda r:r[1], reverse=True)

  print("In 2018 you paid", amount, "in taxes.")
  print("Of that amount, your government spent...")
  for (category, amount) in my2018Breakdown:
    print("...", round(amount, 2), "on", category)

report(10000, taxCalculator2018)
