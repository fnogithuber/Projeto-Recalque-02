from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import numpy as np
import math

janela = Tk()




class Funcs():
    def limpa_campos(self):
        # widgets frame 1
        self.vazao_entry.delete(0, END)
        self.combobox_material.delete(0, END)
        self.tempo_entry.delete(0, END)
        self.altura_succao_entry.delete(0, END)
        self.altura_recalque_entry.delete(0, END)
        self.comp_succao_entry.delete(0, END)
        self.comp_recalque_entry.delete(0, END)
        # widgets frame2
        self.combobox_curva90_s.current(0)
        self.combobox_joelho90_s.current(0)
        self.combobox_curva45_s.current(0)
        self.combobox_joelho45_s.current(0)
        self.combobox_crivo_s.current(0)
        self.combobox_val_globo_s.current(0)
        self.combobox_val_gaveta_s.current(0)
        # widgets frame 3
        self.combobox_curva90_r.current(0)
        self.combobox_joelho90_r.current(0)
        self.combobox_curva45_r.current(0)
        self.combobox_joelho45_r.current(0)
        self.combobox_val_globo_r.current(0)
        self.combobox_val_gaveta_r.current(0)
        self.combobox_ret_leve_r.current(0)
        self.combobox_ret_pesada_r.current(0)


    def listas(self):
        for i in range(1000):
            self.y.insert(i, i)

        for i in range(201):
            self.z.insert(i, i)

    def isNumber(self):
        try:
            int(self.vazao_entry.get())
            self.validation_vazao = True
        except ValueError:
            self.validation_vazao = False

        try:
            int(self.tempo_entry.get())
            self.validation_tempo = True
        except ValueError:
            self.validation_tempo = False

        try:
            int(self.altura_succao_entry.get())
            self.validation_altura_succao = True
        except ValueError:
            self.validation_altura_succao = False

        try:
            int(self.altura_recalque_entry.get())
            self.validation_altura_recalque = True
        except ValueError:
            self.validation_altura_recalque = False

        try:
            int(self.comp_succao_entry.get())
            self.validation_comp_succao = True
        except ValueError:
            self.validation_comp_succao = False

        try:
            int(self.comp_recalque_entry.get())
            self.validation_comp_recalque = True
        except ValueError:
            self.validation_comp_recalque = False

    def tratamento_erros(self):
        self.x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                  13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        self.y = []
        self.z = []

        self.isNumber()
        self.listas()
        # self.y.pop(0)

        if self.validation_vazao == False or (
                self.validation_vazao == True and int(self.vazao_entry.get()) not in self.y) or int(
                self.vazao_entry.get()) == 0 or self.combobox_material.get() not in ["PVC",
                                                                                     "Ferro galvanizado"] or self.validation_tempo == False or int(
                self.tempo_entry.get()) <= 0 or (
                self.validation_altura_succao == False or int(self.altura_succao_entry.get()) not in self.z) or int(
                self.altura_succao_entry.get()) == 0 or self.validation_altura_recalque == False or (
                int(self.altura_recalque_entry.get()) not in self.z or int(self.altura_recalque_entry.get()) == 0) or (
                self.validation_comp_succao == False or int(self.comp_succao_entry.get()) not in self.z or int(
                self.comp_succao_entry.get()) == 0) or (
                self.validation_comp_recalque == False or int(self.comp_recalque_entry.get()) not in self.z or int(
                self.comp_recalque_entry.get()) == 0):
            tkinter.messagebox.showwarning(
                "Aviso", "Erro nos valores digitados!")

        else:
            self.calculo_diametro()
            self.velocidade_economica()
            self.fator_atrito()
            self.perda_carga_distribuida_s()
            self.perda_carga_distribuida_r()
            self.pcs_succao_recalque()
            self.altura_manometrica()
            self.NPSH()
            self.Tela_resultado()

            print(self.perda_carga_singular_final_s)
            print(self.perda_carga_singular_final_r)
            print(self.perda_carga_dist_s)
            print(self.perda_carga_dist_r)






    def calculo_diametro(self):
        self.vazao_ajustada = float(
            (24 * float(self.vazao_entry.get())) / float(self.tempo_entry.get()))
        self.vazao_ajustada_cubic_meters = float(self.vazao_ajustada) / 1000
        self.vazao_ajustada_cubic_hours = float(self.vazao_ajustada_cubic_meters) * 3600

        #self.diametro_tubulacao = 1.3 * \
                                  #math.pow((float(self.tempo_entry.get()) / 24), 1 / 4) * \
                                  #math.sqrt(self.vazao_ajustada_cubic_meters)
        self.diametro_tubulacao = (1.3 *((float(self.tempo_entry.get()) / 24) ** 0.25) * ((self.vazao_ajustada_cubic_meters) ** 0.5)) * 1000

        if self.diametro_tubulacao <= 6.3:
            self.diametro_succao = 6.3
            self.diametro_recalque = 6.3
        elif self.diametro_tubulacao <= 9.5:
            self.diametro_succao = 9.5
            self.diametro_recalque = 6.3
        elif self.diametro_tubulacao <= 12.5:
            self.diametro_succao = 12.5
            self.diametro_recalque = 9.5
        elif self.diametro_tubulacao <= 16:
            self.diametro_succao = 16
            self.diametro_recalque = 12.5
        elif self.diametro_tubulacao <= 19:
            self.diametro_succao = 19
            self.diametro_recalque = 16
        elif self.diametro_tubulacao <= 25:
            self.diametro_succao = 25
            self.diametro_recalque = 19
        elif self.diametro_tubulacao <= 31:
            self.diametro_succao = 31
            self.diametro_recalque = 25
        elif self.diametro_tubulacao <= 38:
            self.diametro_succao = 38
            self.diametro_recalque = 31
        elif self.diametro_tubulacao <= 50:
            self.diametro_succao = 50
            self.diametro_recalque = 38
        elif self.diametro_tubulacao <= 62:
            self.diametro_succao = 62
            self.diametro_recalque = 50
        elif self.diametro_tubulacao <= 75:
            self.diametro_succao = 75
            self.diametro_recalque = 62
        elif self.diametro_tubulacao <= 100:
            self.diametro_succao = 100
            self.diametro_recalque = 75
        elif self.diametro_tubulacao <= 125:
            self.diametro_succao = 125
            self.diametro_recalque = 100
        elif self.diametro_tubulacao <= 150:
            self.diametro_succao = 150
            self.diametro_recalque = 125
        elif self.diametro_tubulacao <= 200:
            self.diametro_succao = 200
            self.diametro_recalque = 150
        elif self.diametro_tubulacao <= 250:
            self.diametro_succao = 250
            self.diametro_recalque = 200
        elif self.diametro_tubulacao <= 300:
            self.diametro_succao = 300
            self.diametro_recalque = 250
        elif self.diametro_tubulacao <= 350:
            self.diametro_succao = 350
            self.diametro_recalque = 300
        elif self.diametro_tubulacao <= 400:
            self.diametro_succao = 400
            self.diametro_recalque = 350
        elif self.diametro_tubulacao <= 450:
            self.diametro_succao = 450
            self.diametro_recalque = 400
        elif self.diametro_tubulacao <= 500:
            self.diametro_succao = 500
            self.diametro_recalque = 450
        elif self.diametro_tubulacao <= 550:
            self.diametro_succao = 550
            self.diametro_recalque = 500
        elif self.diametro_tubulacao <= 600:
            self.diametro_succao = 600
            self.diametro_recalque = 550
        elif self.diametro_tubulacao <= 650:
            self.diametro_succao = 650
            self.diametro_recalque = 600
        elif self.diametro_tubulacao <= 700:
            self.diametro_succao = 700
            self.diametro_recalque = 650
        elif self.diametro_tubulacao <= 750:
            self.diametro_succao = 750
            self.diametro_recalque = 700

    def velocidade_economica(self):
        # Velocidade econ??mica da suc????o
        #self.vel_econ_succao = (4 * (self.vazao_ajustada_cubic_meters)) / \
                               #(math.pi * np.power((float(self.diametro_succao)), 2))
        self.vel_econ_succao = (4 * self.vazao_ajustada_cubic_meters) / (3.1415 * (float((self.diametro_succao / 1000)) ** 2))

        # Velocidade econ??mica do recalque
        #self.vel_econ_recalque = (4 * self.vazao_ajustada_cubic_meters) / \
                                 #(math.pi * np.power((float(self.diametro_recalque)), 2))
        self.vel_econ_recalque = (4 * self.vazao_ajustada_cubic_meters) / (3.1415 * (float((self.diametro_recalque / 1000)) ** 2))

    def pcs_succao_recalque(self):
        self.perda_carga_singular_curva90_s = 0.0
        self.perda_carga_singular_curva45_s = 0.0
        self.perda_carga_singular_joelho90_s = 0.0
        self.perda_carga_singular_joelho45_s = 0.0
        self.perda_carga_singular_crivo_s = 0.0
        self.perda_carga_singular_val_globo_s = 0.0
        self.perda_carga_singular_val_gaveta_s = 0.0

        self.perda_carga_singular_curva90_r = 0.0
        self.perda_carga_singular_curva45_r = 0.0
        self.perda_carga_singular_joelho90_r = 0.0
        self.perda_carga_singular_joelho45_r = 0.0
        self.perda_carga_singular_ret_leve_r = 0.0
        self.perda_carga_singular_ret_pesada_r = 0.0
        self.perda_carga_singular_val_globo_r = 0.0
        self.perda_carga_singular_val_gaveta_r = 0.0

        self.perda_carga_singular_final_s = 0.0
        self.perda_carga_singular_final_r = 0.0
        self.perda_carga_total = 0.0

        # suc????o

        if self.combobox_curva90_s.get() != 0:
            self.perda_carga_singular_curva90_s = ((float(self.combobox_curva90_s.get()) * 0.40) * (
                        np.power(self.vel_econ_succao, 2)) / (2 * 9.81))
        if self.combobox_curva45_s.get() != 0:
            self.perda_carga_singular_curva45_s = ((float(self.combobox_curva45_s.get()) * 0.20) * (
                        np.power(self.vel_econ_succao, 2)) / (2 * 9.81))
        if self.combobox_joelho90_s.get() != 0:
            self.perda_carga_singular_joelho90_s = ((float(self.combobox_joelho90_s.get()) * 0.90) * (
                        np.power(self.vel_econ_succao, 2)) / (2 * 9.81))
        if self.combobox_joelho45_s.get() != 0:
            self.perda_carga_singular_joelho45_s = ((float(self.combobox_joelho45_s.get()) * 0.40) * (
                        np.power(self.vel_econ_succao, 2)) / (2 * 9.81))
        if self.combobox_crivo_s.get() != 0:
            self.perda_carga_singular_crivo_s = ((float(self.combobox_crivo_s.get()) * 1.75) * (
                        np.power(self.vel_econ_succao, 2)) / (2 * 9.81))
        if self.combobox_val_globo_s.get() != 0:
            self.perda_carga_singular_val_globo_s = ((float(self.combobox_val_globo_s.get()) * 10) * (
                        np.power(self.vel_econ_succao, 2)) / (2 * 9.81))
        if self.combobox_val_gaveta_s.get() != 0:
            self.perda_carga_singular_val_gaveta_s = ((float(self.combobox_val_gaveta_s.get()) * 0.20) * (
                        np.power(self.vel_econ_succao, 2)) / (2 * 9.81))
        else:
            self.sem_perda_s = 0

        # recalque

        if self.combobox_curva90_s.get() != 0:
            self.perda_carga_singular_curva90_r = ((float(self.combobox_curva90_r.get()) * 0.40) * (
                        np.power(self.vel_econ_recalque, 2)) / (2 * 9.81))
        if self.combobox_curva45_s.get() != 0:
            self.perda_carga_singular_curva45_r = ((float(self.combobox_curva45_r.get()) * 0.20) * (
                        np.power(self.vel_econ_recalque, 2)) / (2 * 9.81))
        if self.combobox_joelho90_s.get() != 0:
            self.perda_carga_singular_joelho90_r = ((float(self.combobox_joelho90_r.get()) * 0.90) * (
                        np.power(self.vel_econ_recalque, 2)) / (2 * 9.81))
        if self.combobox_joelho45_s.get() != 0:
            self.perda_carga_singular_joelho45_r = ((float(self.combobox_joelho45_r.get()) * 0.40) * (
                        np.power(self.vel_econ_recalque, 2)) / (2 * 9.81))
        if self.combobox_ret_leve_r.get() != 0:
            self.perda_carga_singular_ret_leve_r = ((float(self.combobox_ret_pesada_r.get()) * 2.50) * (
                        np.power(self.vel_econ_recalque, 2)) / (2 * 9.81))
        if self.combobox_ret_pesada_r.get() != 0:
            self.perda_carga_singular_ret_pesada_r = ((float(self.combobox_ret_leve_r.get()) * 2.50) * (
                        np.power(self.vel_econ_recalque, 2)) / (2 * 9.81))
        if self.combobox_val_globo_s.get() != 0:
            self.perda_carga_singular_val_globo_r = ((float(self.combobox_val_globo_r.get()) * 10) * (
                        np.power(self.vel_econ_recalque, 2)) / (2 * 9.81))
        if self.combobox_val_gaveta_s.get() != 0:
            self.perda_carga_singular_val_gaveta_r = ((float(self.combobox_val_gaveta_r.get()) * 0.20) * (
                        np.power(self.vel_econ_recalque, 2)) / (2 * 9.81))
        else:
            self.sem_perda_r = 0

        list_perda_s = [
        self.perda_carga_singular_curva90_s, self.perda_carga_singular_curva45_s, self.perda_carga_singular_joelho90_s,
        self.perda_carga_singular_joelho45_s, self.perda_carga_singular_crivo_s, self.perda_carga_singular_val_globo_s,
        self.perda_carga_singular_val_gaveta_s]

        self.perda_carga_singular_final_s = sum(list_perda_s)

        list_perda_r = [
        self.perda_carga_singular_curva90_r, self.perda_carga_singular_curva45_r, self.perda_carga_singular_joelho90_r,
        self.perda_carga_singular_joelho45_r, self.perda_carga_singular_ret_leve_r, self.perda_carga_singular_ret_pesada_r,
        self.perda_carga_singular_val_globo_r, self.perda_carga_singular_val_gaveta_r]

        self.perda_carga_singular_final_r = sum(list_perda_r)

        self.perda_carga_total = self.perda_carga_singular_final_r + self.perda_carga_singular_final_s + self.perda_carga_dist_s + self.perda_carga_dist_r


    def fator_atrito(self):

        #C??lculo do n??mero de Reynolds para suc????o
        self.reynolds_s = (4 * self.vazao_ajustada_cubic_meters) / (3.1415 * (self.diametro_succao / 1000) * 1E-6)

        # C??lculo do n??mero de Reynolds para o recalque
        self.reynolds_r = (4 * self.vazao_ajustada_cubic_meters) / (3.1415 * (self.diametro_recalque / 1000) * 1E-6)

        #fator de atrito na suc????o com pvc
        self.fator_atrito_s_pvc = 1.325 / (math.log(((5.74 / (self.reynolds_s ** 0.9))), 2.7)) ** 2

        # fator de atrito no recalque com pvc
        self.fator_atrito_r_pvc = 1.325 / (math.log(((5.74 / (self.reynolds_r ** 0.9))), 2.7)) ** 2

        # fator de atrito na suc????o com ferro galvanizado
        self.fator_atrito_s_ferro = 1.325 / (math.log(((0.15 / (3.7 * self.diametro_succao) + (5.74 / (self.reynolds_s ** 0.9)))), 2.7)) ** 2

        # fator de atrito no recalque com ferro galvanizado
        self.fator_atrito_r_ferro = 1.325 / (math.log(((0.15 / (3.7 * self.diametro_recalque) + (5.74 / (self.reynolds_r ** 0.9)))), 2.7)) ** 2



    def perda_carga_distribuida_s(self):
        if str(self.combobox_material.get()) == "PVC":
            self.perda_carga_dist_s = 0.0826 * self.fator_atrito_s_pvc * (float(self.comp_succao_entry.get()) / (self.diametro_succao / 1000)) * self.vazao_ajustada_cubic_meters
        elif str(self.combobox_material.get()) == "Ferro galvanizado":
            self.perda_carga_dist_s = 0.0826 * self.fator_atrito_s_ferro * (float(self.comp_succao_entry.get()) / (self.diametro_succao / 1000)) * self.vazao_ajustada_cubic_meters

    def perda_carga_distribuida_r(self):
        if str(self.combobox_material.get()) == "PVC":
            self.perda_carga_dist_r = 0.0826 * self.fator_atrito_r_pvc * (float(self.comp_recalque_entry.get()) / (self.diametro_recalque / 1000)) * self.vazao_ajustada_cubic_meters
        elif  str(self.combobox_material.get()) == "Ferro galvanizado":
            self.perda_carga_dist_r = 0.0826 * self.fator_atrito_r_ferro * (float(self.comp_recalque_entry.get()) / (self.diametro_recalque / 1000)) * self.vazao_ajustada_cubic_meters


    def altura_manometrica(self):
        self.altura_man_bomba = (float(self.altura_recalque_entry.get()) + float(self.altura_succao_entry.get())) + self.perda_carga_total + ((self.vel_econ_recalque**2 - self.vel_econ_succao**2) /(2 * 9.81))
        self.altura_man_bomba = round(self.altura_man_bomba, 2)

    def NPSH(self):
        self.npsh_disp = round((101300 / 7800) - (2 + self.perda_carga_singular_final_s + (32500 / 7800)), 2)


