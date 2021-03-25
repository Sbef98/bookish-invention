import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        return conn
    
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def select_all_rows(conn, table_name):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + table_name)

    rows = cur.fetchall()

    return rows

def add_row(conn, table_name, table_columns, values_to_insert):
    """
    Create a new task
    :param conn: a valida database connection
    :param table_name: string, the name of the table
    :param tables_columns: tuple of strings, the list of columns to write
    :param values_to_insert: tuple of strings, the list of values to insert in the new rows' columns
    :return: stuff
    """
    #building insert
    sql = "INSERT INTO " + table_name + " ("

    for i in range(len(table_columns)):
        sql = sql + table_columns[i]
        if i != len(table_columns) - 1:
            sql += ","
    sql += ") VALUES("
    for i in range(len(table_columns)):
        sql += "?"
        if i != len(table_columns) - 1:
            sql += ","
    sql += ")"

    #committing insertion
    cur = conn.cursor()
    cur.execute(sql, values_to_insert)
    conn.commit()

    return cur.lastrowid

if __name__ == '__main__':

    db = r".\Database\instadms.db"
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """
    conn = create_connection(db)
    if conn is not None:
        # create projects table
        #create_table(conn, sql_create_projects_table)
        #add_row(conn, "projects", ["name", "begin_date", "end_date"], ["soccmel", "21-02-03", "foreverly infinite"])
        rows = select_all_rows(conn,"ciao")
        for row in rows:
            print(row)
    else:
        print("Error! cannot create the database connection.")