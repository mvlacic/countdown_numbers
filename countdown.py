from itertools import combinations as combs
#Solves the number game from countdown
#Given any input values

def get_arithmetic(pair):
    '''
    Given a tuple pair of numbers, returns a list of all possible
    integer values that can be gotten using simple arithmetic operations
    on the input numbers
    The function works such that if the inputs are both non-negative, then
    all the results will also be non-negative
    '''

    x = max(pair) # Define x as the larger of the two
    y = min(pair) # Define y as the smaller of the two
    results = {
        x+y: f"{x} + {y} = {x+y}",
        x*y: f"{x} * {y} = {x*y}",
        x-y: f"{x} - {y} = {x-y}"
    }
    if y != 0 and x%y == 0:
        results[int(x/y)] = f"{x} / {y} = {int(x/y)}"
    return {i: results[i] for i in results if i not in pair}

def solve(target, smalls, operations):
    """
    Recursive function that solves the game with target value of 'target'
    and available values stored in the list 'smalls'
    The 'operations' input is a list that stores the operations completed so far
    """
    if target in smalls:
        return operations + [str(target)]

    if not smalls:
        return []
    
    else:
        for c in combs(range(len(smalls)), 2):
            c = set(c)

            newsmalls = [i for j,i in enumerate(smalls) if j not in c]
            
            # First try by deleting the pair of numbers from the list entirely
            # i.e. not using them at all in the calculations

            new_ops = solve(target, newsmalls, operations)
            if new_ops:
                return new_ops
            
            # If that doesn't work, try by combining them using arithemtic
            pair = [smalls[i] for i in c]
            newvals = get_arithmetic(pair)
            
            for val in newvals: # For each possible operation
                result = val
                equation = newvals[val]
                new_ops = solve(target, newsmalls+[result], operations)
                if new_ops:
                    return new_ops + [equation]

    return []
                    
                    
def countdown(target, smalls):
    return solve(target, smalls, [])

