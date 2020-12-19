import MySQLdb as mysql
from bs4 import BeautifulSoup as soup

db  = mysql.connect("localhost","root", "admin", "dict", charset="utf8" )

cursor  = db.cursor()

cursor.execute("select version()")

data = cursor.fetchone()

print(data)
#parse file
source = open("/root/mysql/seg")
soup = soup(source)
results = soup.find_all(class_="dictionary_intro")
for result in results:
    print(type(result))
sql = """insert into word(name,phonogram, positive) values("mac", "mac", "mac")"""

try:
    cursor.execute(sql)
    #db.commit()
    print("success")
except Exception as e:
    db.rollback()
    print("fail")
    print(repr(e))

db.close()
