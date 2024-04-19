file = open('restaurants_names.csv', 'r')
lines = file.readlines()
file.close()

stuff = []
restaurants = {}
restaurant_names = []
names_to_remove = []

x = 0
for line in lines:
    stuff.append(line.split(','))
    restaurant_names.append(stuff[x][0])
    x += 1

for i in range(1,len(restaurant_names)):
    restaurants[stuff[i][0]] = stuff[i][1:]
restaurant_names.pop(0)


choice = int(input("""Is anyone in your party a vegetarian?
1. If yes
0. If no : """))

if choice == 1:
    x = len(restaurant_names)
    for i in range(0,x):
        if int(restaurants[restaurant_names[i]][0]) != 1:
            names_to_remove.append(restaurant_names[i])

choice = int(input("""Is anyone in your party a vegan?
1. If yes
0. If no : """))

if choice == 1:
    x = len(restaurant_names)
    for i in range(0,x):
        if int(restaurants[restaurant_names[i]][1]) != 1:
            names_to_remove.append(restaurant_names[i])

choice = int(input("""Is anyone in your party a Gluten-Free?
1. If yes
0. If no : """))

if choice == 1:
    x = len(restaurant_names)
    for i in range(0,x):
        if int(restaurants[restaurant_names[i]][2]) != 1:
            names_to_remove.append(restaurant_names[i])


names_to_remove = list(set(names_to_remove))
for i in range(0,len(names_to_remove)):
    restaurant_names.remove(names_to_remove[i])

print('Here are your restaurant choices')
print(restaurant_names)