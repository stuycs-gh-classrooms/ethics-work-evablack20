def sum67(nums):
  in67 = False
  i = 0
  sum = 0
  while i < len(nums):
    if nums[i]==6 and not in67:
      in67 = True
      i += 1
      continue
    if in67 and nums[i]==7:
      in67 = False
      i += 1
      continue
    if not in67:
      sum += nums[i]
    i +=1
  return sum
