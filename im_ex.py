import sqlite3
import pyodbc


def mig_rdlist():
    # подключение к MSSQL
    server = 'BUDA\\SQLEXPRESS'
    database = 'LISTIM2015'
    username = 'sa'
    password = 'IwB1966Y'
    con_str = 'DRIVER={SQL Server Native Client 11.0}; SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + \
              ';PWD=' + password
    conn = pyodbc.connect(con_str)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM RDList ORDER BY naim')

    # SQLite RDList
    conn2 = sqlite3.connect('db.sqlite3')
    cursor2 = conn2.cursor()
    cursor2.execute(
        ''' CREATE TABLE IF NOT EXISTS RDList
            (
             naim text, 
             prot FLOAT,
             invnum text,
             idnum text,
             bals FLOAT,
             osts FLOAT,
             cod text,
             amgroup NUMERIC,
             norma NUMERIC,
             byear NUMERIC,
             pikets text
            )
        '''
    )
    rows = cursor.fetchall()
    str_q = 'INSERT INTO RDList VALUES(' + ','.join(['?' for _ in range(11)]) + ')'
    cursor2.executemany(str_q, ([[(row[i]) for i in range(11)] for row in rows]))
    conn2.commit()

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM RDList ORDER BY naim')

    # SQLite RDListIO
    conn2 = sqlite3.connect('db.sqlite3')
    cursor2 = conn2.cursor()
    cursor2.execute(
        ''' CREATE TABLE IF NOT EXISTS RDListIO
            (
             naim text, 
             prot FLOAT,
             invnum text,
             idnum text,
             bals FLOAT,
             osts FLOAT,
             cod text,
             amgroup NUMERIC,
             norma NUMERIC,
             byear NUMERIC,
             pikets text,
             most1 FLOAT, am1 FLOAT, most2 FLOAT, am2 FLOAT, most3 FLOAT, am3 FLOAT, most4 FLOAT, am4 FLOAT,
             most5 FLOAT, am5 FLOAT, most6 FLOAT, am6 FLOAT, most7 FLOAT, am7 FLOAT, most8 FLOAT, am8 FLOAT,
             most9 FLOAT, am9 FLOAT, most10 FLOAT, am10 FLOAT, most11 FLOAT, am11 FLOAT, most12 FLOAT, am12 FLOAT,
             most13 FLOAT, am13 FLOAT
            )
        '''
    )

    rows = cursor.fetchall()
    str_q = 'INSERT INTO RDListIO VALUES(' + ','.join(['?' for _ in range(37)]) + ')'
    cursor2.executemany(str_q, ([[(row[i]) for i in range(37)] for row in rows]))

    conn2.commit()
    conn2.close()
    return


# создаем таблици RDList и RDListIO
# mig_rdlist()

def mig_main_list():
    # подключение к MSSQL
    server = 'BUDA\\SQLEXPRESS'
    database = 'LISTIM2015'
    username = 'sa'
    password = 'IwB1966Y'
    con_str = 'DRIVER={SQL Server Native Client 11.0}; SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + \
              ';PWD=' + password
    conn = pyodbc.connect(con_str)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM AllGuimFull')


    # SQLite AllGuimFull
    conn2 = sqlite3.connect('db.sqlite3')

    cursor2 = conn2.cursor()
    cursor2.execute(
        ''' CREATE TABLE IF NOT EXISTS AllGuimFull
            (
            nnp NUMERIC,
            obj NUMERIC,
            cobj NUMERIC,
            mobj text, 
            naim text,
            mat text, 
            lp NUMERIC,
            addr text,
            prot FLOAT,     
            invnum text,
            idnum text
            )
        '''
    )

# база Sqlite
    rows = cursor.fetchall()
    str_q = 'INSERT INTO AllGuimFull VALUES(' + ','.join(['?' for _ in range(11)]) + ')'
    print(str_q)
    #print([[(row[i]) for i in range(65)] for row in rows])
    # f = open('text.txt', 'w')
    # for row in rows:
    #     for i in range(65):
    #         f.write(str(row[i]) + ', ')
    #     f.write('\n')
    # f.close()
    cursor.executemany(str_q, ([[(row[i]) for i in range(11)] for row in rows]))

    conn2.commit()
    conn2.close()

    return

mig_main_list()


def up_rd_list_io():
    # подключение к MSSQL
    server = 'BUDA\\SQLEXPRESS'
    database = 'LISTIM2015'
    username = 'sa'
    password = 'IwB1966Y'
    con_str = 'DRIVER={SQL Server Native Client 11.0}; SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + \
              ';PWD=' + password
    conn = pyodbc.connect(con_str)
    cursor = conn.cursor()
    str_q = "SELECT RDList.naim FROM RDList \
    , sum(AllGuimFull.bals) AS sum_bal \
    , SUM(AllGuimFull.balost) AS sum_ost \
    INNER JOIN AllGuimFull \
    ON RDList.naim = AllGuimFull.mobj \
    GROUP BY RDList.naim ORDER BY RDList.naim"
    print(str_q)
    cursor.execute(str_q)
    rows1 = cursor.fetchall()

    return


#
#up_rd_list_io()
