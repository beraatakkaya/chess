from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QPainter,QPixmap
import sys

class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sayac = 0
        self.ilk_dokunus = 'tiklama'
        self.image = QPixmap('./lichessgenelekran.png')
        self.image_beyaz_piyon = QPixmap('./beyaz_piyon.png')
        self.image_secili_bolge = QPixmap('./secili_bolge.png')
        self.image_beyaz_at = QPixmap('./beyaz_at.png')
        self.image_geldigi_yer = QPixmap('./geldigi_yer.png')
        self.image_gittigi_yer = QPixmap('./gittigi_yer.png')
        self.izin = 'yok'
        self.a=1


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
    def mousePressEvent(self, event):

        print('Mouse coords: ( %d : %d )' % (event.x(), event.y()))
        
        self.mouse_click_x =[event.x()]
        self.mouse_click_y =[event.y()]

        self.mouse_x_yuvarlanmis = self.yuvarlama(self.mouse_click_x[0])
        self.mouse_y_yuvarlanmis = self.yuvarlama(self.mouse_click_y[0])

        if self.ilk_dokunus == 'tiklama':
            for i in range(len(self.taslarin_konumlari_beyaz)):
                if self.mouse_x_yuvarlanmis == self.taslarin_konumlari_beyaz[i][1]:
                        if self.mouse_y_yuvarlanmis == self.taslarin_konumlari_beyaz[i][2]:
                            self.etkin_tas = self.taslarin_konumlari_beyaz[i][0]
                            self.etkin_konum = [self.mouse_x_yuvarlanmis,self.mouse_y_yuvarlanmis]
                            if self.a == 1:
                                self.ilk_dokunus = 'gitme'
                            self.repaint()
        else:
            self.gidecegi_yer = [self.mouse_x_yuvarlanmis,self.mouse_y_yuvarlanmis]
            self.a = 3
            self.ilk_dokunus = 'tiklama'
            self.repaint()

    def paintEvent(self,event):
        qp = QPainter()

        if self.sayac == 0 :
            
            self.taslarin_konumlari_beyaz = [[self.image_beyaz_at,200,200],[self.image_beyaz_piyon,300,300]]
            self.etkin_tas = self.image_beyaz_at
            self.sayac += 1


        
        qp.begin(self)
        qp.drawPixmap(self.rect(),self.image)

        if self.ilk_dokunus == 'gitme':
            qp.drawPixmap(self.etkin_konum[0],self.etkin_konum[1],100,100,self.image_secili_bolge)
            self.a = 2


        
            

        if  self.a == 3:
            qp.drawPixmap(self.mouse_x_yuvarlanmis,self.mouse_y_yuvarlanmis,100,100,self.etkin_tas)
            qp.drawPixmap(self.gidecegi_yer[0],self.gidecegi_yer[1],100,100,self.image_gittigi_yer)
            


            for i in range(len(self.taslarin_konumlari_beyaz)):
                if self.taslarin_konumlari_beyaz[i][0] == self.etkin_tas:
                    self.taslarin_konumlari_beyaz[i][1]= self.mouse_x_yuvarlanmis
                    self.taslarin_konumlari_beyaz[i][2] = self.mouse_y_yuvarlanmis
            if self.ilk_dokunus == 'tiklama':
                qp.drawPixmap(self.etkin_konum[0],self.etkin_konum[1],100,100,self.image_geldigi_yer)
            self.ilk_dokunus = 'tiklama'
            self.a=1
            
        qp.drawPixmap(self.taslarin_konumlari_beyaz[0][1],self.taslarin_konumlari_beyaz[0][2],100,100,self.image_beyaz_at)
        qp.drawPixmap(self.taslarin_konumlari_beyaz[1][1],self.taslarin_konumlari_beyaz[1][2],100,100,self.image_beyaz_piyon)

        qp.end()
        

app =QApplication(sys.argv)
win = Win()
win.show()
sys.exit(app.exec())