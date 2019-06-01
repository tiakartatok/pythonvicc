from prettytable import PrettyTable

list = ["Biosz", "Töri", "Magyar"]

list2 = ["1", "5", "4"]
table = PrettyTable(["Tantargy, Biosz, Töri, Magyar"])



for x in range(0,4):
	table.add_row([list[x],list2[x]])
print(table)