print("Hello") 
#changes in master branch to be merged with branch1
print("Added some new stuff")

from .person import Person
p = Person("Radek", 40)
print(p.name)
print(p.age)