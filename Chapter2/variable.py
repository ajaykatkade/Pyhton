
a = 1

b = 2

print(a+b)

""" Python manages memory using two primary structures: 
Stack Memory: This stores function calls and references (the "names" of your variables). It is used for static allocation and is very fast but limited in size.
Heap Memory: This is a private area where all objects (like lists, integers, or strings) actually live. It is managed by the Python memory manager. 
"""

a = 2 #int
b = 'test' #str
c = 2.5 #float
d = True #bool

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# ========== Variable Naming Rules ==========
# Valid variable names
my_var = 1
_private = 2
myVar2 = 3
MY_CONSTANT = 100

# Invalid variable names (will cause errors)
#test$ = 1   #error - special characters not allowed
#2name = 1   #error - cannot start with a number
#my var = 1  #error - spaces not allowed
#class = 1   #error - reserved keyword

# ========== Python Operators ==========

#1. Arithmetic Operators
x = 10
y = 3
print("--- Arithmetic Operators ---")
print("x + y =", x + y)    # Addition: 13
print("x - y =", x - y)    # Subtraction: 7
print("x * y =", x * y)    # Multiplication: 30
print("x / y =", x / y)    # Division: 3.333...
print("x // y =", x // y)  # Floor Division: 3
print("x % y =", x % y)    # Modulus: 1
print("x ** y =", x ** y)  # Exponentiation: 1000

#2. Comparison (Relational) Operators
print("\n--- Comparison Operators ---")
print("x == y:", x == y)    # Equal: False
print("x != y:", x != y)    # Not Equal: True
print("x > y:", x > y)      # Greater than: True
print("x < y:", x < y)      # Less than: False
print("x >= y:", x >= y)    # Greater or equal: True
print("x <= y:", x <= y)    # Less or equal: False

#3. Logical Operators
print("\n--- Logical Operators ---")
p = True
q = False
print("p and q:", p and q)  # False
print("p or q:", p or q)    # True
print("not p:", not p)      # False

#4. Assignment Operators
print("\n--- Assignment Operators ---")
z = 10       # Simple assignment
z += 5       # z = z + 5 → 15
print("z += 5:", z)
z -= 3       # z = z - 3 → 12
print("z -= 3:", z)
z *= 2       # z = z * 2 → 24
print("z *= 2:", z)
z /= 4       # z = z / 4 → 6.0
print("z /= 4:", z)
z //= 2      # z = z // 2 → 3.0
print("z //= 2:", z)
z %= 2       # z = z % 2 → 1.0
print("z %= 2:", z)
z **= 3      # z = z ** 3 → 1.0
print("z **= 3:", z)

#5. Bitwise Operators
print("\n--- Bitwise Operators ---")
m = 5   # binary: 0101
n = 3   # binary: 0011
print("m & n =", m & n)     # AND: 1   (0001)
print("m | n =", m | n)     # OR: 7    (0111)
print("m ^ n =", m ^ n)     # XOR: 6   (0110)
print("~m =", ~m)            # NOT: -6  (inverts bits)
print("m << 1 =", m << 1)   # Left shift: 10  (1010)
print("m >> 1 =", m >> 1)   # Right shift: 2  (0010)

#6. Membership Operators
print("\n--- Membership Operators ---")
my_list = [1, 2, 3, 4, 5]
print("3 in my_list:", 3 in my_list)         # True
print("6 in my_list:", 6 in my_list)         # False
print("6 not in my_list:", 6 not in my_list) # True

my_string = "Hello Python"
print("'Python' in my_string:", 'Python' in my_string)  # True

#7. Identity Operators
print("\n--- Identity Operators ---")
a1 = [1, 2, 3]
b1 = [1, 2, 3]
c1 = a1
print("a1 is b1:", a1 is b1)         # False (different objects in memory)
print("a1 is c1:", a1 is c1)         # True (same object in memory)
print("a1 is not b1:", a1 is not b1) # True
print("a1 == b1:", a1 == b1)         # True (same values, different objects)

#rules for variable 
#8test = 1 #error
#test = 1 #ok
#test_ = 1 #ok
#test$ = 1 #error


#operator in python
#1.arithmetic operator

#2.comparison operator

#3.logical operator

#4.assignment operator

#5.bitwise operator

#6.membership operator

#7.identity operator

