def main():
    num_lines = int(input())
    input_data = ""
    data = []
    for i in range(num_lines):
        temp = str(input())
        data += [temp.split(" ")]

    for j in data:
        total = 0
        for k in j:
            total += int(k)
        if total == 180:
            print("Seems OK")
        else:
            print("Check")
    
  

main()
