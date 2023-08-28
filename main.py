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
        self.sah = [self.image_beyaz_vezir,self.image_siyah_vezir]
        self.tas_adlari = [self.piyon,self.kale,self.at,self.fil,self.vezir,self.sah]
        self.a=1
        self.gidilebilir_yerler = []
        self.izint = 'var'
        self.izini = 'var'

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
        if self.sira == 'siyah':
            for i in range(len(self.taslarin_konumlari_beyaz)):
                if (self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]-100) or (self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]-100):
                    self.izint = 'yok'
            
                if (self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]-200) or (self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]-200):
                    self.izini = 'yok'
            if self.izint != 'yok':
                self.gidilebilir_yerler.append([self.etkin_konum[0],self.etkin_konum[1]-100])
                self.izint = 'var'
            if self.izini != 'yok':
                if self.etkin_konum[1] == 600:
                        self.gidilebilir_yerler.append([self.etkin_konum[0],self.etkin_konum[1]-200])
                        self.izini = 'var'
        elif self.sira == 'beyaz':
            for i in range(len(self.taslarin_konumlari_beyaz)):
                if (self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]+100) or (self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]+100):
                    self.izint = 'yok'
            
                if (self.taslarin_konumlari_beyaz[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_beyaz[i][2]==self.etkin_konum[1]+200) or (self.taslarin_konumlari_siyah[i][1] ==  self.etkin_konum[0] and self.taslarin_konumlari_siyah[i][2]==self.etkin_konum[1]+200):
                    self.izini = 'yok'
            if self.izint != 'yok':
                self.gidilebilir_yerler.append([self.etkin_konum[0],self.etkin_konum[1]+100])
            if self.izini != 'yok':
                if self.etkin_konum[1] == 100:
                        self.gidilebilir_yerler.append([self.etkin_konum[0],self.etkin_konum[1]+200])
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
                for i in range(len(self.gidilebilir_yerler)):
                    if self.gidecegi_yer[0] == self.gidilebilir_yerler[i][0] and self.gidecegi_yer[1] == self.gidilebilir_yerler[i][1]:
                        print('calisti')
                        self.a = 3
                        self.ilk_dokunus = 'tiklama'
                        self.gidilebilir_yerler = []
                        self.repaint()
                        break
                self.ilk_dokunus = 'tiklama'
                self.sira = 'beyaz'
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
                for i in range(len(self.gidilebilir_yerler)):
                    if self.gidecegi_yer[0] == self.gidilebilir_yerler[i][0] and self.gidecegi_yer[1] == self.gidilebilir_yerler[i][1]:
                        print('calistia')
                        self.a = 3
                        self.ilk_dokunus = 'tiklama'
                        self.gidilebilir_yerler = []
                        self.repaint()
                        break
                self.ilk_dokunus = 'tiklama'
                self.sira = 'siyah'

    def paintEvent(self,event):
        qp = QPainter()

        if self.sayac == 0 :
            self.taslarin_adlari = [self.image_beyaz_at1,self.image_beyaz_piyon1,self.image_beyaz_piyon2,self.image_beyaz_piyon3,self.image_beyaz_piyon4,self.image_beyaz_piyon5,self.image_beyaz_piyon6,self.image_beyaz_piyon7,self.image_beyaz_piyon8,self.image_beyaz_kale1,self.image_beyaz_kale2,self.image_beyaz_at2,self.image_beyaz_fil1,self.image_beyaz_fil2,self.image_beyaz_vezir,self.image_beyaz_sah]

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
                    print(self.gidilebilir_yerler)
            for gidilebilir_yer in self.gidilebilir_yerler:
                qp.drawPixmap(gidilebilir_yer[0],gidilebilir_yer[1],100,100,self.image_gidilebilir_yerler)
            self.a = 2

        if  self.a == 3:
            qp.drawPixmap(self.mouse_x_yuvarlanmis,self.mouse_y_yuvarlanmis,100,100,self.etkin_tas)
            qp.drawPixmap(self.gidecegi_yer[0],self.gidecegi_yer[1],100,100,self.image_gittigi_yer)
            
            for i in range(len(self.taslarin_konumlari_beyaz)):
                if self.taslarin_konumlari_beyaz[i][0] == self.etkin_tas:
                    self.taslarin_konumlari_beyaz[i][1]= self.mouse_x_yuvarlanmis
                    self.taslarin_konumlari_beyaz[i][2] = self.mouse_y_yuvarlanmis
            for i in range(len(self.taslarin_konumlari_siyah)):
                if self.taslarin_konumlari_siyah[i][0] == self.etkin_tas:
                    self.taslarin_konumlari_siyah[i][1]= self.mouse_x_yuvarlanmis
                    self.taslarin_konumlari_siyah[i][2] = self.mouse_y_yuvarlanmis
            qp.drawPixmap(self.etkin_konum[0],self.etkin_konum[1],100,100,self.image_geldigi_yer)

            self.ilk_dokunus = 'tiklama'
            
            self.a=1
        for i in range(16):
            qp.drawPixmap(self.taslarin_konumlari_beyaz[i][1],self.taslarin_konumlari_beyaz[i][2],100,100,self.taslarin_konumlari_beyaz[i][0])
            qp.drawPixmap(self.taslarin_konumlari_siyah[i][1],self.taslarin_konumlari_siyah[i][2],100,100,self.taslarin_konumlari_siyah[i][0])
      
        qp.end()


        
app =QApplication(sys.argv)
win = Win()
win.show()
sys.exit(app.exec())