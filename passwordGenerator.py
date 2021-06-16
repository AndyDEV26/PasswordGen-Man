import random
import string
import sqlite3
#------------------MEDIUM----------------------------
def medium_password():
    chars = list(string.ascii_lowercase)
    big_chars = list(string.ascii_uppercase)
    numbs = list(string.digits)
    things_list = ['~','#','@','$','%','^','&','*','`',':',';','-','_']
    c1 = chars[random.randint(3,22)]
    c2 = chars[random.randint(6,18)]
    bc1 = big_chars[random.randint(3,15)]
    bc2 = big_chars[random.randint(1,20)]
    mi_c = min(chars)
    max_c = max(chars)
    mi_bc = min(big_chars)
    max_bc = max(big_chars)
    n1 = numbs[random.randint(1,8)]
    n2 = numbs[random.randint(1,8)]
    random_char1 = things_list[random.randint(0,12)]
    random_char2 = things_list[random.randint(0,12)]
    all_vars = [c1,c2,bc1,bc2,mi_c,max_c,mi_bc,max_bc,str(n1),str(n2),random_char1,random_char2]
    medium_password= all_vars[random.randint(0,11)] + all_vars[random.randint(0,11)] + all_vars[random.randint(0,11)] + all_vars[random.randint(0,11)] + all_vars[random.randint(0,11)] + all_vars[random.randint(0,11)] + all_vars[random.randint(0,11)] + all_vars[random.randint(0,11)] + all_vars[random.randint(0,11)] + all_vars[random.randint(0,11)] + all_vars[random.randint(0,11)] + all_vars[random.randint(0,11)]
    print('--------------------')
    print('YOUR PASSWORD :',medium_password)
    print('--------------------')
    dbStoringInput = input('Would you like to store this password in a database??[y/n]')
    if dbStoringInput == 'y':
        site = input('Write what this password is going to be used for:')
        insertPassword = f"INSERT INTO passwords(password,site) VALUES ('{medium_password}','{site}');"
        cursor.execute(insertPassword)
        db.commit()
#-----------------------HARD--------------------------
def hard_password():
    chars = list(string.ascii_lowercase)
    big_chars = list(string.ascii_uppercase)
    numbs = list(string.digits)
    things_list = ['~','#','@','$','%','^','&','*','`',':',';','-','_']
    c1 = chars[random.randint(1,23)]
    c2 = chars[random.randint(4,18)]
    c3 = chars[random.randint(1,24)]
    c4 = chars[random.randint(6,24)]
    n1 = numbs[random.randint(1,8)]
    n2 = numbs[random.randint(2,6)]
    n3 = numbs[random.randint(1,7)]
    n4 = numbs[random.randint(2,8)]
    bc1 = big_chars[random.randint(1,24)]
    bc2 = big_chars[random.randint(3,19)]
    bc3 = big_chars[random.randint(4,21)]
    bc4 = big_chars[random.randint(5,16)]
    min_c = min(chars)
    min_bc = min(big_chars)
    max_c = max(chars)
    max_bc = max(big_chars)
    char1 = things_list[random.randint(0,12)]
    char2 = things_list[random.randint(0,12)]
    char3 = things_list[random.randint(0,12)]
    char4 = things_list[random.randint(0,12)]
    all_vars = [c1,c2,c3,c4,str(n1),str(n2),str(n3),str(n4),bc1,bc2,bc3,bc4,min_c,max_c,min_bc,max_bc,char1,char2,char3,char4]
    hard_password = all_vars[random.randint(0,19)] + all_vars[random.randint(0,19)] + all_vars[random.randint(0,19)] + all_vars[random.randint(0,19)] + all_vars[random.randint(0,19)] + all_vars[random.randint(0,19)] + all_vars[random.randint(0,19)] + all_vars[random.randint(0,19)] + all_vars[random.randint(0,19)] + all_vars[random.randint(0,19)] + all_vars[random.randint(0,19)] + all_vars[random.randint(0,19)] + all_vars[random.randint(0,19)] + all_vars[random.randint(0,19)] + all_vars[random.randint(0,19)] + all_vars[random.randint(0,19)] + all_vars[random.randint(0,19)] + all_vars[random.randint(0,19)] + all_vars[random.randint(0,19)] + all_vars[random.randint(0,19)] 
    print('--------------------')
    print('YOUR PASSWORD :',hard_password)
    print('--------------------')
    dbStoringInput = input('Would you like to store this password in a database??[y/n]')
    if dbStoringInput == 'y':
        site = input('Write what this password is going to be used for:')
        insertPassword = f"INSERT INTO passwords(password,site) VALUES ('{hard_password}','{site}');"
        cursor.execute(insertPassword)
        db.commit()
