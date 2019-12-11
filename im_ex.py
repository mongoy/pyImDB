import sqlite3
import pyodbc
import csv
from xlsxwriter.workbook import Workbook

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

def filing_rd_list():
    try:
        # MSSQL
        cursor = conn.cursor()
        cursor.execute("""
            SELECT RDList.naim, 
            SUM(AllGuimFull_C.bals) AS sum_bal, 
            SUM(AllGuimFull_C.balost) AS sum_ost,
            SUM(AllGuimFull_C.balost1) AS expr1,
            SUM(AllGuimFull_C.amort1) AS expr2,
            SUM(AllGuimFull_C.balost2) AS expr3,
            SUM(AllGuimFull_C.amort2) AS expr4,
            SUM(AllGuimFull_C.balost3) AS expr5,
            SUM(AllGuimFull_C.amort3) AS expr6,
            SUM(AllGuimFull_C.balost4) AS expr7,
            SUM(AllGuimFull_C.amort4) AS expr8,
            SUM(AllGuimFull_C.balost5) AS expr9,
            SUM(AllGuimFull_C.amort5) AS expr10,
            SUM(AllGuimFull_C.balost6) AS expr11,
            SUM(AllGuimFull_C.amort6) AS expr12,
            SUM(AllGuimFull_C.balost7) AS expr13,
            SUM(AllGuimFull_C.amort7) AS expr14,
            SUM(AllGuimFull_C.balost8) AS expr15,
            SUM(AllGuimFull_C.amort8) AS expr16,
            SUM(AllGuimFull_C.balost9) AS expr17,
            SUM(AllGuimFull_C.amort9) AS expr18,
            SUM(AllGuimFull_C.balost10) AS expr19,
            SUM(AllGuimFull_C.amort10) AS expr20,
            SUM(AllGuimFull_C.balost11) AS expr21,
            SUM(AllGuimFull_C.amort11) AS expr22,
            SUM(AllGuimFull_C.balost12) AS expr23,
            SUM(AllGuimFull_C.amort12) AS expr24,
            SUM(AllGuimFull_C.balost13) AS expr25,
            SUM(AllGuimFull_C.amort13) AS expr26
            FROM RDList
            INNER JOIN AllGuimFull_C
            ON RDList.naim = AllGuimFull_C.mobj
            GROUP BY RDList.naim
            ORDER BY RDList.naim
        """)

        rows = cursor.fetchall()
        sum_bal = 0
        for row in rows:
            # SQLite
            cursor2 = conn2.cursor()
            str_q = f"UPDATE RDList SET bals = {round(row[1], 2)}, osts = {round(row[27], 2)} WHERE naim = '{row[0]}'"
            print(str_q)
            cursor2.execute(str_q)
            conn2.commit()

    except sqlite3.DatabaseError as err:
        print("Error: ", err)
    else:

        conn2.close()

    return


# filing_rd_list()

def sum_fin_list():
    # проверка суммы балансовой и остаточной
    try:
        cursor2 = conn2.cursor()
        str_q = "SELECT SUM (bals) AS sum_bal, SUM(osts) AS sum_ost FROM RDList"
        cursor2.execute(str_q)
        row = cursor2.fetchone()
        if row:
            print(row)


    except sqlite3.DatabaseError as err:
        print("Error: ", err)
    else:
        conn2.close()

    return


# sum_fin_list()


def xls_io():
    workbook = Workbook('output2.xlsx')
    worksheet = workbook.add_worksheet()

    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    mysel = c.execute("select * from RDList")
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i, j, row[j])
    workbook.close()
    return


#xls_io()


def edt_rd_list():
    try:
        cursor2 = conn2.cursor()
        str_q = "SELECT * FROM AllGuimFull"
        #str_q = "SELECT naim, idnum, invnum FROM RDList"
        mysel = cursor2.execute(str_q)
        row = cursor2.fetchone()
        if row:
            print(row)


    except sqlite3.DatabaseError as err:
        print("Error: ", err)
    else:
        conn2.close()

    return

