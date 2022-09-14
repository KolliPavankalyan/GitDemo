from csv import DictWriter,DictReader

with open("fun.py") as file:
	dict_file = DictReader(file)
	print((dict_file))