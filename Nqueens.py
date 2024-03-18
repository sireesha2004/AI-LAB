def printSolution(X):
    print(" _ "*len(X))
    for i in range(1,len(X)):
        print('| ', end='')
        for j in range(1, len(X)):
            if X[i] == j:
                print(' Q ', end='')
            else:
                print(' . ', end='')
        print('|')
    print()


def place(X, k, i):
    for j in range(1,k):
        if X[j] == i or abs(j-k) == abs(X[j] - i):
            return False
    return True

def NQueens(X, k, N):
    for i in range(1, len(X)):
        if place(X, k, i):
            X[k] = i

            if k == N:
                print(X[1:])
                printSolution(X)
            else:
                NQueens(X, k+1, N)

if __name__ == "__main__":
    N = int(input("Enter the number of Queens: "))

    X = [0] * (N+1)

    NQueens(X, 1, N)
