def main():
	num_scenarios = int(input())
	radius = 0
	num_lines = str(input())
	temp = num_lines.split(" ")
	data = []
	radius = int(temp[0])
	
	for i in range(int(temp[1])):
		temp = str(input())
		temp_2 = temp.split(" ")
		data += temp_2
		
	print("Num scenarios " + str(num_scenarios))
	print("radius " + str(radius))
	print(data)
	
main()