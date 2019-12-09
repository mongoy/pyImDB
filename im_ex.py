import sqlite3
import pyodbc
import csv

# подключение к MSSQL
server = 'BUDA\\SQLEXPRESS'
database = 'LISTIM2015'
username = 'sa'
password = 'IwB1966Y'
con_str = 'DRIVER={SQL Server Native Client 11.0}; SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + \
          ';PWD=' + password
conn = pyodbc.connect(con_str)

# подключение к SQLite
conn2 = sqlite3.connect('db.sqlite3')


def mig_main_list():
    try:
        # MSSQL
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM AllGuimFull_C')

        # SQLite
        cursor2 = conn2.cursor()
        # cursor2.execute(
        #     ''' CREATE TABLE IF NOT EXISTS AllGuimFull
        #             (
        #             nnp INTEGER,
        #             obj INTEGER,
        #             cobj INTEGER,
        #             mobj TEXT,
        #             naim TEXT,
        #             mat TEXT,
        #             lp NUMERIC,
        #             addr TEXT,
        #             prot REAL,
        #             invnum TEXT,
        #             idnum TEXT,
        #             bals REAL,
        #             balost REAL,
        #             okof TEXT,
        #             norma NUMERIC,
        #             gramort NUMERIC,
        #             byear TEXT,
        #             prim TEXT,
        #             primper TEXT,
        #             ops TEXT,
        #             pasportbti TEXT,
        #             zemnum TEXT,
        #             numgosreg TEXT,
        #             disl TEXT,
        #             piket REAL,
        #             piketb REAL,
        #             pikete REAL,
        #             pmobj NUMERIC,
        #             pernum NUMERIC,
        #             onbal INTEGER,
        #             prewriteoff INTEGER,
        #             assignment INTEGER,
        #             datain TEXT,
        #             docin TEXT,
        #             dataout TEXT,
        #             docout TEXT,
        #             inform TEXT,
        #             most1 REAL, am1 REAL, most2 REAL, am2 REAL,
        #             most3 REAL, am3 REAL, most4 REAL, am4 REAL,
        #             most5 REAL, am5 REAL, most6 REAL, am6 REAL,
        #             most7 REAL, am7 REAL, most8 REAL, am8 REAL,
        #             most9 REAL, am9 REAL, most10 REAL, am10 REAL,
        #             most11 REAL, am11 REAL, most12 REAL, am12 REAL,
        #             most13 REAL, am13 REAL,
        #             ybase TEXT,
        #             cat2 TEXT,
        #             cat3 TEXT,
        #             cat4 TEXT,
        #             cat5 TEXT,
        #             cat6 TEXT
        #             )
        #         '''
        # )
        # reader = csv.reader(open('expdata1.csv', 'r'), delimiter=';')
        # print(reader)
        # for row in reader:
        # to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8")]
        # curs.execute("INSERT INTO PCFC (type, term, definition) VALUES (?, ?, ?);", to_db)
        rows = cursor.fetchall()
        str_q = 'INSERT INTO AllGuimFull VALUES(' + ','.join(['?' for _ in range(69)]) + ')'
        cursor2.executemany(str_q, ([[(row[i]) for i in range(69)] for row in rows]))
        # str_q = 'INSERT INTO AllGuimFull VALUES(' + ','.join(['?' for _ in range(10)]) + ')'
        # cursor2.executemany(str_q, ([[(rw[i]) for i in range(10)] for rw in row]))

    except sqlite3.DatabaseError as err:
        print("Error: ", err)
    else:
        conn2.commit()
        conn2.close()
    return


# mig_main_list()

def mig_rd_list():

    return

# mig_rd_list()
