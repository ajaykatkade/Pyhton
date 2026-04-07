#list in python 

my_list = [1, 2, 3, 4, 5]

#Pre installed functions can be used with list in python 

# ========== List Built-in Functions ==========

# 1. append() - Adds an element at the end
my_list.append(6)
print("append(6):", my_list)           # [1, 2, 3, 4, 5, 6]

# 2. insert() - Adds element at a specific position
my_list.insert(0, 0)
print("insert(0, 0):", my_list)        # [0, 1, 2, 3, 4, 5, 6]

# 3. extend() - Adds all elements of another list
my_list.extend([7, 8, 9])
print("extend([7,8,9]):", my_list)     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 4. remove() - Removes first occurrence of a value
my_list.remove(0)
print("remove(0):", my_list)           # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 5. pop() - Removes and returns element at index (default: last)
popped = my_list.pop()
print("pop():", popped, "| list:", my_list)  # 9 | [1, 2, 3, 4, 5, 6, 7, 8]

popped2 = my_list.pop(0)
print("pop(0):", popped2, "| list:", my_list) # 1 | [2, 3, 4, 5, 6, 7, 8]

# 6. clear() - Removes all elements
temp = [1, 2, 3]
temp.clear()
print("clear():", temp)                # []

# 7. index() - Returns index of first occurrence
print("index(5):", my_list.index(5))   # 2

# 8. count() - Counts occurrences of a value
nums = [1, 2, 2, 3, 3, 3]
print("count(3):", nums.count(3))      # 3

# 9. sort() - Sorts the list in place (ascending by default)
unsorted = [5, 2, 8, 1, 9, 3]
unsorted.sort()
print("sort():", unsorted)             # [1, 2, 3, 5, 8, 9]

unsorted.sort(reverse=True)
print("sort(reverse=True):", unsorted) # [9, 8, 5, 3, 2, 1]

# 10. reverse() - Reverses the list in place
my_list.reverse()
print("reverse():", my_list)           # [8, 7, 6, 5, 4, 3, 2]

# 11. copy() - Returns a shallow copy of the list
copied = my_list.copy()
print("copy():", copied)

# ========== Python Built-in Functions with Lists ==========

sample = [10, 20, 30, 40, 50]

# 12. len() - Returns the length
print("len():", len(sample))           # 5

# 13. max() - Returns the maximum value
print("max():", max(sample))           # 50

# 14. min() - Returns the minimum value
print("min():", min(sample))           # 10

# 15. sum() - Returns the sum of all elements
print("sum():", sum(sample))           # 150

# 16. sorted() - Returns a NEW sorted list (doesn't modify original)
unsorted2 = [3, 1, 4, 1, 5]
print("sorted():", sorted(unsorted2))  # [1, 1, 3, 4, 5]
print("original:", unsorted2)          # [3, 1, 4, 1, 5] (unchanged)

# 17. enumerate() - Returns index and value pairs
print("enumerate():")
for index, value in enumerate(sample):
    print(f"  index {index} -> {value}")

# 18. zip() - Combines two lists into pairs
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
print("zip():", list(zip(names, scores)))  # [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# 19. map() - Applies a function to each element
doubled = list(map(lambda x: x * 2, sample))
print("map(x*2):", doubled)            # [20, 40, 60, 80, 100]

# 20. filter() - Filters elements based on condition
even = list(filter(lambda x: x % 2 == 0, sample))
print("filter(even):", even)           # [10, 20, 30, 40, 50]

# ========== List Slicing ==========
print("\n--- List Slicing ---")
s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("s[2:5]:", s[2:5])       # [2, 3, 4]
print("s[:4]:", s[:4])          # [0, 1, 2, 3]
print("s[6:]:", s[6:])          # [6, 7, 8, 9]
print("s[::2]:", s[::2])        # [0, 2, 4, 6, 8] (step of 2)
print("s[::-1]:", s[::-1])      # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed)

# ========== List Comprehension ==========
print("\n--- List Comprehension ---")
squares = [x**2 for x in range(1, 6)]
print("squares:", squares)             # [1, 4, 9, 16, 25]

evens = [x for x in range(10) if x % 2 == 0]
print("evens:", evens)                 # [0, 2, 4, 6, 8]


# ==========================================
#          TUPLE IN PYTHON
# ==========================================
print("\n========== TUPLE ==========")

# Tuple is IMMUTABLE (cannot be changed after creation)
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# ========== Tuple Built-in Methods ==========

# 1. count() - Counts occurrences of a value
t = (1, 2, 2, 3, 3, 3)
print("count(3):", t.count(3))         # 3

# 2. index() - Returns index of first occurrence
print("index(2):", t.index(2))         # 1

# ========== Built-in Functions with Tuples ==========

sample_t = (10, 20, 30, 40, 50)

print("len():", len(sample_t))         # 5
print("max():", max(sample_t))         # 50
print("min():", min(sample_t))         # 10
print("sum():", sum(sample_t))         # 150
print("sorted():", sorted(sample_t))   # [10, 20, 30, 40, 50] (returns list!)

# ========== Tuple Packing & Unpacking ==========
print("\n--- Tuple Packing & Unpacking ---")
packed = 1, 2, 3           # Packing (parentheses optional)
print("packed:", packed)    # (1, 2, 3)

a, b, c = packed            # Unpacking
print(f"a={a}, b={b}, c={c}")  # a=1, b=2, c=3

# ========== Key Difference: List vs Tuple ==========
print("\n--- List vs Tuple ---")
print("List is MUTABLE   -> can add, remove, change elements")
print("Tuple is IMMUTABLE -> cannot modify after creation")
print("Tuple uses () parentheses, List uses [] brackets")
print("Tuple is FASTER than list for iteration")
print("Tuple can be used as DICTIONARY KEY, list cannot")
