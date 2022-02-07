

def create_graph(preferences_matrix,waiting_nodes):
    """Arguments:
    preferences_matrix -- preferences matrix of each player
    waiting_nodes -- list of remaining players (nodes)

    Return:
    graph -- a dictionary representing directed graph created from waiting nodes based on preferences matrix
    """
    graph = dict()

    for v in waiting_nodes:
        for u in preferences_matrix[v]:
            if u in waiting_nodes:
                graph[v]=u
                break
    
    return graph

def find_cycle(graph:dict):
    """Arguments:
    graph -- a dictionary representing directed graph

    Return:
    cycle -- a dictionary representing cycle in given graph
    """
    
    stack = []

    v = list(graph.keys())[0]
    stack.append(v)

    u = None

    while True:
        u = graph[v]
        if u in stack:
            break

        stack.append(u)
        v = u
    
    temp = u
    cycle = dict()

    while stack:
        cycle[stack[-1]]=temp
        if stack[-1] == u:
            break

        temp = stack[-1]
        stack.pop()

    return cycle

def trading_cycle(preferences_matrix):
    """Arguments:
    preferences_matrix -- matrix of each player preference vector

    Return:
    matching -- a dictionary representing matching of players and rooms based on trading cycle algorithm
    """

    for i in range(len(preferences_matrix)):
        for j in range(len(preferences_matrix[i])):
            preferences_matrix[i][j] -= 1

    waiting_nodes = [i for i in range(len(preferences_matrix))]

    result = dict()

    while waiting_nodes:
        
        graph = create_graph(preferences_matrix,waiting_nodes)

        cycle = find_cycle(graph)

        result.update(cycle)

        for key in cycle:
            if key in waiting_nodes:
                waiting_nodes.remove(key)


    return {key+1:value+1 for key,value in result.items()}


if __name__ == "__main__":
    preferences_matrix = [[2,3,1,4,5,6,7],
                        [3,2,5,7,6,1,4],
                        [6,4,1,2,3,5,7],
                        [3,7,2,4,3,6,5],
                        [6,3,1,2,7,4,5],
                        [7,5,6,1,3,2,4],
                        [5,4,2,7,6,3,1]]

    result = trading_cycle(preferences_matrix)

    print("Student\tRoom")
    for key,value in result.items():
        print(f"{key}\t{value}")