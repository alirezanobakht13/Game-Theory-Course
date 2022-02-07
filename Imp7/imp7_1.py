
from copy import deepcopy

def stable_mariage(boys_preferences_matrix,girls_preferences_matrix,boy_optimal=True):
    """Arguments:
    boys_preferences_matrix -- boys_preferences_matrix[i] is vector of rank of girls for boy i
    girls_preferences_matrix -- girls_preferences_matrix[i] is vector of rank of boys for girl i
    boy_optimal -- if True return boy optimal matching and if false return girl optimal matching

    Return:
    Result -- list of tuple which each one contains a match between a boy and a girl
    """

    if not boy_optimal:
        boys_preferences_matrix,girls_preferences_matrix = girls_preferences_matrix,boys_preferences_matrix


    boys_count = len(boys_preferences_matrix)
    girls_count = len(girls_preferences_matrix)

    for i in range(boys_count):
        for j in range(len(boys_preferences_matrix[i])):
            boys_preferences_matrix[i][j] -= 1

    for i in range(girls_count):
        for j in range(len(girls_preferences_matrix[i])):
            girls_preferences_matrix[i][j] -= 1
    
    free_boys = [i for i in range(boys_count)]

    boy_priority = {i:0 for i in range(boys_count)}

    request_to_girls = {i:[] for i in range(girls_count)}

    while free_boys:
        for i in free_boys:
            request_to_girls[boys_preferences_matrix[i][boy_priority[i]]].append(i)
        
        for i in range(girls_count):
            if not request_to_girls[i]:
                continue
            elif len(request_to_girls[i])==1:
                if request_to_girls[i][0] in free_boys:
                    free_boys.remove(request_to_girls[i][0])
            else:
                best = request_to_girls[i][0]
                for j in request_to_girls[i]:
                    if girls_preferences_matrix[i].index(j)<girls_preferences_matrix[i].index(best):
                        best = j
                
                request_to_girls[i].remove(best)

                for j in request_to_girls[i]:
                    boy_priority[j]+=1
                    if j not in free_boys:
                        free_boys.append(j)
                
                request_to_girls[i]=[best,]
                if best in free_boys:
                    free_boys.remove(best)
    
    result = []
    for key,value in request_to_girls.items():
        if boy_optimal:
            result.append((value[0]+1,key+1))
        else:
            result.append((key+1,value[0]+1))

    return result


if __name__ == "__main__":


    ## exmaple from https://www.codechef.com/problems/STABLEMP. use your own example if you want
    girls_preferences_matrix = [[4,3,1,2],
                                [2,1,3,4],
                                [1,3,4,2],
                                [4,3,2,1]]

    boys_preferences_matrix = [[3,2,4,1],
                                [2,3,1,4],
                                [3,1,2,4],
                                [3,2,4,1]]

    boy_optimal_matching = stable_mariage(deepcopy(boys_preferences_matrix),deepcopy(girls_preferences_matrix))
    girl_optimal_matching = stable_mariage(deepcopy(boys_preferences_matrix),deepcopy(girls_preferences_matrix),boy_optimal=False)

    print("boy optimal matching:")
    print("boy\tgirl")
    for m in boy_optimal_matching:
        print(f"{m[0]}\t{m[1]}")

    print()
    print("girl optimal matching:")
    print("boy\tgirl")
    for m in girl_optimal_matching:
        print(f"{m[0]}\t{m[1]}")