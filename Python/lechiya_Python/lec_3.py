# функция

# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res

# print(sum_str('q','e','l'))
# print(sum_str('q','e','l','qf','er','lc'))

# модули

# def max1 (a, b):
#     if a > b:
#         return a
#     return b

# рекурсия

# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)


# list1 = []
# for i in range(1, 10):
#     list1.append(fib(i))
# print(list1)


# алгаритм быстрая сортировка

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array [1:] if i <= pivot]
#     greater = [i for i in array [1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort([2,34,7,1,23,45,65,21,87,6,78,9,5,8,67,3]))


# алгоритм сортировка слиянием

def merge_sort(nums): 
    if len(nums) > 1:
        mid = len(nums) // 2 
        left = nums[:mid] 
        right = nums[mid:] 
        merge_sort(left) 
        merge_sort(right) 
        i=j=k=0
        while i < len(left) and j < len(right): 
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1 
            else:
                nums[k] = right[j]
                j += 1 
            k += 1
        while i < len(left): 
            nums[k] = left[i] 
            i += 1
            k += 1
        while j < len(right): 
            nums[k] = right[j] 
            j += 1
            k += 1


nums = [38, 27, 43, 3, 9, 82, 10] 
merge_sort(nums)
print(nums)

