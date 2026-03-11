import pymssql
import credits as cr

conn = pymssql.connect(cr.server, cr.user, cr.password, cr.db)
cursor = conn.cursor()
 



cursor.execute("""
    USE TEST1
                
        
""")




# УДАЛЯЕМ ВСЕ ТАБЛИЧКИ==============================================
# cursor.execute("""
    # USE TEST1
    # DROP TABLE IF EXISTS TABL_cnyz48;
    # DROP TABLE IF EXISTS Cn_Matherboard;
    # DROP TABLE IF EXISTS Cn_CPU;
    # DROP TABLE IF EXISTS Cn_RAM;
    # DROP TABLE IF EXISTS Cn_GPU;
    # DROP TABLE IF EXISTS Cn_Storage;
    # DROP TABLE IF EXISTS Cn_PowerUnit;
    # DROP TABLE IF EXISTS Cn_Cases;
# """)

# СОЗДАЕМ МАЛЕНЬКИЕ ТАБЛИЧКИ====================================
# cursor.execute("""
#     USE TEST1;
#     CREATE TABLE Cn_Matherboard(
#         id INT IDENTITY(1,1) PRIMARY KEY,
#         Matherboard NVARCHAR(25), 
#     )  
    
#     CREATE TABLE Cn_CPU(
#         id INT IDENTITY(1,1) PRIMARY KEY,
#         CPU NVARCHAR(25), 
#     )  

#     CREATE TABLE Cn_RAM(
#         id INT IDENTITY(1,1) PRIMARY KEY,
#         RAM NVARCHAR(25), 
#     )  

#     CREATE TABLE Cn_GPU(
#         id INT IDENTITY(1,1) PRIMARY KEY,
#         GPU NVARCHAR(25), 
#     )  

#     CREATE TABLE Cn_Storage(
#         id INT IDENTITY(1,1) PRIMARY KEY,
#         Storage NVARCHAR(25), 
#     )  

#     CREATE TABLE Cn_PowerUnit(
#         id INT IDENTITY(1,1) PRIMARY KEY,
#         PowerUnit NVARCHAR(25), 
#     )  

#     CREATE TABLE Cn_Cases(
#         id INT IDENTITY(1,1) PRIMARY KEY,
#         Cases NVARCHAR(25), 
#     )     

# """)



    

# ДОБАВЛЯЕМ В НИХ КОЛОНКИ=========================

# cursor.execute("""
#     USE TEST1   
#     ALTER TABLE Cn_Matherboard ADD
#         Socket INT,
#         FormFactor INT,
#         RAM_slots INT,
#         PGE_slots INT 
# """)

# cursor.execute("""
#     USE TEST1
#     ALTER TABLE Cn_CPU ADD
#         Socket INT,
#         FormFactor INT,
#         RAM_slots INT,
#         PGE_slots INT
# """)

# cursor.execute("""
#     USE TEST1
#     ALTER TABLE Cn_RAM ADD
#         Socket INT,
#         FormFactor INT,
#         RAM_slots INT,
#         PGE_slots INT 
# """)

# cursor.execute("""
#     USE TEST1               
#     ALTER TABLE Cn_GPU ADD
#         Socket INT,
#         FormFactor INT,
#         RAM_slots INT,
#         PGE_slots INT 
# """)

# cursor.execute("""
#     USE TEST1            
#     ALTER TABLE Cn_Storage ADD
#         Socket INT,
#         FormFactor INT,
#         RAM_slots INT,
#         PGE_slots INT
# """)

# cursor.execute("""
#     USE TEST1         
#     ALTER TABLE Cn_PowerUnit ADD
#         Socket INT,
#         FormFactor INT,
#         RAM_slots INT,
#         PGE_slots INT 
# """) 

# cursor.execute("""
#     USE TEST1
#     ALTER TABLE Cn_Cases ADD
#         Socket INT,
#         FormFactor INT,
#         RAM_slots INT,
#         PGE_slots INT  
# """)


# СОЗДАЕМ ГЛАВУЮ ТАБЛИЦУ И ПРИВЯЗЫВАЕМ К НЕЙ МАЛЕНЬКИЕ ===========================

# cursor.execute("""
#     USE TEST1

#     CREATE TABLE ATABL_48(
#         id INT IDENTITY(1,1) PRIMARY KEY,
#         Cn_Matherboard INT, 
#         Cn_CPU INT,
#         Cn_RAM INT,
#         Cn_GPU INT,   
#         Cn_Storage INT,
#         Cn_PowerUnit INT,
#         Cn_Cases INT,
#         constraint FK_Cn_Matherboard foreign key (Cn_Matherboard) references Cn_Matherboard(ID),
#         constraint FK_Cn_CPU foreign key (Cn_CPU) references Cn_CPU(ID),
#         constraint FK_Cn_RAM foreign key (Cn_RAM) references Cn_RAM(ID),
#         constraint FK_Cn_GPU foreign key (Cn_GPU) references Cn_GPU(ID),
#         constraint FK_Cn_Storage foreign key (Cn_Storage) references Cn_Storage(ID),
#         constraint FK_Cn_PowerUnit foreign key (Cn_PowerUnit) references Cn_PowerUnit(ID),
#         constraint FK_Cn_Cases foreign key (Cn_Cases) references Cn_Cases(ID)   
#     )  
# """)


# ЗАПОЛНЯЕМ ================================

# cursor.execute("""
#     USE TEST1
               
#     insert into Cn_Matherboard (Matherboard) values ('rrr_Matherboard')
#     insert into Cn_CPU (CPU) values ('rrr_Matherboard')
#     insert into Cn_RAM (RAM) values ('rrr_Matherboard')
#     insert into Cn_GPU (GPU) values ('rrr_Matherboard')
#     insert into Cn_Storage (Storage) values ('rrr_Matherboard')
#     insert into Cn_PowerUnit (PowerUnit) values ('rrr_Matherboard')
#     insert into Cn_Cases (Cases) values ('rrr_Matherboard')
     

# """)



# cursor.execute("""
#    USE TEST1

#    INSERT INTO TABL_cnyz48(
#    
# 
# 
# 
# 
# 
# 
# 
# 
# )
# """)


# cursor.execute("""
    # SELECT TABL_cnyz48.ID, Cn_Matherboard.Cn_Matherboard, Cn_CPU.Cn_CPU, Cn_RAM.Cn_RAM, Cn_GPU.Cn_GPU, Cn_Storage.Cn_Storage, Cn_PowerUnit.Cn_PowerUnit, Cn_Cases.Cn_Cases
    #     right JOIN Cn_Matherboard ON TABL_cnyz48.Cn_Matherboard = Cn_Matherboard.ID
    #     JOIN Cn_CPU ON TABL_cnyz48.Cn_CPU = Cn_CPU.ID
    #     JOIN Cn_RAM ON TABL_cnyz48.Cn_RAM = Cn_RAM.ID
    #     JOIN Cn_GPU ON TABL_cnyz48.Cn_GPU = Cn_GPU.ID
    #     JOIN Cn_Storage ON TABL_cnyz48.Cn_Storage = Cn_Storage.ID
    #     JOIN Cn_PowerUnit ON TABL_cnyz48.Cn_PowerUnit = Cn_PowerUnit.ID
    #     JOIN Cn_Cases ON TABL_cnyz48.Cn_Cases = Cn_Cases.ID
# """)


for row in cursor:
    print(row)
# print(cursor.fetchone())
# print(cursor.fetchall())


conn.commit()
conn.close()

