

from graphics import Canvas
import time
import random

GAP_W = 70
GAP_H = 40

MESIN_YUVARLAK_R = 70
MESIN_IC_YUVARLAK_R = 5

DIS_CEZA_SAHASI_W = 220
DIS_CEZA_SAHASI_H = 140

IC_CEZA_SAHASI_W = 110
IC_CEZA_SAHASI_H = 70

KALE_W = 40
KALE_H = 60

TOP_R = 8
TOP_V = 5

KALECI_W = 8
KALECI_H = 40

TIME = 60
PIECE = 33


"""
Bu kisimda sadece futbol sahasinda gordugumuz sekilleri olusturuyoruz.
Asagida gordugunuz tum olusan sekiller yukarida verilen constant variablelar sayesinde olusuyor istege gore saha buyultulup kucultulebiliyor
"""

def futbolsahasi(canvas):
    distaki_kutu = canvas.create_rectangle(GAP_W,GAP_H,canvas.get_canvas_width()-GAP_W,canvas.get_canvas_height()-GAP_H)
    canvas.set_fill_color(distaki_kutu,'green')
    mesin_yuvarlak = canvas.create_oval((canvas.get_canvas_width()/2)-MESIN_YUVARLAK_R,(canvas.get_canvas_height()/2)-MESIN_YUVARLAK_R,(canvas.get_canvas_width()/2)-MESIN_YUVARLAK_R+MESIN_YUVARLAK_R*2,((canvas.get_canvas_height()/2)-MESIN_YUVARLAK_R)+MESIN_YUVARLAK_R*2)
    orta_cizgi = canvas.create_line(canvas.get_canvas_width()/2,GAP_H,canvas.get_canvas_width()/2,canvas.get_canvas_height()-GAP_H) 
    
    dis_ceza_sahasi1 = canvas.create_rectangle(GAP_W,GAP_H + DIS_CEZA_SAHASI_H,GAP_W+DIS_CEZA_SAHASI_W,canvas.get_canvas_height()-(GAP_H+DIS_CEZA_SAHASI_H))
    dis_ceza_sahasi2 = canvas.create_rectangle(canvas.get_canvas_width()-(GAP_W+DIS_CEZA_SAHASI_W),GAP_H+DIS_CEZA_SAHASI_H,canvas.get_canvas_width()-GAP_W,canvas.get_canvas_height()-(GAP_H + DIS_CEZA_SAHASI_H))
    
    ic_ceza_sahasi1 = canvas.create_rectangle(GAP_W,GAP_H + DIS_CEZA_SAHASI_H + IC_CEZA_SAHASI_H,GAP_W + IC_CEZA_SAHASI_W,canvas.get_canvas_height()-(GAP_H+DIS_CEZA_SAHASI_H+IC_CEZA_SAHASI_H))
    ic_ceza_sahasi2 = canvas.create_rectangle(canvas.get_canvas_width()-(GAP_W + IC_CEZA_SAHASI_W),GAP_H + DIS_CEZA_SAHASI_H + IC_CEZA_SAHASI_H,canvas.get_canvas_width()-GAP_W,canvas.get_canvas_height()-(GAP_H + DIS_CEZA_SAHASI_H + IC_CEZA_SAHASI_H))
    
    ic_yuvarlak = canvas.create_oval((canvas.get_canvas_width()/2)-MESIN_IC_YUVARLAK_R,(canvas.get_canvas_height()/2)-MESIN_IC_YUVARLAK_R,(canvas.get_canvas_width()/2)-MESIN_IC_YUVARLAK_R+MESIN_IC_YUVARLAK_R*2,((canvas.get_canvas_height()/2)-MESIN_IC_YUVARLAK_R)+MESIN_IC_YUVARLAK_R*2)
    canvas.set_fill_color(ic_yuvarlak,'black')
    
    kale1 = canvas.create_rectangle(KALE_W,canvas.get_canvas_height()/2-KALE_H,GAP_W,canvas.get_canvas_height()/2+KALE_H)
    kale2 = canvas.create_rectangle(canvas.get_canvas_width()-GAP_W,canvas.get_canvas_height()/2-KALE_H,canvas.get_canvas_width()-GAP_W+(GAP_W-KALE_W),canvas.get_canvas_height()/2+KALE_H)
    
"""
Bu kisimda futbol sahasi icerisine once x = 0 ve y = 0 noktasinda bir top olusturup ardindan onu merkeze tasiyoruz.
Ardindan topumuzu hareket ettirmek icin hiz degiskenlerini (dx,dy) -1 ile carpıp move komutuyla birlikte dikdortgen
kenarlarindan topumuzu sektiriyoruz. Kaleye girince dongunun kirilmasi icin de bir True degeri belirleyip if kosuluyla
bu kosulu False a donduruyoruz boylece topumuz kale hizasina geldigi anda animasyon dongusu kiriliyor
"""

