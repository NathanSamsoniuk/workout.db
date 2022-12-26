import fill_loads as fl
import sqlite3

_name = input(f'Qual o seu nome ou seu código?')

conn = sqlite3.connect("workouts.db")

sql = "SELECT * FROM users WHERE upper(name) = ?"
cursor = conn.execute(sql, (_name.upper(),))

for row in cursor:
	print(row)
	for col in row:
		print(col)


'''
fl.create_connection()
fl.add_users()
fl.add_exercises()
fl.add_loads()
fl.list_all_tables()
'''
