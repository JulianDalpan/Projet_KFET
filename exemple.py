import sqlite3
from sqlite3 import Error
from pathlib import Path
import datetime
databaseName = "ants.db"
 
def connectBase():
    ''' return a connector to the database.
        if the database does not exist, it will be created.
    '''
    try:
        file = Path(databaseName)
        if file.exists ():
            conn = sqlite3.connect(databaseName)
            conn.row_factory = lambda c, r: dict(
            [(col[0], r[idx]) for idx, col in enumerate(c.description)])
            return conn
        conn = createBase()
        return conn
    except:
        return False


def createBase():
    ''' create the database with the table ROBOTS


        ROBOT is the table of the robot
            .id          as int
            .x         as int
            .y     as int

            
        PHEROMONE is the table of pheromone
            .id      as int
            .idRob   as int
            .x      as int
            .y      as int


        MOVE is the table of move
            .id     as int
            .move   as int
        '''

    #création de la base
    try:
        conn = sqlite3.connect(databaseName)
    except Error as e:
        return False
    
    c = conn.cursor()
    c.execute('''CREATE TABLE ROBOTS (
                        id     integer,
                        x      integer,
                        y      integer,
                        t      integer,
                        a      integer
                                     )''')
    c.execute('''CREATE TABLE PHEROMONE (
                        id        integer,
                        idRob     integer,
                        x         integer,
                        y         integer
                                     )''')
    c.execute('''CREATE TABLE MOVE (
                        id     integer,
                        move      integer
                                     )''')

    conn.commit()
    return conn

def moveto(id,move):
    with connectBase() as conn:   
        c = conn.cursor()
        #and now, insert 'new' record (really new or not)
        rSQL = '''INSERT INTO MOVE (id,move)
                        VALUES ('{}','{}') ; '''

        c.execute(rSQL.format(id, move))
        conn.commit()
     
     
def addRobot(id,x,y,t,a):
    with connectBase() as conn:   
        c = conn.cursor()

        rSQL = '''DELETE FROM ROBOTS WHERE id = '{}'
                                           AND x = '{}'
                                           AND y='{}';'''
        c.execute(rSQL.format(id, x, y))

        #and now, insert 'new' record (really new or not)
        rSQL = '''INSERT INTO ROBOTS (id, x, y,t,a)
                        VALUES ('{}','{}','{}','{}','{}') ; '''

        c.execute(rSQL.format(id, x, y,t,a))
        conn.commit()

        #c.execute(''' SELECT * FROM ROBOTS''')
        #line=c.fetchall()
        #yield line
def addPhero(id,idRob,x,y):

    with connectBase() as conn:   
        c = conn.cursor()
        rSQL = '''DELETE FROM PHEROMONE WHERE id = '{}';'''
        c.execute(rSQL.format(id))
        #and now, insert 'new' record (really new or not)
        rSQL = '''INSERT INTO PHEROMONE (id, idRob, x, y)
                        VALUES ('{}','{}','{}','{}') ; '''

        c.execute(rSQL.format(id, idRob, x, y))
        conn.commit()


def getrobot(id):
    with connectBase() as conn:   
        c = conn.cursor()
        rSQL='''SELECT * FROM ROBOTS WHERE id="{}" ORDER BY rowid DESC LIMIT 1;'''
        c.execute(rSQL.format(id))
        line=c.fetchall()
        yield line 


def getArrive(a):
    with connectBase() as conn:   
        c = conn.cursor()
        rSQL='''SELECT id FROM ROBOTS WHERE a="{}";'''
        c.execute(rSQL.format(a))
        line=c.fetchall()
        yield line 

def getPhero():
    with connectBase() as conn:   
        c = conn.cursor()
        rSQL='''SELECT * FROM PHEROMONE;'''
        c.execute(rSQL)
        line=c.fetchall()
        yield line 

def getmove(id):
    with connectBase() as conn:   
        c = conn.cursor()
        rSQL='''SELECT move FROM MOVE WHERE id="{}" ORDER BY rowid DESC LIMIT 1;'''
        c.execute(rSQL.format(id))
        line=c.fetchall()
        yield line