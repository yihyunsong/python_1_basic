fruits = ['apple', 'pear', 'banana']
print(fruits[1])
fruits.append('melon')
fruits.remove('pear')
fruits.pop()

sports = ['soccer', 'football', 'basketball']
for sport in sports:
    print(sport)
for i in range(0,3):                     # range-> make tuple or list // range(first, last + 1)
    print(sports[i])

# Tuple
samsung = ('galaxy23', 'galaxy watch4', 'galaxy fold 3')
print(samsung)
# samsung.append('galaxy flip4')

weather = {'vancouver' : 'rain', 'seoul' : 'cold', 'washington' : 'cloudy'}
print(weather['vancouver'])
