def play_game(chairs, data):
	players_remain = len(chairs)
	for i in data:
		for j in range(int(i[1])):
			for player in chairs:
				if chairs[player] == len(chairs):
					chairs[player] = 1
				else:
					chairs[player] += 1
		remove_player(chairs, i[0])
	player_string = ""
	for player in chairs:
		if len(chairs) == 1:
			print(player + " has won.")
			return
		else:
			player_string += " " + player
	
	print("Players left are " + player_string)
			
def remove_player(chairs, value):
	for player in chairs:
		if int(chairs[player]) == int(value):
			print(player + " has been eliminated.")
			old = chairs.pop(player)
			#print(chairs)
			return reset_chairs(chairs, old)

def reset_chairs(chairs, old):
	count = 1
	for player in chairs:
		if (chairs[player] > old):
			chairs[player] -= 1
			if (chairs[player] > len(chairs)):
				chairs[player] = 1
	return chairs
	

def get_players_chairs(names):
	count = 1
	assigned = {}
	for name in names:
		assigned[name] = count
		count += 1
		
	return assigned

def main():
	num_lines = int(input())
	input_data = ""
	names = []
	for i in range(num_lines):
		temp = str(input())
		names.append(temp)
	num_lines = int(input())
	data = []
	for i in range(num_lines):
		temp = str(input())
		temp_2 = temp.split(" ")
		data += [temp_2]
		
	chairs = get_players_chairs(names)
	play_game(chairs, data)

main()