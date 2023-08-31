import psycopg2 as db

conn = db.connect(host="localhost", dbname="RIOC", user="postgres", password="", port=5432)

cur = conn.cursor()

cur.execute("""INSERT INTO public.persona(idpersona, nombre, cedula) 
            VALUES (1, 'Nuggets', '7848827-7'); 
""")

conn.commit()
cur.close()
conn.close()
