""" prepro """
def main():
    """ function """
    matrix = list()
    row, col = int(input()), int(input())

    for _ in range(row):
        matrix.append([])
        for _ in range(col):
            matrix[-1].append(int(input()))

    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()
main()
