import sqlite3

def create_connection():
    conn = sqlite3.connect("workouts.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, last_name TEXT, age INTEGER, genre TEXT, weight INTEGER, height INTEGER);"
    ) 
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS exercises (id INTEGER PRIMARY KEY, name TEXT, muscle_group INTEGER, intensity TEXT);"
    ) 
    
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS loads (id INTEGER PRIMARY KEY, id_exercise INTEGER, id_user INTEGER, weight INTEGER, reps TEXT, rounds INTEGER);"
    ) 
    conn.close()
    
def add_users():
    conn = sqlite3.connect("workouts.db")
    cursor = conn.cursor()
    cursor.execute("INSERT  OR REPLACE  INTO users VALUES (1, 'Nathan', 'Samsoniuk', 23, 'masculino', 78, 1.80 )")
    cursor.execute("INSERT  OR REPLACE INTO users VALUES (2, 'Nicolas', 'Samsoniuk', 23, 'masculino', 70, 1.67 )")
    cursor.execute("INSERT  OR REPLACE INTO users VALUES (3, 'Vitor', 'Couto', 22, 'masculino', 80, 1.80 )")
    conn.commit()
    conn.close()
    
def add_exercises ():
    conn = sqlite3.connect("workouts.db")
    cursor = conn.cursor()
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (1, 'Agachamento', 'Perna', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (2, 'Bulgaro', 'Perna', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (3, 'Extensora', 'Perna', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (4, 'Flexora', 'Perna', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (5, 'Stiff', 'Perna', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (6, 'Supino Reto', 'Peito', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (7, 'Supino Inclinado', 'Peito', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (8, 'Croos Over PA', 'Peito', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (9, 'Croos Over PB', 'Peito', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (10, 'Crucifixo', 'Peito', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (11, 'Barra Fixa', 'Costas', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (12, 'Puxada Frente H', 'Costas', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (13, 'Remada curvada', 'Costas', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (14, 'Remada Cavalinho', 'Costas', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (15, 'Remada Baixa A', 'Costas', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (16, 'Pull Down', 'Costas', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (17, 'Corda', 'Braço', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (18, 'Francês', 'Braço', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (19, 'Testa', 'Braço', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (20, 'Rosca Direta', 'Braço', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (21, 'Rosca Inclinada', 'Braço', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (22, 'Martelo Corda', 'Braço', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (23, 'Desenvolvimento', 'Braço', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (24, 'Elevação Lateral', 'Braço', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (25, 'Elevação frontal Polia', 'Braço', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (26, 'Elevação Lateral Polia', 'Braço', 1 )")
    cursor.execute("INSERT   OR REPLACE  INTO exercises VALUES (27, 'Posterior de Ombro', 'Braço', 1 )")
    conn.commit()
    conn.close()

def add_loads ():
    conn = sqlite3.connect("workouts.db")
    cursor = conn.cursor()
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (1, 1, 1, 110,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (2, 2, 1, 35,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (3, 3, 1, 100,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (4, 4, 1, 70,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (5, 5, 1, 90,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (6, 6, 1, 60,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (7, 7, 1, 30,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (8, 8, 1, 20,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (9, 9, 1, 70,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (10, 10, 1, 15,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (11, 11, 1, 70,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (12, 12, 1, 80,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (13, 13, 1, 60,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (14, 14, 1, 100,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (15, 15, 1, 60,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (16, 16, 1, 60,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (17, 17, 1, 35,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (18, 18, 1, 9,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (19, 19, 1, 40,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (20, 20, 1, 9,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (21, 21, 1, 60,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (22, 22, 1, 60,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (23, 23, 1, 12,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (24, 24, 1, 30,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (25, 25, 1, 110,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (26, 26, 1, 10,'8-12', 4)")
    cursor.execute("INSERT   OR REPLACE  INTO loads VALUES (27, 27, 1, 10,'8-12', 4)")
    conn.commit()
    conn.close()

def list_all_tables():
    
    conn = sqlite3.connect("workouts.db")
    cursor = conn.cursor()
    tables = ['users', 'exercises', 'loads']
    for table in tables:
        cursor.execute('SELECT * FROM {}'.format(table))
        results = cursor.fetchall()

        for row in results:
            print(row)
        print()
    conn.close()

'''
#above the same code but as clean code

def list_all_tables():
    conn = sqlite3.connect("workouts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    for row in results:
        print(row)
    print()
    cursor.execute("SELECT * FROM exercises")
    resultados = cursor.fetchall()
    for row in results:
        print(row)
    print()
    cursor.execute("SELECT * FROM loads")
    resultados = cursor.fetchall()
    for row in results:
        print(row)
    conn.close()
'''

def list_users():
    conn = sqlite3.connect("workouts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    for row in results:
        print(row)
    print()

def list_exercises():
    conn = sqlite3.connect("workouts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM exercises")
    results = cursor.fetchall()
    for row in results:
        print(row)
    print()

def list_loads():
    conn = sqlite3.connect("workouts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM loads")
    results = cursor.fetchall()
    for row in results:
        print(row)
    print()


#create_connection()
#add_users()
#add_exercises()
#add_loads()

#list_all_tables()








