import sqlite3
conn = sqlite3.connect('register.db')
import hashlib
import maskpass  
import base64

conn.execute("""
    CREATE TABLE IF NOT EXISTS REGISTER(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            EMAIL TEXT NOT NULL,
            FIRSTNAME TEXT NOT NULL,
            LASTNAME TEXT NOT NULL,
            PASSWORD TEXT NOT NULL
    )

""")

cursor = conn.cursor()

def login():   
    email = input("Email'nizi daxil edin: ")
    cursor.execute(f"SELECT * FROM REGISTER WHERE EMAIL = '{email}'")
    data = cursor.fetchone()  
    while not data:
        email = input("Email'nizi daxil edin: ")
        cursor.execute(f"SELECT * FROM REGISTER WHERE EMAIL = '{email}'")
        data = cursor.fetchone()
    passwordFromDb = data[4]

    pwd = maskpass.askpass("Şifrənizi daxil edin : ")
    pwd = pwd.encode("utf-8")
    sha256 = hashlib.sha256()
   
    sha256.update(pwd)
    pwd = sha256.hexdigest()
    while pwd!=passwordFromDb:
        pwd = maskpass.askpass("Yalnış daxil etdiniz yenidən sınayın : ")

    print("Giriş etdiniz")

def register():
    email = input("Email daxil edin: ")
    cursor.execute(f"SELECT * FROM REGISTER WHERE EMAIL = '{email}'")
    data = cursor.fetchone()
    while data:
        print('Bu email ilə qeydiyyatdan keçilmişdir, başqa birini daxil edin: ')
        email = input("Email daxil edin: ")
        data = cursor.fetchone()
    firstName = input('Adiniz daxil edin: ')
    lastName = input('Soyadinizi daxil edin: ')
    pwd = maskpass.askpass("Password : ")
    rpwd = maskpass.askpass("Password'u yenidən daxil edin: ") 
    while pwd!=rpwd:
        print('Düzgün daxil etmirsiniz!')
        rpwd = maskpass.askpass("Password'u yenidən daxil edin: ") 

    pwd = pwd.encode("utf-8")
    sha256 = hashlib.sha256()
   
    sha256.update(pwd)
    pwd = sha256.hexdigest()
    cursor.execute(f"INSERT INTO REGISTER (EMAIL,FIRSTNAME,LASTNAME,PASSWORD) VALUES (?,?,?,?)",(email,firstName,lastName,pwd))
    conn.commit()
    return "Qeydiyyat müvəffəqiyyətlə bitdi!"
    


while True:
    n = int(input("Qeydiyyatdan keç (1), Giriş (2), Çıxış (3)"))
    if n == 1:
        print(register())
    elif n == 2:
        login()
    elif n == 3:
        break

# from cryptography.fernet import Fernet
# key = Fernet.generate_key() 
# cipher_suite = Fernet(key)
# n = input()
# n = n.encode('utf-8')
# print(n,'87')
# encoded_text = cipher_suite.encrypt(n)
# print(encoded_text)
# decoded_text = cipher_suite.decrypt(encoded_text)
# print(decoded_text)


