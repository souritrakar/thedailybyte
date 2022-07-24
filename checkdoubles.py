n = [0, 9]

def checkDoubles(numbers):
    
    d = dict()
    for el in numbers:
        d[el] = d.get(el, 0)+1
    for num in numbers:

        if(num*2 in d.keys()):
            return True
    return False

print(checkDoubles(n))
