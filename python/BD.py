from time import sleep
import mysql.connector


class Connector():
    while True:
        try:
            db = mysql.connector.connect(
                    host="db",
                    user="root",
                    passwd = "digo12",
                    database = "bancodeteste"  ##mycursor.execute("CREATE DATABASE bancodeteste")
                )
            mycursor = db.cursor()
            break
        except:
            print("Could not connect to database. Retrying....")
            sleep(4)
    

    #Deleting All Elements
    # mycursor.execute("TRUNCATE TABLE Course")
    # mycursor.execute("TRUNCATE TABLE Vinculations")
    # mycursor.execute("TRUNCATE TABLE Subject")



    #Deleting All Tables
    # mycursor.execute("DROP TABLE Course")
    # mycursor.execute("DROP TABLE Vinculations")
    # mycursor.execute("DROP TABLE Subject")
    #mycursor.execute("DESCRIBE Course")


    # for x in mycursor:
    #     print(x)


    #mycursor.execute("INSERT INTO Course(name, tipo) VALUES (%s,%s)", ("Direito", "GRADUACAO"))
    # db.commit() #used to confirm changes in database


    #mycursor.execute("INSERT INTO Course(name, tipo) VALUES ({},{})".format("Engenharia", "GRADUACAO"))