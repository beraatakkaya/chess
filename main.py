from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QMessageBox
from PyQt5.QtGui import QPainter,QPixmap
import sys
from copy import deepcopy

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
        self.image_siyaha_boyama = QPixmap('./siyaha_boyama.png')
        self.image_beyaza_boyama = QPixmap('./beyaza_boyama.png')
        self.image_gidilebilir_yerler = QPixmap('./gidilecek_yerler.png')
        self.image_sag_alt = QPixmap('./sag_alt.png')
        self.image_sol_alt = QPixmap('./sol_alt.png')
        self.image_sag_ust = QPixmap('./sag_ust.png')
        self.image_sol_ust = QPixmap('./sol_ust.png')

        self.siyah_sah_sah = QPixmap('./siyah_sah_sah.png')
        self.beyaz_sah_sah = QPixmap('./beyaz_sah_sah.png')

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

        self.image_secim_ekrani_beyaz = QPixmap('./secim_ekrani_beyaz.png')
        self.image_secim_ekrani_siyah = QPixmap('./secme_ekrani_siyah.png') 

        self.piyon = [self.image_beyaz_piyon1,self.image_beyaz_piyon2,self.image_beyaz_piyon3,self.image_beyaz_piyon4,self.image_beyaz_piyon5,self.image_beyaz_piyon6,self.image_beyaz_piyon7,self.image_beyaz_piyon8,self.image_siyah_piyon1,self.image_siyah_piyon2,self.image_siyah_piyon3,self.image_siyah_piyon4,self.image_siyah_piyon5,self.image_siyah_piyon6,self.image_siyah_piyon7,self.image_siyah_piyon8]
        self.kale = [self.image_beyaz_kale1,self.image_beyaz_kale2,self.image_siyah_kale1,self.image_siyah_kale2]
        self.at = [self.image_beyaz_at1,self.image_beyaz_at2,self.image_siyah_at1,self.image_siyah_at2]
        self.fil = [self.image_beyaz_fil1,self.image_beyaz_fil2,self.image_siyah_fil1,self.image_siyah_fil2]
        self.vezir = [self.image_beyaz_vezir,self.image_siyah_vezir]
        self.sah = [self.image_beyaz_sah,self.image_siyah_sah]
        self.tas_adlari = [self.piyon,self.kale,self.at,self.fil,self.vezir,self.sah]
        self.a=1
        self.gidilebilir_yerler = []
        self.izint = ['var','0','0']
        self.izini = ['var','0','0']
        self.izin3 = ['var','0','0']
        self.izin4 = ['var','0','0']
        self.gecerken_alma = ['yok']
        self.piyon_atama = 'hayir'
        self.secim_iznib = 'yok'
        self.secim_iznis = 'yok'
        self.piyon_mu = 'degil'
        self.tahta_yazdirma = 'hayir'
        self.sah_cekildi_beyaz = False
        self.sah_cekildi_siyah = False
        self.sah_ceken_tas = []
        self.beyaz_taslarin_gordugu_yerler = []
        self.siyah_taslarin_gordugu_yerler = []
        self.taslarin_konumlari_beyaz_kopya = ['a','b']

        self.sahin_yeri = ['a','b']
        self.taslarin_gordugu_yerler = []
        self.rok_icin_tas_oynama = [[self.image_beyaz_kale1,'oynamadi'],[self.image_beyaz_kale2,'oynamadi'],[self.image_beyaz_sah,'oynamadi'],\
            [self.image_siyah_kale1,'oynamadi'],[self.image_siyah_kale2,'oynamadi'],[self.image_siyah_sah,'oynamadi']]

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
                    for siyah_tas in self.taslarin_konumlari_siyah:
                        if (self.etkin_konum[0]-100 == siyah_tas[1] and self.etkin_konum[1]-200 == siyah_tas[2]) or \
                            (self.etkin_konum[0]+100 == siyah_tas[1] and self.etkin_konum[1]-200 == siyah_tas[2]):
                            self.gecerken_alma_ihtimali_var = 'var'
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
                    self.izini[0] = 'yok'
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
    def fil_hareketi(self,dahil= False):
        self.izint[0] = 'var'
        self.izini[0] = 'var'
        self.izin3[0] = 'var'
        self.izin4[0] = 'var'
        if self.sira == 'beyaz':                          
            for j in range(100,800,100):
                for i in range(len(self.taslarin_konumlari_beyaz)):
                    if len(self.taslarin_konumlari_beyaz[i]) == 3:
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
                        if dahil == True:
                            self.izint[2] = True
                    if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0]-j and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]+j and self.izini[0] == 'var':
                        self.izini[0]='yok'
                        if dahil == True:
                            self.izini[2] = True
                    if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0]+j and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]-j and self.izin3[0] == 'var':
                        self.izin3[0]='yok'
                        if dahil == True:
                            self.izin3[2] = True
                    if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0]-j and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]-j and self.izin4[0] == 'var':
                        self.izin4[0]='yok'
                        if dahil == True:
                            self.izin4[2] = True
                if self.izint[0] != 'yok' or self.izint[1]  == '1' or self.izint[2] == True:
                    self.gidilebilir_yerler.append([self.etkin_konum[0]+j,self.etkin_konum[1]+j])
                    self.izint[1] = '0'
                    self.izint[2] = False
                if self.izini[0] != 'yok' or self.izini[1]  == '1' or self.izini[2] == True:
                    self.gidilebilir_yerler.append([self.etkin_konum[0]-j,self.etkin_konum[1]+j])
                    self.izini[1] = '0'
                    self.izini[2] = False
                if self.izin3[0] != 'yok' or self.izin3[1]  == '1' or self.izin3[2] == True:
                    self.gidilebilir_yerler.append([self.etkin_konum[0]+j,self.etkin_konum[1]-j])
                    self.izin3[1] = '0'
                    self.izin3[2] = False
                if self.izin4[0] != 'yok' or self.izin4[1]  == '1' or self.izin4[2] == True:
                    self.gidilebilir_yerler.append([self.etkin_konum[0]-j,self.etkin_konum[1]-j])
                    self.izin4[1] = '0'
                    self.izin4[2] = False
        elif self.sira == 'siyah':                          
            for j in range(100,800,100):
                for i in range(len(self.taslarin_konumlari_siyah)):
                    if len(self.taslarin_konumlari_siyah[i]) == 3:
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
                        if dahil == True:
                            self.izint[2] = True
                    if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0]-j and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]+j and self.izini[0] == 'var':
                        self.izini[0]='yok'
                        if dahil == True:
                            self.izini[2] = True
                    if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0]+j and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]-j and self.izin3[0] == 'var':
                        self.izin3[0]='yok'
                        if dahil == True:
                            self.izin3[2] = True
                    if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0]-j and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]-j and self.izin4[0] == 'var':
                        self.izin4[0]='yok'
                        if dahil == True:
                            self.izin4[2] = True
                if self.izint[0] != 'yok' or self.izint[1]  == '1' or self.izint[2] == True:
                    self.gidilebilir_yerler.append([self.etkin_konum[0]+j,self.etkin_konum[1]+j])
                    self.izint[1] = '0'
                    self.izint[2] = False
                if self.izini[0] != 'yok' or self.izini[1]  == '1' or self.izini[2] == True:
                    self.gidilebilir_yerler.append([self.etkin_konum[0]-j,self.etkin_konum[1]+j])
                    self.izini[1] = '0'
                    self.izini[2] = False
                if self.izin3[0] != 'yok' or self.izin3[1]  == '1' or self.izin3[2] == True:
                    self.gidilebilir_yerler.append([self.etkin_konum[0]+j,self.etkin_konum[1]-j])
                    self.izin3[1] = '0'
                    self.izin3[2] = False
                if self.izin4[0] != 'yok' or self.izin4[1]  == '1' or self.izin4[2] == True:
                    self.gidilebilir_yerler.append([self.etkin_konum[0]-j,self.etkin_konum[1]-j])
                    self.izin4[1] = '0'
                    self.izin4[2] = False
        return self.gidilebilir_yerler
    def kale_hareketi(self,dahil=False):
        self.izint[0] = 'var'
        self.izini[0] = 'var'
        self.izin3[0] = 'var'
        self.izin4[0] = 'var'
        if self.sira == 'beyaz':                         
            for j in range(100,800,100):
                for i in range(len(self.taslarin_konumlari_beyaz)):
                    if len(self.taslarin_konumlari_beyaz[i]) == 3:
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
                        if dahil == True:
                            self.izint[2] = True
                    if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]+j and self.izini[0] == 'var':
                        self.izini[0]='yok'
                        if dahil == True:   
                            self.izini[2] = True
                    if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0]-j and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1] and self.izin3[0] == 'var':
                        self.izin3[0]='yok'
                        if dahil == True:
                            self.izin3[2] = True
                    if self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]-j and self.izin4[0] == 'var':
                        self.izin4[0]='yok'
                        if dahil == True:
                            self.izin4[2] = True
                if self.izint[0] != 'yok' or self.izint[1]  == '1' or self.izint[2] == True:
                    self.gidilebilir_yerler.append([self.etkin_konum[0]+j,self.etkin_konum[1]])
                    self.izint[1] = '0'
                    self.izint[2] = False
                if self.izini[0] != 'yok' or self.izini[1]  == '1' or self.izini[2] == True:
                    self.gidilebilir_yerler.append([self.etkin_konum[0],self.etkin_konum[1]+j])
                    self.izini[1] = '0'
                    self.izini[2] = False
                if self.izin3[0] != 'yok' or self.izin3[1]  == '1' or self.izin3[2] == True:
                    self.gidilebilir_yerler.append([self.etkin_konum[0]-j,self.etkin_konum[1]])
                    self.izin3[1] = '0'
                    self.izin3[2] = False
                if self.izin4[0] != 'yok' or self.izin4[1]  == '1' or self.izin4[2] == True:
                    self.gidilebilir_yerler.append([self.etkin_konum[0],self.etkin_konum[1]-j])
                    self.izin4[1] = '0'
                    self.izin4[2] = False
        elif self.sira == 'siyah':                          
            for j in range(100,800,100):
                for i in range(len(self.taslarin_konumlari_siyah)):
                    if len(self.taslarin_konumlari_siyah[i]) == 3:
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
                        if dahil == True:   
                            self.izint[2] = True
                    if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]+j and self.izini[0] == 'var':
                        self.izini[0]='yok'
                        if dahil == True:   
                            self.izini[2] = True
                    if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0]-j and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1] and self.izin3[0] == 'var':
                        self.izin3[0]='yok'
                        if dahil == True:   
                            self.izin3[2] = True
                    if self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]-j and self.izin4[0] == 'var':
                        self.izin4[0]='yok'
                        if dahil == True:   
                            self.izin4[2] = True
                if self.izint[0] != 'yok' or self.izint[1]  == '1' or self.izint[2] == True:
                    self.gidilebilir_yerler.append([self.etkin_konum[0]+j,self.etkin_konum[1]])
                    self.izint[1] = '0'
                    self.izint[2] = False
                if self.izini[0] != 'yok' or self.izini[1]  == '1' or self.izini[2] == True:
                    self.gidilebilir_yerler.append([self.etkin_konum[0],self.etkin_konum[1]+j])
                    self.izini[1] = '0'
                    self.izini[2] = False
                if self.izin3[0] != 'yok' or self.izin3[1]  == '1' or self.izin3[2] == True:
                    self.gidilebilir_yerler.append([self.etkin_konum[0]-j,self.etkin_konum[1]])
                    self.izin3[1] = '0'
                    self.izin3[2] = False
                if self.izin4[0] != 'yok' or self.izin4[1]  == '1' or self.izin4[2] == True:
                    self.gidilebilir_yerler.append([self.etkin_konum[0],self.etkin_konum[1]-j])
                    self.izin4[1] = '0'
                    self.izin4[2] = False
        return self.gidilebilir_yerler
    def sah_hareketi(self,dahil = False):
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
                    if dahil == True:
                        continue
                    if self.sah_ihtimalleri[i][0] == self.taslarin_konumlari_siyah[j][1] and\
                         self.taslarin_konumlari_siyah[j][2] == self.sah_ihtimalleri[i][1]:
                         break
                else:
                    self.gidilebilir_yerler.append([self.sah_ihtimalleri[i][0],self.sah_ihtimalleri[i][1]])
        elif self.sira == 'siyah':
            self.izint[0] = 'var'
            for i in range(len(self.sah_ihtimalleri)):
                for j in range(len(self.taslarin_konumlari_beyaz)):
                    if dahil == True:
                        continue
                    if self.sah_ihtimalleri[i][0] == self.taslarin_konumlari_beyaz[j][1] and\
                        self.taslarin_konumlari_beyaz[j][2] == self.sah_ihtimalleri[i][1]:
                        break
                else:
                    self.gidilebilir_yerler.append([self.sah_ihtimalleri[i][0],self.sah_ihtimalleri[i][1]])
        self.sah_ihtimalleri = []
        return self.gidilebilir_yerler
    def at_hareketi(self,dahil = False):
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
                    if dahil == True:
                        continue
                    if self.at_ihtimalleri[i][0] == self.taslarin_konumlari_siyah[j][1] and\
                         self.taslarin_konumlari_siyah[j][2] == self.at_ihtimalleri[i][1]:
                         break
                else:
                    self.gidilebilir_yerler.append([self.at_ihtimalleri[i][0],self.at_ihtimalleri[i][1]])
        elif self.sira == 'siyah':
            self.izint[0] = 'var'
            for i in range(len(self.at_ihtimalleri)):
                for j in range(len(self.taslarin_konumlari_beyaz)):
                    if dahil == True:
                        continue
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
        if self.piyon_atama == 'evet':
            if self.sira == 'beyaz':
                if self.mouse_y_yuvarlanmis == 300:
                    for siyah_tas in self.taslarin_konumlari_siyah:
                        if siyah_tas[0] == self.etkin_tas:
                            self.piyon.remove(siyah_tas[0])
                            siyah_tas[0] = QPixmap('./siyah_vezir.png')
                            self.vezir.append(siyah_tas[0])
                            self.piyon_atama = 'hayir'
                            self.tahta_yazdirma = 'evet'
                            self.repaint()
                            
                elif self.mouse_y_yuvarlanmis == 400:
                   for siyah_tas in self.taslarin_konumlari_siyah:
                        if siyah_tas[0] == self.etkin_tas:
                            self.piyon.remove(siyah_tas[0])
                            siyah_tas[0] = QPixmap('./siyah_at.png')
                            self.at.append(siyah_tas[0])
                            self.piyon_atama = 'hayir'
                            self.tahta_yazdirma = 'evet'
                            self.repaint()

                elif self.mouse_y_yuvarlanmis == 500:
                    for siyah_tas in self.taslarin_konumlari_siyah:
                        if siyah_tas[0] == self.etkin_tas:
                            self.piyon.remove(siyah_tas[0])
                            siyah_tas[0] = QPixmap('./siyah_kale.png')
                            self.kale.append(siyah_tas[0])
                            self.piyon_atama = 'hayir'
                            self.tahta_yazdirma = 'evet'
                            self.repaint()
                elif self.mouse_y_yuvarlanmis == 600:
                    for siyah_tas in self.taslarin_konumlari_siyah:
                        if siyah_tas[0] == self.etkin_tas:
                            self.piyon.remove(siyah_tas[0])
                            siyah_tas[0] = QPixmap('./siyah_fil.png')
                            self.fil.append(siyah_tas[0])
                            self.piyon_atama = 'hayir'
                            self.tahta_yazdirma = 'evet'
                            self.repaint()
            else:
                if self.mouse_y_yuvarlanmis == 100:
                    for beyaz_tas in self.taslarin_konumlari_beyaz:
                        if beyaz_tas[0] == self.etkin_tas:
                            self.piyon.remove(beyaz_tas[0])
                            beyaz_tas[0] = QPixmap('./beyaz_vezir.png')
                            self.vezir.append(beyaz_tas[0])
                            self.piyon_atama = 'hayir'
                            self.tahta_yazdirma = 'evet'
                            self.repaint()
                elif self.mouse_y_yuvarlanmis == 200:
                    for beyaz_tas in self.taslarin_konumlari_beyaz:
                        if beyaz_tas[0] == self.etkin_tas:
                            self.piyon.remove(beyaz_tas[0])
                            beyaz_tas[0] = QPixmap('./beyaz_at.png')
                            self.at.append(beyaz_tas[0])
                            self.piyon_atama = 'hayir'
                            self.tahta_yazdirma = 'evet'
                            self.repaint()
                elif self.mouse_y_yuvarlanmis == 300:
                    for beyaz_tas in self.taslarin_konumlari_beyaz:
                        if beyaz_tas[0] == self.etkin_tas:
                            self.piyon.remove(beyaz_tas[0])
                            beyaz_tas[0] = QPixmap('./beyaz_kale.png')
                            self.fil.append(beyaz_tas[0])
                            self.piyon_atama = 'hayir'
                            self.tahta_yazdirma = 'evet'
                            self.repaint()
                elif self.mouse_y_yuvarlanmis == 400:
                    for beyaz_tas in self.taslarin_konumlari_beyaz:
                        if beyaz_tas[0] == self.etkin_tas:
                            self.piyon.remove(beyaz_tas[0])
                            beyaz_tas[0] = QPixmap('./beyaz_fil.png')
                            self.kale.append(beyaz_tas[0])
                            self.piyon_atama = 'hayir'
                            self.tahta_yazdirma = 'evet'
                            self.repaint()
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
                    self.tahta_yazdirma = 'evet'
                for siyah_tas in self.taslarin_konumlari_siyah:
                    if self.gidecegi_yer[0] == siyah_tas[1] and self.gidecegi_yer[1] == siyah_tas[2]:
                        self.etkin_tas = siyah_tas[0]
                        self.ilk_dokunus = 'gitme'
                        self.sira = 'beyaz'
                        self.gidilebilir_yerler=[]
                        self.yenilebilir_taslar=[]
                        self.etkin_konum = [self.gidecegi_yer[0],self.gidecegi_yer[1]]
                        self.repaint()
                else:
                    for i in range(len(self.gidilebilir_yerler)):
                        if self.gidecegi_yer[0] == self.gidilebilir_yerler[i][0] and self.gidecegi_yer[1] == self.gidilebilir_yerler[i][1]:
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
                    self.tahta_yazdirma = 'evet'
                for beyaz_tas in self.taslarin_konumlari_beyaz:
                    if self.gidecegi_yer[0] == beyaz_tas[1] and self.gidecegi_yer[1] == beyaz_tas[2]:
                        self.etkin_tas = beyaz_tas[0]
                        self.ilk_dokunus = 'gitme'
                        self.sira = 'siyah'
                        self.gidilebilir_yerler=[]
                        self.yenilebilir_taslar=[]
                        self.etkin_konum = [self.gidecegi_yer[0],self.gidecegi_yer[1]]                       
                        self.repaint()

                else:
                    for i in range(len(self.gidilebilir_yerler)):
                        if self.gidecegi_yer[0] == self.gidilebilir_yerler[i][0] and self.gidecegi_yer[1] == self.gidilebilir_yerler[i][1]:
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
        if self.tahta_yazdirma == 'evet':
            for i in range(len(self.taslarin_konumlari_beyaz)):
                qp.drawPixmap(self.taslarin_konumlari_beyaz[i][1],self.taslarin_konumlari_beyaz[i][2],100,100,self.taslarin_konumlari_beyaz[i][0])
            for i in range (len(self.taslarin_konumlari_siyah)):
                qp.drawPixmap(self.taslarin_konumlari_siyah[i][1],self.taslarin_konumlari_siyah[i][2],100,100,self.taslarin_konumlari_siyah[i][0])
            self.tahta_yazdirma = 'hayir'
        else:
            if self.ilk_dokunus == 'gitme':
                self.c,self.d = self.etkin_konum[0],self.etkin_konum[1]

                qp.drawPixmap(self.etkin_konum[0],self.etkin_konum[1],100,100,self.image_secili_bolge)
                for i in range(len(self.piyon)):
                    if self.etkin_tas == self.piyon[i]:
                        self.gidilebilir_yerler = self.piyon_hareketi()
                        if self.gecerken_alma[0] == 'var':
                            if self.etkin_tas == self.gecerken_alma[1][0]:
                                self.gidilebilir_yerler.extend([self.gecerken_alma[2]])
                                self.yenilebilir_taslar.extend([self.gecerken_alma[3]])
                            if len(self.gecerken_alma) == 7:
                                if self.etkin_tas == self.gecerken_alma[4][0]:
                                    self.gidilebilir_yerler.extend([self.gecerken_alma[5]])
                                    self.yenilebilir_taslar.extend([self.gecerken_alma[7]])
                        break
                for i in range(len(self.fil)):
                    if self.etkin_tas == self.fil[i]:
                        self.gidilebilir_yerler = self.fil_hareketi()
                        break
                for i in range(len(self.kale)):
                    if self.etkin_tas == self.kale[i]:
                        self.gidilebilir_yerler = self.kale_hareketi()
                        break
                for i in range(len(self.at)):
                    if self.etkin_tas == self.at[i]:
                        self.gidilebilir_yerler = self.at_hareketi()
                        break
                for i in range(len(self.vezir)):
                    if self.etkin_tas == self.vezir[i]:
                        self.gidilebilir_yerler = self.fil_hareketi()
                        self.gidilebilir_yerler.extend(self.kale_hareketi())

                        break
                for i in range(2):
                    if self.etkin_tas == self.sah[i]:
                        self.gidilebilir_yerler = self.sah_hareketi()
                        if self.sira == 'siyah':
                            self.gidilebilir_yerler = [gidilebilir_yer for gidilebilir_yer in self.gidilebilir_yerler if gidilebilir_yer  not in self.siyah_taslarin_gordugu_yerler]
                            if self.rok_icin_tas_oynama[2][1] == 'oynandi':
                                pass 
                            else:
                                if self.rok_icin_tas_oynama[0][1] == 'oynamadi':
                                    for beyaz_tas in self.taslarin_konumlari_beyaz:
                                        if (beyaz_tas[1] == 100 and beyaz_tas[2] == 700) or \
                                            (beyaz_tas[1] == 200 and beyaz_tas[2] == 700) or \
                                            (beyaz_tas[1] == 300 and beyaz_tas[2] == 700):
                                            break
                                    else:
                                        for gorulen_yer in self.taslarin_gordugu_yerler:
                                            if (gorulen_yer[0] == 200 and gorulen_yer[1] == 700) or\
                                                (gorulen_yer[0] == 300 and gorulen_yer[1] == 700) or\
                                                (gorulen_yer[0] == 400 and gorulen_yer[1] == 700):
                                                break
                                        else:
                                            self.gidilebilir_yerler.append([200,700])

                                if self.rok_icin_tas_oynama[1][1] == 'oynamadi':
                                    for beyaz_tas in self.taslarin_konumlari_beyaz:
                                        if (beyaz_tas[1] == 500 and beyaz_tas[2] == 700) or \
                                            (beyaz_tas[1] == 600 and beyaz_tas[2] == 700):
                                            break
                                    else:
                                        for gorulen_yer in self.taslarin_gordugu_yerler:
                                            if (gorulen_yer[0] == 400 and gorulen_yer[1] == 700) or\
                                                (gorulen_yer[0] == 500 and gorulen_yer[1] == 700) or\
                                                (gorulen_yer[0] == 600 and gorulen_yer[1] == 700):
                                                break
                                        else:
                                            self.gidilebilir_yerler.append([600,700])
                        else:
                            self.gidilebilir_yerler = [gidilebilir_yer for gidilebilir_yer in self.gidilebilir_yerler if gidilebilir_yer  not in self.beyaz_taslarin_gordugu_yerler]
                            print(self.beyaz_taslarin_gordugu_yerler)
                            if self.rok_icin_tas_oynama[5][1] == 'oynandi':
                                pass 
                            else:
                                if self.rok_icin_tas_oynama[3][1] == 'oynamadi':
                                    for siyah_tas in self.taslarin_konumlari_siyah:
                                        if (siyah_tas[1] == 100 and siyah_tas[2] == 0) or \
                                            (siyah_tas[1] == 200 and siyah_tas[2] == 0) or \
                                            (siyah_tas[1] == 300 and siyah_tas[2] == 0):
                                            break
                                    else:
                                        for gorulen_yer in self.taslarin_gordugu_yerler:
                                            if (gorulen_yer[0] == 200 and gorulen_yer[1] == 0) or\
                                                (gorulen_yer[0] == 300 and gorulen_yer[1] == 0) or\
                                                (gorulen_yer[0] == 400 and gorulen_yer[1] == 0):
                                                break
                                        else:
                                            self.gidilebilir_yerler.append([200,0])

                                if self.rok_icin_tas_oynama[4][1] == 'oynamadi':
                                    for siyah_tas in self.taslarin_konumlari_siyah:
                                        if (siyah_tas[1] == 500 and siyah_tas[2] == 0) or \
                                            (siyah_tas[1] == 600 and siyah_tas[2] == 0):
                                            break
                                    else:
                                        for gorulen_yer in self.taslarin_gordugu_yerler:
                                            if (gorulen_yer[0] == 400 and gorulen_yer[1] == 0) or\
                                                (gorulen_yer[0] == 500 and gorulen_yer[1] == 0) or\
                                                (gorulen_yer[0] == 600 and gorulen_yer[1] == 0):
                                                break
                                        else:
                                            self.gidilebilir_yerler.append([600,0])
                        break
                    self.taslarin_gordugu_yerler = []

                self.gidilebilir_yerler = [gidilebilir_yer for gidilebilir_yer in self.gidilebilir_yerler if not(gidilebilir_yer[0]>700 or gidilebilir_yer[0]<0 or\
                    gidilebilir_yer[1]<0 or gidilebilir_yer[1]>700)]
                self.yenilebilir_taslar = [yenilebilir_tas for yenilebilir_tas in self.yenilebilir_taslar if yenilebilir_tas in self.gidilebilir_yerler]

                                

                            
                
                donguden_cikma = False
                silecegim_tas = []
                for i in range(len(self.at)):
                    # for sah_ceken_tas in self.sah_ceken_tas:
                    #     if sah_ceken_tas[0] == self.at[i]:
                    #         donguden_cikma = True
                    #         break
                    if donguden_cikma == True:
                        break
                else:
                    if self.sira == 'siyah':
                        for i in range(len(self.taslarin_konumlari_beyaz)):
                            if self.etkin_tas == self.taslarin_konumlari_beyaz[i][0]:
                                self.gidilebilir_yerler_kopya = deepcopy(self.gidilebilir_yerler)
                                cikaracagim_konumlar = []
                                for gidilebilir_yer in self.gidilebilir_yerler_kopya:
                                    silecegim_tas = []
                                    print(f'baktigim gidilebilir yerin konumu {gidilebilir_yer[0]},{gidilebilir_yer[1]}')
                                    self.siyah_taslarin_gordugu_yerler = []
                                    self.x, self.y = self.taslarin_konumlari_beyaz[i][1],self.taslarin_konumlari_beyaz[i][2]
                                    self.taslarin_konumlari_beyaz[i][1],self.taslarin_konumlari_beyaz[i][2] = gidilebilir_yer[0],gidilebilir_yer[1]
                                    for siyah_tas in self.taslarin_konumlari_siyah:
                                        # for i in range(len(self.piyon)):
                                        #     if self.etkin_tas == self.piyon[i]:
                                        #         if self.gecerken_alma[0] == 'var':
                                        #             if self.etkin_tas == self.gecerken_alma[1][0]:
                                        #                 if gidilebilir_yer[0] == self.gecerken_alma[2][0] and gidilebilir_yer[1] == self.gecerken_alma[2][1]:
                                        #                     e,f = gecerken_alma[1][1],gecerken_alma[1][2]
                                        #                     silecegim_tas = [gecerken_alma[1][1],gecerken_alma[1][2]]
                                        #                     self.yenilebilir_taslar.extend([self.gecerken_alma[1]])
                                        #                     break
                                        #             # if len(self.gecerken_alma) == 7:
                                        #             #     if self.etkin_tas == self.gecerken_alma[4][0]:
                                        #             #         self.gidilebilir_yerler.extend([self.gecerken_alma[5]])
                                        #             #         self.yenilebilir_taslar.extend([self.gecerken_alma[4]])
                                        # else:
                                        if siyah_tas[1] == gidilebilir_yer[0] and siyah_tas[2] == gidilebilir_yer[1]:
                                            e,f = siyah_tas[1],siyah_tas[2]
                                            silecegim_tas = [siyah_tas[1],siyah_tas[2]]
                                    if self.gecerken_alma[0] == 'var':
                                        if self.etkin_tas == self.gecerken_alma[1][0]:
                                            if gidilebilir_yer[0] == self.gecerken_alma[2][0] and gidilebilir_yer[1] == self.gecerken_alma[2][1]:
                                                e,f = self.gecerken_alma[2][0],self.gecerken_alma[2][1]+100
                                                silecegim_tas = [self.gecerken_alma[2][0],self.gecerken_alma[2][1]+100]
                                                print(f'silecegim tas: {silecegim_tas}')
                                    
                                    if len(silecegim_tas)>0:
                                        self.taslarin_konumlari_siyah = [[tas] if (x == silecegim_tas[0] and y == silecegim_tas[1]) else [tas, x, y] for tas, x, y in self.taslarin_konumlari_siyah ]
                                        print('konumlar silindi')
                                    self.gidilebilir_yerler = []
                                    # self.gidilebilir_yerler = []
                                    if self.taslarin_baktigi_yerler() == False:
                                        print(f'{gidilebilir_yer} konumunu cikariyorum')
                                        cikaracagim_konumlar.append(gidilebilir_yer)
                                        # self.gidilebilir_yerler.extend(self.gidilebilir_yerler_kopya)
                                        # self.gidilebilir_yerler.remove(gidilebilir_yer)
                                        # print('ben buralara kadar geldim')
                                        # print(gidilebilir_yer)
                                    # print(self.gidilebilir_yerler)
                                    # else:
                                    #     self.gidilebilir_yerler.extend(self.gidilebilir_yerler_kopya)
                                    self.taslarin_konumlari_beyaz[i][1],self.taslarin_konumlari_beyaz[i][2] = self.x, self.y
                                    for siyah_tas in self.taslarin_konumlari_siyah:
                                        if len(siyah_tas) == 1:
                                            siyah_tas.append(e)
                                            siyah_tas.append(f)
                                            print('ekledim')
                                        print(siyah_tas)
                                # for siyah_taslarin_gordugu_yer in self.siyah_taslarin_gordugu_yerler:
                                #     qp.drawPixmap(siyah_taslarin_gordugu_yer[0],siyah_taslarin_gordugu_yer[1],100,100,self.image_siyaha_boyama)
                                self.gidilebilir_yerler = [gy for gy in self.gidilebilir_yerler_kopya if gy not in cikaracagim_konumlar]
                # if self.sira == 'siyah' and self.sah_cekildi_beyaz == True and self.etkin_tas != self.image_beyaz_sah:
                #     for i in range(len(self.sah_ceken_tas)):
                #         self.gidilebilir_yerler = [gidilebilir_yer for gidilebilir_yer in self.gidilebilir_yerler if gidilebilir_yer[0] == self.sah_ceken_tas[i][1] and\
                #             gidilebilir_yer[1] == self.sah_ceken_tas[i][2]]
                # if self.sira == 'beyaz' and self.sah_cekildi_siyah == True and self.etkin_tas != self.image_siyah_sah:
                #     for i in range(len(self.sah_ceken_tas)):
                #         self.gidilebilir_yerler = [gidilebilir_yer for gidilebilir_yer in self.gidilebilir_yerler if gidilebilir_yer[0] == self.sah_ceken_tas[i][1] and\
                #             gidilebilir_yer[1] == self.sah_ceken_tas[i][2]]
                # if self.sira == 'siyah':
                #     for beyaz_tas in self.taslarin_konumlari_beyaz:
                #         if beyaz_tas == self.etkin_tas:
                #             cikaracagim_konumlar = []
                #             self.gidilebilir_yerler_kopya = deepcopy(self.gidilebilir_yerler)
                #             for gidilebilir_yer in self.gidilebilir_yerler_kopya:
                #                 self.siyah_taslarin_gordugu_yerler = []
                #                 x,y = beyaz_tas[1],beyaz_tas[2]
                #                 beyaz_tas[1],beyaz_tas[2] = gidilebilir_yer[0],gidilebilir_yer[1]
                #                 for siyah_tas in self.taslarin_konumlari_siyah:
                #                     if siyah_tas[1] == gidilebilir_yer[0] and siyah_tas[2] == gidilebilir_yer[1]:
                #                         e,f = siyah_tas[1],siyah_tas[2]
                #                         silecegim_tas = [siyah_tas[1],siyah_tas[2]]
                #                 if len(silecegim_tas)>0:
                #                     self.taslarin_konumlari_siyah = [[tas] if (x == silecegim_tas[0] and y == silecegim_tas[1]) else [tas, x, y] for tas, x, y in self.taslarin_konumlari_siyah ]
                #                     print('konumlar silindi')
                    elif self.sira == 'beyaz':
                        for i in range(len(self.taslarin_konumlari_siyah)):
                            if self.etkin_tas == self.taslarin_konumlari_siyah[i][0]:
                                self.gidilebilir_yerler_kopya = deepcopy(self.gidilebilir_yerler)
                                cikaracagim_konumlar = []
                                for gidilebilir_yer in self.gidilebilir_yerler_kopya:
                                    silecegim_tas = []
                                    print(f'baktigim gidilebilir yerin konumu {gidilebilir_yer[0]},{gidilebilir_yer[1]}')
                                    self.beyaz_taslarin_gordugu_yerler = []
                                    self.x, self.y = self.taslarin_konumlari_siyah[i][1],self.taslarin_konumlari_siyah[i][2]
                                    self.taslarin_konumlari_siyah[i][1],self.taslarin_konumlari_siyah[i][2] = gidilebilir_yer[0],gidilebilir_yer[1]
                                    for beyaz_tas in self.taslarin_konumlari_beyaz:
                                        if beyaz_tas[1] == gidilebilir_yer[0] and beyaz_tas[2] == gidilebilir_yer[1]:
                                            e,f = beyaz_tas[1],beyaz_tas[2]
                                            silecegim_tas = [beyaz_tas[1],beyaz_tas[2]]
                                    if len(silecegim_tas)>0:
                                        self.taslarin_konumlari_beyaz = [[tas] if (x == silecegim_tas[0] and y == silecegim_tas[1]) else [tas, x, y] for tas, x, y in self.taslarin_konumlari_beyaz ]
                                        print('konumlar silindi')

                                    self.gidilebilir_yerler = []
                                    print(self.taslarin_baktigi_yerler())
                                    if self.taslarin_baktigi_yerler() == False:
                                        print(f'{gidilebilir_yer} konumunu cikariyorum')
                                        cikaracagim_konumlar.append(gidilebilir_yer)
                                        # self.gidilebilir_yerler.extend(self.gidilebilir_yerler_kopya)
                                        # self.gidilebilir_yerler.remove(gidilebilir_yer)
                                        # print('ben buralara kadar geldim')
                                        # print(gidilebilir_yer)
                                    # print(self.gidilebilir_yerler)
                                    # else:
                                    #     self.gidilebilir_yerler.extend(self.gidilebilir_yerler_kopya)
                                    self.taslarin_konumlari_siyah[i][1],self.taslarin_konumlari_siyah[i][2] = self.x, self.y
                                    for beyaz_tas in self.taslarin_konumlari_beyaz:
                                        if len(beyaz_tas) == 1:
                                            beyaz_tas.append(e)
                                            beyaz_tas.append(f)
                                            print('ekledim')
                                # for beyaz_taslarin_gordugu_yer in self.beyaz_taslarin_gordugu_yerler:
                                #     qp.drawPixmap(beyaz_taslarin_gordugu_yer[0],beyaz_taslarin_gordugu_yer[1],100,100,self.image_siyaha_boyama)
                                self.gidilebilir_yerler = [gy for gy in self.gidilebilir_yerler_kopya if gy not in cikaracagim_konumlar]

                for gidilebilir_yer in self.gidilebilir_yerler:
                    if self.sira == 'beyaz':
                        for beyaz_tas in self.taslarin_konumlari_beyaz:
                            
                            if gidilebilir_yer[0] == beyaz_tas[1] and gidilebilir_yer[1] == beyaz_tas[2]:
                                self.yenilebilir_taslar.append(beyaz_tas)
                                if beyaz_tas[0] == self.image_beyaz_sah:
                                    result = QMessageBox.question(self,'lichess','Oyun bitti, siyah kazandi! ',QMessageBox.Ok)
                                    if (result == QMessageBox.Ok):
                                        self.close()
                                        QMessageBox.close()
                                break
                        else:
                            qp.drawPixmap(gidilebilir_yer[0]+15,gidilebilir_yer[1]+15,70,70,self.image_gidilebilir_yerler)

                    else:
                        for siyah_tas in self.taslarin_konumlari_siyah:
                            if gidilebilir_yer[0] == siyah_tas[1] and gidilebilir_yer[1] == siyah_tas[2]:
                                self.yenilebilir_taslar.append(siyah_tas)
                                if siyah_tas[0] == self.image_siyah_sah:
                                    result = QMessageBox.question(self,'lichess','Oyun bitti, beyaz kazandi! ',QMessageBox.Ok)
                                    if (result == QMessageBox.Ok):
                                        self.close()
                                        QMessageBox.close()
                                break
                        else:
                            qp.drawPixmap(gidilebilir_yer[0]+15,gidilebilir_yer[1]+15,70,70,self.image_gidilebilir_yerler)
                for yenilebilir_tas in self.yenilebilir_taslar:
                    qp.drawPixmap(yenilebilir_tas[1]-5,yenilebilir_tas[2]-5,30,30,self.image_sol_ust)
                    qp.drawPixmap(yenilebilir_tas[1]+75,yenilebilir_tas[2]-5,30,30,self.image_sag_ust)
                    qp.drawPixmap(yenilebilir_tas[1]-5,yenilebilir_tas[2]+75,30,30,self.image_sol_alt)
                    qp.drawPixmap(yenilebilir_tas[1]+75,yenilebilir_tas[2]+75,30,30,self.image_sag_alt)
                self.taslarin_gordugu_yerler = []
                self.a = 2
                self.siyah_taslarin_gordugu_yerler = []
                self.beyaz_taslarin_gordugu_yerler = []
                # print(self.gidilebilir_yerler)
            
            
            if  self.a == 3:
                self.sah_ceken_tas = []
                self.siyah_taslarin_gordugu_yerler = []
                self.beyaz_taslarin_gordugu_yerler = []
                self.sah_cekildi_beyaz = False
                self.sah_cekildi_siyah = False
                for kale in self.kale:
                    if self.etkin_tas == kale:
                        print(f'{kale} oynandi')
                        for i in range(len(self.rok_icin_tas_oynama)):
                            if kale == self.rok_icin_tas_oynama[i][0]:
                                self.rok_icin_tas_oynama[i][1] = 'oynandi'
                for sah in self.sah:
                    if self.etkin_tas == sah:
                        print(f'{sah} oynandi')
                        for i in range(len(self.rok_icin_tas_oynama)):
                            if sah == self.rok_icin_tas_oynama[i][0]:
                                self.rok_icin_tas_oynama[i][1] = 'oynandi'
                        if self.etkin_konum == [400,700] or self.etkin_konum == [400,0]:
                            if self.gidecegi_yer == [200,700]:
                                for beyaz_tas in self.taslarin_konumlari_beyaz:
                                    if beyaz_tas[0] == self.image_beyaz_kale1:
                                        beyaz_tas[1] = 300
                            if self.gidecegi_yer == [600,700]:
                                for beyaz_tas in self.taslarin_konumlari_beyaz:
                                    if beyaz_tas[0] == self.image_beyaz_kale2:
                                        beyaz_tas[1] = 500
                            if self.gidecegi_yer == [200,0]:
                                for siyah_tas in self.taslarin_konumlari_siyah:
                                    if siyah_tas[0] == self.image_siyah_kale1:
                                        siyah_tas[1] = 300
                            if self.gidecegi_yer == [600,0]:
                                for siyah_tas in self.taslarin_konumlari_siyah:
                                    if siyah_tas[0] == self.image_siyah_kale2:
                                        siyah_tas[1] = 500
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
                    if self.gidecegi_yer[1] == 0:
                        for i in range(len(self.piyon)):
                            if self.etkin_tas == self.piyon[i]:
                                self.secim_iznib = 'var'
                    if self.etkin_konum[1] == 600:
                        if self.gidecegi_yer[1] ==  400:
                            for i in range(len(self.piyon)):
                                if self.etkin_tas == self.piyon[i]:
                                    for siyah_tas in self.taslarin_konumlari_siyah:
                                        if (siyah_tas[1] == self.gidecegi_yer[0]-100 and siyah_tas[2] == 400) or\
                                            (siyah_tas[1] == self.gidecegi_yer[0]+100 and siyah_tas[2] == 400):
                                            self.gecerken_alma[0] = 'var'
                                            self.gecerken_alma.append([siyah_tas[0],self.gidecegi_yer[0],500])
                                            self.gecerken_alma.append([self.gidecegi_yer[0],500])
                                            self.gecerken_alma.append([self.etkin_tas])
                    elif self.gecerken_alma[0] == 'var':
                        if self.etkin_tas ==  self.gecerken_alma[1][0]:
                            if self.gidecegi_yer[0] == self.gecerken_alma[2][0] and  self.gidecegi_yer[1] == self.gecerken_alma[2][1] :
                                for siyah_tas in self.taslarin_konumlari_siyah:
                                    if siyah_tas[0] == self.gecerken_alma[3][0]:
                                        self.taslarin_konumlari_siyah.remove(siyah_tas)
                                        self.gecerken_alma = ['yok']
                                        break
                        else:
                            self.gecerken_alma = ['yok']
                        if len(self.gecerken_alma) == 7:
                            if self.etkin_tas ==  self.gecerken_alma[4][0]:
                                if self.gidecegi_yer[0] == self.gecerken_alma[5][0] and  self.gidecegi_yer[1] == self.gecerken_alma[5][1] :
                                    for siyah_tas in self.taslarin_konumlari_siyah:
                                        if siyah_tas[0] == self.gecerken_alma[6][0]:
                                            self.taslarin_konumlari_siyah.remove(siyah_tas)
                                            self.gecerken_alma = ['yok']
                                            break
                        else:
                            self.gecerken_alma = ['yok']



                    # for siyah_tas in self.taslarin_konumlari_siyah:
                    #     if self.etkin_konum[1] == 600 and self.gidecegi_yer[1] == 400:
                    #         if (self.gidecegi_yer[0]+100 == siyah_tas[1] and self.gidecegi_yer[1] == siyah_tas[2]) or\
                    #              (self.gidecegi_yer[0]-100 == siyah_tas[1] and self.gidecegi_yer[1] == siyah_tas[2]):
                    #              self.gecerken_alma[0] = 'var'
                    #              self.gecerken_alma.append([siyah_tas])
                                 

                    self.taslarin_konumlari_siyah = [tas for tas in self.taslarin_konumlari_siyah if not (tas[1] == self.mouse_x_yuvarlanmis and tas[2] == self.mouse_y_yuvarlanmis)]
                else:
                    for i in range(len(self.taslarin_konumlari_siyah)):
                        if self.taslarin_konumlari_siyah[i][0] == self.etkin_tas:
                            self.taslarin_konumlari_siyah[i][1]= self.mouse_x_yuvarlanmis
                            self.taslarin_konumlari_siyah[i][2] = self.mouse_y_yuvarlanmis
                    if self.gidecegi_yer[1] == 700:
                        for i in range(len(self.piyon)):
                            if self.etkin_tas == self.piyon[i]:
                                self.secim_iznis = 'var'
                    if self.etkin_konum[1] == 100:
                        if self.gidecegi_yer[1] ==  300:
                            for i in range(len(self.piyon)):
                                if self.etkin_tas == self.piyon[i]:
                                    for beyaz_tas in self.taslarin_konumlari_beyaz:
                                        if (beyaz_tas[1] == self.gidecegi_yer[0]-100 and beyaz_tas[2] == 300) or\
                                            (beyaz_tas[1] == self.gidecegi_yer[0]+100 and beyaz_tas[2] == 300):
                                            self.gecerken_alma[0] = 'var'
                                            self.gecerken_alma.append([beyaz_tas[0],self.gidecegi_yer[0],200])
                                            self.gecerken_alma.append([self.gidecegi_yer[0],200])
                                            self.gecerken_alma.append([self.etkin_tas])
                    elif self.gecerken_alma[0] == 'var':                   
                        if self.etkin_tas ==  self.gecerken_alma[1][0]:
                            if self.gidecegi_yer[0] == self.gecerken_alma[2][0] and  self.gidecegi_yer[1] == self.gecerken_alma[2][1] :
                                for beyaz_tas in self.taslarin_konumlari_beyaz:
                                    if beyaz_tas[0] == self.gecerken_alma[3][0]:
                                        self.taslarin_konumlari_beyaz.remove(beyaz_tas)
                                        self.gecerken_alma = ['yok']
                                        break
                        else:
                            self.gecerken_alma = ['yok']
                        if len(self.gecerken_alma) == 7:
                            if self.etkin_tas ==  self.gecerken_alma[4][0]:
                                if self.gidecegi_yer[0] == self.gecerken_alma[5][0] and  self.gidecegi_yer[1] == self.gecerken_alma[5][1] :
                                    for beyaz_tas in self.taslarin_konumlari_beyaz:
                                        if beyaz_tas[0] == self.gecerken_alma[6][0]:
                                            self.taslarin_konumlari_beyaz.remove(beyaz_tas)
                                            self.gecerken_alma = ['yok']
                                            break          
                            else:
                                self.gecerken_alma = ['yok']
                        
                    self.taslarin_konumlari_beyaz = [tas for tas in self.taslarin_konumlari_beyaz if not (tas[1] == self.mouse_x_yuvarlanmis and tas[2] == self.mouse_y_yuvarlanmis)]
                self.etkin_konum[0],self.etkin_konum[1] = self.c,self.d

                qp.drawPixmap(self.etkin_konum[0],self.etkin_konum[1],100,100,self.image_geldigi_yer)
                self.ilk_dokunus = 'tiklama'
                self.taslarin_baktigi_yerler()   
                self.a=1
                self.yenilebilir_taslar = []
        for i in range(len(self.taslarin_konumlari_beyaz)):
                if self.taslarin_konumlari_beyaz[i][0] != self.image_beyaz_sah or self.sah_cekildi_beyaz != True:
                    qp.drawPixmap(self.taslarin_konumlari_beyaz[i][1],self.taslarin_konumlari_beyaz[i][2],100,100,self.taslarin_konumlari_beyaz[i][0])
                else:
                    qp.drawPixmap(self.taslarin_konumlari_beyaz[i][1],self.taslarin_konumlari_beyaz[i][2],100,100,self.beyaz_sah_sah)

        for i in range (len(self.taslarin_konumlari_siyah)):
            if self.taslarin_konumlari_siyah[i][0] != self.image_siyah_sah or self.sah_cekildi_siyah != True:
                qp.drawPixmap(self.taslarin_konumlari_siyah[i][1],self.taslarin_konumlari_siyah[i][2],100,100,self.taslarin_konumlari_siyah[i][0])
            else:
                qp.drawPixmap(self.taslarin_konumlari_siyah[i][1],self.taslarin_konumlari_siyah[i][2],100,100,self.siyah_sah_sah)
        if self.secim_iznib == 'var':
            qp.drawPixmap(self.gidecegi_yer[0],self.gidecegi_yer[1]+100,100,400,self.image_secim_ekrani_beyaz)
            self.secim_iznib = 'yok'
            self.piyon_mu = 'degil'
            self.piyon_atama = 'evet'
        if self.secim_iznis == 'var':
            qp.drawPixmap(self.gidecegi_yer[0],self.gidecegi_yer[1]-400,100,400,self.image_secim_ekrani_siyah)
            self.secim_iznis = 'yok'
            self.piyon_mu = 'degil'
            self.piyon_atama = 'evet'
        qp.end()
    def taslarin_baktigi_yerler(self):
        if self.sira == 'siyah':
            if self.ilk_dokunus == 'tiklama':
                print('salak')
                for siyah_tas in self.taslarin_konumlari_siyah:
                    for i in range(len(self.sah)):
                        if siyah_tas[0] == self.sah[i]:
                            self.sahin_yeri[0] = [siyah_tas[1],siyah_tas[2]]                   
                for beyaz_tas in self.taslarin_konumlari_beyaz:
                    self.etkin_konum = [beyaz_tas[1],beyaz_tas[2]]
                    for i in range(len(self.piyon)):
                        if self.piyon[i] == beyaz_tas[0]:
                            self.taslarin_gordugu_yerler.append([beyaz_tas[1]-100,beyaz_tas[2]-100])
                            self.taslarin_gordugu_yerler.append([beyaz_tas[1]+100,beyaz_tas[2]-100])
                            if (beyaz_tas[1]-100 == self.sahin_yeri[0][0] and beyaz_tas[2]-100 == self.sahin_yeri[0][1]) or\
                                (beyaz_tas[1]+100 == self.sahin_yeri[0][0] and beyaz_tas[2]-100 == self.sahin_yeri[0][1]):
                                self.sah_ceken_tas.append(beyaz_tas)
                    for i in range(len(self.fil)):
                        if self.fil[i] == beyaz_tas[0]:
                            self.taslarin_gordugu_yerler.extend(self.fil_hareketi(True))
                            for gidilebilir_yer in self.gidilebilir_yerler:
                                if gidilebilir_yer[0] == self.sahin_yeri[0][0] and gidilebilir_yer[1] == self.sahin_yeri[0][1]:
                                    self.sah_ceken_tas.append(beyaz_tas)
                            self.gidilebilir_yerler = []
                    for i in range(len(self.at)):
                        if self.at[i] == beyaz_tas[0]:
                            self.taslarin_gordugu_yerler.extend(self.at_hareketi(True))
                            for gidilebilir_yer in self.gidilebilir_yerler:
                                if gidilebilir_yer[0] == self.sahin_yeri[0][0] and gidilebilir_yer[1] == self.sahin_yeri[0][1]:
                                    self.sah_ceken_tas.append(beyaz_tas)
                            self.gidilebilir_yerler = []
                    for i in range(len(self.kale)):
                        if self.kale[i] == beyaz_tas[0]:
                            self.taslarin_gordugu_yerler.extend(self.kale_hareketi(True))
                            for gidilebilir_yer in self.gidilebilir_yerler:
                                if gidilebilir_yer[0] == self.sahin_yeri[0][0] and gidilebilir_yer[1] == self.sahin_yeri[0][1]:
                                    self.sah_ceken_tas.append(beyaz_tas)
                            self.gidilebilir_yerler = []
                    for i in range(len(self.vezir)):
                        if self.vezir[i] == beyaz_tas[0]:
                            self.taslarin_gordugu_yerler.extend(self.kale_hareketi(True))
                            self.taslarin_gordugu_yerler.extend(self.fil_hareketi(True))
                            for gidilebilir_yer in self.gidilebilir_yerler:
                                if gidilebilir_yer[0] == self.sahin_yeri[0][0] and gidilebilir_yer[1] == self.sahin_yeri[0][1]:
                                    self.sah_ceken_tas.append(beyaz_tas)
                            self.gidilebilir_yerler = []
                    for i in range(len(self.sah)):
                        if self.sah[i] == beyaz_tas[0]:
                            self.taslarin_gordugu_yerler.extend(self.sah_hareketi(True))
                            for gidilebilir_yer in self.gidilebilir_yerler:
                                if gidilebilir_yer[0] == self.sahin_yeri[0][0] and gidilebilir_yer[1] == self.sahin_yeri[0][1]:
                                    self.sah_ceken_tas.append(beyaz_tas)
                            self.gidilebilir_yerler = []
                for gorulen_yer in self.taslarin_gordugu_yerler:
                    # qp.drawPixmap(gorulen_yer[0],gorulen_yer[1],100,100,self.image_siyaha_boyama)
                    if gorulen_yer == self.sahin_yeri[0]:
                        self.sah_cekildi_siyah = True                        
                self.gidilebilir_yerler = []
                self.beyaz_taslarin_gordugu_yerler.extend(self.taslarin_gordugu_yerler)

            if self.ilk_dokunus == 'gitme':  
                for beyaz_tas in self.taslarin_konumlari_beyaz:
                    if len(beyaz_tas) == 3:
                        for i in range(len(self.sah)):
                            if beyaz_tas[0] == self.sah[i]:
                                self.sahin_yeri[1] = [beyaz_tas[1],beyaz_tas[2]]
                for siyah_tas in self.taslarin_konumlari_siyah:
                    if len(siyah_tas) == 3:
                        self.etkin_konum = [siyah_tas[1],siyah_tas[2]]
                        for i in range(len(self.piyon)):
                            if self.piyon[i] == siyah_tas[0]:
                                self.siyah_taslarin_gordugu_yerler.append([siyah_tas[1]-100,siyah_tas[2]+100])
                                self.siyah_taslarin_gordugu_yerler.append([siyah_tas[1]+100,siyah_tas[2]+100])
                                # if (siyah_tas[1]-100 == self.sahin_yeri[1][0] and siyah_tas[2]+100 == self.sahin_yeri[1][1]) or\
                                #         (siyah_tas[1]+100 == self.sahin_yeri[1][0] and siyah_tas[2]+100 == self.sahin_yeri[1][1]):
                                #         self.sah_ceken_tas.append(siyah_tas)
                        for i in range(len(self.fil)):
                            if self.fil[i] == siyah_tas[0]:
                                self.siyah_taslarin_gordugu_yerler.extend(self.fil_hareketi(True))
                                # for gidilebilir_yer in self.gidilebilir_yerler:
                                    # if gidilebilir_yer[0] == self.sahin_yeri[1][0] and gidilebilir_yer[1] == self.sahin_yeri[1][1]:
                                    #     self.sah_ceken_tas.append(siyah_tas)
                                self.gidilebilir_yerler = []
                        for i in range(len(self.at)):
                            if self.at[i] == siyah_tas[0]:
                                self.siyah_taslarin_gordugu_yerler.extend(self.at_hareketi(True))
                                # for gidilebilir_yer in self.gidilebilir_yerler:
                                    # if gidilebilir_yer[0] == self.sahin_yeri[1][0] and gidilebilir_yer[1] == self.sahin_yeri[1][1]:
                                    #     self.sah_ceken_tas.append(siyah_tas)
                                self.gidilebilir_yerler = []
                        for i in range(len(self.kale)):
                            if self.kale[i] == siyah_tas[0]:
                                self.siyah_taslarin_gordugu_yerler.extend(self.kale_hareketi(True))
                                # for gidilebilir_yer in self.gidilebilir_yerler:
                                    # if gidilebilir_yer[0] == self.sahin_yeri[1][0] and gidilebilir_yer[1] == self.sahin_yeri[1][1]:
                                    #     self.sah_ceken_tas.append(siyah_tas)
                                self.gidilebilir_yerler = []
                        for i in range(len(self.vezir)):
                            if self.vezir[i] == siyah_tas[0]:
                                self.siyah_taslarin_gordugu_yerler.extend(self.kale_hareketi(True))
                                self.siyah_taslarin_gordugu_yerler.extend(self.fil_hareketi(True))
                                # for gidilebilir_yer in self.gidilebilir_yerler:
                                    # if gidilebilir_yer[0] == self.sahin_yeri[1][0] and gidilebilir_yer[1] == self.sahin_yeri[1][1]:
                                    #     self.sah_ceken_tas.append(siyah_tas)
                                self.gidilebilir_yerler = []
                        for i in range(len(self.sah)):
                            if self.sah[i] == siyah_tas[0]:
                                self.siyah_taslarin_gordugu_yerler.extend(self.sah_hareketi(True))
                                # for gidilebilir_yer in self.gidilebilir_yerler:
                                    # if gidilebilir_yer[0] == self.sahin_yeri[1][0] and gidilebilir_yer[1] == self.sahin_yeri[1][1]:
                                    #     self.sah_ceken_tas.append(siyah_tas)
                                self.gidilebilir_yerler = []
                print('ben buraya da geldim')
                for siyah_taslarin_gordugu_yer in self.siyah_taslarin_gordugu_yerler:
                    if siyah_taslarin_gordugu_yer[0] == self.sahin_yeri[1][0] and siyah_taslarin_gordugu_yer[1] == self.sahin_yeri[1][1]:
                        return False

        elif self.sira == 'beyaz':
            if self.ilk_dokunus == 'tiklama':
                for beyaz_tas in self.taslarin_konumlari_beyaz:
                    for i in range(len(self.sah)):
                        if beyaz_tas[0] == self.sah[i]:
                            self.sahin_yeri[1] = [beyaz_tas[1],beyaz_tas[2]]
                for siyah_tas in self.taslarin_konumlari_siyah:
                    self.etkin_konum = [siyah_tas[1],siyah_tas[2]]
                    for i in range(len(self.piyon)):
                        if self.piyon[i] == siyah_tas[0]:
                            self.taslarin_gordugu_yerler.append([siyah_tas[1]-100,siyah_tas[2]+100])
                            self.taslarin_gordugu_yerler.append([siyah_tas[1]+100,siyah_tas[2]+100])
                            if (siyah_tas[1]-100 == self.sahin_yeri[1][0] and siyah_tas[2]+100 == self.sahin_yeri[1][1]) or\
                                    (siyah_tas[1]+100 == self.sahin_yeri[1][0] and siyah_tas[2]+100 == self.sahin_yeri[1][1]):
                                    self.sah_ceken_tas.append(siyah_tas)
                    for i in range(len(self.fil)):
                        if self.fil[i] == siyah_tas[0]:
                            self.taslarin_gordugu_yerler.extend(self.fil_hareketi(True))
                            for gidilebilir_yer in self.gidilebilir_yerler:
                                if gidilebilir_yer[0] == self.sahin_yeri[1][0] and gidilebilir_yer[1] == self.sahin_yeri[1][1]:
                                    self.sah_ceken_tas.append(siyah_tas)
                            self.gidilebilir_yerler = []
                    for i in range(len(self.at)):
                        if self.at[i] == siyah_tas[0]:
                            self.taslarin_gordugu_yerler.extend(self.at_hareketi(True))
                            for gidilebilir_yer in self.gidilebilir_yerler:
                                if gidilebilir_yer[0] == self.sahin_yeri[1][0] and gidilebilir_yer[1] == self.sahin_yeri[1][1]:
                                    self.sah_ceken_tas.append(siyah_tas)
                            self.gidilebilir_yerler = []
                    for i in range(len(self.kale)):
                        if self.kale[i] == siyah_tas[0]:
                            self.taslarin_gordugu_yerler.extend(self.kale_hareketi(True))
                            for gidilebilir_yer in self.gidilebilir_yerler:
                                if gidilebilir_yer[0] == self.sahin_yeri[1][0] and gidilebilir_yer[1] == self.sahin_yeri[1][1]:
                                    self.sah_ceken_tas.append(siyah_tas)
                            self.gidilebilir_yerler = []
                    for i in range(len(self.vezir)):
                        if self.vezir[i] == siyah_tas[0]:
                            self.taslarin_gordugu_yerler.extend(self.kale_hareketi(True))
                            self.taslarin_gordugu_yerler.extend(self.fil_hareketi(True))
                            for gidilebilir_yer in self.gidilebilir_yerler:
                                if gidilebilir_yer[0] == self.sahin_yeri[1][0] and gidilebilir_yer[1] == self.sahin_yeri[1][1]:
                                    self.sah_ceken_tas.append(siyah_tas)
                            self.gidilebilir_yerler = []
                    for i in range(len(self.sah)):
                        if self.sah[i] == siyah_tas[0]:
                            self.taslarin_gordugu_yerler.extend(self.sah_hareketi(True))
                            # for gidilebilir_yer in self.gidilebilir_yerler:
                                # if gidilebilir_yer[0] == sen_yeri[1][0] and gidilebilir_yer[1] == self.sahin_yeri[1][1]:
                                #     self.sah_ceken_tas.append(siyah_taslf.sahi)
                            self.gidilebilir_yerler = []
                for gorulen_yer in self.taslarin_gordugu_yerler:
                    # qp.drawPixmap(gorulen_yer[0],gorulen_yer[1],100,100,self.image_siyaha_boyama)
                    if gorulen_yer == self.sahin_yeri[1]:
                        self.sah_cekildi_beyaz = True
                self.gidilebilir_yerler = []
                self.siyah_taslarin_gordugu_yerler.extend(self.taslarin_gordugu_yerler)
        # for siyah_taslarin_gordugu_yer in self.siyah_taslarin_gordugu_yerler:
        #     if gorulen_yer == 
            if self.ilk_dokunus == 'gitme':  
                    for siyah_tas in self.taslarin_konumlari_siyah:
                        if len(siyah_tas) == 3:
                            for i in range(len(self.sah)):
                                if siyah_tas[0] == self.sah[i]:
                                    self.sahin_yeri[0] = [siyah_tas[1],siyah_tas[2]]
                    for beyaz_tas in self.taslarin_konumlari_beyaz:
                        if len(beyaz_tas) == 3:
                            self.etkin_konum = [beyaz_tas[1],beyaz_tas[2]]
                            for i in range(len(self.piyon)):
                                if self.piyon[i] == beyaz_tas[0]:
                                    self.beyaz_taslarin_gordugu_yerler.append([beyaz_tas[1]-100,beyaz_tas[2]+100])
                                    self.beyaz_taslarin_gordugu_yerler.append([beyaz_tas[1]+100,beyaz_tas[2]+100])
                                    # if (siyah_tas[1]-100 == self.sahin_yeri[1][0] and siyah_tas[2]+100 == self.sahin_yeri[1][1]) or\
                                    #         (siyah_tas[1]+100 == self.sahin_yeri[1][0] and siyah_tas[2]+100 == self.sahin_yeri[1][1]):
                                    #         self.sah_ceken_tas.append(siyah_tas)
                            for i in range(len(self.fil)):
                                if self.fil[i] == beyaz_tas[0]:
                                    self.beyaz_taslarin_gordugu_yerler.extend(self.fil_hareketi(True))
                                    # for gidilebilir_yer in self.gidilebilir_yerler:
                                        # if gidilebilir_yer[0] == self.sahin_yeri[1][0] and gidilebilir_yer[1] == self.sahin_yeri[1][1]:
                                        #     self.sah_ceken_tas.append(siyah_tas)
                                    self.gidilebilir_yerler = []
                            for i in range(len(self.at)):
                                if self.at[i] == beyaz_tas[0]:
                                    self.beyaz_taslarin_gordugu_yerler.extend(self.at_hareketi(True))
                                    # for gidilebilir_yer in self.gidilebilir_yerler:
                                        # if gidilebilir_yer[0] == self.sahin_yeri[1][0] and gidilebilir_yer[1] == self.sahin_yeri[1][1]:
                                        #     self.sah_ceken_tas.append(siyah_tas)
                                    self.gidilebilir_yerler = []
                            for i in range(len(self.kale)):
                                if self.kale[i] == beyaz_tas[0]:
                                    self.beyaz_taslarin_gordugu_yerler.extend(self.kale_hareketi(True))
                                    # for gidilebilir_yer in self.gidilebilir_yerler:
                                        # if gidilebilir_yer[0] == self.sahin_yeri[1][0] and gidilebilir_yer[1] == self.sahin_yeri[1][1]:
                                        #     self.sah_ceken_tas.append(siyah_tas)
                                    self.gidilebilir_yerler = []
                            for i in range(len(self.vezir)):
                                if self.vezir[i] == beyaz_tas[0]:
                                    self.beyaz_taslarin_gordugu_yerler.extend(self.kale_hareketi(True))
                                    self.beyaz_taslarin_gordugu_yerler.extend(self.fil_hareketi(True))
                                    # for gidilebilir_yer in self.gidilebilir_yerler:
                                        # if gidilebilir_yer[0] == self.sahin_yeri[1][0] and gidilebilir_yer[1] == self.sahin_yeri[1][1]:
                                        #     self.sah_ceken_tas.append(siyah_tas)
                                    self.gidilebilir_yerler = []
                            for i in range(len(self.sah)):
                                if self.sah[i] == beyaz_tas[0]:
                                    self.beyaz_taslarin_gordugu_yerler.extend(self.sah_hareketi(True))
                                    # for gidilebilir_yer in self.gidilebilir_yerler:
                                        # if gidilebilir_yer[0] == self.sahin_yeri[1][0] and gidilebilir_yer[1] == self.sahin_yeri[1][1]:
                                        #     self.sah_ceken_tas.append(siyah_tas)
                                    self.gidilebilir_yerler = []
                    print('ben buraya da geldim')
                    for beyaz_taslarin_gordugu_yer in self.beyaz_taslarin_gordugu_yerler:
                        if beyaz_taslarin_gordugu_yer[0] == self.sahin_yeri[0][0] and beyaz_taslarin_gordugu_yer[1] == self.sahin_yeri[0][1]:
                            return False
        self.etkin_konum[0],self.etkin_konum[1] = self.c,self.d
    
app =QApplication(sys.argv)
win = Win()
win.show()
sys.exit(app.exec())