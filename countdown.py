from itertools import combinations as combs
#Solves the number game from countdown
#Given any input values

def get_arithmetic(pair, frac=False):
    '''
    Given a tuple pair of numbers, returns a list of all possible
    values that can be gotten using simple arithmetic operations
    on the input numbers
    '''

    x = pair[0]
    y = pair[1]
    if x*y == 0:
        return [x+y, 0, x-y]
    else:
        if frac:
            return [x+y, x*y, x-y, x/y, y/x]
        else:
            if x%y == 0:
                return [x+y, x*y, x-y, int(x/y)]
            else:
                return [x+y, x*y, x-y]

def solve(target, smalls, frac=False):
    "target is the target value, smalls is a list of small values to be used"
    n = len(smalls)
    ix = list(range(n))
    smalls.sort()
    global operations
    if target in smalls:
        print(target)
        operations.append(target)
        return 1
    
    else:
        newsmalls = []
        for c in combs(ix, 2):
            smallscopy = smalls.copy()
            smallscopy2 = smalls.copy()
            smallscopy3 = smalls.copy()
            c = list(c)
            c.sort(reverse=True)
            
            # First try by deleting the pair of numbers from the list entirely
            # i.e. not using them at all in the calculations
            
            del smallscopy3[c[0]]
            del smallscopy3[c[1]]
            if solve(target, smallscopy3, frac) == 1:
                return 1
            
            # If this doesnt work, try by combining them using arithemtic
            
            pair = [smalls[i] for i in c]
            newvals = get_arithmetic(pair, frac)
            del smallscopy[c[0]]
            del smallscopy[c[1]]
            
            for num,val in enumerate(newvals): # For each possible operation
                if solve(target, smallscopy+[val], frac) == 1:
                    if num==0:
                        print(smallscopy2[c[0]],'+',smallscopy2[c[1]],'=',val)
                        operations.append(str(smallscopy2[c[0]])+
                                          '+'+str(smallscopy2[c[1]])+
                                          '='+str(val))
                    elif num==1:
                        print(smallscopy2[c[0]],'*',smallscopy2[c[1]],'=',val)
                        operations.append(str(smallscopy2[c[0]])+
                                          '*'+str(smallscopy2[c[1]])+
                                          '='+str(val))
                    elif num==2:
                        print(smallscopy2[c[0]],'-',smallscopy2[c[1]],'=',val)
                        operations.append(str(smallscopy2[c[0]])+
                                          '-'+str(smallscopy2[c[1]])+
                                          '='+str(val))
                    elif num==3:
                        print(smallscopy2[c[0]],'/',smallscopy2[c[1]],'=',val)
                        operations.append(str(smallscopy2[c[0]])+
                                          '/'+str(smallscopy2[c[1]])+
                                          '='+str(val))
                    else:
                        print(smallscopy2[c[1]],'/',smallscopy2[c[0]],'=',val)
                        operations.append(str(smallscopy2[c[1]])+
                                          '/'+str(smallscopy2[c[0]])+
                                          '='+str(val))
                    return 1
                    
                    
def countdown(target, smalls, frac=False):
    global operations
    operations=[]
    solve(target, smalls, frac)

