def sum13(nums):
  i = 0
  sum = 0
  while i < len(nums):
    if nums[i]==13: 
      i+=2
      continue
    else:
      sum += nums[i]
      i += 1
  return sum
