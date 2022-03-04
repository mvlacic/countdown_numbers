// Solves the number game from countdown
// Given any input values

function get_arithmetic_results(v1, v2){
    /**
    Given a tuple pair of numbers, returns a dictionary where each key is
    an integer value that can be calculated using simple arithmetic operations
    on the input numbers, and the associated value is the corresponding equation string

    The function works such that if the inputs are both non-negative, then
    all the results will also be non-negative
    **/

    var x = Math.max(v1,v2); // Define x as the larger of the two
    var y = Math.min(v1,v2); // Define y as the smaller of the two
    var results = new Object();

    results[x+y] = `${x} + ${y} = ${x+y}`;
    results[x*y] = `${x} * ${y} = ${x*y}`;
    results[x-y] = `${x} - ${y} = ${x-y}`;

    if (y != 0 && x%y == 0){
        results[x/y] = `${x} / ${y} = ${x/y}`;
    }


    return results;
};


function solve(target, smalls, operations){
    /*
    Recursive function that solves the game with target value of 'target'
    and available values stored in the list 'smalls'
    The 'operations' input is a list that stores the operations completed so far
    */

    if (smalls.length == 0){
        return [];
    };
    
    if (smalls.includes(target)){
        return [target.toString(10)].concat(operations);
    }

    else {
        for (let i = 0; i < smalls.length - 1; i++){
            for (let j = i + 1; j < smalls.length; j++){
                let newsmalls = [...smalls];
                newsmalls.splice(j,1);
                newsmalls.splice(i,1);

                let new_ops = solve(target, newsmalls, operations);
                if (new_ops.length > 0){
                    return new_ops;
                }

                let results = get_arithmetic_results(smalls[j], smalls[i]);
                for (const [result, equation] of Object.entries(results)){

                    let new_ops = solve(target, newsmalls.concat([parseInt(result)]), operations);
                    if (new_ops.length > 0){
                        return [equation].concat(new_ops);
                    }
                }


            }
        }

    }
    return [];
};


