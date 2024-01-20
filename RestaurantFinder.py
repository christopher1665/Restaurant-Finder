restaurant = {"Joe's Burgers":[0,0,0], 
              'Pizza Place':[1,0,1], 
              'Cafe':[1,1,1], 
              "Mama's Fine Italian":[1,0,0],
              "The Chef's Kitchen":[1,1,1]}

restaurantList = [k for k, v in restaurant.items()]
choice = [0,0,0]

choice[0] = int(input("""Is anyone in your party a vegetarian?
# 1. If yes
# 0. If no
"""))

choice[1] = int(input("""Is anyone in your party a vegan?
# 1. If yes
# 0. If no
"""))

choice[2] = int(input("""Is anyone in your party a Gluten-Free?
# 1. If yes
# 0. If no
"""))

count = 0
restaurantList2 = []
for i in range(0,len(restaurant)):
    for y in range(0,len(restaurant[restaurantList[0]])):
        if restaurant[restaurantList[i]][y] == 0 and choice[y] == 1:
            count = 0
            continue
        count += 1
        if count == len(restaurant[restaurantList[0]]):
            count = 0
            restaurantList2.append(restaurantList[i])

print('Here are your restaurant choices')
for i in range(0, len(restaurantList2)):
    print(restaurantList2[i])