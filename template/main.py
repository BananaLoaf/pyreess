import numpy as np


def main():
    arr = np.zeros((11, 11))
    for i in range(11):
        arr[i, i] = 1
        arr[i, -i-1] = 1

    print(arr)


if __name__ == '__main__':
    main()
