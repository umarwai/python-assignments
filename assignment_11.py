# 1️⃣ Create set, add and update elements
s = {10, 20, 30}
s.add(50)
s.update([40, 60])
print("Final set:", s)

# 2️⃣ Remove with remove() and discard()
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")         # Will raise error if item not found
fruits.discard("orange")        # Safe even if item not found
print("Fruits:", fruits)

# 3️⃣ Pop and clear set
colors = {"red", "green", "blue"}
colors.pop()
print("After pop:", colors)
colors.clear()
print("After clear:", colors)

# 4️⃣ Perform union, intersection, difference, symmetric_difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))

# 5️⃣ Subset, Superset, Disjoint check
A = {1, 2, 3}
B = {1, 2}
print("Is B subset of A?", B.issubset(A))
print("Is A superset of B?", A.issuperset(B))
print("Are they disjoint?", A.isdisjoint(B))

# 6️⃣ Frozenset immutability
v = frozenset(['a', 'e', 'i', 'o', 'u'])
try:
    v.add('x')
except Exception as e:
    print("Error:", e)
try:
    v.remove('a')
except Exception as e:
    print("Error:", e)

# 7️⃣ Frozenset operations
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([2, 3, 4])
print("Union:", fs1.union(fs2))
print("Intersection:", fs1.intersection(fs2))
print("Difference:", fs1.difference(fs2))
print("Symmetric Difference:", fs1.symmetric_difference(fs2))

# 8️⃣ Membership check and isdisjoint
cities = {"Lahore", "Karachi", "Islamabad"}
for city in ["Lahore", "Peshawar"]:
    if city in cities:
        print(city, "is in the set")
    else:
        print(city, "is NOT in the set")
new_cities = {"Multan", "Quetta"}
print("Disjoint?", cities.isdisjoint(new_cities))

# 9️⃣ Operators: |, &, -, ^
setA = {1, 2, 3}
setB = {3, 4, 5}
print("Union:", setA | setB)         # all elements from both
print("Intersection:", setA & setB)  # common elements
print("Difference:", setA - setB)    # in A not in B
print("Symmetric Difference:", setA ^ setB)  # in either A or B, not both

# 🔟 Input list, convert to set then frozenset, try modifying
items = []
for i in range(5):
    item = input("Enter item: ")
    items.append(item)
set_items = set(items)
fset_items = frozenset(set_items)
print("Frozen set:", fset_items)
try:
    fset_items.add("new")
except Exception as e:
    print("Error:", e)
