samplePrices = {
    "apple": .5,
    "banana": .3,
    "strawberry": .1,
    "kiwi": .3
}
sampleItemsBought = {
    "apple": 2,
    "banana": 5,
    "strawberry": 2,
    "kiwi": 1
}
## Expected cost = 1 + 1.5 + 0.2 + 0.3 = 3

def calculateBill(prices, itemsBought):
    cost = 0
    for item in itemsBought.keys():
        if not prices[item]:
            print(f"Error: \'{item}\' doesn't exist in prices dictionary.")
            return;
    
        cost += prices[item] * itemsBought[item]

    return cost

print(calculateBill(samplePrices, sampleItemsBought))