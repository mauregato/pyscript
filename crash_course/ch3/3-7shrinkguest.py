dinner_people = [ 'Paul', 'Tom', 'Ruth' ]
print ("Dear " + dinner_people[0] + " you are invite to dinner this night")
print ("Dear " + dinner_people[1] + " you are invite to dinner this night")
print ("Dear " + dinner_people[2] + " you are invite to dinner this night")

print("Unfourtunately " + dinner_people[1] + " can't assist to diner")

dinner_people.remove('Tom')
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

#
print("Dear friends I can only invite tow pepople")
dinner_people.pop(4)
print("Dear " + dinner_people.pop() + " so sorry but you are not invite to dinner")
