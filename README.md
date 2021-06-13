# PasswordGen-Man
A password generator and manager written in python.Hope you enjoy!
# Reuirements
1.Python3 installed on your pc
2.Mysql Connector for python3(Command:all mysql-connector-python)
# Setup
1.Install MySQL.if tou have it installed already,don't install it again.(Tutorial:FOR WINDOWS : https://www.youtube.com/watch?v=WuBcTJnIuzo; FOR LINUX:it depends on what distro you have, search the web for the perfect tutorial )
NOTE:After every MySQL command , type ';'
2.Run these command in this order:
 1.CREATE DATABASE PasswordGenMan;
 2.GRANT ALL PRIVILEGES ON PasswordGenMan.* TO 'youruser'@'yourhost';|REMEMBER:When you start the program , you must enter the user and the password that you accorded the privileges!!!! 
 3.USE PasswordGenMan;
 4.CREATE TABLE passwords(password VARCHAR (255),site VARCHAR(255));
 5.quit;
