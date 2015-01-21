NEGINF = -10**20
def solve(matrix,n):
    box = [[NEGINF for j in range(n)] for i in range(n)]
    box[0][0] = matrix[0][0]
    for i in range(1,n):
        for j in range(i+1): 
            if j-1 >= 0:
                box[i][j] = max(box[i-1][j-1],box[i-1][j]) + matrix[i][j]
            else:
                box[i][j] = box[i-1][j] + matrix[i][j]
   
    maximum = NEGINF 
    for j in range(n):
        if box[n-1][j] > maximum:
            maximum = box[n-1][j]
    return maximum


#matrix = [[1,],[1,4],[2,3,5],[1,2,3,4]]
def main():
    n = int(raw_input())
    while n!=0:
        nol = int(raw_input())
        matrix = [[] for i in range(nol)] 
        for i in range(nol):
	    ip=raw_input().split()
            for value in ip:
                matrix[i].append(int(value))
            
        print solve(matrix,nol)

        n = n - 1 

main()
        
            
            
