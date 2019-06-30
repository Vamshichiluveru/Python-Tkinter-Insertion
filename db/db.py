import mysql.connector
import sys

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="testing"
)

cursor = con.cursor()

#make a function to access the db
def user_login(tup):
    try:
        cursor.execute("SELECT * FROM `admin` WHERE `email`=%s AND `password`=%s",tup)
        return cursor.fetchone()
    except:
        return False

def add_income(tup):
    cursor.execute("INSERT INTO `income`(`income_source`,`description`) values(%s,%s)",tup)
    con.commit()
    return True
