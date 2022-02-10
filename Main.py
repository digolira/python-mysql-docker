import os
import Opcoes
from BD import Connector


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():

    def count_table_elements(table_name: str):
        query = "SELECT COUNT(*) from %s" %table_name
        Connector.mycursor.execute(query)             #executing query separately
        res = Connector.mycursor.fetchone() #transforma numa tupla o resultado da query
        return res[0]


    def list_all_table_elements(table_name: str):
        print("Those are the {}s offered by the University:\n".format(table_name))
        if (count_table_elements(table_name) > 0):
            Connector.mycursor.execute("SELECT * FROM %s" % (table_name,)) #cursor.execute requires a sql query and a tuple as parameters
            #Parameter substitution in the DB API is only for values - not tables or fields. You'll need to use normal string substitution for those
            for element in Connector.mycursor:
                print("ID: " + str(element[0]) + " - " + element[1])
        else:
            print("No registers found.\n")


    def get_details(table_name: str):
            list_all_table_elements(table_name)
            option = input("Do you want to see details about a %s? Y/N\n"%table_name)
            if (option in ["Y","y","YES", "Yes", "yes"]):
                try:
                    id = int(input("Insert %s ID:" %table_name))
                    result = find_element_byId(id, table_name) 
                    if result != None:
                        print("%s ID: - %s"%(table_name, result))
                        opposite = get_opposite(table_name)
                        opt = input("""
                            What do you want to do?
                            1- Edit Name
                            2- Delete Course
                            3- Get %s List
                            4- Leave to Menu
                            Insert a number of your choice: """%opposite)
                        try:
                            opt = int(opt)
                            if (opt == 1):
                                edit_element(id, table_name)
                            elif (opt == 2):
                                delete_element(id, table_name)
                            elif (opt == 3):
                                get_vinculations(id, table_name)
                            else:
                                input("Leaving, press enter to continue.")
                        except Exception as e:
                            print(e)
                            print("Invalid option.")
                    else:
                        return input("Couldn't find subject. Press enter to continue")
                except Exception as e:
                    print(e)
                    input("Error, wrong format, ID only allows numbers. Press Enter to return to Menu")
            elif (option in ["N","n","NO", "No", "no"]):
                input("Cancelled. Press Enter.")
                clear()
            else:
                input("Option invalid. Press enter to return to menu.")



    def get_vinculations(id: int, table_name: str):
        result = find_element_byId(id, table_name) 
        if result != None:
                        clear()
                        print("{}\nID: {} - Name: {}\n".format(table_name, id,result))
                        opposite = get_opposite(table_name)
                        print("%s List: "%opposite)
                        query = """
                        SELECT Vinculations.%s_id, %s.name FROM Vinculations
                        INNER JOIN %s
                        ON Vinculations.%s_id = %s.%s_id
                        WHERE Vinculations.%s_id = %i
                        """ % (opposite.lower(), opposite, opposite, opposite.lower(), opposite, opposite.lower(),table_name.lower(), id)
                        Connector.mycursor.execute(query)
                        for element in Connector.mycursor:
                            print("ID: %i - %s"% (element[0], element[1]))
                        return input("Press enter to continue")
        return input("Couldn't find this register. Press enter to continue")




    def get_opposite(table_name: str):
        if (table_name == "Subject"):
                return "Course"
        elif (table_name == "Course"):
                return "Subject"
        else:
                return "None"



    def edit_element(id: int, table_name: str):
        result = find_element_byId(id, table_name)
        if result != None:
            print("{}\nID: {} - Name: {}\n".format(table_name, id,result))
            new_name = input("Insert name to be updated: ")
            opt = input("Course name will be updated to: %s. Press Y to confirm, any other key to leave.\n"%(new_name))
            if (opt.lower() == 'y'):
                try:
                    query = """
                    UPDATE %s
                    SET
                        name = '%s'
                    WHERE
                        %s_id= %s
                    """ %(table_name, new_name, table_name.lower(), id)
                    Connector.mycursor.execute(query)
                    Connector.db.commit()
                    input("Update done! Press enter to continue. ")
                except:

                    input("Something wrong updating data at the Database. Press enter to continue.")
            else:
                return "Leaving. Press enter to continue"
        else:
            return input ("Couldn't find this register. Press enter to continue")



    def delete_element(id: int, table_name: str):
        result = find_element_byId(id, table_name)
        if result != None:
            opt = input("Course name: %s will be deleted. Press Y to confirm, any other key to leave.\n"%(result))
            if (opt.lower() == 'y'):
                try:
                    query = """
                    DELETE FROM %s
                    WHERE
                        %s_id= %s
                    """ %(table_name, table_name.lower(), id)
                    Connector.mycursor.execute(query)
                    Connector.db.commit()
                    input("Delete done! Press enter to continue. ")
                except Exception as e:
                    print(e)
                    input("Something wrong deleting data at the Database. Press enter to continue.")
            else:
                return "Leaving. Press enter to continue"
        else:
            return input ("Couldn't find this register. Press enter to continue")



    def find_element_byId(id: int, table_name: str):
        query = "SELECT name FROM %s WHERE %s_id = %i"%(table_name,table_name.lower(),id)
        Connector.mycursor.execute(query)
        res = Connector.mycursor.fetchone()
        if res[0]== 0:
            print("ID not found")
            return None
        else:
            return res[0]


    def get_unique_list(list):
        unique = []
        for element in list:
            if element not in unique:
                unique.append(element)
        return unique



    def create_course():
        cancel = 0
        #Get course name
        while(True):
            clear()
            course_name = input("Type the new course name: ")
            try:
                option = int(input("The name of the course is: "+course_name+".\nType 1 to confirm and 0 to come back \n")) 
            except ValueError:
                input("Error! You need to select a number within the presented interval. Press Enter to continue.")
            finally:
                if (option == 1):
                    break
                else:
                    clear()

        #Get course type
        while(True):
            try:
                graduation_type = int(input("Choose the type: \n" +
                                "1- Graduation \n" +
                                "2- Master \n" +
                                "3- Doctorate \n"
                                "4- Back to the main menu\n"))
            except:
                print("Error! You need to select a number within the presented interval.")
                input("Press Enter to return.")
            finally:
                if graduation_type in [1,2,3,4]:
                    if (option == 4):
                        cancel = 1
                    clear()
                    break
                else:
                    input("Couldn't find the option! You must select a number within the presented interval.\n Press Enter to continue")
                
        #Confirmation:
        while(cancel == 0):
            option = input("The following course will be created:\n"
                "Course - " + course_name + " | Type - " + Opcoes.TipoGraduacao(graduation_type).name + ".\n"
                "Do you confirm? Y/N\n")

            if (option in ["Y","y","YES", "Yes", "yes"]):
                Connector.mycursor.execute("INSERT INTO Course(name, type) VALUES (%s,%s)", (course_name, Opcoes.TipoGraduacao(graduation_type).name))
                Connector.db.commit()
                input("Course created. Press enter to continue.")
                break
            elif (option in ["N","n","NO", "No", "no"]):
                input("Cancelled. Press Enter.")
                break
            else:
                input("Invalid Option.")


    def create_subject():
        while(True):
            clear()
            subject_name = input("Type the new subject name: ")
            option = input("The name of the subject is: "+ subject_name +".\n"+
                            "Confirm? Y/N \n")
            if (option in ["Y","y","YES", "Yes", "yes"]):
                Connector.mycursor.execute("INSERT INTO Subject(name) VALUES (%s)", (subject_name,)) #cursor.execute requires a sql query and a tuple as parameters
                Connector.db.commit()
                input("Subject created. Press enter to continue.")
                break
            elif (option in ["N","n","NO", "No", "no"]):
                input("Cancelled. Press Enter.")
                break
            else:
                input("Invalid Option.")


    def vinculate_subject():
        clear()
        while(True):
            print("(Press S if you need subject list)")
            print("(Press E to leave)")
            id = input("Insert Subject ID: ")
            if id in ["E","e","S","s"]:
                if id in ["E","e"]:
                    break
                else: 
                    clear()
                    list_all_table_elements("Subject")
                continue

            else:
                try:
                    subject_id = int(id)
                except:
                    print("ID must be a number")
                    continue
                subject = find_element_byId(subject_id, "Subject")
                if subject != None:
                    clear()
                    while (True):
                        print("Subject: {}!".format(subject))
                        print("Insert Course ID to vinculate to this subject.\n"
                            + "You can add more than one if you want, just add the ids followed by a comma\n"+
                            "Example:  301, 302, 405.\n")
                        print("(Press C if you need course list)")
                        print("(Press E to back)")
                        course_id_list = input("Type the ID's bellow: \n")

                        if course_id_list in ["E","e","C","c"]:
                            if course_id_list in ["E","e"]:
                                break
                            else: 
                                clear()
                                list_all_table_elements("Course")        
                        else:
                            try:
                                course_id_list = course_id_list.replace(" ", "")
                                course_id_list = course_id_list.split(",")
                                course_id_list = [int(item) for item in course_id_list]
                                course_id_list = get_unique_list(course_id_list)

                                if len(course_id_list) > 0:
                                    for course_id in course_id_list:
                                        course_query = find_element_byId(course_id, "Course")
                                        if course_query != None:
                                                query = "INSERT INTO Vinculations VALUES (%i,%i)" % (subject_id,course_id)
                                                Connector.mycursor.execute(query)
                                                Connector.db.commit()
                                                print("Subject ID: {} vinculated with course ID: {}".format(subject_id, course_id))
                                        else:
                                            print("Course ID: {} NOT FOUND.").format(course_id)                           
                                    input("Press Enter to Continue")
                                    clear()
                                    break
                                else:
                                    print("No course provided")
                                    input("Press Enter to Continue")
                                    clear()
                            except:
                                print("Error! Invalid input")
                else:
                    print("Subject not found!")
                    print("(Press E to leave)")
                    


    Connector()
    while(True):

        print("Welcome to the registry program")
        print("Choose what you want to do:")
        print(" 1- Course List\n",
                "2- Subject List\n",
                "3- Create New Course\n",
                "4- Create New Subject\n",
                "5- Vinculate Subject with Course\n"
                "6- Exit Program\n")

        try:
            option = int(input("Select your option: "))
        except:
            input("Invalid Option. You need to choose a number.")
            clear()
            continue
        if option < 1 or option > 6:
            print("Invalid number")



        elif option == Opcoes.MenuPrincipal.CHECK_COURSES_DETAILS:
            get_details("Course")

        elif option == Opcoes.MenuPrincipal.CHECK_SUBJECTS_DETAILS:
            get_details("Subject")
            
        elif option == Opcoes.MenuPrincipal.CREATE_COURSE:
            create_course()

        elif option == Opcoes.MenuPrincipal.CREATE_SUBJECT:
            create_subject()
                    
        elif option == Opcoes.MenuPrincipal.VINCULATE_SUBJECT:
            vinculate_subject()

        elif option == Opcoes.MenuPrincipal.LEAVE:
            input("Good bye!!! Press enter to finish the program\n")
            clear()
            break
        clear()

main()