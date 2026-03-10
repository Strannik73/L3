import pymssql
import credits as cr

conn = pymssql.connect(cr.server, cr.user, cr.password, cr.db)
cursor = conn.cursor()
 
cursor.execute("""
    USE TEST1
    
    CREATE TABLE groups_cnyz48(
        group_id INT IDENTITY(1000, 1),
        Name NVARCHAR(5),
        PRIMARY KEY (group_id)
    )          

    CREATE TABLE cnyz48(
        id INT IDENTITY(1,1) PRIMARY KEY,
        name NVARCHAR(20), 
        group_id INT,
        FOREIGN KEY (group_id) REFERENCES groups_cnyz48 (group_id)
    )
      
    INSERT INTO groups_cnyz48 VALUES ('GR1')           
    INSERT INTO cnyz48 VALUES ('IVAN', 1000)
""")


    # USE TEST1
    
    #1. CREATE TABLE groups_cnyz48(
    #     group_id INT IDENTITY(1000, 1),
    #     Name NVARCHAR(5),
    #     PRIMARY KEY (group_id)
    # )

    #2. CREATE TABLE cnyz48(
    #     id INT IDENTITY(1,1) PRIMARY KEY,
    #     name NVARCHAR(20), 
    #     group_id INT,
    #     FOREIGN KEY (group_id) REFERENCES groups_cnyz48 (group_id)
    # )
               
    #3. INSERT INTO groups_cnyz48 VALUES ('GR1')           
    #4. INSERT INTO cnyz48 VALUES ('IVAN', 1000)

for row in cursor:
    print(row)
# print(cursor.fetchone())
# print(cursor.fetchall())


conn.commit()

conn.close()




===============================================================

import pymssql
import credits as cr

conn = pymssql.connect(cr.server, cr.user, cr.password, cr.db)
cursor = conn.cursor()
 
cursor.execute("""
    USE TEST1

    IF OBJECT_ID('TABL_cnyz48', 'U') IS NOT NULL DROP TABLE TABL_cnyz48;
               

    CREATE TABLE TABL_cnyz48(
        id INT IDENTITY(1,1) PRIMARY KEY,
        Cn_Matherboard INT, 
        Cn_CPU INT,
        Cn_RAM INT,
        Cn_GPU INT,   
        Cn_Storage INT,
        Cn_PowerUnit INT,
        Cn_Cases INT,
        constraint FK_Cn_Matherboard foreign key (Cn_Matherboard) references Cn_Matherboard(ID),
        constraint FK_Cn_CPU foreign key (Cn_CPU) references Cn_CPU(ID),
        constraint FK_Cn_RAM foreign key (Cn_RAM) references Cn_RAM(ID),
        constraint FK_Cn_GPU foreign key (Cn_GPU) references Cn_GPU(ID),
        constraint FK_Cn_Storage foreign key (Cn_Storage) references Cn_Storage(ID),
        constraint FK_Cn_PowerUnit foreign key (Cn_PowerUnit) references Cn_PowerUnit(ID),
        constraint FK_Cn_Cases foreign key (Cn_Cases) references Cn_Cases(ID)   
    )    
    
               

     

""")
#   DROP TABLE IF EXISTS TABL_cnyz48;


    # insert into pc_Cn_Matherboard values ('rrr_Matherboard')
    # insert into pc_Cn_CPU values ('rrr_Matherboard')
    # insert into pc_Cn_RAM values ('rrr_Matherboard')
    # insert into pc_Cn_GPU values ('rrr_Matherboard')
    # insert into pc_Cn_Storage values ('rrr_Matherboard')
    # insert into pc_Cn_PowerUnit values ('rrr_Matherboard')
    # insert into pc_Cn_Cases values ('rrr_Matherboard')

    # CREATE TABLE Cn_Matherboard(
    #     id INT IDENTITY(1,1) PRIMARY KEY,
    #     Matherboard NVARCHAR(25), 
    # )  
    

    # CREATE TABLE Cn_CPU(
    #     id INT IDENTITY(1,1) PRIMARY KEY,
    #     Matherboard NVARCHAR(25), 
    # )  

    # CREATE TABLE Cn_RAM(
    #     id INT IDENTITY(1,1) PRIMARY KEY,
    #     Matherboard NVARCHAR(25), 
    # )  

    # CREATE TABLE Cn_GPU(
    #     id INT IDENTITY(1,1) PRIMARY KEY,
    #     Matherboard NVARCHAR(25), 
    # )  

    # CREATE TABLE Cn_Storage(
    #     id INT IDENTITY(1,1) PRIMARY KEY,
    #     Matherboard NVARCHAR(25), 
    # )  

    # CREATE TABLE Cn_PowerUnit(
    #     id INT IDENTITY(1,1) PRIMARY KEY,
    #     Matherboard NVARCHAR(25), 
    # )  

    # CREATE TABLE Cn_Cases(
    #     id INT IDENTITY(1,1) PRIMARY KEY,
    #     Matherboard NVARCHAR(25), 
    # )     


  


    #3. INSERT INTO groups_cnyz48 VALUES ('GR1')           
    #4. INSERT INTO cnyz48 VALUES ('IVAN', 1000)



for row in cursor:
    print(row)
# print(cursor.fetchone())
# print(cursor.fetchall())


conn.commit()
conn.close()
