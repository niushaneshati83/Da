
def merge_and_count(arr, temp_arr, left, mid, right,n):
    i = left    
    j = mid + 1 
    k = left    
    inv_count = 0
    o =0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
            o=o+1
        else:
            temp_arr[k] = arr[j]
            inv_count = inv_count + mid 
            inv_count = inv_count -i 
            inv_count = inv_count + 1
            j += 1
            o=o+1
        k += 1 
        o=1+o
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
        o=1+o
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
        o=1+o

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
        o+=1
       
    return inv_count

def func_merge(arr, temp_arr, left, right,n):
    inv_count = 0
    o =0
    o=1+o
    if left < right: 
        mid = left  
        mid = mid + right
        mid = mid // 2
        inv_count =inv_count + func_merge(arr, temp_arr, left, mid,0 )+func_merge(arr, temp_arr, mid + 1, right,0)
        inv_count =inv_count + merge_and_count(arr, temp_arr, left, mid, right,0)
        o=1+o

    return inv_count

def count_inversions(arr,n):
    temp_arr = [0] * n
    o =0
    return func_merge(arr, temp_arr, 0, n - 1)
    o=o+1


input_1=input()
n_ = int(input_1) 
input_2=input().split()
arr = []
for i in range(n_):
    o =0
    arr.append(int(input_2[i]))
    o=o+1
temp_arr = [0] * n_

print(func_merge(arr, temp_arr, 0, n_ - 1,0))