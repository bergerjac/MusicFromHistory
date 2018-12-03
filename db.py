import sqlite3

def setUp_database(db_address):
    conn = sqlite3.connect(db_address)
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS videos')
    c.execute('CREATE TABLE videos (date text, video_name text, video_id text, video_url text)')
    conn.commit()

def saveVideo(db_address, date, name, id, url):
    conn = sqlite3.connect(db_address)
    c = conn.cursor()
    name = name.replace("'","").replace('"', '')
    query = "INSERT INTO videos VALUES ('{0}', '{1}', '{2}', '{3}')".format(date, name, id, url)
    print(query)
    c.execute(query)
    conn.commit()