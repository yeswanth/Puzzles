def main():
    n = int(raw_input())
    for i in range(n):
        val = int(raw_input())
        if val % 2 == 0:
            print val 
        else:
            print val - 1 
main()
