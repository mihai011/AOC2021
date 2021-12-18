import math 

def read_input():

  with open("input.txt") as f:
    data = f.read() 

  binary = ''
  for c in data:
    c = c.lower()
    int_value = int(c, base=16)
    bin_value = bin(int_value)[2:]
    bin_value = bin_value.rjust(4, '0')
    binary += bin_value
  return binary


def check_greater(values):

  if values[0] > values[1]:
    return 1

  return 0
  
def check_less(values):

  if values[0] < values[1]:
    return 1

  return 0

def check_equal(values):

  if values[0] == values[1]:
    return 1

  return 0

def literal(binary):

  values = []
  for i in range(0, len(binary), 5):
    group = binary[i:i+5]
    values.append(group[1:])
    if group[0] == '0':
      break
  values = ''.join(values)

  return int(values, base=2), i+4

version = 0
operations = {0:sum, 1:math.prod, 2:min, 3:max, 5:check_greater,\
   6:check_less, 7:check_equal}

def process(binary, t):
  global version

  total_length = len(binary)
  values = []
  while len(binary) > 6:
    version += int(binary[:3], base=2)
    type_id = binary[3:6]
    type_id = int(type_id, base=2)
    if type_id == 4:
      value, index = literal(binary[6:])
      binary = binary[index+7:]
      values.append(value)
    else:
      if binary[6] == '0':
        slice = binary[7:22]
        if len(slice) < 6:
          break
        length = int(slice, base=2)
        if len(values) > 1:
          values = [operations[t](values)]
        value, length = process(binary[22:22+length], type_id)
        if len(value) > 1:
          value = operations[type_id](value)
        binary = binary[22+length:]
        values.append(value)
      else:
        packets = int(binary[7:18], base=2)
        if len(values) > 1:
          values = [operations[t](values)]
        for i in range(packets):
          value, length = process(binary[18:], type_id)
          binary = binary[18+length:]
          if len(value) > 1:
            value = operations[type_id if t == None else t](value)
          values.append(value)


  # filter empty lists
  values = list(filter(lambda l : l!=[], values))
  return values, total_length
  

if __name__ == "__main__":

  data = read_input()
  values, length = process(data, None)
  print(version)
  print(values)