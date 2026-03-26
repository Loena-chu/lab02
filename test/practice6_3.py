nums=[1,2,3,4,5,6]
def filter_evens(lst):
    return([i for i in lst if i %2==0])
print(filter_evens(nums))
def square_all(lst):
    return([i**2 for i in lst])
print (square_all(nums))
print(square_all(filter_evens(nums)))