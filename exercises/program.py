def nStarTriangle(n : int) -> None: 
    for i in range(1, n + 1):
        for j in range(0, (n - i)):
            print(" ", end = "") 
        for k in range(0, (2 * i) - 1):
            print("*", end = "") 
        for l in range(0, (n - i)): 
            print(" ", end = "")
        print(" ")

nStarTriangle(5) 
