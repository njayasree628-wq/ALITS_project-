fruits = ['banana', 'mango', 'jackfruit', 'papaya']
fruitscopy = fruits.copy()
fruitscopy.append('orange')
print(fruitscopy)
print("count value:",fruitscopy.count('orange'))
fruits1=['a','b','c']
joinfruit=fruitscopy + fruits1 #concatenate two different list 
print("Join two list:",joinfruit)
fruits2=['d','e','f']
print("fruit2:",fruits2)
fruits2.extend(fruits1)
print("Fruits2 extend:",fruits2)
print(fruits2.index('f'))
fruits2.reverse()
print(fruits2)

fruits = ['banana', 'mango', 'jackfruit', 'papaya']

# create a copy of fruits
fruitscopy = fruits.copy()

# append element
fruitscopy.append('orange')

# print updated list
print(fruitscopy)

# count occurrences
print("count value:", fruitscopy.count('orange'))

# concatenate lists
fruits1 = ['a', 'b', 'c']
joinfruit = fruitscopy + fruits1
print("Join two list:", joinfruit)

# extend list
fruits2 = ['d', 'e', 'f']
print("fruit2:", fruits2)

fruits2.extend(fruits1)
print("Fruits2 extend:", fruits2)

# index
print(fruits2.index('f'))

# reverse list
fruits2.reverse()
print(fruits2)
