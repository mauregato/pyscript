dinner_people = [ 'Paul', 'Tom', 'Ruth' ]
print ("Dear " + dinner_people[0] + " you are invite to dinner this night")
print ("Dear " + dinner_people[1] + " you are invite to dinner this night")
print ("Dear " + dinner_people[2] + " you are invite to dinner this night")

print("Unfourtunately " + dinner_people[1] + " can't assist to diner")
del dinner_people[1]
#dinner_people.remove('Tom')
print ("Dear " + dinner_people[0] + " you are invite to dinner this night")
print ("Dear " + dinner_people[1] + " you are invite to dinner this night")
print("We have a bigger dinner table, we can invite more people")
dinner_people.insert(0, 'Veronica')
dinner_people.insert(2, 'Sara')
dinner_people.append('Jhon')

print ("Dear " + dinner_people[0] + " you are invite to dinner this night")
print ("Dear " + dinner_people[1] + " you are invite to dinner this night")
print ("Dear " + dinner_people[2] + " you are invite to dinner this night")
print ("Dear " + dinner_people[3] + " you are invite to dinner this night")
print ("Dear " + dinner_people[4] + " you are invite to dinner this night")
print("Total of people invited: \n")
print(len(dinner_people))
