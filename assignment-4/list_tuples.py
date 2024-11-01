# lists - mutable data type 
list = [80, 85, 100, 90, 95]
print(list.sort())
print(type(list), list)

# tuples - immutable data type 
tuple = (80, 85, 90, 95, 100)
print(tuple[0])
print(type(tuple), tuple)
print(tuple.index(80))
print(tuple.count(90))

#palindrome check 
marks = [10, 20, 30, 20, 10];

marks_copy = marks.copy()

if(marks == marks_copy):
    print("this is a palindrome")
else:
    print("this is not a palindrome")