# TUPLE

#Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable.
#Once a tuple is created, we cannot change its values. Tuples are unchangeable, or immutable as it also is called.

#Example:

movies = ("The Shawshank Redemption", "The Godfather", "The Dark Knight", "12 Angry Men")


##Finding data type

print(type(movies))
#Output: <class 'tuple'>


## uple Length
print(len(movies))
#Output: 4


##Count method in tuple
#The count() method returns the number of times a specified value appears in the tuple.

my_cars = ("BMW", "Ford", "Bugatti", "Mercedes", "Ford", "Ferrari", "Audi", "Ford", "Rolls-Royce")
no_of_ford = my_cars.count("Ford")
print(no_of_ford)
#Output: 3


## Index method in tuple
#The index() method finds the first occurrence of the specified value.
#The index() method raises an exception if the value is not found.

my_new_cars = ("BMW", "Ford", "Bugatti", "Mercedes", "Ford", "Ferrari", "Audi", "Ford", "Rolls-Royce")
index_of_ford = my_new_cars.index("Ford")
print(index_of_ford)
#Output: 1


##Access Tuple Items
#We can access tuple items by referring to the index number.
#We can also use negative index. -1 refers to the last item, -2 refers to the second last item.
#We will get a new tuple when we specify a range of indexes.

fav_movies = ("The Shawshank Redemption", "The Godfather", "The Dark Knight", "12 Angry Men", "Schindler's List", "The Lord of the Rings: The Return of the King", "Forrest Gump", " Fight Club")
print(fav_movies[1])
#Output: "The Godfather"
print(fav_movies[3])
#Output: "12 Angry Men"
print(fav_movies[-1])
#Output: "Fight Club"
print(fav_movies[-3])
#Output: "The Lord of the Rings: The Return of the King"
print(fav_movies[2:5])
#Output: ('The Dark Knight', '12 Angry Men', "Schindler's List")
print(fav_movies[:4])
#Output: ('The Shawshank Redemption', 'The Godfather', 'The Dark Knight', '12 Angry Men')
print(fav_movies[2:])
#Output: ('The Dark Knight', '12 Angry Men', "Schindler's List", 'The Lord of the Rings: The Return of the King', 'Forrest Gump', ' Fight Club')
print(fav_movies[-4:-1])
#Output: ("Schindler's List", 'The Lord of the Rings: The Return of the King', 'Forrest Gump')


##Unpacking a Tuple
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking".

#Example for packing a tuple:
animals = ("cat", "dog", "tiger")

#Example for unpacking a tuple:
birds = ("eagle", "sparrow", "parrot")
(a, b, c) = birds
print(a)
#Output: eagle
print(b)
#Output: sparrow
print(c)
#Output: parrot

##Using Asterisk*
#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list.

fav_birds = ("eagle", "sparrow", "parrot", "crow", "owl")
(x, y, *z) = fav_birds
print(x)
#Output: eagle
print(y)
#Output: sparrow
print(z)
#Output: ['parrot', 'crow', 'owl']


##Join Two Tuples
#To join two or more tuples we can use the + operator.

my_cars = ("BMW", "Ford", "Bugatti")
friend_cars = ("Ford", "Ferrari")
our_cars = my_cars + friend_cars
print(our_cars)
#Output: ('BMW', 'Ford', 'Bugatti', 'Ford', 'Ferrari')


##Multiply Tuples
new_cars = ("BMW", "Ford", "Bugatti")
my_new_cars = new_cars * 3
print(my_new_cars)
#Output: ('BMW', 'Ford', 'Bugatti', 'BMW', 'Ford', 'Bugatti', 'BMW', 'Ford', 'Bugatti')