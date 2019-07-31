"""
#ARRAY OR LIST same data structure
students = ["Alice", "Javi", "Damien"]
students.append("Delilah") #adding new element to data structure
print(students)

students.insert(1, "Zoe")
print(students)

students.remove("Javi") #first one will be removed
print(students)

for name in smith_siblings:
    #print(name + " Smith")
    print(len(smith_siblings))

smith_siblings = ["Emily", "Monique", "Giovanni", "Maria", "Alice", "Javi", "Damien" ]

for index in range(len(smith_siblings)):
    smith_siblings[index] = smith_siblings[index] + " Smith"
print(smith_siblings)

superheroes = ["captain Marvel", "Wonder women", "Storm", "Kamala Khan", "Bumblebee", "Jessica Jones"]
demoted_hero = str(raw_input("What superhero do you want to eliminate from the top 5?"))
if demoted_hero in superheroes:
    superheroes.remove(demoted_hero)
    print("Top 5 heroes", superheroes)
else:
    print("Hero not found.")

#my_list[start:end:step]
names = ["Rickon", "Bran", "Arya","Sansa","Jon", "Robb"]
print(names[::-1]) #['Robb', 'Jon', 'Sansa', 'Arya', 'Bran', 'Rickon']
print(names[4:2:-1]) #['Jon', 'Sansa']
print(names[:2]) #end index is not included ['Rickon', 'Bran']
print(names[::2]) #every other name ['Rickon', 'Arya', 'Jon']
"""
#DICTIONARY
states = {
"NY": "New York",
"CA": "California",
"TX": "Texas",
"HI": "Hawaii"
}
for abbreviation in states:
    print(abbreviation + " is short for "+states[abbreviation])
me = {
"name": "Gaby",
"age": 17,
"gender": "female"
}
for gabyInfo in states:
    print(gabyInfo  + " is " + me[gabyInfo])
#print(pets[2]['name'])
