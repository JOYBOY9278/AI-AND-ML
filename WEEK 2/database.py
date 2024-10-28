import sqlite3
conn = sqlite3.connect('company.db')
print("opened database successfully")
conn.execute('''CREATE TABLE EMPLOYEE13
             (ID INT PRIMARY KEY NOT NULL,
              NAME TEXT NOT NULL,
              AGE INT NOT NULL,
              ADDRESS CHAR(50),
              SALARY REAL);''')
print("table created successfully")

conn.execute("INSERT INTO EMPLOYEE13 (ID,NAME,AGE,ADDRESS,SALARY)\
VALUES(1,'AKASH','50','AFRICA','100.00')");
conn.execute("INSERT INTO EMPLOYEE13 (ID,NAME,AGE,ADDRESS,SALARY)\
VALUES(2,'YASHU','55','CANADA','10000.00')");
conn.execute("INSERT INTO EMPLOYEE13 (ID,NAME,AGE,ADDRESS,SALARY)\
VALUES(3,'LUKMAN','60','SOUDI AREBIA','1000.00')");
conn.execute("INSERT INTO EMPLOYEE13 (ID,NAME,AGE,ADDRESS,SALARY)\
VALUES(4,'DARSHAN','25','UGANDA','200.00')");
conn.execute("INSERT INTO EMPLOYEE13 (ID,NAME,AGE,ADDRESS,SALARY)\
VALUES(5,'ROHITH','66','PAKISTHAN','300.00')");
conn.commit()
print("records created successfully")
resultset=conn.execute("SELECT id,name,age,address,salary from EMPLOYEE13")
for row in resultset:
    print("ID=",row[0])
    print("NAME=",row[1])
    print("AGE=",row[2])
    print("ADDRESS=",row[3])
    print("SALARY=",row[4],"\n")
print("operation done successfully")
conn.close()
