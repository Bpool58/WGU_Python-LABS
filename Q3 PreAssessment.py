"""
Task:
Create a solution that accepts an integer input representing the index value for any
of the five elements in the following list:

various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

Using the built-in function type() and getting its name by using the .name attribute,
output data type (e.g., int”, “float”, “bool”, “str”) based on the input index value of the list element.

The solution output should be in the format

Element index_value: data_type
Sample Input/Output:
If the input is

4
then the expected output is

Element 4: tuple
"""

various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"),
                      {"apple": 1, "pear": 5}]

#use built-in function type()
#get name by using the built-in attribute __name__
#solution accepts integer input representing list element index
#solution outputs data type of list element based on input index value


index = int(input())

element = various_data_types[index]

type_of_element = type(element).__name__

print(f"Element {index}: {type_of_element}")
