import sqlite3
import os


def open_db():
    
    
    path = os.environ.get("HOME")+"/Library/Messages/"
    os.chdir(path)
    con = sqlite3.connect('chat.db')
    return con

def execute_query():
    con = open_db()
    cur = con.cursor()
    query_result = cur.execute(
    "SELECT m.rowid, h.id, m.text, datetime((m.date / 1000000000) + 978307200, 'unixepoch', 'localtime') as TextDate, m.is_from_me FROM message as m, handle as h on m.handle_id = h.rowid WHERE m.text like '..%' ORDER BY DATE DESC LIMIT 1"
    )
    query_results = tuple(query_result.fetchone())
    con.close()

    os.chdir(os.environ.get('HEFTYFISH_PROJECT_LOCATION'))
    return query_results
