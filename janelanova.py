import tkinter
from tkinter import *
from tkinter import ttk
from ler import ler_lista_jogos
from tkinter.messagebox import showinfo
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ler import numeros_ler

janela = Tk()


class Aplicacao:
    def __init__(self):
        self.janela = janela

        # criando frames
        self.frame0 = Frame(self.janela, background="#9c9a92")
        self.frame1 = Frame(self.janela, background="#9c9a92")

        # criando botões
        self.btChute = Button(self.frame0, text="Chute", command=self.chute_jogada)
        self.btUpdate = Button(self.frame0, text="Update", command=self.ler_banco)

        # criando variaveis
        self.dupla_count = 0
        self.terno_count = 0
        self.quadra_count = 0
        self.quina_count = 0
        self.mega_count = 0

        # criando rótulos
        self.lbDupla = Label(self.frame1, text=f'Duplas : {self.dupla_count}')
        self.lbTerno = Label(self.frame1, text=f'Terno : {self.terno_count}')
        self.lbQuadra = Label(self.frame1, text=f'Quadra : {self.quadra_count}')
        self.lbQuina = Label(self.frame1, text=f'Quina : {self.quina_count}')
        self.lbMega = Label(self.frame1, text=f'Mega : {self.mega_count}')

        # criando inputs
        self.enNumero1 = Entry(self.frame0)
        self.enNumero2 = Entry(self.frame0)
        self.enNumero3 = Entry(self.frame0)
        self.enNumero4 = Entry(self.frame0)
        self.enNumero5 = Entry(self.frame0)
        self.enNumero6 = Entry(self.frame0)

        # criando tabela
        self.listaCliente = ttk.Treeview(self.frame1, height=3,
                                         columns=(
                                             "coluna1",
                                             "coluna2",
                                             "coluna3",
                                             "coluna4",
                                             "coluna5",
                                             "coluna6",
                                             "coluna7",
                                             "coluna8",
                                             "coluna9"))

        # criando scrollbar
        self.scrollLista = Scrollbar(self.frame1, orient="vertical")

    def tela(self):
        self.janela.title("NETFLIX")
        self.janela.configure(background="#bdbcb3")
        self.janela.geometry("700x750")
        self.janela.resizable(True, True)
        self.janela.minsize(width=700, height=500)

        self.frames()
        self.botoes()
        self.labels()
        self.inputs()
        self.lista_frame2()
        self.grafic()
        mainloop()

    def frames(self):
        self.frame0.place(relheight=0.07, relwidth=0.94, relx=0.03, rely=0.03)
        self.frame1.place(relheight=0.40, relwidth=0.94, relx=0.03, rely=0.12)

    def botoes(self):
        self.btChute.place(relx=0.65, rely=0.4, relwidth=0.1, relheight=0.5)
        self.btUpdate.place(relx=0.85, rely=0.4, relwidth=0.1, relheight=0.5)

    def labels(self):
        self.lbDupla.place(relx=0.025, rely=0.04, relwidth=0.1, relheight=0.1)
        self.lbTerno.place(relx=0.2375, rely=0.04, relwidth=0.1, relheight=0.1)
        self.lbQuadra.place(relx=0.450, rely=0.04, relwidth=0.1, relheight=0.1)
        self.lbQuina.place(relx=0.6625, rely=0.04, relwidth=0.1, relheight=0.1)
        self.lbMega.place(relx=0.875, rely=0.04, relwidth=0.1, relheight=0.1)

    def inputs(self):
        self.enNumero1.place(relx=0.05, rely=0.37, relwidth=0.05, relheight=0.5)
        self.enNumero2.place(relx=0.15, rely=0.37, relwidth=0.05, relheight=0.5)
        self.enNumero3.place(relx=0.25, rely=0.37, relwidth=0.05, relheight=0.5)
        self.enNumero4.place(relx=0.35, rely=0.37, relwidth=0.05, relheight=0.5)
        self.enNumero5.place(relx=0.45, rely=0.37, relwidth=0.05, relheight=0.5)
        self.enNumero6.place(relx=0.55, rely=0.37, relwidth=0.05, relheight=0.5)

    def lista_frame2(self):
        self.listaCliente.heading("#0", text="ID")
        self.listaCliente.heading("#1", text="Ano")
        self.listaCliente.heading("#2", text="Jogo")
        self.listaCliente.heading("#3", text="1")
        self.listaCliente.heading("#4", text="2")
        self.listaCliente.heading("#5", text="3")
        self.listaCliente.heading("#6", text="4")
        self.listaCliente.heading("#7", text="5")
        self.listaCliente.heading("#8", text="6")
        self.listaCliente.heading("#9", text="Acertos")

        self.listaCliente.column("#0", width=35)
        self.listaCliente.column("#1", width=70)
        self.listaCliente.column("#2", width=70)
        self.listaCliente.column("#3", width=35)
        self.listaCliente.column("#4", width=35)
        self.listaCliente.column("#5", width=35)
        self.listaCliente.column("#6", width=35)
        self.listaCliente.column("#7", width=35)
        self.listaCliente.column("#8", width=35)
        self.listaCliente.column("#9", width=70)

        self.listaCliente.place(relx=0.025, rely=0.173, relwidth=0.927, relheight=0.755)

        self.listaCliente.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.95, rely=0.175, relwidth=0.025, relheight=0.75)
        self.scrollLista.config(command=self.listaCliente.yview)

    def ler_banco(self):
        self.listaCliente.delete(*self.listaCliente.get_children())

        lista_jogos = ler_lista_jogos()
        for jogo in lista_jogos:
            self.listaCliente.insert('', tkinter.END,
                                     values=[jogo[1][1],
                                             [jogo[1][2]],
                                             [jogo[1][3]],
                                             [jogo[1][4]],
                                             [jogo[1][5]],
                                             [jogo[1][6]],
                                             [jogo[1][7]],
                                             [jogo[1][8]],
                                             [jogo[0]]],
                                     text=jogo[0])

    def testar_jogos(self, lista_chute):
        lista_jogos = ler_lista_jogos()
        jogos_que_tem = []
        self.dupla_count = 0
        self.terno_count = 0
        self.quadra_count = 0
        self.quina_count = 0
        self.mega_count = 0
        for jogo in lista_jogos:
            count = 0
            jogo_arrumado = jogo[3:]
            for numero in lista_chute:
                if numero in jogo_arrumado:
                    count += 1
            if count == 2:
                dupla = ["duque", jogo]
                jogos_que_tem.append(dupla)
                self.dupla_count += 1
            elif count == 3:
                terno = ["terno", jogo]
                jogos_que_tem.append(terno)
                self.terno_count += 1
            elif count == 4:
                quadra = ["quadra", jogo]
                jogos_que_tem.append(quadra)
                self.quadra_count += 1
            elif count == 5:
                quina = ["quina", jogo]
                jogos_que_tem.append(quina)
                self.quina_count += 1
            elif count == 6:
                mega = ["mega", jogo]
                jogos_que_tem.append(mega)
                self.mega_count += 1
        return jogos_que_tem

    def chute_jogada(self):
        try:
            lista_numeros = [int(self.enNumero1.get()), int(self.enNumero2.get()), int(self.enNumero3.get()),
                             int(self.enNumero4.get()), int(self.enNumero5.get()), int(self.enNumero6.get())]
            soma = 0
            teste = 0
            numero_errado = False
            lista_numeros.sort()
            for numero_teste in lista_numeros:
                soma += numero_teste

                if numero_teste > 60 or numero_teste < 1:
                    numero_errado = True

                for numero_teste_dois in lista_numeros:
                    if numero_teste == numero_teste_dois:
                        teste += 1

            if teste >= 8 or numero_errado == True:
                showinfo(title='Error',
                         message='Algo está errado no preechimento, por favor usuário reveja os números digitados.')
            else:
                lista_jogos = self.testar_jogos(lista_chute=lista_numeros)
                self.listaCliente.delete(*self.listaCliente.get_children())
                for jogo in lista_jogos:
                    self.listaCliente.insert('', tkinter.END,
                                             values=[jogo[1][1],
                                                     [jogo[1][2]],
                                                     [jogo[1][3]],
                                                     [jogo[1][4]],
                                                     [jogo[1][5]],
                                                     [jogo[1][6]],
                                                     [jogo[1][7]],
                                                     [jogo[1][8]],
                                                     [jogo[0]]],
                                             text=jogo[1][0])

                self.lbDupla.config(text=f"Duplas : {self.dupla_count}")
                self.lbTerno.config(text=f'Terno : {self.terno_count}')
                self.lbQuadra.config(text=f'Quadra : {self.quadra_count}')
                self.lbQuina.config(text=f'Quina : {self.quina_count}')
                self.lbMega.config(text=f'Mega : {self.mega_count}')

        except:
            showinfo(title='Error', message='Todos os campos tem que estar preenchidos.')

    def grafic(self):
        lista_numeros = numeros_ler()
        numero = []
        quantidade_numeros = []

        fig = plt.figure(figsize=(11, 4), dpi=50)
        ax = fig.add_subplot(111)

        canva = FigureCanvasTkAgg(fig, self.janela)
        canva.get_tk_widget().place(relheight=0.415, relwidth=0.94, relx=0.03, rely=0.56)
        for numero_unidade in lista_numeros:
            numero.append(numero_unidade[0])
            quantidade_numeros.append(numero_unidade[1])
        ax.bar(numero, quantidade_numeros)

        ax.set_ylabel('quantidade')
        ax.set_title('números')
