import sqlite3
from random import randint
conn = sqlite3.connect('casino.db')
conn.execute("""
            CREATE TABLE IF NOT EXISTS CASINOPLAYER(
             ID INTEGER PRIMARY KEY AUTOINCREMENT,
             NAME TEXT NOT NULL,
             PASSWORD INT NOT NULL,
             CASH INT NOT NULL
            )

""")
cursor = conn.cursor()


class Player:
    def __init__(self,player_name):
        self.player_name = player_name
    
    def get_data(self):
        cursor.execute(f"SELECT * FROM CASINOPLAYER WHERE NAME='{self.player_name}'")
        data = cursor.fetchone()
        return data
    
    def login(self):
        if self.get_data():
            password = int(input('Sifreni daxil edin: '))
            while password!=self.get_data()[2]:
                print('Şifrə doğru deyil!')
                password = int(input('Sifreni daxil edin: '))
            return self.get_data()
        else:
            return False
    
    def check_balance(self,data):
        return data
    
    def delete_player(self): 
        if self.get_data():
            password = int(input('Sifreni daxil edin: '))
            while password!=self.get_data()[2]:
                print('Şifrə doğru deyil!')
                password = int(input('Sifreni daxil edin: '))
            cursor.execute(f"DELETE FROM CASINOPLAYER WHERE name = '{self.get_data()[1]}'")
            conn.commit()
          
            return "İstifadəçi bazadan silindi!"
           


def game(id):
    userId = id
    cursor.execute(f"SELECT * FROM CASINOPLAYER WHERE ID='{userId}'")
    data = cursor.fetchone()
    cash = data[3]
    n = input('1 və 10 arası bir ədəd daxil edin (Əgər oyunu bitirmək istəsəniz "stop" daxil edin): ')
    while n!='stop':
        randomNumber = randint(1,11)
        if cash>=5:
        
            if int(n)==randomNumber:
                print('Qalibsiniz!')
                cash+=10
            else:
                print('Uduzdunuz!')
                cash-=5
            cursor.execute(f"UPDATE CASINOPLAYER SET CASH = '{cash}' WHERE ID= '{userId}'")
            conn.commit()
            data = cursor.fetchone()     
            n = input('1 və 10 arası bir ədəd daxil edin (Əgər oyunu bitirmək istəsəniz "stop" daxil edin): ') 
        else:
            print('Balansiniz bitdi!')
            break

def begin():  
    n = int(input('Secim edin  (1) Qeydiyyatdan kecin (2) Sistemə giriş edin (5) Cixish: ')) 
    while True:
        if n==5:
            print("Oyundan çıxdınız")
            break
        elif n==1:
            name = input('Adinizi daxil edin: ')
            cursor.execute(f"SELECT * FROM CASINOPLAYER WHERE NAME='{name}'")
            data = cursor.fetchone()
            while data:
                name = input('Belə bir ad bazada mövcuddur. Yeni adinizi daxil edin: ')
                cursor.execute(f"SELECT * FROM CASINOPLAYER WHERE NAME='{name}'")
                data = cursor.fetchone()
            password = int(input('Password daxil edin(ancaq rəqəmlə): '))
            repassword = int(input('Password"u yenidən daxil edin(ancaq rəqəmlə): '))
            while password!=repassword:
                repassword = int(input('Password"u yenidən daxil edin(ancaq rəqəmlə):'))
            cash = int(input('Nə qədər cash daxil edirsiz?: '))
            while cash<=0:
                cash = int(input('Cash"ı artırın az daxil edirsiz: '))
            print("Istifadəçi uğurla qeydiyyatdan keçdi.")
            cursor.execute("INSERT INTO CASINOPLAYER (NAME,PASSWORD,CASH) VALUES (?,?,?)",(name,password,cash))
            conn.commit()    
        elif n==2:
            name = input("Adinizi daxil edin: ")
            playerObj = Player(name)
            data = playerObj.login()
            if data:
                while True:
                    n = int(input('Secim edin (2) Oyuna basla (3) İstifadəçini bazadan silin (4) Balansi yoxla (5) Cixish: '))
                    if n==5:
                        print('Sitemdən çıxdınız')
                        break
                    elif n==2:
                        if data[3]>=5:
                            game(data[0])
                        else:
                            print('Balansinizda kifayet qeder mebleg yoxdur')
                    elif n==3:
                        
                        print(playerObj.delete_player())
                        begin()
                    

                    elif n==4:
                        print(playerObj.check_balance(data[3]))
            else:
                print('Belə bir istifadəçi yoxdur')
        n = int(input('Secim edin  (1) Qeydiyyatdan kecin (2) Sistemə giriş edin (5) Cixish '))


begin()