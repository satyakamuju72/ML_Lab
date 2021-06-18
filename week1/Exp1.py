def solve():
  probAbsentFriday=0.03
  probFriday=0.2
  bayesResult = (probAbsentFriday / probFriday)
  return (bayesResult * 100)


#Baye's Rule Application - Probability of a student absent on friday
print(solve())
