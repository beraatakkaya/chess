from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QPainter,QPixmap
import sys

class Win(QMainWindow):
    def __init__(self):
        super().__init__()

        self.sayac = 0
        self.ilk_dokunus = 'tiklama'
        self.sira = 'beyaz'

        self.image = QPixmap('./lichessgenelekran.png')
        self.image_secili_bolge = QPixmap('./secili_bolge.png')
        self.image_geldigi_yer = QPixmap('./geldigi_yer.png')
        self.image_gittigi_yer = QPixmap('./gittigi_yer.png')
        self.image_gidilebilir_yerler = QPixmap('./gidilecek_yerler.png')
        self.image_sag_alt = QPixmap('./sag_alt.png')
        self.image_sol_alt = QPixmap('./sol_alt.png')
        self.image_sag_ust = QPixmap('./sag_ust.png')
        self.image_sol_ust = QPixmap('./sol_ust.png')

        self.image_beyaz_piyon1 = QPixmap('./beyaz_piyon.png')
        self.image_beyaz_piyon2 = QPixmap('./beyaz_piyon.png')
        self.image_beyaz_piyon3 = QPixmap('./beyaz_piyon.png')
        self.image_beyaz_piyon4 = QPixmap('./beyaz_piyon.png')
        self.image_beyaz_piyon5 = QPixmap('./beyaz_piyon.png')
        self.image_beyaz_piyon6 = QPixmap('./beyaz_piyon.png')
        self.image_beyaz_piyon7 = QPixmap('./beyaz_piyon.png')
        self.image_beyaz_piyon8 = QPixmap('./beyaz_piyon.png')

        self.image_beyaz_kale1 = QPixmap('./beyaz_kale.png')
        self.image_beyaz_kale2 = QPixmap('./beyaz_kale.png')

        self.image_beyaz_at1 = QPixmap('./beyaz_at.png')
        self.image_beyaz_at2 = QPixmap('./beyaz_at.png')

        self.image_beyaz_fil1 = QPixmap('./beyaz_fil.png')
        self.image_beyaz_fil2 = QPixmap('./beyaz_fil.png')

        self.image_beyaz_vezir = QPixmap('./beyaz_vezir.png')

        self.image_beyaz_sah = QPixmap('./beyaz_sah.png')

        self.image_siyah_piyon1 = QPixmap('./siyah_piyon.png')
        self.image_siyah_piyon2 = QPixmap('./siyah_piyon.png')
        self.image_siyah_piyon3 = QPixmap('./siyah_piyon.png')
        self.image_siyah_piyon4 = QPixmap('./siyah_piyon.png')
        self.image_siyah_piyon5 = QPixmap('./siyah_piyon.png')
        self.image_siyah_piyon6 = QPixmap('./siyah_piyon.png')
        self.image_siyah_piyon7 = QPixmap('./siyah_piyon.png')
        self.image_siyah_piyon8 = QPixmap('./siyah_piyon.png')

        self.image_siyah_kale1 = QPixmap('./siyah_kale.png')
        self.image_siyah_kale2 = QPixmap('./siyah_kale.png')

        self.image_siyah_at1 = QPixmap('./siyah_at.png')
        self.image_siyah_at2 = QPixmap('./siyah_at.png')

        self.image_siyah_fil1 = QPixmap('./siyah_fil.png')
        self.image_siyah_fil2 = QPixmap('./siyah_fil.png')

        self.image_siyah_vezir = QPixmap('./siyah_vezir.png')

        self.image_siyah_sah = QPixmap('./siyah_sah.png')

        self.piyon = [self.image_beyaz_piyon1,self.image_beyaz_piyon2,self.image_beyaz_piyon3,self.image_beyaz_piyon4,self.image_beyaz_piyon5,self.image_beyaz_piyon6,self.image_beyaz_piyon7,self.image_beyaz_piyon8,self.image_siyah_piyon1,self.image_siyah_piyon2,self.image_siyah_piyon3,self.image_siyah_piyon4,self.image_siyah_piyon5,self.image_siyah_piyon6,self.image_siyah_piyon7,self.image_siyah_piyon8]
        self.kale = [self.image_beyaz_kale1,self.image_beyaz_kale2,self.image_siyah_kale1,self.image_siyah_kale2]
        self.at = [self.image_beyaz_at1,self.image_beyaz_at2,self.image_siyah_at1,self.image_siyah_at2]
        self.fil = [self.image_beyaz_fil1,self.image_beyaz_fil2,self.image_siyah_fil1,self.image_siyah_fil2]
        self.vezir = [self.image_beyaz_vezir,self.image_siyah_vezir]
        self.sah = [self.image_beyaz_sah,self.image_siyah_sah]
        self.tas_adlari = [self.piyon,self.kale,self.at,self.fil,self.vezir,self.sah]
        self.a=1
        self.gidilebilir_yerler = []
        self.izint = ['var','0']
        self.izini = ['var','0']
        self.izin3 = ['var','0']
        self.izin4 = ['var','0']
        self.yenilebilir_taslar = []
        self.yenilen_tas = []


        self.initUI()
    def yuvarlama(self,sayi):
        
        yuvarlama_kalan = sayi%100
        sayi = sayi - yuvarlama_kalan

        return sayi

    def initUI(self):
        self.setWindowTitle('Satranc')
        self.setGeometry(0,0,800,800)

        self.mouse_x_yuvarlanmis = 0
        self.mouse_y_yuvarlanmis = 0
    def piyon_hareketi(self):
        self.izint[0] = 'var'
        self.izini[0] = 'var'
        if self.sira == 'siyah':
            for i in range(len(self.taslarin_konumlari_beyaz)):
                if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]-100:
                    self.izint[0] = 'yok'
                    self.izini[0] = 'yok'
                if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]-200:
                    self.izini[0] = 'yok'
            for i in range(len(self.taslarin_konumlari_siyah)):
                if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]-100:
                    self.izint[0] = 'yok'
                    self.izini[0] = 'yok'
                if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]-200:
                    self.izini[0] = 'yok'
                if self.etkin_konum[0]+100 == self.taslarin_konumlari_siyah[i][1] and self.etkin_konum[1]-100 == self.taslarin_konumlari_siyah[i][2]:
                    self.gidilebilir_yerler.append([self.etkin_konum[0]+100,self.etkin_konum[1]-100])
                if self.etkin_konum[0]-100 == self.taslarin_konumlari_siyah[i][1] and self.etkin_konum[1]-100 == self.taslarin_konumlari_siyah[i][2]:
                    self.gidilebilir_yerler.append([self.etkin_konum[0]-100,self.etkin_konum[1]-100])
            if self.izint[0] != 'yok':
                self.gidilebilir_yerler.append([self.etkin_konum[0],self.etkin_konum[1]-100])
                self.izint[0] = 'var'
            if self.izini[0] != 'yok':
                if self.etkin_konum[1] == 600:
                        self.gidilebilir_yerler.append([self.etkin_konum[0],self.etkin_konum[1]-200])
                        self.izini[0] = 'var'
        elif self.sira == 'beyaz':
            for i in range(len(self.taslarin_konumlari_beyaz)):
                if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]+100:
                    self.izint[0] = 'yok'
                    self.izini[0] = 'yok'
                if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]+200:
                    self.izini[0] = 'yok'
                if self.etkin_konum[0]-100 == self.taslarin_konumlari_beyaz[i][1] and self.etkin_konum[1]+100 == self.taslarin_konumlari_beyaz[i][2]:
                    self.gidilebilir_yerler.append([self.etkin_konum[0]-100,self.etkin_konum[1]+100])
                if self.etkin_konum[0]+100 == self.taslarin_konumlari_beyaz[i][1] and self.etkin_konum[1]+100 == self.taslarin_konumlari_beyaz[i][2]:
                    self.gidilebilir_yerler.append([self.etkin_konum[0]+100,self.etkin_konum[1]+100])

            for i in range(len(self.taslarin_konumlari_siyah)):
                if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]+100:
                    self.izint[0] = 'yok'
                    self.izini = 'yok'
                if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]+200:
                    self.izini[0] = 'yok'
            if self.izint[0] != 'yok':
                self.gidilebilir_yerler.append([self.etkin_konum[0],self.etkin_konum[1]+100])
                self.izint[0] = 'var'
            if self.izini[0] != 'yok':
                if self.etkin_konum[1] == 100:
                        self.gidilebilir_yerler.append([self.etkin_konum[0],self.etkin_konum[1]+200])
                        self.izini[0] = 'var'
        return self.gidilebilir_yerler
    def fil_hareketi(self):
        self.izint[0] = 'var'
        self.izini[0] = 'var'
        self.izin3[0] = 'var'
        self.izin4[0] = 'var'
        if self.sira == 'beyaz':                          
            for j in range(100,800,100):
                for i in range(len(self.taslarin_konumlari_beyaz)):
                        if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0]+j and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]+j and self.izint[0] == 'var':
                            self.izint[0]='yok'
                            self.izint[1] = '1'
                        if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0]-j and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]+j and self.izini[0] == 'var':
                            self.izini[0]='yok'
                            self.izini[1] = '1'
                        if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0]+j and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]-j and self.izin3[0] == 'var':
                            self.izin3[0]='yok'
                            self.izin3[1] = '1'
                        if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0]-j and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]-j and self.izin4[0] == 'var':
                            self.izin4[1] = '1'
                            self.izin4[0] = 'yok'
                for i in range(len(self.taslarin_konumlari_siyah)):
                    if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0]+j and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]+j and self.izint[0] == 'var':
                        self.izint[0]='yok'
                    if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0]-j and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]+j and self.izini[0] == 'var':
                        self.izini[0]='yok'
                    if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0]+j and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]-j and self.izin3[0] == 'var':
                        self.izin3[0]='yok'
                    if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0]-j and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]-j and self.izin4[0] == 'var':
                        self.izin4[0]='yok'
                if self.izint[0] != 'yok' or self.izint[1]  == '1':
                    self.gidilebilir_yerler.append([self.etkin_konum[0]+j,self.etkin_konum[1]+j])
                    self.izint[1] = '0'
                if self.izini[0] != 'yok' or self.izini[1]  == '1':
                    self.gidilebilir_yerler.append([self.etkin_konum[0]-j,self.etkin_konum[1]+j])
                    self.izini[1] = '0'
                if self.izin3[0] != 'yok' or self.izin3[1]  == '1':
                    self.gidilebilir_yerler.append([self.etkin_konum[0]+j,self.etkin_konum[1]-j])
                    self.izin3[1] = '0'
                if self.izin4[0] != 'yok' or self.izin4[1]  == '1':
                    self.gidilebilir_yerler.append([self.etkin_konum[0]-j,self.etkin_konum[1]-j])
                    self.izin4[1] = '0'
        elif self.sira == 'siyah':                          
            for j in range(100,800,100):
                for i in range(len(self.taslarin_konumlari_siyah)):
                        if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0]+j and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]+j and self.izint[0] == 'var':
                            self.izint[0]='yok'
                            self.izint[1] = '1'
                        if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0]-j and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]+j and self.izini[0] == 'var':
                            self.izini[0]='yok'
                            self.izini[1] = '1'
                        if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0]+j and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]-j and self.izin3[0] == 'var':
                            self.izin3[0]='yok'
                            self.izin3[1] = '1'
                        if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0]-j and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]-j and self.izin4[0] == 'var':
                            self.izin4[1] = '1'
                            self.izin4[0] = 'yok'
                for i in range(len(self.taslarin_konumlari_beyaz)):
                    if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0]+j and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]+j and self.izint[0] == 'var':
                        self.izint[0]='yok'
                    if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0]-j and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]+j and self.izini[0] == 'var':
                        self.izini[0]='yok'
                    if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0]+j and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]-j and self.izin3[0] == 'var':
                        self.izin3[0]='yok'
                    if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0]-j and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]-j and self.izin4[0] == 'var':
                        self.izin4[0]='yok'
                if self.izint[0] != 'yok' or self.izint[1]  == '1':
                    self.gidilebilir_yerler.append([self.etkin_konum[0]+j,self.etkin_konum[1]+j])
                    self.izint[1] = '0'
                if self.izini[0] != 'yok' or self.izini[1]  == '1':
                    self.gidilebilir_yerler.append([self.etkin_konum[0]-j,self.etkin_konum[1]+j])
                    self.izini[1] = '0'
                if self.izin3[0] != 'yok' or self.izin3[1]  == '1':
                    self.gidilebilir_yerler.append([self.etkin_konum[0]+j,self.etkin_konum[1]-j])
                    self.izin3[1] = '0'
                if self.izin4[0] != 'yok' or self.izin4[1]  == '1':
                    self.gidilebilir_yerler.append([self.etkin_konum[0]-j,self.etkin_konum[1]-j])
                    self.izin4[1] = '0'
        return self.gidilebilir_yerler
    def kale_hareketi(self):
        self.izint[0] = 'var'
        self.izini[0] = 'var'
        self.izin3[0] = 'var'
        self.izin4[0] = 'var' 
        if self.sira == 'beyaz':                         
            for j in range(100,800,100):
                for i in range(len(self.taslarin_konumlari_beyaz)):
                        if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0]+j and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1] and self.izint[0] == 'var':
                            self.izint[0]='yok'
                            self.izint[1] = '1'
                        if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]+j and self.izini[0] == 'var':
                            self.izini[0]='yok'
                            self.izini[1] = '1'
                        if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0]-j and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1] and self.izin3[0] == 'var':
                            self.izin3[0]='yok'
                            self.izin3[1] = '1'
                        if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]-j and self.izin4[0] == 'var':
                            self.izin4[1] = '1'
                            self.izin4[0] = 'yok'
                for i in range(len(self.taslarin_konumlari_siyah)):
                    if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0]+j and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1] and self.izint[0] == 'var':
                        self.izint[0]='yok'
                    if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]+j and self.izini[0] == 'var':
                        self.izini[0]='yok'
                    if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0]-j and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1] and self.izin3[0] == 'var':
                        self.izin3[0]='yok'
                    if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]-j and self.izin4[0] == 'var':
                        self.izin4[0]='yok'
                if self.izint[0] != 'yok' or self.izint[1]  == '1':
                    self.gidilebilir_yerler.append([self.etkin_konum[0]+j,self.etkin_konum[1]])
                    self.izint[1] = '0'
                if self.izini[0] != 'yok' or self.izini[1]  == '1':
                    self.gidilebilir_yerler.append([self.etkin_konum[0],self.etkin_konum[1]+j])
                    self.izini[1] = '0'
                if self.izin3[0] != 'yok' or self.izin3[1]  == '1':
                    self.gidilebilir_yerler.append([self.etkin_konum[0]-j,self.etkin_konum[1]])
                    self.izin3[1] = '0'
                if self.izin4[0] != 'yok' or self.izin4[1]  == '1':
                    self.gidilebilir_yerler.append([self.etkin_konum[0],self.etkin_konum[1]-j])
                    self.izin4[1] = '0'
        elif self.sira == 'siyah':                          
            for j in range(100,800,100):
                for i in range(len(self.taslarin_konumlari_siyah)):
                        if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0]+j and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1] and self.izint[0] == 'var':
                            self.izint[0]='yok'
                            self.izint[1] = '1'
                        if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]+j and self.izini[0] == 'var':
                            self.izini[0]='yok'
                            self.izini[1] = '1'
                        if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0]-j and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1] and self.izin3[0] == 'var':
                            self.izin3[0]='yok'
                            self.izin3[1] = '1'
                        if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]-j and self.izin4[0] == 'var':
                            self.izin4[1] = '1'
                            self.izin4[0] = 'yok'
                for i in range(len(self.taslarin_konumlari_beyaz)):
                    if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0]+j and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1] and self.izint[0] == 'var':
                        self.izint[0]='yok'
                    if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]+j and self.izini[0] == 'var':
                        self.izini[0]='yok'
                    if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0]-j and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1] and self.izin3[0] == 'var':
                        self.izin3[0]='yok'
                    if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]-j and self.izin4[0] == 'var':
                        self.izin4[0]='yok'
                if self.izint[0] != 'yok' or self.izint[1]  == '1':
                    self.gidilebilir_yerler.append([self.etkin_konum[0]+j,self.etkin_konum[1]])
                    self.izint[1] = '0'
                if self.izini[0] != 'yok' or self.izini[1]  == '1':
                    self.gidilebilir_yerler.append([self.etkin_konum[0],self.etkin_konum[1]+j])
                    self.izini[1] = '0'
                if self.izin3[0] != 'yok' or self.izin3[1]  == '1':
                    self.gidilebilir_yerler.append([self.etkin_konum[0]-j,self.etkin_konum[1]])
                    self.izin3[1] = '0'
                if self.izin4[0] != 'yok' or self.izin4[1]  == '1':
                    self.gidilebilir_yerler.append([self.etkin_konum[0],self.etkin_konum[1]-j])
                    self.izin4[1] = '0'
        return self.gidilebilir_yerler
    def sah_hareketi(self):
        print('girdi')
        self.sah_ihtimalleri = [
            [self.etkin_konum[0]+100,self.etkin_konum[1]],
            [self.etkin_konum[0],self.etkin_konum[1]+100],
            [self.etkin_konum[0]-100,self.etkin_konum[1]],
            [self.etkin_konum[0],self.etkin_konum[1]-100],
            [self.etkin_konum[0]+100,self.etkin_konum[1]+100],
            [self.etkin_konum[0]+100,self.etkin_konum[1]-100],
            [self.etkin_konum[0]-100,self.etkin_konum[1]+100],
            [self.etkin_konum[0]-100,self.etkin_konum[1]-100]]
        if self.sira == 'beyaz':
            self.izint[0] = 'var'
            for i in range(len(self.sah_ihtimalleri)):
                for j in range(len(self.taslarin_konumlari_siyah)):
                    if self.sah_ihtimalleri[i][0] == self.taslarin_konumlari_siyah[j][1] and\
                         self.taslarin_konumlari_siyah[j][2] == self.sah_ihtimalleri[i][1]:
                         break
                else:
                    self.gidilebilir_yerler.append([self.sah_ihtimalleri[i][0],self.sah_ihtimalleri[i][1]])
        elif self.sira == 'siyah':
            self.izint[0] = 'var'
            for i in range(len(self.sah_ihtimalleri)):
                for j in range(len(self.taslarin_konumlari_beyaz)):
                    if self.sah_ihtimalleri[i][0] == self.taslarin_konumlari_beyaz[j][1] and\
                        self.taslarin_konumlari_beyaz[j][2] == self.sah_ihtimalleri[i][1]:
                        break
                else:
                    self.gidilebilir_yerler.append([self.sah_ihtimalleri[i][0],self.sah_ihtimalleri[i][1]])
        self.sah_ihtimalleri = []
        return self.gidilebilir_yerler
    def at_hareketi(self):
        self.at_ihtimalleri = [
        [self.etkin_konum[0]+200,self.etkin_konum[1]+100],
        [self.etkin_konum[0]+200,self.etkin_konum[1]-100],
        [self.etkin_konum[0]-200,self.etkin_konum[1]-100],
        [self.etkin_konum[0]-200,self.etkin_konum[1]+100],
        [self.etkin_konum[0]+100,self.etkin_konum[1]+200],
        [self.etkin_konum[0]+100,self.etkin_konum[1]-200],
        [self.etkin_konum[0]-100,self.etkin_konum[1]+200],
        [self.etkin_konum[0]-100,self.etkin_konum[1]-200]]
        if self.sira == 'beyaz':
            self.izint[0] = 'var'
            for i in range(len(self.at_ihtimalleri)):
                for j in range(len(self.taslarin_konumlari_siyah)):
                    if self.at_ihtimalleri[i][0] == self.taslarin_konumlari_siyah[j][1] and\
                         self.taslarin_konumlari_siyah[j][2] == self.at_ihtimalleri[i][1]:
                         break
                else:
                    self.gidilebilir_yerler.append([self.at_ihtimalleri[i][0],self.at_ihtimalleri[i][1]])
        elif self.sira == 'siyah':
            self.izint[0] = 'var'
            for i in range(len(self.at_ihtimalleri)):
                for j in range(len(self.taslarin_konumlari_beyaz)):
                    if self.at_ihtimalleri[i][0] == self.taslarin_konumlari_beyaz[j][1] and\
                        self.taslarin_konumlari_beyaz[j][2] == self.at_ihtimalleri[i][1]:
                        break
                else:
                    self.gidilebilir_yerler.append([self.at_ihtimalleri[i][0],self.at_ihtimalleri[i][1]])
        self.at_ihtimalleri = []
        return self.gidilebilir_yerler
    def mousePressEvent(self, event):
        
        self.mouse_click_x =[event.x()]
        self.mouse_click_y =[event.y()]

        self.mouse_x_yuvarlanmis = self.yuvarlama(self.mouse_click_x[0])
        self.mouse_y_yuvarlanmis = self.yuvarlama(self.mouse_click_y[0])
        if self.sira == 'beyaz':
            if self.ilk_dokunus == 'tiklama':
                for i in range(len(self.taslarin_konumlari_beyaz)):
                    if self.mouse_x_yuvarlanmis == self.taslarin_konumlari_beyaz[i][1]:
                            if self.mouse_y_yuvarlanmis == self.taslarin_konumlari_beyaz[i][2]:
                                self.etkin_tas = self.taslarin_konumlari_beyaz[i][0]
                                self.etkin_konum = [self.mouse_x_yuvarlanmis,self.mouse_y_yuvarlanmis]
                                if self.a == 1:
                                    self.ilk_dokunus = 'gitme'
                                self.sira = 'siyah'
                                self.repaint()
                                
            else:
                self.gidecegi_yer = [self.mouse_x_yuvarlanmis,self.mouse_y_yuvarlanmis]
                if self.gidecegi_yer[0] == self.etkin_konum[0] and self.gidecegi_yer[1] == self.etkin_konum[1]:
                    self.ilk_dokunus = 'tiklama'
                    self.a =1
                    self.sira = 'siyah'
                    self.gidilebilir_yerler=[]
                    print('sira degistirildi')
                for siyah_tas in self.taslarin_konumlari_siyah:
                    if self.gidecegi_yer[0] == siyah_tas[1] and self.gidecegi_yer[1] == siyah_tas[2]:
                        self.etkin_tas = siyah_tas[0]
                        self.ilk_dokunus = 'gitme'
                        self.sira = 'beyaz'
                        self.gidilebilir_yerler=[]
                        self.etkin_konum = [self.gidecegi_yer[0],self.gidecegi_yer[1]]
                        print('deneme basarili')
                        self.repaint()
                else:
                    for i in range(len(self.gidilebilir_yerler)):
                        if self.gidecegi_yer[0] == self.gidilebilir_yerler[i][0] and self.gidecegi_yer[1] == self.gidilebilir_yerler[i][1]:
                            print('calisti')
                            self.a = 3
                            self.ilk_dokunus = 'tiklama'
                            self.gidilebilir_yerler = []
                            self.repaint()
                            break
        elif self.sira == 'siyah':
            if self.ilk_dokunus == 'tiklama':
                for i in range(len(self.taslarin_konumlari_siyah)):
                    if self.mouse_x_yuvarlanmis == self.taslarin_konumlari_siyah[i][1]:
                            if self.mouse_y_yuvarlanmis == self.taslarin_konumlari_siyah[i][2]:
                                self.etkin_tas = self.taslarin_konumlari_siyah[i][0]
                                self.etkin_konum = [self.mouse_x_yuvarlanmis,self.mouse_y_yuvarlanmis]
                                if self.a == 1:
                                    self.ilk_dokunus = 'gitme'
                                self.sira = 'beyaz'
                                self.repaint()
            else:
                self.gidecegi_yer = [self.mouse_x_yuvarlanmis,self.mouse_y_yuvarlanmis]
                if self.gidecegi_yer[0] == self.etkin_konum[0] and self.gidecegi_yer[1] == self.etkin_konum[1]:
                    self.ilk_dokunus = 'tiklama'
                    self.a =1
                    self.sira = 'beyaz'
                    self.gidilebilir_yerler=[]
                    print('sira degistirildi')
                for beyaz_tas in self.taslarin_konumlari_beyaz:
                    if self.gidecegi_yer[0] == beyaz_tas[1] and self.gidecegi_yer[1] == beyaz_tas[2]:
                        print('deneme basarili')
                        self.etkin_tas = beyaz_tas[0]
                        self.ilk_dokunus = 'gitme'
                        self.sira = 'siyah'
                        self.gidilebilir_yerler=[]
                        self.etkin_konum = [self.gidecegi_yer[0],self.gidecegi_yer[1]]
                        self.repaint()

                else:
                    for i in range(len(self.gidilebilir_yerler)):
                        if self.gidecegi_yer[0] == self.gidilebilir_yerler[i][0] and self.gidecegi_yer[1] == self.gidilebilir_yerler[i][1]:
                            print('calistia')
                            self.a = 3
                            self.ilk_dokunus = 'tiklama'
                            self.gidilebilir_yerler = []
                            self.repaint()
                            break

    def paintEvent(self,event):
        qp = QPainter()

        if self.sayac == 0 :
            taslarin_adlari = [self.image_beyaz_at1,self.image_beyaz_piyon1,self.image_beyaz_piyon2,self.image_beyaz_piyon3,self.image_beyaz_piyon4,self.image_beyaz_piyon5,self.image_beyaz_piyon6,self.image_beyaz_piyon7,self.image_beyaz_piyon8,self.image_beyaz_kale1,self.image_beyaz_kale2,self.image_beyaz_at2,self.image_beyaz_fil1,self.image_beyaz_fil2,self.image_beyaz_vezir,self.image_beyaz_sah]

            self.taslarin_konumlari_beyaz = [[self.image_beyaz_at1,100,700],[self.image_beyaz_piyon1,0,600],[self.image_beyaz_piyon2,100,600],[self.image_beyaz_piyon3,200,600],[self.image_beyaz_piyon4,300,600],[self.image_beyaz_piyon5,400,600],[self.image_beyaz_piyon6,500,600],[self.image_beyaz_piyon7,600,600],[self.image_beyaz_piyon8,700,600],[self.image_beyaz_kale1,0,700],[self.image_beyaz_kale2,700,700],[self.image_beyaz_at2,600,700],[self.image_beyaz_fil1,200,700],[self.image_beyaz_fil2,500,700],[self.image_beyaz_vezir,300,700],[self.image_beyaz_sah,400,700]]
            self.taslarin_konumlari_siyah = [[self.image_siyah_at1,100,0],[self.image_siyah_piyon1,0,100],[self.image_siyah_piyon2,100,100],[self.image_siyah_piyon3,200,100],[self.image_siyah_piyon4,300,100],[self.image_siyah_piyon5,400,100],[self.image_siyah_piyon6,500,100],[self.image_siyah_piyon7,600,100],[self.image_siyah_piyon8,700,100],[self.image_siyah_kale1,0,0],[self.image_siyah_kale2,700,0],[self.image_siyah_at2,600,0],[self.image_siyah_fil1,200,0],[self.image_siyah_fil2,500,0],[self.image_siyah_vezir,300,0],[self.image_siyah_sah,400,0]]

            self.etkin_tas = self.image_beyaz_at1
            self.sayac += 1

        qp.begin(self)
        qp.drawPixmap(self.rect(),self.image)

        if self.ilk_dokunus == 'gitme':
            qp.drawPixmap(self.etkin_konum[0],self.etkin_konum[1],100,100,self.image_secili_bolge)
            for i in range(16):
                if self.etkin_tas == self.piyon[i]:
                    self.gidilebilir_yerler = self.piyon_hareketi()
                    break
            for i in range(4):
                if self.etkin_tas == self.fil[i]:
                    self.gidilebilir_yerler = self.fil_hareketi()
                    break
                elif self.etkin_tas == self.kale[i]:
                    self.gidilebilir_yerler = self.kale_hareketi()
                    break
                elif self.etkin_tas == self.at[i]:
                    self.gidilebilir_yerler = self.at_hareketi()
                    break
            for i in range(2):
                if self.etkin_tas == self.vezir[i]:
                    self.gidilebilir_yerler = self.fil_hareketi()
                    self.gidilebilir_yerler.extend(self.kale_hareketi())
                elif self.etkin_tas == self.sah[i]:
                    self.gidilebilir_yerler = self.sah_hareketi()
                
            for gidilebilir_yer in self.gidilebilir_yerler:
                if self.sira == 'beyaz':
                    for beyaz_tas in self.taslarin_konumlari_beyaz:
                        
                        if gidilebilir_yer[0] == beyaz_tas[1] and gidilebilir_yer[1] == beyaz_tas[2]:
                            self.yenilebilir_taslar.append(beyaz_tas)
                            break
                    else:
                        qp.drawPixmap(gidilebilir_yer[0]+15,gidilebilir_yer[1]+15,70,70,self.image_gidilebilir_yerler)

                else:
                    for siyah_tas in self.taslarin_konumlari_siyah:
                        if gidilebilir_yer[0] == siyah_tas[1] and gidilebilir_yer[1] == siyah_tas[2]:
                            self.yenilebilir_taslar.append(siyah_tas)
                            break
                    else:
                        qp.drawPixmap(gidilebilir_yer[0]+15,gidilebilir_yer[1]+15,70,70,self.image_gidilebilir_yerler)

            for yenilebilir_tas in self.yenilebilir_taslar:
                qp.drawPixmap(yenilebilir_tas[1]-5,yenilebilir_tas[2]-5,30,30,self.image_sol_ust)
                qp.drawPixmap(yenilebilir_tas[1]+75,yenilebilir_tas[2]-5,30,30,self.image_sag_ust)
                qp.drawPixmap(yenilebilir_tas[1]-5,yenilebilir_tas[2]+75,30,30,self.image_sol_alt)
                qp.drawPixmap(yenilebilir_tas[1]+75,yenilebilir_tas[2]+75,30,30,self.image_sag_alt)
            self.a = 2
            print(self.gidilebilir_yerler)
        
        
        if  self.a == 3:
            # for i in range(len(self.yenilebilir_taslar)):
            #     print('girdi')
            #     if self.gidecegi_yer[0] == self.yenilebilir_taslar[i][1] and self.gidecegi_yer[1] == self.yenilebilir_taslar[i][2]:
            #         self.yenilen_tas.append([self.yenilebilir_taslar[i][0],self.yenilebilir_taslar[i][1],self.yenilebilir_taslar[i][2]])
            # print(self.yenilen_tas)
            # qp.drawPixmap(self.mouse_x_yuvarlanmis,self.mouse_y_yuvarlanmis,100,100,self.etkin_tas)
            qp.drawPixmap(self.gidecegi_yer[0],self.gidecegi_yer[1],100,100,self.image_gittigi_yer)

            if self.sira == 'siyah':
                for i in range(len(self.taslarin_konumlari_beyaz)):
                    if self.taslarin_konumlari_beyaz[i][0] == self.etkin_tas:
                        self.taslarin_konumlari_beyaz[i][1]= self.mouse_x_yuvarlanmis
                        self.taslarin_konumlari_beyaz[i][2] = self.mouse_y_yuvarlanmis

                self.taslarin_konumlari_siyah = [tas for tas in self.taslarin_konumlari_siyah if not (tas[1] == self.mouse_x_yuvarlanmis and tas[2] == self.mouse_y_yuvarlanmis)]
            else:
                for i in range(len(self.taslarin_konumlari_siyah)):
                    if self.taslarin_konumlari_siyah[i][0] == self.etkin_tas:
                        self.taslarin_konumlari_siyah[i][1]= self.mouse_x_yuvarlanmis
                        self.taslarin_konumlari_siyah[i][2] = self.mouse_y_yuvarlanmis
                               
                self.taslarin_konumlari_beyaz = [tas for tas in self.taslarin_konumlari_beyaz if not (tas[1] == self.mouse_x_yuvarlanmis and tas[2] == self.mouse_y_yuvarlanmis)]

            qp.drawPixmap(self.etkin_konum[0],self.etkin_konum[1],100,100,self.image_geldigi_yer)

            self.ilk_dokunus = 'tiklama'
            self.a=1
            self.yenilebilir_taslar = []
        

        for i in range(len(self.taslarin_konumlari_beyaz)):
            qp.drawPixmap(self.taslarin_konumlari_beyaz[i][1],self.taslarin_konumlari_beyaz[i][2],100,100,self.taslarin_konumlari_beyaz[i][0])
        for i in range (len(self.taslarin_konumlari_siyah)):
            qp.drawPixmap(self.taslarin_konumlari_siyah[i][1],self.taslarin_konumlari_siyah[i][2],100,100,self.taslarin_konumlari_siyah[i][0])

        qp.end()

app =QApplication(sys.argv)
win = Win()
win.show()
sys.exit(app.exec())