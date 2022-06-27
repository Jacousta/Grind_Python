from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Chirag", "Mitul"])
table.add_column("Type", ["Electric", "Human", "Animal"])
table.align = "l"
print(table)
