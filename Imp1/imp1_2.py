import numpy as np
from imp1_1 import two_player_zero_sum_game_minmax_value_and_strategies as zero_sum

def two_player_general_sum_game(row_player,column_player):
    """Arguments:
        row_player -- payoff matrix of row player
        column_player -- payoff matrix of column player
    
    return:
        agreement_point -- tuple that contains agreement point
        profit_sharing -- tuple that show how to share profit
        p --  threat strategy of row player
        q --  threat strategy of column player
    """


    row_player = np.array(row_player,dtype=np.float32)
    column_player = np.array(column_player,dtype=np.float32)

    sum_matrix = row_player + column_player

    agreement_value = np.max(sum_matrix)
    agreement_point = tuple(np.unravel_index(np.argmax(sum_matrix),sum_matrix.shape) +\
                        np.array([1,1]))

    sub_matrix = row_player - column_player

    v,p,q = zero_sum(sub_matrix)

    profit_sharing = ((agreement_value+v)/2,(agreement_value-v)/2)
    
    return agreement_point,\
            profit_sharing,\
            p,\
            q






if __name__ == "__main__":
    
    row_player = [[-3,2,0,1],
                [2,2,-3,1],
                [2,-5,-1,1],
                [-4,2,1,-3]]
    
    column_player = [[-4,-1,6,1],
                [0,2,0,-2],
                [-3,1,-1,-3],
                [3,-5,2,1]]
    
    agreement_point,profit_sharing,p,q=two_player_general_sum_game(row_player,column_player)

    print(f"agreement point: {agreement_point}")
    print(f"profit of row player: {profit_sharing[0]} || profit of column player: {profit_sharing[1]}")
    print(f"threat strategy for row player: {p}")
    print(f"threat strategy for column player: {q}")