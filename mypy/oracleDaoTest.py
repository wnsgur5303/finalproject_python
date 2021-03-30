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
while True:
    if seri.in_waiting != 0 :
        content1 = seri.readline()
        content2 = content1[:-2].decode().split('/')
        print(content1[:-2].decode())
        print(content2[0],content2[1],content2[2],content2[3])
        #서버를 통해 데이터넣기
        URL = 'http://192.168.0.126/finalProject/fdata/addData?msr_code='+content2[0]+'&msr_temp='+content2[1]+'&msr_humid='+content2[2]+'&msr_bright='+content2[3]
        response = requests.get(URL)
        response.status_code
        response.text
        
        #직접 db에 넣기
#         conn=cx_Oracle.connect("team3_202008f/java@112.220.114.130:1521/xe")
#         cursor=conn.cursor() #커서 생성
#         sql="insert into mserec values(seq_mserec.nextval,:1,sysdate,:2,:3,:4)"
#         data=(content2[0],content2[1],content2[2],content2[3])
#         cursor.execute(sql,data)
#         cursor.close()
#         conn.commit()
#         conn.close()
        
