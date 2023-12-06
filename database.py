import sqlite3
from sqlite3 import Error
from pathlib import Path
from datetime import datetime

#Global definition
databaseName = "KFET.db"


#Create Database KFET.db
class DatabaseConnector:
    def __init__(self, database_name):
        self.database_name = database_name
        self.conn = None

    def __enter__(self):
        try:
            file = Path(self.database_name)
            if file.exists():
                self.conn = sqlite3.connect(self.database_name)
                self.conn.row_factory = lambda c, r: dict(
                    [(col[0], r[idx]) for idx, col in enumerate(c.description)])
                return self.conn
            self.conn = self.create_database()
            return self.conn
        except:
            return None

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()

    def create_database(self):
        try:
            conn = sqlite3.connect(self.database_name)
        except Error as e:
            return None

        c = conn.cursor()
        c.execute('''CREATE TABLE ITEM (
                        name        text,
                        price       integer,
                        quantity    integer,
                        purchasedprice   integer
                    )''')
        print('table ITEM créé ..............' )

        c.execute('''CREATE TABLE SALE (
                        product     integer,
                        price       integer,
                        quantity    integer,
                        time        integer,
                        team       integer
                    )''')
        print('table SALE créé ..............' )
        conn.commit()
        return conn

#Add an Item to the table ITEM
def addItems(name, price, quantity,purchased_price):
    with DatabaseConnector(databaseName) as conn:
        if conn:
            c = conn.cursor()
            rSQL = '''DELETE FROM ITEM WHERE name = '{}';'''
            c.execute(rSQL.format(name))
            rSQL = '''INSERT INTO ITEM (name, price, quantity, purchasedprice )
                      VALUES ('{}','{}', '{}','{}'); '''.format(name, price, quantity,purchased_price)
            c.execute(rSQL)
            conn.commit()

def getpurchased_price(name):
    with DatabaseConnector(databaseName) as conn:
        if conn:
            c = conn.cursor()
            rSQL='''SELECT purchasedprice FROM ITEM WHERE name="{}";'''.format(name)
            c.execute(rSQL)
            line=c.fetchall()
            return line 
            conn.commit() 
   
def getStock(name):
    with DatabaseConnector(databaseName) as conn:
        if conn: 
            c = conn.cursor()
            rSQL='''SELECT quantity FROM ITEM WHERE name="{}";'''
            c.execute(rSQL.format(name))
            line=c.fetchall()
            return line 
        
def getPrice(name):
    with DatabaseConnector(databaseName) as conn:
        if conn: 
            c = conn.cursor()
            rSQL='''SELECT price FROM ITEM WHERE name="{}";'''
            c.execute(rSQL.format(name))
            line=c.fetchall()
            return line 
        
def addSales(product,price,quantity,time,team):
    with DatabaseConnector(databaseName) as conn:
        if conn:
            c = conn.cursor()
            rSQL = '''INSERT INTO SALE (product, price, quantity, time, team) VALUES ('{}', '{}', '{}','{}','{}'); '''.format(product, price, quantity,time,team)
            c.execute(rSQL)
            conn.commit()

def getAll(): 
    with DatabaseConnector(databaseName) as conn:
        if conn: 
            c = conn.cursor()
            rSQL='''SELECT * FROM ITEM ;'''
            c.execute(rSQL)
            line=c.fetchall()
            return line 
        
def getALLSale():
    with DatabaseConnector(databaseName) as conn:
        if conn: 
            c = conn.cursor()
            rSQL='''SELECT * FROM SALE WHERE DATE(time) = DATE('now');'''
            c.execute(rSQL)
            line=c.fetchall()
            return line 
        
def getLastSale():
    with DatabaseConnector(databaseName) as conn:
        if conn: 
            c = conn.cursor()
            rSQL='''SELECT * FROM SALE ORDER BY rowid DESC LIMIT 1;'''
            c.execute(rSQL)
            line=c.fetchall()
            return line 
        
def getAllItem():
    with DatabaseConnector(databaseName) as conn:
        if conn: 
            c = conn.cursor()
            rSQL='''SELECT name FROM ITEM ;'''
            c.execute(rSQL)
            line=c.fetchall()
            return line 

def getItemSale(name):
    with DatabaseConnector(databaseName) as conn:
        if conn: 
            c = conn.cursor()
            rSQL='''SELECT * FROM SALE WHERE product="{}" AND DATE(time) = DATE('now');'''
            c.execute(rSQL.format(name))
            line=c.fetchall()
            return line 
    