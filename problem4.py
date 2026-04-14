import random

lotterySet = set()

while len(lotterySet) < 6: 
    lotterySet.add(random.randint(1, 50))

print(lotterySet)