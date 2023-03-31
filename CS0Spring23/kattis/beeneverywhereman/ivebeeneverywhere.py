# input the number of test cases

# for each test case:
#   input the number of cities
#   for each city name:
#       if city exists, add 1 to value
#       if city does not exist, create itm in list and set value to 1
#   print(length of the dictionary) = number of unique cities

tests = int(input())
cities = {}
for t in range(tests):
    num_cities = int(input())
    for n in range(num_cities):
        city = input()
        if city in cities:
            cities[city] = cities[city] + 1
        else:
            cities[city] = 1
    print(len(cities))
    cities.clear()

