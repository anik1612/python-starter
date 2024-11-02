# function
def sum(a, b):
    return a + b

print(sum(5, 5))

# recursive function 
def recursive_func(n, lst=None):
    if lst is None:
        lst = []
    if n == 0:
        return lst
    lst.append(n)
    return recursive_func(n-1, lst)

result = recursive_func(5)
print(result)