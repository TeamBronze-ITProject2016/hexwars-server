import sqlite3, json
from flask import Flask, g

DATABASE = '/var/www/hexwars/hexwars/hexwars.db'

app = Flask(__name__)

@app.route('/hexwars')
def index():
    c = get_db().cursor()
    c.execute('''SELECT name, score FROM scores ORDER BY score DESC''')
    result = c.fetchall()
    c.close()
    return json.dumps(result)

@app.route('/hexwars/<name>/<score>')
def update(name, score):
    # set up the queries
    insert = '''INSERT INTO scores VALUES (?, ?)'''
    update = '''UPDATE scores SET score = ? WHERE name = ?'''
    get_name = '''SELECT COUNT(*) FROM scores WHERE name = ?'''

    # Check if name already exists, if so, update it
    c = get_db().cursor()
    c.execute(get_name, [name])
    count = c.fetchall()[0][0]
    if count is not 0:
        c.execute(update, [score, name])
    else:
        c.execute(insert, [name, score])

    get_db().commit()
    get_db().close()
    return '200'

@app.route('/remove/all')
def remove():
    remove = '''DELETE FROM scores'''
    c = get_db().cursor()
    c.execute(remove)
    get_db().commit()
    get_db().close()
    return '200'

@app.route('/remove/<name>')
def remove_one(name):
    remove = '''DELETE FROM scores WHERE name = ?'''
    c = get_db().cursor()
    c.execute(remove, [name])
    get_db().commit()
    get_db().close
    return '200'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        c = db.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS scores (name text, score int)''')
        db.commit()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0")

