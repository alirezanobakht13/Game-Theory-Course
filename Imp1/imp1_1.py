from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpMinimize
import numpy as np

def two_player_zero_sum_game_minmax_value_and_strategies(game:list):
    """Argument:
        game -- payoff matrix of row player
    
    return: v,p,q
        v -- value of game
        p -- strategy of row player
        q -- strategy of column player
    """

    # --------------------- Linear Programming for row player -------------------- #

    lp_for_row_player = LpProblem(name="row_player",sense=LpMaximize)

    p = {i:LpVariable(name=f"p{i+1}",lowBound=0) for i in range(len(game))}
    v1 = LpVariable(name="v1")

    for i in range(len(game[0])):
        lp_for_row_player += (lpSum(float(game[j][i])*p[j] for j in range(len(game)))>=v1,f"constrain {i}")
    
    lp_for_row_player += (lpSum(p[i] for i in range(len(p)))==1.0)

    lp_for_row_player += v1

    status1 = lp_for_row_player.solve()


    # ------------------- Linear Programming for column player ------------------- #

    lp_for_column_player = LpProblem(name="column_player", sense=LpMinimize)

    q = {i:LpVariable(name=f"q{i+1}",lowBound=0) for i in range(len(game[0]))}
    v2 = LpVariable(name="v2")

    for i in range(len(game)):
        lp_for_column_player += (lpSum(float(game[i][j])*q[j] for j in range(len(game[0])))<=v2,f"constrain {i}")


    lp_for_column_player += (lpSum(q[i] for i in range(len(q)))==1.0)

    lp_for_column_player += v2

    status2 = lp_for_column_player.solve()

    return lp_for_row_player.variables()[-1].value(),\
            {var.name:var.value() for var in lp_for_row_player.variables()[:-1]},\
            {var.name:var.value() for var in lp_for_column_player.variables()[:-1]}



if __name__ == "__main__":

    
    game = [[1.0,2.0,3.0],
            [4.0,5.0,6.0],
            [7.0,8.0,9.0]]

    game2 = np.array([[1,1,1],[1,1,1],[1,1,1]])

    ## Create your custom game payoff matrix and pass to function below:

    v,p,q = two_player_zero_sum_game_minmax_value_and_strategies(game)


    print("matrix payoff:")
    print(np.array(game))
    print()
    print(f"Optimal Value: {v}")
    print("Optimal strategy for row player:")
    print(p)
    print("Optimal strategy for column player:")
    print(q)
