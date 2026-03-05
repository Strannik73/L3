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