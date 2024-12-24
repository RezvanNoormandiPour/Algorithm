def find_subsets_with_sum(nums, target, start=0, current_subset=[]):
    if sum(current_subset) == target:
        print(" ".join(map(str, current_subset)))
        return
    
    if sum(current_subset) > target:
        return
    
   
    for i in range(start, len(nums)):
        current_subset.append(nums[i])
        find_subsets_with_sum(nums, target, i + 1, current_subset)
        current_subset.pop()

W = int(input())
numbers = list(map(int, input().split()))

if not find_subsets_with_sum(numbers, W):
    print("هیچ پاسخی یافت نشد")
            
