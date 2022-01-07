def min_max(n,*nums):
    max=n
    min=n
    for i in range(0,len(nums)):
        if nums[i] > max:
            max=nums[i]
        if nums[i] < min:
            min=nums[i]
    return max,min

max,min=min_max(1,2,3,4,5)
print(f'最大{max},最小{min}')
max,min=min_max(1)
print(f'最大{max},最小{min}')
