#solution accepts five integer inputs

user_num1 = int(input())
user_num2 = int(input())
user_num3 = int(input())
user_num4 = int(input())
user_num5 = int(input())

#solution outputs three sums of input values; convert before calculating sum



#first output: sum of five inputs maintained as INTEGER values
total = user_num1 + user_num2 + user_num3 + user_num4 + user_num5

print(f"Integer: {total}")


#second output: sum of five inputs converted to FLOAT values
print(f"Float: {total:.1f}")




#third output: sum of five inputs converted to STRING values (concatenate)

print(f"String: {user_num1}{user_num2}{user_num3}{user_num4}{user_num5}")


#ALTERNATIVE third output: sum of five inputs converted to STRING values (concatenate)
string_sum = str(user_num1) + str(user_num2) + str(user_num3) + str(user_num4) + str(user_num5)
print(f"String: {string_sum}")
