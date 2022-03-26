# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_PPT_game.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(837, 665)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(170, 0, 0, 255), stop:1 rgba(0, 0, 108, 255));")
        self.actionConectar_al_servidor = QAction(MainWindow)
        self.actionConectar_al_servidor.setObjectName(u"actionConectar_al_servidor")
        icon = QIcon()
        icon.addFile(u"../Assets_UI/Icon_ChainLinked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionConectar_al_servidor.setIcon(icon)
        self.actionDesconectar_del_servidor = QAction(MainWindow)
        self.actionDesconectar_del_servidor.setObjectName(u"actionDesconectar_del_servidor")
        icon1 = QIcon()
        icon1.addFile(u"../Assets_UI/Icon_ChainBroken.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDesconectar_del_servidor.setIcon(icon1)
        self.actionSalir_del_juego = QAction(MainWindow)
        self.actionSalir_del_juego.setObjectName(u"actionSalir_del_juego")
        icon2 = QIcon()
        icon2.addFile(u"../Assets_UI/Icon_Close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSalir_del_juego.setIcon(icon2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Frame_Title_Game = QFrame(self.centralwidget)
        self.Frame_Title_Game.setObjectName(u"Frame_Title_Game")
        self.Frame_Title_Game.setGeometry(QRect(220, 0, 391, 51))
        self.Frame_Title_Game.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"background-color: rgba(0, 0, 0, 100);")
        self.Frame_Title_Game.setFrameShape(QFrame.StyledPanel)
        self.Frame_Title_Game.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Frame_Title_Game)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Icon_left_title_game = QPushButton(self.Frame_Title_Game)
        self.Icon_left_title_game.setObjectName(u"Icon_left_title_game")
        icon3 = QIcon()
        icon3.addFile(u"../Assets_UI/Icon_control_joystick.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Icon_left_title_game.setIcon(icon3)
        self.Icon_left_title_game.setIconSize(QSize(33, 33))
        self.Icon_left_title_game.setFlat(True)

        self.horizontalLayout.addWidget(self.Icon_left_title_game)

        self.Lb_Title_Game = QLabel(self.Frame_Title_Game)
        self.Lb_Title_Game.setObjectName(u"Lb_Title_Game")
        self.Lb_Title_Game.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.Lb_Title_Game.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.Lb_Title_Game)

        self.Icon_right_title_game = QPushButton(self.Frame_Title_Game)
        self.Icon_right_title_game.setObjectName(u"Icon_right_title_game")
        self.Icon_right_title_game.setIcon(icon3)
        self.Icon_right_title_game.setIconSize(QSize(33, 33))
        self.Icon_right_title_game.setFlat(True)

        self.horizontalLayout.addWidget(self.Icon_right_title_game)

        self.Line_Vertical = QFrame(self.centralwidget)
        self.Line_Vertical.setObjectName(u"Line_Vertical")
        self.Line_Vertical.setGeometry(QRect(420, 50, 20, 401))
        self.Line_Vertical.setStyleSheet(u"background-color: rgba(0, 0, 0, 150);")
        self.Line_Vertical.setFrameShape(QFrame.VLine)
        self.Line_Vertical.setFrameShadow(QFrame.Sunken)
        self.Line_horizontal = QFrame(self.centralwidget)
        self.Line_horizontal.setObjectName(u"Line_horizontal")
        self.Line_horizontal.setGeometry(QRect(0, 450, 841, 20))
        self.Line_horizontal.setStyleSheet(u"background-color: rgba(0, 0, 0, 150);")
        self.Line_horizontal.setFrameShape(QFrame.HLine)
        self.Line_horizontal.setFrameShadow(QFrame.Sunken)
        self.Frame_player_1_red = QFrame(self.centralwidget)
        self.Frame_player_1_red.setObjectName(u"Frame_player_1_red")
        self.Frame_player_1_red.setGeometry(QRect(120, 60, 181, 301))
        self.Frame_player_1_red.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.Frame_player_1_red.setFrameShape(QFrame.StyledPanel)
        self.Frame_player_1_red.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Frame_player_1_red)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.Frame_player_1_red)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Lb_player1_title = QLabel(self.frame_2)
        self.Lb_player1_title.setObjectName(u"Lb_player1_title")
        self.Lb_player1_title.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_2.addWidget(self.Lb_player1_title)

        self.Icon_player1_red = QPushButton(self.frame_2)
        self.Icon_player1_red.setObjectName(u"Icon_player1_red")
        icon4 = QIcon()
        icon4.addFile(u"../Assets_UI/Icon_MarioBros.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Icon_player1_red.setIcon(icon4)
        self.Icon_player1_red.setIconSize(QSize(50, 50))
        self.Icon_player1_red.setFlat(True)

        self.horizontalLayout_2.addWidget(self.Icon_player1_red)


        self.verticalLayout.addWidget(self.frame_2)

        self.Lb_imagen_player1_red = QLabel(self.Frame_player_1_red)
        self.Lb_imagen_player1_red.setObjectName(u"Lb_imagen_player1_red")
        self.Lb_imagen_player1_red.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.Lb_imagen_player1_red.setPixmap(QPixmap()) #u"../Assets_UI/Tijera_Red.PNG"
        self.Lb_imagen_player1_red.setScaledContents(True)

        self.verticalLayout.addWidget(self.Lb_imagen_player1_red)

        self.Lb_opt_chosen_player1_red = QLabel(self.Frame_player_1_red)
        self.Lb_opt_chosen_player1_red.setObjectName(u"Lb_opt_chosen_player1_red")

        self.verticalLayout.addWidget(self.Lb_opt_chosen_player1_red)

        self.Frame_player_2_blue = QFrame(self.centralwidget)
        self.Frame_player_2_blue.setObjectName(u"Frame_player_2_blue")
        self.Frame_player_2_blue.setGeometry(QRect(550, 60, 181, 301))
        self.Frame_player_2_blue.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.Frame_player_2_blue.setFrameShape(QFrame.StyledPanel)
        self.Frame_player_2_blue.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Frame_player_2_blue)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.Frame_player_2_blue)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Lb_player2_title = QLabel(self.frame_5)
        self.Lb_player2_title.setObjectName(u"Lb_player2_title")
        self.Lb_player2_title.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_3.addWidget(self.Lb_player2_title)

        self.Icon_player2_blue = QPushButton(self.frame_5)
        self.Icon_player2_blue.setObjectName(u"Icon_player2_blue")
        icon5 = QIcon()
        icon5.addFile(u"../Assets_UI/Icon_HomeroS.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Icon_player2_blue.setIcon(icon5)
        self.Icon_player2_blue.setIconSize(QSize(50, 50))
        self.Icon_player2_blue.setFlat(True)

        self.horizontalLayout_3.addWidget(self.Icon_player2_blue)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.Lb_imagen_player2_blue = QLabel(self.Frame_player_2_blue)
        self.Lb_imagen_player2_blue.setObjectName(u"Lb_imagen_player2_blue")
        self.Lb_imagen_player2_blue.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.Lb_imagen_player2_blue.setPixmap(QPixmap()) #u"../Assets_UI/Papel_Blue.PNG"
        self.Lb_imagen_player2_blue.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.Lb_imagen_player2_blue)

        self.Lb_opt_chosen_player2_blue = QLabel(self.Frame_player_2_blue)
        self.Lb_opt_chosen_player2_blue.setObjectName(u"Lb_opt_chosen_player2_blue")

        self.verticalLayout_2.addWidget(self.Lb_opt_chosen_player2_blue)

        self.GB_opciones_player1_red = QGroupBox(self.centralwidget)
        self.GB_opciones_player1_red.setObjectName(u"GB_opciones_player1_red")
        self.GB_opciones_player1_red.setGeometry(QRect(60, 370, 184, 61))
        self.GB_opciones_player1_red.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"background-color: rgba(255, 255, 255, 150);")
        self.horizontalLayout_4 = QHBoxLayout(self.GB_opciones_player1_red)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.RB_piedra_player1_red = QRadioButton(self.GB_opciones_player1_red)
        self.RB_piedra_player1_red.setObjectName(u"RB_piedra_player1_red")
        self.RB_piedra_player1_red.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.RB_piedra_player1_red)

        self.RB_papel_player1_red = QRadioButton(self.GB_opciones_player1_red)
        self.RB_papel_player1_red.setObjectName(u"RB_papel_player1_red")
        self.RB_papel_player1_red.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.RB_papel_player1_red)

        self.RB_tijera_player1_red = QRadioButton(self.GB_opciones_player1_red)
        self.RB_tijera_player1_red.setObjectName(u"RB_tijera_player1_red")
        self.RB_tijera_player1_red.setStyleSheet(u"background-color: rgba(255, 255, 255, 150);")

        self.horizontalLayout_4.addWidget(self.RB_tijera_player1_red)

        self.GB_opciones_player2_blue = QGroupBox(self.centralwidget)
        self.GB_opciones_player2_blue.setObjectName(u"GB_opciones_player2_blue")
        self.GB_opciones_player2_blue.setGeometry(QRect(500, 370, 184, 61))
        self.GB_opciones_player2_blue.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"background-color: rgba(255, 255, 255, 150);")
        self.horizontalLayout_5 = QHBoxLayout(self.GB_opciones_player2_blue)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.RB_piedra_player2_blue = QRadioButton(self.GB_opciones_player2_blue)
        self.RB_piedra_player2_blue.setObjectName(u"RB_piedra_player2_blue")
        self.RB_piedra_player2_blue.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.RB_piedra_player2_blue)

        self.RB_papel_player2_blue = QRadioButton(self.GB_opciones_player2_blue)
        self.RB_papel_player2_blue.setObjectName(u"RB_papel_player2_blue")
        self.RB_papel_player2_blue.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.RB_papel_player2_blue)

        self.RB_tijera_player2_blue = QRadioButton(self.GB_opciones_player2_blue)
        self.RB_tijera_player2_blue.setObjectName(u"RB_tijera_player2_blue")
        self.RB_tijera_player2_blue.setStyleSheet(u"background-color: rgba(255, 255, 255, 150);")

        self.horizontalLayout_5.addWidget(self.RB_tijera_player2_blue)

        self.PB_play_player1_red = QPushButton(self.centralwidget)
        self.PB_play_player1_red.setObjectName(u"PB_play_player1_red")
        self.PB_play_player1_red.setGeometry(QRect(310, 380, 81, 41))
        self.PB_play_player1_red.setStyleSheet(u"background-color: rgba(255, 255, 255, 150);")
        icon6 = QIcon()
        icon6.addFile(u"../Assets_UI/Icon_Control_wireless.png", QSize(), QIcon.Normal, QIcon.Off)
        self.PB_play_player1_red.setIcon(icon6)
        self.PB_play_player1_red.setIconSize(QSize(40, 40))
        self.PB_play_player1_red.setFlat(False)
        self.PB_play_player2_blue = QPushButton(self.centralwidget)
        self.PB_play_player2_blue.setObjectName(u"PB_play_player2_blue")
        self.PB_play_player2_blue.setGeometry(QRect(730, 380, 81, 41))
        self.PB_play_player2_blue.setStyleSheet(u"background-color: rgba(255, 255, 255, 150);")
        self.PB_play_player2_blue.setIcon(icon6)
        self.PB_play_player2_blue.setIconSize(QSize(40, 40))
        self.PB_play_player2_blue.setFlat(False)
        self.Line_horizontal_2 = QFrame(self.centralwidget)
        self.Line_horizontal_2.setObjectName(u"Line_horizontal_2")
        self.Line_horizontal_2.setGeometry(QRect(0, 530, 841, 20))
        self.Line_horizontal_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 150);")
        self.Line_horizontal_2.setFrameShape(QFrame.HLine)
        self.Line_horizontal_2.setFrameShadow(QFrame.Sunken)
        self.Lb_icon_messages_2 = QLabel(self.centralwidget)
        self.Lb_icon_messages_2.setObjectName(u"Lb_icon_messages_2")
        self.Lb_icon_messages_2.setGeometry(QRect(10, 470, 61, 61))
        self.Lb_icon_messages_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.Lb_icon_messages_2.setPixmap(QPixmap(u"../Assets_UI/Icon_Comments.png"))
        self.Lb_icon_messages_2.setScaledContents(True)
        self.Frame_messages = QFrame(self.centralwidget)
        self.Frame_messages.setObjectName(u"Frame_messages")
        self.Frame_messages.setGeometry(QRect(340, 470, 181, 61))
        self.Frame_messages.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.Frame_messages.setFrameShape(QFrame.StyledPanel)
        self.Frame_messages.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.Frame_messages)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Lb_messages = QLabel(self.Frame_messages)
        self.Lb_messages.setObjectName(u"Lb_messages") #u"Lb_messages"
        self.Lb_messages.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_6.addWidget(self.Lb_messages)

        self.Lb_icon_messages = QLabel(self.Frame_messages)
        self.Lb_icon_messages.setObjectName(u"Lb_icon_messages")
        self.Lb_icon_messages.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.Lb_icon_messages.setPixmap(QPixmap())#u"../Assets_UI/Icon_Fireworks.png"
        self.Lb_icon_messages.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.Lb_icon_messages)

        self.PB_icon_score_player1_red = QPushButton(self.centralwidget)
        self.PB_icon_score_player1_red.setObjectName(u"PB_icon_score_player1_red")
        self.PB_icon_score_player1_red.setGeometry(QRect(10, 560, 41, 41))
        icon7 = QIcon()
        icon7.addFile(u"../Assets_UI/Icon_Score.png", QSize(), QIcon.Normal, QIcon.Off)
        self.PB_icon_score_player1_red.setIcon(icon7)
        self.PB_icon_score_player1_red.setIconSize(QSize(40, 40))
        self.PB_icon_score_player1_red.setFlat(True)
        self.Frame_score_player1_red = QFrame(self.centralwidget)
        self.Frame_score_player1_red.setObjectName(u"Frame_score_player1_red")
        self.Frame_score_player1_red.setGeometry(QRect(50, 550, 201, 71))
        self.Frame_score_player1_red.setStyleSheet(u"background-color: rgba(226, 0, 0, 150);")
        self.Frame_score_player1_red.setFrameShape(QFrame.StyledPanel)
        self.Frame_score_player1_red.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.Frame_score_player1_red)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.Frame_G_player1_red = QFrame(self.Frame_score_player1_red)
        self.Frame_G_player1_red.setObjectName(u"Frame_G_player1_red")
        self.Frame_G_player1_red.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);")
        self.Frame_G_player1_red.setFrameShape(QFrame.StyledPanel)
        self.Frame_G_player1_red.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Frame_G_player1_red)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Lb_G_player1_red = QLabel(self.Frame_G_player1_red)
        self.Lb_G_player1_red.setObjectName(u"Lb_G_player1_red")
        self.Lb_G_player1_red.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_3.addWidget(self.Lb_G_player1_red)

        self.LCDNum_G_player1_red = QLCDNumber(self.Frame_G_player1_red)
        self.LCDNum_G_player1_red.setObjectName(u"LCDNum_G_player1_red")
        self.LCDNum_G_player1_red.setMode(QLCDNumber.Dec)

        self.verticalLayout_3.addWidget(self.LCDNum_G_player1_red)


        self.horizontalLayout_7.addWidget(self.Frame_G_player1_red)

        self.Frame_P_player2_blue = QFrame(self.Frame_score_player1_red)
        self.Frame_P_player2_blue.setObjectName(u"Frame_P_player2_blue")
        self.Frame_P_player2_blue.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);")
        self.Frame_P_player2_blue.setFrameShape(QFrame.StyledPanel)
        self.Frame_P_player2_blue.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Frame_P_player2_blue)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Lb_P_player1_red = QLabel(self.Frame_P_player2_blue)
        self.Lb_P_player1_red.setObjectName(u"Lb_P_player1_red")
        self.Lb_P_player1_red.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_4.addWidget(self.Lb_P_player1_red)

        self.LCDNum_P_player1_red = QLCDNumber(self.Frame_P_player2_blue)
        self.LCDNum_P_player1_red.setObjectName(u"LCDNum_P_player1_red")
        self.LCDNum_P_player1_red.setMode(QLCDNumber.Dec)

        self.verticalLayout_4.addWidget(self.LCDNum_P_player1_red)


        self.horizontalLayout_7.addWidget(self.Frame_P_player2_blue)

        self.Frame_E_player1_red = QFrame(self.Frame_score_player1_red)
        self.Frame_E_player1_red.setObjectName(u"Frame_E_player1_red")
        self.Frame_E_player1_red.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);")
        self.Frame_E_player1_red.setFrameShape(QFrame.StyledPanel)
        self.Frame_E_player1_red.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.Frame_E_player1_red)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Lb_E_player1_red = QLabel(self.Frame_E_player1_red)
        self.Lb_E_player1_red.setObjectName(u"Lb_E_player1_red")
        self.Lb_E_player1_red.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_5.addWidget(self.Lb_E_player1_red)

        self.LCDNum_E_player1_red = QLCDNumber(self.Frame_E_player1_red)
        self.LCDNum_E_player1_red.setObjectName(u"LCDNum_E_player1_red")
        self.LCDNum_E_player1_red.setMode(QLCDNumber.Dec)

        self.verticalLayout_5.addWidget(self.LCDNum_E_player1_red)


        self.horizontalLayout_7.addWidget(self.Frame_E_player1_red)

        self.PB_icon_score_player2_blue = QPushButton(self.centralwidget)
        self.PB_icon_score_player2_blue.setObjectName(u"PB_icon_score_player2_blue")
        self.PB_icon_score_player2_blue.setGeometry(QRect(780, 560, 41, 41))
        self.PB_icon_score_player2_blue.setIcon(icon7)
        self.PB_icon_score_player2_blue.setIconSize(QSize(40, 40))
        self.PB_icon_score_player2_blue.setFlat(True)
        self.Frame_score_player2_blue = QFrame(self.centralwidget)
        self.Frame_score_player2_blue.setObjectName(u"Frame_score_player2_blue")
        self.Frame_score_player2_blue.setGeometry(QRect(580, 550, 201, 71))
        self.Frame_score_player2_blue.setStyleSheet(u"background-color: rgba(0, 0, 216, 150);")
        self.Frame_score_player2_blue.setFrameShape(QFrame.StyledPanel)
        self.Frame_score_player2_blue.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.Frame_score_player2_blue)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_12 = QFrame(self.Frame_score_player2_blue)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Lb_G_player2_blue = QLabel(self.frame_12)
        self.Lb_G_player2_blue.setObjectName(u"Lb_G_player2_blue")
        self.Lb_G_player2_blue.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_6.addWidget(self.Lb_G_player2_blue)

        self.LCDNum_G_player2_blue = QLCDNumber(self.frame_12)
        self.LCDNum_G_player2_blue.setObjectName(u"LCDNum_G_player2_blue")
        self.LCDNum_G_player2_blue.setMode(QLCDNumber.Dec)

        self.verticalLayout_6.addWidget(self.LCDNum_G_player2_blue)


        self.horizontalLayout_8.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.Frame_score_player2_blue)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Lb_P_player2_blue = QLabel(self.frame_13)
        self.Lb_P_player2_blue.setObjectName(u"Lb_P_player2_blue")
        self.Lb_P_player2_blue.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_7.addWidget(self.Lb_P_player2_blue)

        self.LCDNum_P_player2_blue = QLCDNumber(self.frame_13)
        self.LCDNum_P_player2_blue.setObjectName(u"LCDNum_P_player2_blue")
        self.LCDNum_P_player2_blue.setMode(QLCDNumber.Dec)

        self.verticalLayout_7.addWidget(self.LCDNum_P_player2_blue)


        self.horizontalLayout_8.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.Frame_score_player2_blue)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_14)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Lb_E_player2_blue = QLabel(self.frame_14)
        self.Lb_E_player2_blue.setObjectName(u"Lb_E_player2_blue")
        self.Lb_E_player2_blue.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_8.addWidget(self.Lb_E_player2_blue)

        self.LCDNum_E_player2_blue = QLCDNumber(self.frame_14)
        self.LCDNum_E_player2_blue.setObjectName(u"LCDNum_E_player2_blue")
        self.LCDNum_E_player2_blue.setMode(QLCDNumber.Dec)

        self.verticalLayout_8.addWidget(self.LCDNum_E_player2_blue)


        self.horizontalLayout_8.addWidget(self.frame_14)

        self.PB_icon_python_title = QPushButton(self.centralwidget)
        self.PB_icon_python_title.setObjectName(u"PB_icon_python_title")
        self.PB_icon_python_title.setGeometry(QRect(10, 0, 51, 51))
        icon8 = QIcon()
        icon8.addFile(u"../Assets_UI/Icon_Python.png", QSize(), QIcon.Normal, QIcon.Off)
        self.PB_icon_python_title.setIcon(icon8)
        self.PB_icon_python_title.setIconSize(QSize(50, 50))
        self.PB_icon_python_title.setFlat(True)
        self.PB_icon_windows_title = QPushButton(self.centralwidget)
        self.PB_icon_windows_title.setObjectName(u"PB_icon_windows_title")
        self.PB_icon_windows_title.setGeometry(QRect(60, 0, 51, 51))
        icon9 = QIcon()
        icon9.addFile(u"../Assets_UI/Windows_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.PB_icon_windows_title.setIcon(icon9)
        self.PB_icon_windows_title.setIconSize(QSize(40, 40))
        self.PB_icon_windows_title.setFlat(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 837, 22))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuMenu.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuMenu.setTearOffEnabled(False)
        icon10 = QIcon()
        icon10.addFile(u"../Assets_UI/Icon_Menu_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuMenu.setIcon(icon10)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionConectar_al_servidor)
        self.menuMenu.addAction(self.actionDesconectar_del_servidor)
        self.menuMenu.addAction(self.actionSalir_del_juego)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionConectar_al_servidor.setText(QCoreApplication.translate("MainWindow", u"Conectar al servidor", None))
        self.actionDesconectar_del_servidor.setText(QCoreApplication.translate("MainWindow", u"Desconectar del servidor", None))
        self.actionSalir_del_juego.setText(QCoreApplication.translate("MainWindow", u"Salir del juego", None))
        self.Icon_left_title_game.setText("")
        self.Lb_Title_Game.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">PIEDRA, PAPEL O TIJERA</span></p></body></html>", None))
        self.Icon_right_title_game.setText("")
        self.Lb_player1_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Jugador 1</span></p></body></html>", None))
        self.Icon_player1_red.setText("")
        self.Lb_imagen_player1_red.setText("")
        self.Lb_opt_chosen_player1_red.setText("") #QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Tijera</span></p></body></html>", None)
        self.Lb_player2_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Jugador 2</span></p></body></html>", None))
        self.Icon_player2_blue.setText("")
        self.Lb_imagen_player2_blue.setText("")
        self.Lb_opt_chosen_player2_blue.setText("") #QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Papel</span></p></body></html>", None)
        self.GB_opciones_player1_red.setTitle(QCoreApplication.translate("MainWindow", u"Elija una opcion: ", None))
        self.RB_piedra_player1_red.setText(QCoreApplication.translate("MainWindow", u"Piedra", None))
        self.RB_papel_player1_red.setText(QCoreApplication.translate("MainWindow", u"Papel", None))
        self.RB_tijera_player1_red.setText(QCoreApplication.translate("MainWindow", u"Tijera", None))
        self.GB_opciones_player2_blue.setTitle(QCoreApplication.translate("MainWindow", u"Elija una opcion: ", None))
        self.RB_piedra_player2_blue.setText(QCoreApplication.translate("MainWindow", u"Piedra", None))
        self.RB_papel_player2_blue.setText(QCoreApplication.translate("MainWindow", u"Papel", None))
        self.RB_tijera_player2_blue.setText(QCoreApplication.translate("MainWindow", u"Tijera", None))
        self.PB_play_player1_red.setText(QCoreApplication.translate("MainWindow", u"Jugar", None))
        self.PB_play_player2_blue.setText(QCoreApplication.translate("MainWindow", u"Jugar", None))
        self.Lb_icon_messages_2.setText("")
        self.Lb_messages.setText("") #QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">\u00a1Ganaste!</span></p></body></html>", None)
        self.Lb_icon_messages.setText("")
        self.PB_icon_score_player1_red.setText("")
        self.Lb_G_player1_red.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">G</span></p></body></html>", None))
        self.Lb_P_player1_red.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">P</span></p></body></html>", None))
        self.Lb_E_player1_red.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">E</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.PB_icon_score_player2_blue.setText("")
        self.Lb_G_player2_blue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">G</span></p></body></html>", None))
        self.Lb_P_player2_blue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">P</span></p></body></html>", None))
        self.Lb_E_player2_blue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">E</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.PB_icon_python_title.setText("")
        self.PB_icon_windows_title.setText("")
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

