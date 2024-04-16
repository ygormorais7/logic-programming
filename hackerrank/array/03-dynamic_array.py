def dynamicArray(n, queries):
    arr = []
    lastAnswer = 0
    arr_answer = []
    
    for query in queries:
        x = int(str(query)[2])
        y = int(str(query)[4])
        idx = (x ^ lastAnswer) % n
        
        if str(query)[0] == "1":
            arr[idx].append(y)
        else:
            lastAnswer = arr[idx][y % len(arr[idx])]
            arr_answer.append(lastAnswer)
            
    return arr_answer


def dynamicArray2(n, queries):
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    arr_answer = []
    
    for query in (queries):
        op, x, y = query
        idx = (x ^ lastAnswer) % n
        
        if op == 1:
            arr[idx].append(y)
        else:
            lastAnswer = arr[idx][y % len(arr[idx])]
            arr_answer.append(lastAnswer)
            
    return arr_answer