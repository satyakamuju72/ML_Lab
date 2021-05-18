probAbsentFriday=0.03
probFriday=0.2

# bayes Formula
#p(A|F)=p(F| A)p(A)/p(F)
# p(A|F) =p(A ∩ F)/ p(F)


bayesResult = (probAbsentFriday / probFriday)
print(bayesResult * 100)
