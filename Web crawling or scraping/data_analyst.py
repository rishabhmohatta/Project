import csv
import mysql.connector
mydb11 = mysql.connector.connect(
host='localhost',user='root',password='root'
)

mycursor = mydb11.cursor()
mycursor.execute("CREATE DATABASE edulab")
mycursor.execute("USE edulab")
mycursor.execute("create table data_analyst_ncr(id int primary key auto_increment,company_name varchar(100),experience varchar(80),jdescp varchar(150),job_description_link varchar(500),job_title varchar(100),keyskills varchar(150),salary varchar(80),DoU varchar(100))")
mycursor.execute("create table location_jobs(lid int auto_increment,jid int,location varchar(40),primary key(lid,jid),foreign key(jid) references data_analyst_ncr(id))")
mycursor.execute("create table scraped( jobid int primary key auto_increment,company_name varchar(100),experience varchar(80),jdescp varchar(150),job_description_link varchar(500),job_title varchar(100),keyskills varchar(150),location varchar(100),salary varchar(80)")
mycursor.execute("alter table data_analyst_ncr add auto_increment = 0 ")
with open('data_analytic.csv','r') as file:
    csv_data = csv.reader(file)
    n = 0
    count = 0
    for row in csv_data:
        
       try :
          mycursor.execute('INSERT INTO data_analyst_ncr(id,company_name,experience,jdescp,job_description_link,job_title,keyskills,salary,dou) values(0,"'+row[0]+'","'+row[1]+'","'+row[2]+'","'+row[3]+'","'+row[4]+'","'+row[5]+'","'+row[7]+'",curdate())')
          mycursor.execute('INSERT INTO scraped(jobid,company_name,experience,jdescp,job_description_link,job_title,keyskills,location,salary) values(0,"'+row[0]+'","'+row[1]+'","'+row[2]+'","'+row[3]+'","'+row[4]+'","'+row[5]+'","'+row[6]+'","'+row[7]+'")')
       
       
          row2 = row[6].split(",")
          for row3 in row2:
             location = row3.split(",")
             print(location)
             
             for i in location:
                mycursor.execute('select jobid from scraped where location in ('+i+')')
                for r in mycursor.fetchall():
                   s = str(r)
                   mycursor.execute('insert into location_jobs(lid,jid,location)values(0,'+s+',"'+i+'")')   
       except IndexError:
          pass  
mydb11.commit()
mycursor.close()
print("Done")