class Recalque(Funcs):
    def __init__(self):
        self.janela = janela
        self.cria_janela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.widgets_frame2()
        self.widgets_frame3()
        self.labels_frames()
        self.labels_succao_recalque()
        self.botoes()

        janela.mainloop()


    def cria_janela(self):
        self.janela.title("C??lculo para Recalque")
        self.janela.configure(background='lightgray')
        self.janela.geometry("1000x600")
        self.janela.resizable(width=False, height=False)



    def widgets_frame1(self):
        # Criando campo de vaz??o
        self.vazao_entry = Entry(self.frame_1)
        self.vazao_entry.place(x=15, y=30)
        self.vazao_entry.configure(width=4, font=("arial", 12))

        # Criando label do campo de vaz??o
        self.label_vazao = Label(self.frame_1, text="Vaz??o (L/s)", bg='#778899', font=("Arial", 12), fg='white')
        self.label_vazao.place(x=2, y=5)

        # Criando combobox para sele????o do material
        self.combobox_material = ttk.Combobox(self.frame_1, width=13, height=8, font=("arial", 12))
        self.combobox_material.place(x=150, y=32)
        self.combobox_material['values'] = ("PVC", "Ferro galvanizado", "")

        # Criando label para o combobox
        self.label_material = Label(self.frame_1, text="Material", bg='#778899', font=("Arial", 12), fg='white')
        self.label_material.place(x=190, y=5)

        # Criando label de tempo de funcionamento
        self.label_tempo = Label(self.frame_1, text="Bomba ON (h)", bg='#778899', font=("Arial", 12), fg='white')
        self.label_tempo.place(x=330, y=5)

        # Criando entry para o tempo
        self.tempo_entry = Entry(self.frame_1)
        self.tempo_entry.place(x=370, y=30)
        self.tempo_entry.configure(width=3, font=("arial", 12))

        # label para altura de suc????o
        self.altura_succao = Label(self.frame_1, text="Altura de suc????o (m)", bg='#778899', font=("Arial", 12),
                                   fg='white')
        self.altura_succao.place(x=510, y=5)

        # entry para altura de suc????o
        self.altura_succao_entry = Entry(self.frame_1)
        self.altura_succao_entry.place(x=570, y=30)
        self.altura_succao_entry.configure(width=3, font=("arial", 12))

        # label para altura de recalque
        self.altura_recalque = Label(self.frame_1, text="Altura de recalque (m)", bg='#778899', font=("Arial", 12),
                                     fg='white')
        self.altura_recalque.place(x=710, y=5)

        # Cria????o da entry para altura de recalque
        self.altura_recalque_entry = Entry(self.frame_1)
        self.altura_recalque_entry.place(x=770, y=30)
        self.altura_recalque_entry.configure(width=3, font=("arial", 12))

        # label para comprimento da suc????o
        self.comprimento_succao = Label(self.frame_1, text="L suc????o (m)", bg='#778899', font=("Arial", 12), fg='white')
        self.comprimento_succao.place(x=3, y=80)

        # entry para comprimento da suc????o
        self.comp_succao_entry = Entry(self.frame_1)
        self.comp_succao_entry.place(x=15, y=105)
        self.comp_succao_entry.configure(width=3, font=("arial", 12))

        # label para comprimento do recalque
        self.comprimento_recalque = Label(self.frame_1, text="L recalque (m)", bg='#778899', font=("Arial", 12),
                                          fg='white')
        self.comprimento_recalque.place(x=150, y=80)

        # entry para comprimento do recalque
        self.comp_recalque_entry = Entry(self.frame_1)
        self.comp_recalque_entry.place(x=180, y=105)
        self.comp_recalque_entry.configure(width=3, font=("arial", 12))

    def widgets_frame2(self):
        # Comboboxs do frame2
        self.combobox_curva90_s = ttk.Combobox(self.frame_2, width=2, height=8, font=("arial", 12))
        self.combobox_curva90_s.place(x=30, y=50)
        self.combobox_curva90_s['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.combobox_curva90_s.current(0)

        self.combobox_joelho90_s = ttk.Combobox(self.frame_2, width=2, height=8, font=("arial", 12))
        self.combobox_joelho90_s.place(x=150, y=50)
        self.combobox_joelho90_s['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.combobox_joelho90_s.current(0)

        self.combobox_curva45_s = ttk.Combobox(self.frame_2, width=2, height=8, font=("arial", 12))
        self.combobox_curva45_s.place(x=270, y=50)
        self.combobox_curva45_s['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.combobox_curva45_s.current(0)

        self.combobox_joelho45_s = ttk.Combobox(self.frame_2, width=2, height=8, font=("arial", 12))
        self.combobox_joelho45_s.place(x=30, y=140)
        self.combobox_joelho45_s['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.combobox_joelho45_s.current(0)

        self.combobox_crivo_s = ttk.Combobox(self.frame_2, width=2, height=8, font=("arial", 12))
        self.combobox_crivo_s.place(x=150, y=140)
        self.combobox_crivo_s['values'] = (0, 1)
        self.combobox_crivo_s.current(0)

        self.combobox_val_globo_s = ttk.Combobox(self.frame_2, width=2, height=8, font=("arial", 12))
        self.combobox_val_globo_s.place(x=270, y=140)
        self.combobox_val_globo_s['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.combobox_val_globo_s.current(0)

        self.combobox_val_gaveta_s = ttk.Combobox(self.frame_2, width=2, height=8, font=("arial", 12))
        self.combobox_val_gaveta_s.place(x=30, y=230)
        self.combobox_val_gaveta_s['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.combobox_val_gaveta_s.current(0)

    def widgets_frame3(self):
        # Comboboxs do frame3
        self.combobox_curva90_r = ttk.Combobox(self.frame_3, width=2, height=8, font=("arial", 12))
        self.combobox_curva90_r.place(x=30, y=50)
        self.combobox_curva90_r['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.combobox_curva90_r.current(0)

        self.combobox_joelho90_r = ttk.Combobox(self.frame_3, width=2, height=8, font=("arial", 12))
        self.combobox_joelho90_r.place(x=150, y=50)
        self.combobox_joelho90_r['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.combobox_joelho90_r.current(0)

        self.combobox_curva45_r = ttk.Combobox(self.frame_3, width=2, height=8, font=("arial", 12))
        self.combobox_curva45_r.place(x=270, y=50)
        self.combobox_curva45_r['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.combobox_curva45_r.current(0)

        self.combobox_joelho45_r = ttk.Combobox(self.frame_3, width=2, height=8, font=("arial", 12))
        self.combobox_joelho45_r.place(x=30, y=140)
        self.combobox_joelho45_r['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.combobox_joelho45_r.current(0)

        self.combobox_val_globo_r = ttk.Combobox(self.frame_3, width=2, height=8, font=("arial", 12))
        self.combobox_val_globo_r.place(x=150, y=140)
        self.combobox_val_globo_r['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.combobox_val_globo_r.current(0)

        self.combobox_val_gaveta_r = ttk.Combobox(self.frame_3, width=2, height=8, font=("arial", 12))
        self.combobox_val_gaveta_r.place(x=270, y=140)
        self.combobox_val_gaveta_r['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.combobox_val_gaveta_r.current(0)

        self.combobox_ret_leve_r = ttk.Combobox(self.frame_3, width=2, height=8, font=("arial", 12))
        self.combobox_ret_leve_r.place(x=30, y=230)
        self.combobox_ret_leve_r['values'] = (0, 1)
        self.combobox_ret_leve_r.current(0)

        self.combobox_ret_pesada_r = ttk.Combobox(self.frame_3, width=2, height=8, font=("arial", 12))
        self.combobox_ret_pesada_r.place(x=150, y=230)
        self.combobox_ret_pesada_r['values'] = (0, 1)
        self.combobox_ret_pesada_r.current(0)

    def labels_frames(self):
        # labels da Suc????o
        self.label01 = Label(self.frame_2, text="curva de 90??", bg='#778899', font=("Arial", 10), fg='white')
        self.label01.place(x=15, y=25)

        self.label02 = Label(self.frame_2, text="joelho de 90??", bg='#778899', font=("Arial", 10), fg='white')
        self.label02.place(x=130, y=25)

        self.label03 = Label(self.frame_2, text="curva de 45??", bg='#778899', font=("Arial", 10), fg='white')
        self.label03.place(x=260, y=25)

        self.label04 = Label(self.frame_2, text="joelho de 45??", bg='#778899', font=("Arial", 10), fg='white')
        self.label04.place(x=15, y=115)

        self.label05 = Label(self.frame_2, text="v??lvula de p?? e crivo", bg='#778899', font=("Arial", 10), fg='white')
        self.label05.place(x=110, y=115)

        self.label06 = Label(self.frame_2, text="v??lvula globo", bg='#778899', font=("Arial", 10), fg='white')
        self.label06.place(x=260, y=115)

        self.label07 = Label(self.frame_2, text="v??lvula gaveta", bg='#778899', font=("Arial", 10), fg='white')
        self.label07.place(x=15, y=205)

        # labels do Recalque
        self.label08 = Label(self.frame_3, text="curva de 90??", bg='#778899', font=("Arial", 10), fg='white')
        self.label08.place(x=15, y=25)

        self.label09 = Label(self.frame_3, text="joelho de 90??", bg='#778899', font=("Arial", 10), fg='white')
        self.label09.place(x=130, y=25)

        self.label10 = Label(self.frame_3, text="curva de 45??", bg='#778899', font=("Arial", 10), fg='white')
        self.label10.place(x=260, y=25)

        self.label11 = Label(self.frame_3, text="joelho de 45??", bg='#778899', font=("Arial", 10), fg='white')
        self.label11.place(x=15, y=115)

        self.label12 = Label(self.frame_3, text="v??lvula globo", bg='#778899', font=("Arial", 10), fg='white')
        self.label12.place(x=130, y=115)

        self.label13 = Label(self.frame_3, text="v??lvula gaveta", bg='#778899', font=("Arial", 10), fg='white')
        self.label13.place(x=260, y=115)

        self.label14 = Label(self.frame_3, text="reten????o leve", bg='#778899', font=("Arial", 10), fg='white')
        self.label14.place(x=15, y=205)

        self.label15 = Label(self.frame_3, text="reten????o pesada", bg='#778899', font=("Arial", 10), fg='white')
        self.label15.place(x=120, y=205)

    def labels_succao_recalque(self):
        label16 = self.label16 = Label(self.frame_2, text="Suc????o", bg='#420eed', foreground='#420eed',
                                       font=("Arial", 30), fg='white')
        self.label16.place(x=110, y=320)

        label17 = self.label17 = Label(self.frame_3, text="Recalque", bg='#420eed', foreground='#420eed',
                                       font=("Arial", 30), fg='white')
        self.label17.place(x=110, y=320)

    def botoes(self):
        self.btn_limpar = Button(self.frame_4, width=19, bd=4, height=3, bg='#e6ebe7', text="LIMPAR",
                                 command=self.limpa_campos)
        self.btn_limpar.place(x=10, y=20)

        self.btn_calcular = Button(self.frame_4, width=19, bd=4, height=3, bg='#e6ebe7', text="CALCULAR",
                                   command=self.tratamento_erros)
        self.btn_calcular.place(x=10, y=100)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.janela, bd=4, bg='#778899', highlightbackground='#6495ED', highlightthickness=3)
        self.frame_1.place(x=10, y=10, width=980, height=180)

        self.frame_2 = Frame(self.janela, bd=4, bg='#778899', highlightbackground='#6495ED', highlightthickness=3)
        self.frame_2.place(x=10, y=200, width=380, height=380)

        self.frame_3 = Frame(self.janela, bd=4, bg='#778899', highlightbackground='#6495ED', highlightthickness=3)
        self.frame_3.place(x=410, y=200, width=380, height=380)

        self.frame_4 = Frame(self.janela, bd=4, bg='#778899', highlightbackground='#6495ED', highlightthickness=3)
        self.frame_4.place(x=810, y=200, width=180, height=380)


    def Tela_resultado(self):
        result = Tk()
        self.result = result


        self.result.title("Resultados")
        self.result.configure(background='lightgray')
        self.result.geometry("500x530")
        self.result.resizable(width=False, height=False)

        self.frame_result = Frame(self.result, bd=4, bg='#778899', highlightbackground='#6495ED', highlightthickness=3)
        self.frame_result.place(x=10, y=10, width=480, height=510)

        self.widgets_tela_resultado()
        self.limpa_campos()


        result.mainloop()


    def widgets_tela_resultado(self):
        self.vel_econ_recalque = round(self.vel_econ_recalque, 2)
        self.vel_econ_succao = round(self.vel_econ_succao, 2)
        self.perda_carga_singular_final_r = round(self.perda_carga_singular_final_r, 2)
        self.perda_carga_singular_final_s = round(self.perda_carga_singular_final_s, 2)
        self.perda_carga_total = round(self.perda_carga_total, 2)
        self.perda_carga_total_s = round(self.perda_carga_singular_final_s + self.perda_carga_dist_s, 2)
        self.perda_carga_total_r = round(self.perda_carga_singular_final_r + self.perda_carga_dist_r, 2)

        label18 = self.label18 = Label(self.frame_result, text="Altura manom??trica da bomba: " + str(self.altura_man_bomba) + " m", foreground='white',
                                font=("Arial", 15), fg='black')
        self.label18.place(x=20, y=20)

        label19 = self.label19 = Label(self.frame_result, text="Vaz??o do sistema: " + str(self.vazao_ajustada_cubic_hours) + " m??/h", foreground='white',
                                       font=("Arial", 15), fg='black')
        self.label19.place(x=20, y=60)

        label20 = self.label20 = Label(self.frame_result, text="NPSH dispon??vel: " + str(self.npsh_disp) + " m", foreground='white',
                                       font=("Arial", 15), fg='black')
        self.label20.place(x=20, y=100)

        label21 = self.label21 = Label(self.frame_result,text="Velocidade de recalque: " + str(self.vel_econ_recalque) + " m/s", foreground='white',
                                       font=("Arial", 15), fg='black')
        self.label21.place(x=20, y=140)

        label22 = self.label22 = Label(self.frame_result, text="Velocidade de suc????o: " + str(self.vel_econ_succao) + " m/s", foreground='white',
                                       font=("Arial", 15), fg='black')
        self.label22.place(x=20, y=180)

        label23 = self.label23 = Label(self.frame_result, text="Di??metro do recalque: " + str(self.diametro_recalque) + " mm", foreground='white',
                                       font=("Arial", 15), fg='black')
        self.label23.place(x=20, y=220)

        label24 = self.label24 = Label(self.frame_result, text="Di??metro da suc????o: " + str(self.diametro_succao) + " mm", foreground='white',
                                       font=("Arial", 15), fg='black')
        self.label24.place(x=20, y=260)

        label25 = self.label25 = Label(self.frame_result, text="Perda de carga no recalque: " + str(self.perda_carga_total_r) + " m", foreground='white',
                                       font=("Arial", 15), fg='black')
        self.label25.place(x=20, y=300)

        label26 = self.label26 = Label(self.frame_result, text="Perda de carga na suc????o: " + str(self.perda_carga_total_s) + " m", foreground='white',
                                       font=("Arial", 15), fg='black')
        self.label26.place(x=20, y=340)

        label27 = self.label27 = Label(self.frame_result, text="Perda de carga total: " + str(self.perda_carga_total) + " m", foreground='white',
                                       font=("Arial", 15), fg='black')
        self.label27.place(x=20, y=380)



Recalque()
