# no duplication
ts = {"apple", "banana", "cherry", "apple"}
print(ts) #prints unordered

# can not access elements and randomly selected
for i in ts:
    print(i)

if "banana" in ts:
    print("banana in ts\n")

#add elkemetn
ts.add("orange")

#add 
ts2 = {"pineapple", "papaya"}
ts.update(ts2)
print(ts)

print()

#add any iterable objects
ls = ["kiwi", "cherry", 1]
ts.update(ls)
print(ts)

print()

# remove items
ts.remove("banana")
print(ts)
print()

# remove errors so use discard to avoid error
ts.discard("cherry")
print(ts)
print()

# pop function doesnt use index. randomly
ts.pop()
print(ts)

# remove all items
ts.clear()
print(ts)

# remove the variable and if you print it will error
del ts
print()

# union
s1 = {"a", "b", "c"}
s2 = {1, 2, 3}
s3 = s1.union(s2)
print(s3)
