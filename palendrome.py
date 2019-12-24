import math

def is_pal(num):
  num_str = str(num)
  is_pal = False

  for val in range(math.floor(len(num_str)/2) - 1):
    end_pos = -1 - val

    print('end_pos is', end_pos)

    if x[val] == x[end_pos]:
      is_pal = True
    else: 
      is_pal = False

  return is_pal

print(is_pal(22))