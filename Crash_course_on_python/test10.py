# Manually sort a list of 10 integers in python
def sort_integer(unordered):
    ordered = []
    for i in range(len(unordered)):
        ordered.append(min(unordered))
        unordered.remove(ordered[i])
    print(ordered)
list= [3,4,1,2]
sort_integer(list)


            



   