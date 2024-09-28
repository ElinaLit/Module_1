food = ["apple", "coconut", "banana"]
print(food)
print(food[0])
food[0] = "peach"
print(food)
food[1] = "grape"
print(food)
food.append(True)
print(food)
food.extend("elis")
print(food)
food.extend(["elis",2])
print(food)
food.remove("banana")
print(food)
print("coconut" in food)
print("coconut" not in food)
print(food[0:2])
print(food[0:2:2])