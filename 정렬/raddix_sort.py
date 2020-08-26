
def countingSort(arr, digit):
    n = len(arr)

    # 배열이 크기에 맞는 result 배열을 생성하고 10개의 0을 가진 count 배열을 생성한다.
    result = [0] * n
    count = [0] * 10

    # digit, 자릿수에 맞는 count 배열 인덱스값에 += 1을 한다.
    for i in range(n):
        index = int(arr[i]/digit)
        count[(index % 10)] += 1

    # count 배열을 이용해 digit(자릿수)로 잡은 result 포지션을 설정한다.
    for i in range(9):
        count[i+1] += count[i]

    for i in range(n-1, -1, -1):
        index = int(arr[i]/digit)
        result[count[(index % 10)] - 1] = arr[i]
        count[(index % 10)] -= 1

    for i in range(n):
        arr[i] = result[i]



def radixSort(arr):
    # arr배열 안에 있는 수 중 max값을 찾는다. 다음 주어진 배열에서는 802가 max값이다.
    # 자릿수 반복을 결정하는 과정이다. 802는 3자리이므로 3번 반복
    maxNum = max(arr)
    # 자릿수마다 counting sort를 시작한다
    digit = 1  # 1의 자리수부터 시작
    while int(maxNum/digit) > 0:
        countingSort(arr, digit)
        digit *= 10 # 10의 자리, 100의 자리로 자릿수를 올려주는 용도이다.

arr = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr)