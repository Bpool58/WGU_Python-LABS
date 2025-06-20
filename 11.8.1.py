#Replacing For Loop with equivelant List Comprehension

#Adding 10 to every element
my_list = [5, 20, 50]
for i in range(len(my_list)):
    my_list[i] += 10
print(my_list)

my_list = [5, 20, 50]
my_list = [ (i + 10) for i in my_list ]
print(my_list)

#Converting every element to a string
my_list = [5, 20, 50]
for i in range(len(my_list)):
    my_list[i] = str(my_list[i])
print(my_list)

my_list = [5, 20, 50]
my_list = [ str(i) for i in my_list ]
print(my_list)

#Convert user input into a list of integers
inp = input("Enter numbers:")
my_list = []
for i in inp.split():
    my_list.append(int(i))
print(my_list)

inp = input("Enter numbers:")
my_list = [ int(i) for i in inp.split()]
print(my_list)

#Find the sum of each row in a two dimensional list
my_list = [[5, 10, 15], [2, 3, 16], [100]]
sum_list = []
for row in my_list:
    sum_list.append(sum(row))
print(sum_list)

my_list = [[5, 10, 15], [2, 3, 16], [100]]
sum_list = [ sum(row) for row in my_list ]
print(sum_list)

#Find the sum of the row with the smallest sum in a two-dimensional table
my_list = [[5, 10, 15], [2, 3, 16], [100]]
sum_list = []
for row in my_list:
    sum_list.append(sum(row))
    min_row = min(sum_list)
print(min_row)

my_list = [[5, 10, 15], [2, 3, 16], [100]]
min_row = min([sum(row) for row in my_list])
print(min_row)