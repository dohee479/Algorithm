# counting_sort

# A : input array
# k : A배열 안에 최대 값
def counting_sort(A, k):
    # 결과 배열
    result_array = [0] * len(A)

    # counting array
    counting_array = [0] * (k + 1)

    # A 배열 안에 숫자 개수를 카운팅하여 counting_array 안에 배정
    for num in A:
        counting_array[num] += 1
    print(counting_array)

    # 인덱스 0에 있는 개수를 인덱스 1에 개수와 더하여 인덱스 1에 배정, 이 과정 반복(1 -> 2)
    for num in range(k):
        counting_array[num+1] += counting_array[num]
    print(counting_array)
    # result_array 에 반영
    for index in range(len(A), -1, -1):
        result_array[counting_array[A[index]] - 1] = A[index]
        counting_array[A[index]] -= 1

    return result_array

A = [2, 0, 2, 0, 4, 1, 5, 5, 2, 0, 2, 4, 0, 4, 0, 3]
print(counting_sort(A, max(A)))