#----------------------IMPOSSIBLE-----------------------------
def impossible():
    chars = list(string.ascii_lowercase)
    big_chars = list(string.ascii_uppercase)
    numbs = list(string.digits)
    things_list = ['~','#','@','$','%','^','&','*','`',':',';','-','_']
    c1 = chars[random.randint(0,24)]
    c2 = chars[random.randint(3,21)]
    c3 = chars[random.randint(4,17)]
    c4 = chars[random.randint(0,13)]
    c5 = chars[random.randint(2,19)]
    n1 = numbs[random.randint(0,8)]
    n2 = numbs[random.randint(0,8)]
    n3 = numbs[random.randint(0,8)]
    n4 = numbs[random.randint(0,8)]
    n5 = numbs[random.randint(0,8)]
    bc1 = big_chars[random.randint(0,23)]
    bc2 = big_chars[random.randint(2,24)]
    bc3 = big_chars[random.randint(3,19)]
    bc4 = big_chars[random.randint(5,17)]
    bc5 = big_chars[random.randint(2,21)]
    l_min = [min(chars),min(chars),min(big_chars),min(big_chars)]
    l_max = [max(chars),max(chars),max(big_chars),max(big_chars)]
    min1 = l_min[random.randint(0,3)]
    min2 = l_min[random.randint(0,3)]
    max1 = l_max[random.randint(0,3)]
    max2 = l_max[random.randint(0,3)]
    char1 = things_list[random.randint(0,12)]
    char2 = things_list[random.randint(0,12)]
    char3 = things_list[random.randint(0,12)]
    char4 = things_list[random.randint(0,12)]
    char5 = things_list[random.randint(0,12)]
    all_list = [c1,c2,c3,c4,c5,str(n1),str(n2),str(n3),str(n4),str(n5),bc1,bc2,bc3,bc4,bc5,min1,min2,max1,max2,char1,char2,char3,char4,char5]
    impossible_password = all_list[random.randint(0,23)] + all_list[random.randint(0,23)] + all_list[random.randint(0,23)] + all_list[random.randint(0,23)] + all_list[random.randint(0,23)] + all_list[random.randint(0,23)] + all_list[random.randint(0,23)] + all_list[random.randint(0,23)] + all_list[random.randint(0,23)] + all_list[random.randint(0,23)] + all_list[random.randint(0,23)] + all_list[random.randint(0,23)] + all_list[random.randint(0,23)] + all_list[random.randint(0,23)] + all_list[random.randint(0,23)] + all_list[random.randint(0,23)] + all_list[random.randint(0,23)] + all_list[random.randint(0,23)] + all_list[random.randint(0,23)] + all_list[random.randint(0,23)] + all_list[random.randint(0,23)] + all_list[random.randint(0,23)] + all_list[random.randint(0,23)] + all_list[random.randint(0,23)]
    print('--------------------')
    print('YOUR PASSWORD :',impossible_password)
    print('--------------------')
    dbStoringInput = input('Would you like to store this password in a database??[y/n]')
    if dbStoringInput == 'y':
        site = input('Write what this password is going to be used for:')
        insertPassword = f"INSERT INTO passwords(password,site) VALUES ('{impossible_password}','{site})'"
        cursor.execute(insertPassword)
        db.commit()

#-------------------MENU-------------------------
db = sqlite3.connect('test.db')
cursor = db.cursor()

print('Welcome to Password Generator and Manager!')
while True:
    print('''Please select one of the following opperations:
                [1]Medium
                [2]Hard
                [3]Impossible
                [4]Print database
                [5]Add to database
                [6]Delete from database
                [7]Exit''')
    menu = input()
    if menu == '1':
        medium_password()
    elif menu == '2':
        hard_password()
    elif menu == '3':
        impossible()
    elif menu == '4':
        cursor.execute("SELECT * FROM passwords")
        result = cursor.fetchall()
        print(result)
    elif menu == '5':
        passwordMenuInsert = input('Insert the password:')
        passwordForWhat = input('What is the password for?')
        insertValuesMenu = f"INSERT INTO passwords(password,site) VALUES ('{passwordMenuInsert}','{passwordForWhat}')"
        cursor.execute(insertValuesMenu)
        db.commit()
    elif menu == '6':
        whatToDelete = input('Please the name of the site that corresponds with the password you want to delete:')
        cursor.execute(f"DELETE FROM passwords WHERE site='{whatToDelete}'")
        db.commit()
    elif menu == '7':
        break
