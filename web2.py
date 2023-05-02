from selenium import webdriver
from selenium.webdriver.common.by import By
import mysql.connector
from ler import buscar_numeros


class Web:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.jogodic = {}
        self.jogonumeros = []
        self.listaanos = []
        self.count = 0
        self.contador2 = 0
        self.abrir()
        self.create()

    def abrir(self):
        for t in range(1996, 2025):
            try:
                self.driver.get(f'https://asloterias.com.br/resultados-da-mega-sena-{t}')
                self.count = 0

                for i in range(4, 114):
                    try:
                        self.puxar(i=i, t=t)
                    except:
                        break
            except:
                break

    def puxar(self, i, t):
        print(t, end=" | ")
        jogo = self.driver.find_element(By.XPATH, f"/html/body/main/div[2]/div/div/div[1]/strong[{i}]").text
        print(jogo, end=" | ")
        self.jogonumeros.clear()
        for j in range(6):
            self.count += 1
            num = self.driver.find_element(By.XPATH,
                                           f"/html/body/main/div[2]/div/div/div[1]/span[{self.count}]").text
            try:
                self.jogonumeros.append(int(num))
                print(num, end="")
                print(f"({self.count})", end=" ")
            except:
                self.count += 1
                num = self.driver.find_element(By.XPATH,
                                               f"/html/body/main/div[2]/div/div/div[1]/span[{self.count}]").text
                print(num, end="")
                self.jogonumeros.append(int(num))
                print(f"({self.count})", end=" ")

            self.jogodic[int(jogo)] = self.jogonumeros[:]
        self.listaanos.append(t)
        print()

    def create(self):
        conexao = mysql.connector.connect(
            host='localhost',
            database='loteria',
            user='root',
            password=''
        )
        cursor = conexao.cursor()
        count2 = 0

        for teste in range(1, 10000):
            try:
                jogo = list(self.jogodic.values())[count2]
                count2 += 1

                print(jogo)

                comando = f'INSERT INTO jogos (ano, jogo, numero1, numero2, numero3, numero4, numero5, numero6) VALUES ({self.listaanos[count2 - 1]}, {teste}, {jogo[0]}, {jogo[1]}, {jogo[2]}, {jogo[3]}, {jogo[4]}, {jogo[5]})'
                cursor.execute(comando)
                conexao.commit()  # edita o banco de dados (create, update, delete)

                for jogo_num in jogo:
                    for i in range(1, 61):
                        if i == jogo_num:
                            buscar_numeros(jogo_num)
            except:
                break
        cursor.close()
        conexao.close()


j = Web()
