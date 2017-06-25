## Gradient Algorithm for N by M game.




def best_response(g,b,ret = False):
    '''
    Takes the Gameboard G and converts it into Expressions A1 through An to maximize
    For Best Response
    g[first_player][second_player] = u(F,S) for FP
    b is the second player's move.
    '''
    expressions = []
    m = len(g)
    n = len(g[0])
    
    for i in range(0,m): # iterate through a
        # i = probability of playing strategy
        expected_value = 0
        for r in range(0,n): # interate through b
            move_weight = b[r]
            
            expected_value += move_weight * g[i][r]
        expressions.append(expected_value)
    #print expressions
    c =  max(expressions)
    idx = expressions.index(c)
    m = [0 for i in range(0,m)]
    m[idx] += 1 # Pure Strategy Best Response!
    if not ret:
        return c
    else:
        return c,m # if you need the best response itself.
    
    
def gradient_search(g,m,n):
    # we are optimizing b, which is 2nd player with a vector of size n.
    #Minimize p1
    epsilon = 0.001
    current_vector = [1] + [0 for i in range(0,n-1)]
    prev = float("inf")
    current_response = best_response(g,current_vector) # start with pure strategy nash equilibrium
    while abs(prev-current_response) > epsilon:
        print "Current Optimal Table: %s, expected value of %s"%(current_vector,round(current_response,6))
        prev = current_response
        optimal = [current_response,current_vector]
        # Decrease one strategy by epsilon, increase another since they need to sum to 1.
        for decrease_index in range(0,n):
            for increase_index in range(0,n):
                if decrease_index != increase_index and (current_vector[decrease_index] - epsilon) >= 0  and (current_vector[increase_index] + epsilon) <= 1:
                    new_vector = list(current_vector)
                    new_vector[decrease_index] -= epsilon
                    new_vector[increase_index] += epsilon
                    new_response = best_response(g,new_vector)
                    if new_response < optimal[0]:
                        optimal = [new_response,new_vector]
        current_response = optimal[0]
        current_vector = optimal[1]
    print "Found A Nash Equilibria(For P2 B) at %s"%(current_vector)
    return current_vector,current_response
