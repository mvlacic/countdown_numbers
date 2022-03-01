from itertools import combinations as combs
#Solves the number game from countdown
#Given any input values

def get_arithmetic(pair, frac=False):
    '''
    Given a tuple pair of numbers, returns a list of all possible
    values that can be gotten using simple arithmetic operations
    on the input numbers
    The function works such that if the inputs are both non-negative, then
    all the results will also be non-negative
    The frac flag determines if fractional solutions are to be included
    '''

    x = max(pair) # Define x as the larger of the two
    y = min(pair) # Define y as the smaller of the two
    if x*y == 0: # If either value is 0
        return [
            {
                "result": 0,
                "equation": f"{x} * {y} = {0}",
            },
            {
                "result": x-y,
                "equation": f"{x} - {y} = {x-y}"
            }
            ]
    else: # If both values are non-zero
        if frac:
            return [
                {
                    "result": x+y,
                    "equation": f"{x} + {y} = {x+y}"
                },
                {
                    "result": x*y,
                    "equation": f"{x} * {y} = {x*y}"
                },
                {
                    "result": x-y,
                    "equation": f"{x} - {y} = {x-y}"
                },
                {
                    "result": x/y,
                    "equation": f"{x} / {y} = {x/y}"
                },
                {
                    "result": y/x,
                    "equation": f"{y} / {x} = {y/x}"
                }
                ]
        else:
            if x%y == 0:
                return [
                {
                    "result": x+y,
                    "equation": f"{x} + {y} = {x+y}"
                },
                {
                    "result": x*y,
                    "equation": f"{x} * {y} = {x*y}"
                },
                {
                    "result": x-y,
                    "equation": f"{x} - {y} = {x-y}"
                },
                {
                    "result": int(x/y),
                    "equation": f"{x} / {y} = {int(x/y)}"
                }
                ]
            else:
                return [
                {
                    "result": x+y,
                    "equation": f"{x} + {y} = {x+y}"
                },
                {
                    "result": x*y,
                    "equation": f"{x} * {y} = {x*y}"
                },
                {
                    "result": x-y,
                    "equation": f"{x} - {y} = {x-y}"
                }
                ]

def solve(target, smalls, frac=False):
    """
    Recursive function that solves the game with target value of 'target'
    and available values stored in the list 'smalls'
    """
    global operations
    if target in smalls:
        print(target)
        operations.append(target)
        return 1
    
    else:
        newsmalls = []
        for c in combs(range(len(smalls)), 2):
            c = set(c)

            newsmalls = [i for j,i in enumerate(smalls) if j not in c]
            
            # First try by deleting the pair of numbers from the list entirely
            # i.e. not using them at all in the calculations

            if solve(target, newsmalls, frac) == 1:
                return 1
            
            # If this doesnt work, try by combining them using arithemtic
            pair = [smalls[i] for i in c]
            newvals = get_arithmetic(pair, frac)
            
            for val in newvals: # For each possible operation
                result = val["result"]
                equation = val["equation"]
                if solve(target, newsmalls+[result], frac) == 1:
                    print(equation)
                    operations.append(equation)
                    return 1
                    
                    
def countdown(target, smalls, frac=False):
    global operations
    operations=[]
    solve(target, smalls, frac)
    return operations

