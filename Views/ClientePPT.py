from Ui_GUI_PPT_game import Ui_MainWindow
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import threading
import socket
import time
import sys

HOST = 'localhost'
PORT = 9999


class Cliente():
    def __init__(self, _host, _port, _socket_client):
        self.host = _host
        self.port = _port
        self.socket_client = _socket_client
        self.idClient = 0
        self.eleccion = ''
        self.puntaje = [0,0,0] #[G, P, E]
        self.puntaje_rival = [0,0,0]

    def receive_pack(self): #regresa class<'str'>
        data = self.socket_client.recv(1024)
        dt = data.decode()
        return dt
    
    def send_pack(self, option):
        dt = bytes(option, 'UTF-8')
        self.socket_client.send(dt)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        socket_client = socket.socket()
        self.client = Cliente(HOST, PORT, socket_client)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        iconN = QIcon()
        iconN.addFile(u"../Assets_UI/Icon_chevron-turn-swipe-circle-right", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.PB_icon_windows_title.setIcon(iconN)
        self.ui.PB_icon_windows_title.setEnabled(False)
        self.ui.GB_opciones_player1_red.setEnabled(False)
        self.ui.GB_opciones_player2_blue.setEnabled(False)
        self.ui.PB_play_player1_red.setEnabled(False)
        self.ui.PB_play_player2_blue.setEnabled(False)

        self.ui.actionConectar_al_servidor.triggered.connect(self.qactionCatcher_conectar_servidor)
        self.ui.actionDesconectar_del_servidor.triggered.connect(self.qactionCatcher_desconectar_servidor)
        self.ui.actionSalir_del_juego.triggered.connect(self.qactionCatcher_salir_juego)

        self.ui.PB_play_player1_red.clicked.connect(self.jugador1_eleccion)
        self.ui.PB_play_player2_blue.clicked.connect(self.jugador2_eleccion)

        self.ui.PB_icon_windows_title.clicked.connect(self.esperando_partida)

#- - - - - - - - - - - - - - - - DEFINIENDO QACTION CATCHERS - - - - - - - - - -
    def qactionCatcher_conectar_servidor(self, s):
        self.client.socket_client.connect((self.client.host, self.client.port))
        t = threading.Thread(target=self.esperando_partida, args=())
        t.start()

    def qactionCatcher_desconectar_servidor(self, s):
        self.client.socket_client.close()

    def qactionCatcher_salir_juego(self, s):
        ...

#- - - - - - - - - - - - - - - - DEFINIENDO SLOTS - - - - - - - - - - - - - - - - 
    def jugador1_eleccion(self):
        t = threading.Thread(target = self.esperando_respuesta, args =())
        if(self.ui.RB_piedra_player1_red.isChecked()):
            print("\npiedra")
            self.client.eleccion = 'piedra'
            self.client.send_pack(self.client.eleccion)
            self.ui.PB_play_player1_red.setEnabled(False)
            self.ui.GB_opciones_player1_red.setEnabled(False)
            self.ui.Lb_imagen_player1_red.setPixmap(u"../Assets_UI/Piedra_Red")
            self.ui.Lb_imagen_player2_blue.setPixmap(u"../Assets_UI/Icon_HourGlass_finished")
            t.start()

        elif(self.ui.RB_papel_player1_red.isChecked()):
            print("\npapel")
            self.client.eleccion = 'papel'
            self.client.send_pack(self.client.eleccion)
            self.ui.PB_play_player1_red.setEnabled(False)
            self.ui.GB_opciones_player1_red.setEnabled(False)
            self.ui.Lb_imagen_player1_red.setPixmap(u"../Assets_UI/Papel_Red")
            self.ui.Lb_imagen_player2_blue.setPixmap(u"../Assets_UI/Icon_HourGlass_finished")
            t.start()
            
        elif(self.ui.RB_tijera_player1_red.isChecked()):
            print("\ntijera")
            self.client.eleccion = 'tijera'
            self.client.send_pack(self.client.eleccion)
            self.ui.PB_play_player1_red.setEnabled(False)
            self.ui.GB_opciones_player1_red.setEnabled(False)
            self.ui.Lb_imagen_player1_red.setPixmap(u"../Assets_UI/Tijera_Red")
            self.ui.Lb_imagen_player2_blue.setPixmap(u"../Assets_UI/Icon_HourGlass_finished")
            t.start()

    def jugador2_eleccion(self):
        t = threading.Thread(target = self.esperando_respuesta, args =())
        if(self.ui.RB_piedra_player2_blue.isChecked()):
            print("\npiedra")
            self.client.eleccion = 'piedra'
            self.client.send_pack(self.client.eleccion)
            self.ui.PB_play_player2_blue.setEnabled(False)
            self.ui.GB_opciones_player2_blue.setEnabled(False)
            self.ui.Lb_imagen_player2_blue.setPixmap(u"../Assets_UI/Piedra_Blue")
            self.ui.Lb_imagen_player1_red.setPixmap(u"../Assets_UI/Icon_HourGlass_finished")
            t.start()

        elif(self.ui.RB_papel_player2_blue.isChecked()):
            print("\npapel")
            self.client.eleccion = 'papel'
            self.client.send_pack(self.client.eleccion)
            self.ui.PB_play_player2_blue.setEnabled(False)
            self.ui.GB_opciones_player2_blue.setEnabled(False)
            self.ui.Lb_imagen_player2_blue.setPixmap(u"../Assets_UI/Papel_Blue")
            self.ui.Lb_imagen_player1_red.setPixmap(u"../Assets_UI/Icon_HourGlass_finished")
            t.start()

        elif(self.ui.RB_tijera_player2_blue.isChecked()):
            print("\ntijera")
            self.client.eleccion = 'tijera'
            self.client.send_pack(self.client.eleccion)
            self.ui.PB_play_player2_blue.setEnabled(False)
            self.ui.GB_opciones_player2_blue.setEnabled(False)
            self.ui.Lb_imagen_player2_blue.setPixmap(u"../Assets_UI/Tijera_Blue")
            self.ui.Lb_imagen_player1_red.setPixmap(u"../Assets_UI/Icon_HourGlass_finished")
            t.start()
    
#- - - - - - - - - - - - - - - - DEFINIENDO METODOS AUXILIARES - -
    def esperando_partida(self):
        self.ui.Lb_imagen_player1_red.setPixmap("")
        self.ui.Lb_imagen_player2_blue.setPixmap("")
        self.ui.PB_icon_windows_title.setEnabled(False)
        self.ui.GB_opciones_player1_red.setEnabled(False)
        self.ui.GB_opciones_player2_blue.setEnabled(False)
        self.ui.PB_play_player1_red.setEnabled(False)
        self.ui.PB_play_player2_blue.setEnabled(False)
        self.ui.Lb_messages.setText("")
        if(self.client.idClient==0):
            idDisponibles = ['1','2']
            ans = self.client.receive_pack()
            while(not ans in idDisponibles):
                ans = self.client.receive_pack()
                time.sleep(2)

            self.client.idClient = int(ans)

        if(self.client.idClient==1):
            self.ui.Icon_player2_blue.setEnabled(False)
            self.ui.Lb_opt_chosen_player1_red.setText("Esperando Rival ...")
            self.ui.Lb_opt_chosen_player2_blue.setText("Buscando rival...")
        elif(self.client.idClient==2):
            self.ui.Icon_player1_red.setEnabled(False)
        ans = ''
        while(ans != 'MATCH'):
            ans = self.client.receive_pack()
            time.sleep(1)

        self.ui.Lb_opt_chosen_player1_red.setText("Partida Lista")
        self.ui.Lb_opt_chosen_player2_blue.setText("Partida Lista")
        if(self.client.idClient==1):
            self.ui.GB_opciones_player1_red.setEnabled(True)
            self.ui.PB_play_player1_red.setEnabled(True)
        elif(self.client.idClient==2):
            self.ui.GB_opciones_player2_blue.setEnabled(True)
            self.ui.PB_play_player2_blue.setEnabled(True)
        
    def esperando_respuesta(self):
        resultados = ['ganaste','perdiste','empate']
        ans = self.client.receive_pack()
        while(not ans in resultados):
            time.sleep(5)
    
        rival = self.complemento_eleccion(self.client.eleccion, ans)

        if(self.client.idClient==1):
            if(rival=='piedra'):
                self.ui.Lb_imagen_player2_blue.setPixmap(u"../Assets_UI/Piedra_Blue")
            elif(rival=='papel'):
                self.ui.Lb_imagen_player2_blue.setPixmap(u"../Assets_UI/Papel_Blue")
            elif(rival=='tijera'):
                self.ui.Lb_imagen_player2_blue.setPixmap(u"../Assets_UI/Tijera_Blue")
        elif(self.client.idClient==2):
            if(rival=='piedra'):
                self.ui.Lb_imagen_player1_red.setPixmap(u"../Assets_UI/Piedra_Red")
            elif(rival=='papel'):
                self.ui.Lb_imagen_player1_red.setPixmap(u"../Assets_UI/Papel_Red")
            elif(rival=='tijera'):
                self.ui.Lb_imagen_player1_red.setPixmap(u"../Assets_UI/Tijera_Red")
        
        if(ans == 'ganaste'):
            self.ui.Lb_messages.setFont(QFont('Times', 20))
            self.ui.Lb_messages.setText("GANASTE")
            self.client.puntaje[0] += 1
            self.client.puntaje_rival[1] += 1
        elif(ans == 'perdiste'):
            self.ui.Lb_messages.setFont(QFont('Times', 20))
            self.ui.Lb_messages.setText("PERDISTE")
            self.client.puntaje[1] += 1
            self.client.puntaje_rival[0] += 1
        else:
            self.ui.Lb_messages.setFont(QFont('Times', 20))
            self.ui.Lb_messages.setText("EMPATASTE")
            self.client.puntaje[2] += 1   
            self.client.puntaje_rival[2] += 1
        
        if(self.client.idClient==1):
            self.ui.LCDNum_G_player1_red.display(self.client.puntaje[0])
            self.ui.LCDNum_P_player1_red.display(self.client.puntaje[1])
            self.ui.LCDNum_E_player1_red.display(self.client.puntaje[2])

            self.ui.LCDNum_G_player2_blue.display(self.client.puntaje_rival[0])
            self.ui.LCDNum_P_player2_blue.display(self.client.puntaje_rival[1])
            self.ui.LCDNum_E_player2_blue.display(self.client.puntaje_rival[2])
        elif(self.client.idClient==2):
            self.ui.LCDNum_G_player2_blue.display(self.client.puntaje[0])
            self.ui.LCDNum_P_player2_blue.display(self.client.puntaje[1])
            self.ui.LCDNum_E_player2_blue.display(self.client.puntaje[2])

            self.ui.LCDNum_G_player1_red.display(self.client.puntaje_rival[0])
            self.ui.LCDNum_P_player1_red.display(self.client.puntaje_rival[1])
            self.ui.LCDNum_E_player1_red.display(self.client.puntaje_rival[2])

        self.ui.PB_icon_windows_title.setEnabled(True)

    def complemento_eleccion(self, eleccion, resultado):
        lpieTij = ['piedra','ganaste','tijera']
        lpiePap = ['piedra','perdiste','papel']
        lpiePie = ['piedra','empate','piedra']
        lpapPie = ['papel','ganaste','piedra']
        lpapTij = ['papel','perdiste','tijera']
        lpapPap = ['papel','empate','papel']
        ltijPap = ['tijera','ganaste','papel']
        ltijPie = ['tijera','perdiste','piedra']
        ltijTij = ['tijera','empate','tijera']
        listaTotal = [lpieTij, lpiePap, lpiePie, lpapPie, lpapTij, lpapPap, ltijPap, ltijPie, ltijTij]
        for i in listaTotal:
            if(eleccion==i[0] and resultado==i[1]):
                return i[2]
        
    def adiciona_puntaje_global(self):
        
        ...

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# - - - - - - - - - - - - - - - DEFINIENDO CUERPO PRINCIPAL - - -
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_() 