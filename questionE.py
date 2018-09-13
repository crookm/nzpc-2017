def main():
  num_bytes = int(input())

  bytes = []
  for i in range(num_bytes):
    bytes.append(input().split(" "))

  parity = input().split(" ")

  num_odd = 0
  num_even = 0

  for byte in bytes:
    evenodd = byte.count("1") % 2
    if evenodd == 1: num_odd += 1
    else: num_even += 1

  even = True if num_even > num_odd else False

  broken_byte = 0
  i = 0
  for byte in bytes:
    i += 1
    evenodd = "".join(byte).count("1") % 2
    broken_byte = i if evenodd != (0 if even else 1) else broken_byte
  
  print()
  broken_bit = 0
  for i in range(8):
    print("i =", i, "--", end=' ')
    res = []
    for j in range(num_bytes):
      res.append(bytes[j][i])
    res.append(parity[i])
    
    evenodd = "".join(res).count("1") % 2
    broken_bit = i+1 if evenodd != (0 if even else 1) else broken_bit

  if even: print("Even")
  else: print("Odd")
  
  print("Byte {} is broken".format(broken_byte))
  print("Bit {} is broken".format(broken_bit))

main()
