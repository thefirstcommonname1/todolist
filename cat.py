CGREEN  = '\33[32m'
CEND = '\033[0m'
string = ""
count = 0
import sys
def get_status(array):
	total = 0
	count = 0
	for item in array:
		if item[0] == 'x' or item[0] == '*':
			total += 1
			if item[0] == 'x':
				count += 1
	return count / total
	
file_name = "Todo.txt"

with open(file_name) as file:
	file_list = file.readlines()
	index = file_list.index("Today\n")
	status = file_list[index:]
	count = get_status(status)
	for i in range(len(status)):
		if status[i][0] == 'x':
			status[i] = status[i][:-1] + " " + CGREEN + "✔" + CEND + "\n"
	string = "".join(status)
print("\nPercent completed: %.2f" % (count * 100))
print("\n"+string, end="")


