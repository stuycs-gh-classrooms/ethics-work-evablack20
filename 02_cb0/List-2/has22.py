def has22(nums):
  nextTo2 = False
  for i in nums:
    if i == 2:
      if nextTo2 == True:
        return True
      nextTo2 = True
    else:
      nextTo2 = False
  return False

