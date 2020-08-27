# quick sort는 pivot를 이용한 정렬방법
# pivot은 기준 값이고 pivot을 기준으로 작은 값 그룹, 큰 값 그룹으로 나눈다.
# 그 다음 작은 그룹을 동일한 방식으로 정렬, 큰 그룹을 동일 방식으로 정렬
# 최종 합친다.

# 이해하기 쉬운 방법
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


def quick_sort(arr):
    # 재귀함수이며, 정렬 범위를 시작인덱스와 끝 인덱스로 받는다
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            # 시작 인덱스가 가리키는 값과 pivot 값을 비교해서 더 작은 경우 반복해서 시작 인덱스값을 증가
            # pivot 값보다 큰데 좌측에 있는 값을 찾기 위해
            while arr[low] < pivot:
                low += 1
            # 끝 인덱스가 가리키는 값과 pivot 값을 비교해서 더 큰 경우 반복해서 끝 인덱스가 감소
            #  pivot 값보다 작은데 우측에 있는 값을 찾기 위해
            while arr[high] > pivot:
                high -= 1
            # 두 인덱스가 아직 서로 교차해서 지나치치 않았다면 시작인덱스가 가리키는 값과 끝 인덱스가 가리키는 값을
            # 바꿔줍니다. (잘못된 위치의 두 값을 바꾸기위해)
            # 바꾼 후, 다음 값을 가리키기 위해 두 인덱스를 각자 진행방향으로 한칸 씩 이동시킵니다.
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        # 다음 재귀 호출의 분할 기준이 될 시작 인덱스를 리턴합니다.
        return low
    return sort(0, len(arr) - 1)
