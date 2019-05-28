dinner_people = [ 'Paul', 'Tom', 'Ruth' ]
print(dinner_people)
print ("Dear " + dinner_people[0] + " you are invite to dinner this night")
print ("Dear " + dinner_people[1] + " you are invite to dinner this night")
print ("Dear " + dinner_people[2] + " you are invite to dinner this night")

print("Unfourtunately " + dinner_people[1] + " can't assist to diner")

del dinner_people[1]
print(dinner_people)

print ("Dear " + dinner_people[0] + " you are invite to dinner this night")
print ("Dear " + dinner_people[1] + " you are invite to dinner this night")
print("We have a bigger dinner table, we can invite more people")
dinner_people.insert(0, 'Veronica')
dinner_people.insert(2, 'Sara')
dinner_people.append('Jhon')
print(dinner_people)

print ("Dear " + dinner_people[0] + " you are invite to dinner this night")
print ("Dear " + dinner_people[1] + " you are invite to dinner this night")
print ("Dear " + dinner_people[2] + " you are invite to dinner this night")
print ("Dear " + dinner_people[3] + " you are invite to dinner this night")
print ("Dear " + dinner_people[4] + " you are invite to dinner this night")

#
print("Dear friends I can only invite two pepople")
print(dinner_people)
delete_people=dinner_people.pop()
print("Dear " + delete_people + " so sorry but you are not invite to dinner")
print(dinner_people)
delete_people=dinner_people.pop()
print("Dear " + delete_people + " so sorry but you are not invite to dinner")
print(dinner_people)
delete_people=dinner_people.pop()
print("Dear " + delete_people + " so sorry but you are not invite to dinner")
print(dinner_people)

print("Dear " + dinner_people[0] + " you are invite to dinner\n")
print("Dear " + dinner_people[1] + " you are invite to dinner\n")
del dinner_people[1]
del dinner_people[0]
print(dinner_people)
