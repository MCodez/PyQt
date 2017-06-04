# -*- coding: utf-8 -*-
"""
ANACONDA DISTRIBUTION
IDE : SPYDER
Created on Sun Jun  4 18:44:29 2017

@author: LALIT ARORA
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from pycricbuzz import Cricbuzz

class Ui_PyCricket(object):
    def setupUi(self, PyCricket):
        c = Cricbuzz() 
        matches = c.matches()
        livematches=[]
        affected=[]
        for match in matches:
            if(match['mchstate']=='inprogress'):
                livematches.append(match['mchdesc'])
            elif ('rain' in match['mchstate']):
                affected.append(match['mchdesc'])
        
        if len(affected)==0:
            ui.totalaffected=ui.totalaffected+"No Match Affected.."
            
        else:
            for i in range(len(affected)):
                ui.totalaffected=ui.totalaffected+affected[i]+" "
            
        PyCricket.setObjectName("PyCricket")
        PyCricket.resize(544,570)
        
        PyCricket.setMaximumSize(QtCore.QSize(544, 16777215))
        self.raina = QtWidgets.QLabel(PyCricket)
        self.raina.setGeometry(QtCore.QRect(20,550, 501, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.raina.setFont(font)
        self.raina.setObjectName("rainaffected")
        self.raina.setText(ui.totalaffected)
        self.label = QtWidgets.QLabel(PyCricket)
        self.label.setGeometry(QtCore.QRect(80, 30, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.livematches = QtWidgets.QComboBox(PyCricket)
        self.livematches.setGeometry(QtCore.QRect(230, 30, 231, 22))
        self.livematches.setObjectName("livematches")
        self.livematches.addItems(livematches)
        self.pushButton = QtWidgets.QPushButton(PyCricket)
        self.pushButton.setGeometry(QtCore.QRect(210, 80,130, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.score)
        self.label_2 = QtWidgets.QLabel(PyCricket)
        self.label_2.setGeometry(QtCore.QRect(20,530, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(PyCricket)
        self.label_3.setGeometry(QtCore.QRect(80, 130, 401, 301))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        
        self.label_3.hide()==True
        self.retranslateUi(PyCricket)
        QtCore.QMetaObject.connectSlotsByName(PyCricket)

    def retranslateUi(self, PyCricket):
        _translate = QtCore.QCoreApplication.translate
        PyCricket.setWindowTitle(_translate("PyCricket", "PYCRICKET v1.0"))
        self.label.setText(_translate("PyCricket", "LIVE MATCHES"))
        self.pushButton.setText(_translate("PyCricket", "GET SCORE AND UPDATE"))
        self.label_2.setText(_translate("PyCricket", "Matches Affected By Rain"))
        self.raina.setText(_translate("PyCricket", " "))
        self.label_3.setText(_translate("PyCricket",ui.totalaffected))
    
    def score(self):
        self.raina.setText(ui.totalaffected)
        c=Cricbuzz()
        matches=c.matches()
        finalscorecard=""
        ui.selectedmatch=self.livematches.currentText()
        if ui.selectedmatch!="":
            for match in matches:
                if ui.selectedmatch in match['mchdesc']:
                    identity=match['id']
                    finalscorecard=finalscorecard+str(match['srs'])
                    finalscorecard=finalscorecard+"\n"+str(match['mchdesc'])
                    finalscorecard=finalscorecard+"\n"+str(match['type'])+str(match['mnum'])
                    finalscorecard=finalscorecard+"\n"+str(match['status'])
                    scorecard=c.scorecard(identity)
                    seperator="-------------------------------------------------------------------------------"
                    finalscorecard=finalscorecard+"\n"+seperator
                    finalscorecard=finalscorecard+"\n"+"BATTING TEAM :"+str(scorecard['scorecard'][0]['batteam'])
                    for i in range(len(scorecard['scorecard'][0]['batcard'])):
                        temp=""
                        temp=str(scorecard['scorecard'][0]['batcard'][i]['name'])+" "+str(scorecard['scorecard'][0]['batcard'][i]['runs'])+"of"+str(scorecard['scorecard'][0]['batcard'][i]['balls'])+",  Fours :"+str(scorecard['scorecard'][0]['batcard'][i]['fours'])+", Sixes :"+str(scorecard['scorecard'][0]['batcard'][i]['six'])+", Dismissal :"+str(scorecard['scorecard'][0]['batcard'][i]['dismissal'])
                        finalscorecard=finalscorecard+"\n"+temp
                        
                    finalscorecard=finalscorecard+"\n"+"Score :"+str(scorecard['scorecard'][0]['runs'])+"/"+str(scorecard['scorecard'][0]['wickets'])
                    finalscorecard=finalscorecard+"\n"+"Runrate :"+str(scorecard['scorecard'][0]['runrate'])
                    finalscorecard=finalscorecard+"\n"+seperator
                    finalscorecard=finalscorecard+"\n"+"BOWLING TEAM :"+str(scorecard['scorecard'][0]['bowlteam'])
                    for i in range(len(scorecard['scorecard'][0]['bowlcard'])):
                        temp=""
                        temp=str(scorecard['scorecard'][0]['bowlcard'][i]['name'])+"Overs :"+str(scorecard['scorecard'][0]['bowlcard'][i]['overs'])+", Runs :"+str(scorecard['scorecard'][0]['bowlcard'][i]['runs'])+", Wickets :"+str(scorecard['scorecard'][0]['bowlcard'][i]['wickets'])
                        finalscorecard=finalscorecard+"\n"+temp
            self.label_3.setText(finalscorecard)
            self.label_3.show()==True
        else:
            self.label_3.setText("Select the Live Match ")
            self.label_3.show()==True
        

if __name__ == '__main__':
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog=QtWidgets.QDialog()
    ui=Ui_PyCricket()
    ui.selectedmatch=""
    ui.totalaffected=""
    p = QtGui.QPalette()
    gradient = QtGui.QLinearGradient(0, 0, 0, 400)
    gradient.setColorAt(0.0, QtGui.QColor(240, 240, 240))
    gradient.setColorAt(1.0, QtGui.QColor(240, 160, 160))
    p.setBrush(QtGui.QPalette.Window,QtGui.QBrush(gradient))
    Dialog.setPalette(p)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())