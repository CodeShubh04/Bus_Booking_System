import sqlite3
con=sqlite3.connect("Shubhanshi's DB")
cur=con.cursor()
'''
cur.execute('create table bus(BusId int primary key,BusType varchar(20),Capacity int,Fare int,OpId int,RouteId int)')
cur.execute('insert into bus(BusId,BusType,Capacity,Fare,OpId,RouteId) values(1,"AC 2x2",30,1000,1,1) , (2,"AC 3x2",50,800,1,2) , (3,"Non AC 2x2",30,600,1,3) , (4,"Non AC 3x2",30,600,1,4)')


cur.execute('create table operator(OpertorId int primary key,Name varchar(20),Address varchar(20),Phone int,Email varchar(20))')
cur.execute('insert into operator(OpertorId,Name,Address,Phone,Email) values(1,"Kamla","AB road Guna",12345,"kamlabus@gmail.com"),(2,"Rayeen","AB road Guna",12346,"rayeen@gmail.com"),(3,"Kalyani","Hauj Khas Delhi",12347,"kalyani@gmail.com"),(4,"Mahakaal","AB road Jhansi",12348,"mahakaal@gmail.com")')


cur.execute('create table route(RouteId int primary key,SId int,StationName varchar(20))')
cur.execute('insert into route(RouteId,SId,StationName) values(1,1,"guna"),(1,2,"JP College"),(1,3,"Binagunj"),(1,4,"Biora"),(1,5,"Bhopal"),(2,1,"Bhopal"),(2,2,"Biora"),(2,3,"Binagunj"),(2,4,"JP College",(2,5,"Guna"),(3,1,"Delhi"),(3,2,"Agra"),(3,3,"Jhansi"),(3,4,"Shivpuri"),(3,5,"Guna"),(3,6,"JP College"),(3,7,"Binagunj"),(3,8,"Biora"),(3,9,"Bhopal"),(4,1,"Bhopal"),(4,2,"Biora"),(4,3,"Binagunj"),(4,4,"JP College"),(4,5,"Guna"),(4,6,"Shivpuri"),(4,7,"Jhansi"),(4,8,"Agra"),(4,9,"Delhi")')


cur.execute('create table runs(BusId int,RunsDate date,SeatAvail int,foreign key(BusId) references Bus_Details(BusId))')
cur.execute('insert into runs(BusId,RunsDate,SeatAvail) values(1,"2022-09-20",30),(1,"2022-09-21",30),(1,"2022-09-22",30),(1,"2022-09-23",30),(2,"2022-09-20",30),(2,"2022-09-21",30),(2,"2022-09-22",30),(2,"2022-09-23",30),(3,"2022-09-20",30),(3,"2022-09-21",30),(3,"2022-09-22",30),(3,"2022-09-23",30),(4,"2022-09-20",30),(4,"2022-09-21",30),(4,"2022-09-22",30),(4,"2022-09-23",30)')


cur.execute('create table BookingHistory(Ref_no int primary key,Passenger varchar(20),PassengerDetails varchar(20),No_of_seats int,BookingDate date,JourneyDate date,From varchar(20),To varchar(20))')
cur.execute('ALTER TABLE route RENAME COLUMN "to" TO "destination" ')
cur.execute('ALTER TABLE route RENAME COLUMN "from" TO "source" ')
'''

print(cur.execute('select * from bus').fetchall())
print(cur.execute('select * from operator').fetchall())
print(cur.execute('select * from route').fetchall())
print(cur.execute('select * from runs').fetchall())
result=cur.fetchall()
print(result)
con.commit()
