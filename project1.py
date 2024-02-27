import mysql.connector


try:
    conn=mysql.connector.connect(host='localhost',user='sva',password='Sudheersva24',database='Student')
        
    print("connected to the database")
    cursor=conn.cursor()
    cursor.execute("create table data(id int(20) primary key,name varchar(40),location varchar(40))")
    print("table created successfully")

except mysql.connector.Error as error:
    print(error)  


finally:
    if cursor:
        cursor.close()    
    if conn:
        conn.close()      
    