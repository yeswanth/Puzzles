class ChestNut(object):
    def __init__(self,start_time,interval):
        self.start_time = start_time
        self.interval = interval


def solve(n,m,k,trees):
    matrix = [[]]

def main():
    t = int(raw_input())
    for i in range(t):
        n,m,k = map(int,raw_input().split(" "))
        trees = []
        for i in range(m):
            start_time, interval = raw_input().split(" ")
            tree = ChestNut(start_time,interval)
            trees.append(tree)

if __name__ == '__main__':
    main()