def main_game(canvas, TIME, PIECE):
    skor1 = 0
    skor2 = 0
    hiz_listesi = [-5,-6,-7,-8,+5,+6,+7,+8]
    ky_hiz_listesi = [-15,+15]
    dx = random.choice(hiz_listesi)
    dy = random.choice(hiz_listesi)
    ky = random.choice(ky_hiz_listesi)
    skor_yazisi = canvas.create_text(canvas.get_canvas_width()/2,GAP_H/2 ,str(skor1)+" : "+str(skor2)),
    skor_yazisi_outline = canvas.create_rectangle(canvas.get_canvas_width()/2 - 40,0,canvas.get_canvas_width()/2 + 40,GAP_H)
    canvas.set_font(skor_yazisi, "Arial",20)
    random_color = canvas.get_random_color()
    random_color2 = canvas.get_random_color()
    kaleci = canvas.create_rectangle(0, 0, KALECI_W, KALECI_H)
    canvas.set_fill_color(kaleci, random_color)
    canvas.move_to(kaleci,(2*GAP_W + IC_CEZA_SAHASI_W)/2 - KALE_W/2,canvas.get_canvas_height()/2-KALECI_H/2)
    kaleci2 = canvas.create_rectangle(0, 0, KALECI_W, KALECI_H)
    canvas.set_fill_color(kaleci2, random_color2)
    canvas.move_to(kaleci2,canvas.get_canvas_width()-(GAP_W + IC_CEZA_SAHASI_W)/2 - KALE_W/2, canvas.get_canvas_height()/2-KALECI_H/2)
    top = canvas.create_oval(0,0,2*TOP_R,2*TOP_R)
    canvas.set_fill_color(top,'blue')
    canvas.move_to(top,canvas.get_canvas_width()/2-TOP_R,(canvas.get_canvas_height()/2)-TOP_R)
    canvas.wait_for_click()
    top_disarida = True
    
    tabela = canvas.create_text(canvas.get_canvas_width()-GAP_W -10,GAP_H -20, 'TIME: ' + str(TIME))
    canvas.set_font(tabela, 'Franklin Gothic Heavy', 20)
    
    while top_disarida and TIME > 0:
        canvas.move(top, dx, dy)
        canvas.update()
        top_koordinat = canvas.coords(top)
        x1 = top_koordinat[0]
        y1 = top_koordinat[1]
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        
        if canvas.get_top_y(top) + TOP_R*2 > canvas.get_canvas_height() - GAP_H or canvas.get_top_y(top) <= GAP_H:
            dy *= -1
        
        if canvas.get_left_x(top) + TOP_R*2 > canvas.get_canvas_width() - GAP_W or canvas.get_left_x(top) <= GAP_W:
            dx *= -1
        
        '''
        Bu kisimda top, kaleci'nin kalesine girdiginde kaleci2'nin skor sayisinin artmasi kosulunu
        eger kaleci2'nin skoru 3 olursa dongunun tamamen kirilip ekranda 'kaybettiniz' yazisinin belirmesi kosulunu yaziyoruz
        '''
        if canvas.get_left_x(top) <= GAP_W and canvas.get_canvas_height()/2 - KALE_H <= canvas.get_top_y(top) <= (canvas.get_canvas_height()/2 + KALE_H) - TOP_R:
            top_disarida = False
            canvas.delete(skor_yazisi)
            skor2 += 1
            skor_yazisi = canvas.create_text(canvas.get_canvas_width()/2,GAP_H/2 ,str(skor1)+" : "+str(skor2))
            canvas.set_font(skor_yazisi,"Arial",20)
            canvas.move_to(top,GAP_W + IC_CEZA_SAHASI_W,(canvas.get_canvas_height()/2)-TOP_R)
            canvas.move_to(kaleci,(2*GAP_W + IC_CEZA_SAHASI_W)/2 - KALE_W/2,canvas.get_canvas_height()/2-KALECI_H/2)
            canvas.move_to(kaleci2,canvas.get_canvas_width()-(GAP_W + IC_CEZA_SAHASI_W)/2 - KALE_W/2, canvas.get_canvas_height()/2-KALECI_H/2)
            if skor2 == 3:
                top_disarida = False
                bitis_yazisi2 = canvas.create_text(canvas.get_canvas_width()/2,canvas.get_canvas_height()/2,"Bilgisayara karşı kaybettiniz.")
                canvas.set_font(bitis_yazisi2,"Franklin Gothic Heavy", 25)
                break
            
            canvas.wait_for_click()
            top_disarida = True          
        
        '''
        Bu kisimda da yukarıdaki fonksiyonun aynisini, bu sefer kaleci'nin skorunun artmasi kosulunu yaziyoruz.
        Skor kaleci tarafinda 3 oldugunda ekranda 'kazandiniz' yazisi beliriyor
        '''
        if canvas.get_left_x(top) >= canvas.get_canvas_width() - (GAP_W + TOP_R*2) and canvas.get_canvas_height()/2 - KALE_H <= canvas.get_top_y(top) <= (canvas.get_canvas_height()/2 + KALE_H)-TOP_R:
            top_disarida = False
            canvas.delete(skor_yazisi)
            skor1 += 1
            skor_yazisi = canvas.create_text(canvas.get_canvas_width()/2,GAP_H/2 ,str(skor1)+" : "+str(skor2))
            canvas.set_font(skor_yazisi, "Arial",20)
            canvas.move_to(top,canvas.get_canvas_width() - (GAP_W + IC_CEZA_SAHASI_W),(canvas.get_canvas_height()/2)-TOP_R)
            canvas.move_to(kaleci,(2*GAP_W + IC_CEZA_SAHASI_W)/2 - KALE_W/2,canvas.get_canvas_height()/2-KALECI_H/2)
            canvas.move_to(kaleci2,canvas.get_canvas_width()-(GAP_W + IC_CEZA_SAHASI_W)/2 - KALE_W/2, canvas.get_canvas_height()/2-KALECI_H/2)
            if skor1 == 3:
                top_disarida = False
                bitis_yazisi = canvas.create_text(canvas.get_canvas_width()/2,canvas.get_canvas_height()/2,"Tebrikler Oyunu Kazandiniz !")
                canvas.set_font(bitis_yazisi,"Franklin Gothic Heavy", 25)
                break
            
            canvas.wait_for_click()
            top_disarida = True
        
        '''
        Bu kisimda kalecilerin hareket komutlarini yaziyoruz.
        kaleci'nin hareketini oyuncu istedigi sekilde yonlendirirken, kaleci2'nin hareketinin belirli konumlar 
        arasinda sabit bir sekilde asagi-yukari hareket etmesini sagladik.
        '''
        if x1 <= canvas.get_left_x(kaleci) + KALECI_W and canvas.get_top_y(kaleci) < y1 <= canvas.get_top_y(kaleci) + KALE_H and x1 >= canvas.get_left_x(kaleci):
            dx *= -1  
        
        if x1 >= (canvas.get_canvas_width()-(GAP_W + IC_CEZA_SAHASI_W)/2 - KALE_W/2) and canvas.get_top_y(kaleci2) <= y1 <= (canvas.get_top_y(kaleci2) + KALE_H) and x1 <= (canvas.get_canvas_width()-(GAP_W + IC_CEZA_SAHASI_W)/2):
            dx *= -1
        
        canvas.move(kaleci2,0,ky)
        
        if canvas.get_top_y(kaleci2) < GAP_H + DIS_CEZA_SAHASI_H or canvas.get_top_y(kaleci2) >= canvas.get_canvas_height() - (GAP_H + DIS_CEZA_SAHASI_H + KALECI_H):
            ky *= -1
    
        canvas.moveto(kaleci,mouse_x,mouse_y)   
        
        '''
        Bu kisimda belirledigimiz sure zarfinda herhangi bir galibiyet ya da maglubiyet olmadigi takdirde oyun dongusunun kirilarak ekranda
        'kaybettiniz' yazisinin belirmesini sagliyoruz
        '''
        if PIECE == 0:
            TIME -=1
            PIECE = 33
        else:
            PIECE -=1
            
        if TIME == 0:
            bitis_yazisi3 = canvas.create_text(canvas.get_canvas_width()/2 ,canvas.get_canvas_height()/2,"Bilgisayara karsi kaybettiniz. HAHA LOL !!")
            canvas.set_font(bitis_yazisi3,"Franklin Gothic Heavy", 25)
            canvas.move_to(top,canvas.get_canvas_width()/2-TOP_R ,GAP_H+TOP_R*2)
            canvas.move_to(kaleci,(2*GAP_W + IC_CEZA_SAHASI_W)/2 - KALE_W/2,canvas.get_canvas_height()/2-KALECI_H/2)
            canvas.move_to(kaleci2,canvas.get_canvas_width()-(GAP_W + IC_CEZA_SAHASI_W)/2 - KALE_W/2, canvas.get_canvas_height()/2-KALECI_H/2)
            
        

        canvas.set_text(tabela,  'TIME: ' + str(TIME)+ 's' )
        time.sleep(0.03)
        

'''
Bu kisimda oyunumuz baslamadan once oyun hakkinda gerekli bilgileri iceren bir baslangic ekranin belirmesi fonksiyonunu yaziyoruz.
'''    
         
def giris_ekrani(canvas):
    
    giris_yazisi = canvas.create_text(canvas.get_canvas_width()/2,canvas.get_canvas_height()/4,"BILGI KISMI\n----------\nSol tarafta baslayacaksiniz.\nKaleciyi mouse ile kontrol edeceksiniz.\nBilgisayar karsisinda 60 saniye icerisinde 3 gol atabilirseniz kazanirsiniz, \natamazsaniz kaybedersiniz.\nDevam etmek icin ekrana tıklayiniz.\n\n\nBASARILAR ...")
    canvas.set_font(giris_yazisi,"Franklin Gothic Heavy",20)
    canvas.wait_for_click()
    canvas.delete(giris_yazisi)
    
def main():
    canvas = Canvas(1100,700)
    canvas.set_canvas_title("FUTBOL OYUNU")
    giris_ekrani(canvas)
    futbolsahasi(canvas)
    main_game(canvas, TIME, PIECE)
    canvas.mainloop()

if __name__ == '__main__':
    main()
        
