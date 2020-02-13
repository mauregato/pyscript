#4-9. Cube Comprehension: Use a list comprehension to generate a list of the
#first 10 cubes.

cubes = [cubes**3 for cubes in range(1,11)]

for cube in cubes:
	print(cube)
