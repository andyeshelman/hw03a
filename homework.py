#======= Question 1 =======

# Task 1: sort grades in descending order

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort(reverse=True)
print(grades)

# Task 2: average

average = sum(grades)/len(grades)
print(average)


#======= Question 2 =======

# Task 1 : find intersection

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

both = [x for x in submitted if x in attended]
print(both)


#======= Question 3 =======

# Task 1 : extract second week of temps

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91,
                92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week = temperatures[7:14]
print(second_week)

# Task 2 : extract temps over 100

high_temps = [x for x in temperatures if x > 100]
print(high_temps)