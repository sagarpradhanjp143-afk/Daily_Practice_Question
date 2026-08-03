nums = [1,2,4,5,6,7,8,9,8,7,5,4]

def func(arr, left, right):
    if left >= right:
        return

    arr[left], arr[right] = arr[right], arr[left]

    func(arr, left + 1, right - 1)

func(nums, 1,7)

print(nums)