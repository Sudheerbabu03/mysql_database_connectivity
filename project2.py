import mysql.connector

try:

    conn=mysql.connector.connect(
        host='localhost',
        user='sva',
        password='Sudheersva24',
        database='Student'
    )

    cursor=conn.cursor()
    cursor.execute("insert into data (id,name,location)values(101,'sudheer babu','srikalahasti')")
    conn.commit()
    print("Record inserted Successfully")

except mysql.connector.Error as error:
    print(error)    

finally:
    if cursor:
        cursor.close()    
    if conn:
        conn.close()    
    