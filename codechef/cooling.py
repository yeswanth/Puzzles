def result(pies, weights):
    count = 0
    i,j = (len(pies)-1, len(weights)-1)
    while i >= 0 and j >= 0: 
        #Whether to rotate or not
        if weights[j] - pies[i] >= 0:
            count = count + 1
            i = i - 1 
            j = j - 1
        else:
            i = i - 1

    return count


def rotate(pies, weights):
    return pies, weights

def main():
    t = int(raw_input())
    for i in range(t):
        n = int(raw_input()) 
        input1 = raw_input()
        input2 = raw_input()
        pies = [int(i) for i in input1.split()]
        weights = [int(i) for i in input2.split()]
        pies.sort()
        weights.sort()
        print result(pies,weights)
    

if __name__ == '__main__':
    main()
