import pymysql
def query(q):
    con = pymysql.connect(
        host='localhost', 
        user='root',
        password='street31012000', 
        database='hospital')
    cur = con.cursor()
    result = cur.execute(q)
    con.commit()
    con.close()
    return cur, result;