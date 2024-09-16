A = 10
print(A)
print(type(A))
print(id(A))


# Numeric types ##
age = 30                # int
print("age :", age, "| type:", type(age))
pi = 3.14159            # float
print("pi:", pi, "| type:", type(pi))

sci_not = 1.2e4
print(sci_not)
complex_number = 2 + 3j # complex
print("complex_number:", complex_number, "| type:", type(complex_number))
print('Real_Part:',complex_number.real,'Imaginary_Part:',complex_number.imag)


# Bool##
a = 10
b = 20
c = a < b
print(c)

a = True + True
b = True + False
c = False + False
output=bool(a)
print("a: ", a, "b: ", b, "c: ", c)
print(output)



# Sequence types
name = "Alice"               # str
print("name:", name, "| type:", type(name))

numbers = [1, 'a', 3.0, 4.5, 5,5]    # list
numbers.insert(2,['newinput'])
print("numbers:", numbers, "| type:", type(numbers))
print(numbers[1])     #first element at index 0

coordinates = (10.0, 20.0, 40.0)   # tuple
print("coordinates:", coordinates, "| type:", type(coordinates))
print(coordinates[1])     #first element at index 0

range_numbers = range(10)    # range
print("range_numbers:", range_numbers[3], "| type:", type(range_numbers))


# Mapping type  # #

# Set types
unique_numbers = {100,0,10,200,10,'apple'}       # set
immutable_set = frozenset([100,0,10,200,10,'apple'])    # frozenset
unique_numbers.add(4)
unique_numbers.remove(10)
print("unique_numbers:", unique_numbers, "| type:", type(unique_numbers))
print("immutable_set:", immutable_set, "| type:", type(immutable_set))

person = {"name": "Alice", "age": 30, "City": "XYZ"}  # dict
test_none = person.get("address", None)

print("person:", person, "| type:", type(person))
print(person["name"], person["age"])
print(test_none)





# Boolean type
is_active = True  # bool

print("is_active:", is_active, "| type:", type(is_active))   # Output: is_active: True | type: <class 'bool'>

# Binary types
byte_data = b'hello'                     # bytes
mutable_byte_data = bytearray(b'hello')  # bytearray
memory_view = memoryview(b'hello')       # memoryview

print("byte_data:", byte_data, "| type:", type(byte_data))            # Output: byte_data: b'hello' | type: <class 'bytes'>
print("mutable_byte_data:", mutable_byte_data, "| type:", type(mutable_byte_data))  # Output: mutable_byte_data: bytearray(b'hello') | type: <class 'bytearray'>
print("memory_view:", memory_view, "| type:", type(memory_view))      # Output

d = {101:'Java',102:'C++',103:'Python'}
print(d[101])

