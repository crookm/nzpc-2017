values = {
	"A": 1,
	"B": 2,
	"C": 3,
	"D": 4,
	"E": 5,
	"F": 6,
	"G": 7}
acceptable_difference = [2, 4, 6]

def check_notes(notes):
	last_note = ""
	for note in notes:
		if last_note == "":
			last_note = note
		else:
			difference = values[note] - values[last_note]
			print(abs(difference))
			if abs(difference) not in acceptable_difference:
				print("Ouch! That hurts my ears!")
				return
			else:
				last_note = note
	print("That music is beautiful!")
	
def main():
	num_lines = int(input())
	input_data = ""
	data = []
	for i in range(num_lines):
		temp = str(input())
		data += [temp]
	
	for notes in data:
		if (len(notes) == 1):
			print("That music is beautiful!")
		else:
			check_notes(notes)

main()