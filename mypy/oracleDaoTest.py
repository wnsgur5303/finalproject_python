import serial
import string
import cx_Oracle
import requests


def makeDictFactory(cursor):
   columnNames = [d[0] for d in cursor.description]
 
 
   def createRow(*args):
      return dict(zip(columnNames, args))
 

   return createRow

port = 'COM3'
brate = 115200 #boudrate
cmd = 'temp'

seri = serial.Serial(port, baudrate = brate, timeout = None)
print(seri.name)

seri.write(cmd.encode())

a = 1
while a:
    if seri.in_waiting != 0 :
        content1 = seri.readline()
        content2 = content1[:-2].decode().split('/')
        print(content1[:-2].decode())
#       print(content2[1])
        print(content2[0],content2[1],content2[2],content2[3])
#       URL = 'http://192.168.0.117/springboard/board/addBoard?addboardname='+content2[0]
#       response = requests.get(URL)
#       response.status_code
#       response.text
        
        
        conn=cx_Oracle.connect("team3_202008f/java@112.220.114.130:1521/xe")
        cursor=conn.cursor() #커서 생성
        sql="insert into msrrec values(seq_msrrec.nextval,:1,sysdate,:2,:3,:4)"
        data=(content2[0],content2[1],content2[2],content2[3])
        cursor.execute(sql,data)
        cursor.close()
        conn.commit()
        conn.close()
        
