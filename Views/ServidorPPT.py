from PPT_how_win import iguales, evalua_ganador

import threading
import socket
import time
import sys

global toolsave

HOST = 'localhost'
PORT = 9999
MAX_SOLICITUDES_CONEX = 6


class ToolSave(object):
    def __init__(self):
        self.sala = {}
        self.salaRespuestas = {}
        self.salaContinuar = {}

    def __repr__(self):
        return "{}".format(self.answers)
    def __str__(self):
        return "{}".format(self.answers)
    
class Servidor():
    def __init__(self, _host, _port, _max_solicitudes_conex):
        self.host = _host
        self.port = _port
        self.max_solicitudes_conex = _max_solicitudes_conex
        
    def inicializar(self):
        socket_server = socket.socket()

        socket_server.bind((self.host, self.port)) #Configuramos el servidor con un HOST y un PORT
        socket_server.listen(self.max_solicitudes_conex) #Configuramos el numero maximo de solicitudes de conexión
        
        idSala = 0
        while True:
            idSala += 1
            lista = []
            for i in range(2):
                print("\nEsperando conexión ...")
                conexion, direccion = socket_server.accept()
                lista.append(direccion[1])
                hilo = Hilo_servidor(conexion, direccion[1], idSala)
                hilo.start()
            toolsave.sala[idSala] = lista
            toolsave.salaRespuestas[idSala] = []
                
    # - - - - - - - METODOS AUXILIARES - - - - - - - - -

            
class Hilo_servidor(threading.Thread):
    def __init__(self, conexion, direccion_sock, _idSala):
        threading.Thread.__init__(self)
        self.conexion = conexion
        self.direccion = direccion_sock
        self.condicionContinuar = True
        self.idSala = _idSala # E {N}
        self.idJugador = 0 # {1,2}

    def send_pack(self, msg):
        dt = bytes(msg, 'UTF-8')
        self.conexion.send(dt)
    
    def receive_pack(self):
        data = self.conexion.recv(1024)
        dt = data.decode('UTF-8')
        return dt
    
    def reiniciar_ronda(self):
        
        ...

    def run(self):
        opciones = ['piedra','papel','tijera']
        while self.condicionContinuar:
            try:
                while(not toolsave.sala.get(self.idSala)):
                    time.sleep(2)

                if(self.idJugador==0):
                    self.idJugador = toolsave.sala[self.idSala].index(self.direccion)+1
                    print(self.idJugador)
                    try:
                        self.send_pack(str(self.idJugador))
                    except ConnectionResetError:
                        raise ConnectionAbortedError

                cadena = 'MATCH'
                try:
                    self.send_pack(cadena)
                except ConnectionResetError:
                    raise ConnectionAbortedError

                try:
                    ans = self.receive_pack()
                except ConnectionResetError:
                    raise ConnectionAbortedError
                while(not ans in opciones):
                    time.sleep(2)
            
                toolsave.salaRespuestas[self.idSala].insert(self.idJugador-1, ans)
                print(toolsave.salaRespuestas)
                while(len(toolsave.salaRespuestas[self.idSala])<2):
                    time.sleep(2)

                resultado = evalua_ganador(toolsave.salaRespuestas[self.idSala])
            
                try:
                    self.send_pack(resultado[self.idJugador-1])
                except ConnectionResetError:
                    raise ConnectionAbortedError
        
                time.sleep(5)
                toolsave.salaRespuestas[self.idSala] = []
            except ConnectionAbortedError:
                print("Se cerro la conexión de", self.idJugador, self.direccion)
                self.conexion.close()
                self.condicionContinuar = False


if(__name__ == '__main__'):
    toolsave = ToolSave()
    servidor = Servidor(HOST, PORT, MAX_SOLICITUDES_CONEX)
    servidor.inicializar()

