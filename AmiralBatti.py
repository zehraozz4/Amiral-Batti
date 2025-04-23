# AD:ZEHRA  SOYAD:OZ  NUMARA:22100011049
# Kullanicidan x ve y degeri alinirken 0 dan boyuta kadar olan degerleri giriniz(0 dahil boyut dahi degil).
import copy
import random
print(">>>AMIRAL BATTI<<<")
kontrol1=0
while kontrol1==0:
    print("Secim1:Oyun oynamak")
    print("Secim2:Cikis yapmak")
    secim1=int(input("Lutfen yapmak istediginiz secimi giriniz:"))
    if secim1==1:
        kontrol2=0
        while kontrol2==0:
            print("Amiral batti oyunu basliyorrr...")
            boyut=int(input("Lutfen oyun alaninin boyutunu giriniz(en az 10):"))
            if boyut<10:
                print("Lutfen en az 10 olacak sekilde boyut giriniz!!!")
            else:
                oyun_alani1=[["?" for i in range(boyut)]for i in range(boyut)]
                oyun_alani2=copy.deepcopy(oyun_alani1)
                gemi_boyutlari=[1,2,3,4]
                gemi_konumlari=[]
                gemi_konumlari1=[]
                gemi_konumlari2=[]
                gemi_konumlari3=[]
                gemi_konumlari4=[]
                for i in range(1,len(gemi_boyutlari)+1):
                    yerlesti_mi=False
                    while yerlesti_mi==False:
                        sayac=0
                        x=random.randint(0,boyut-1)
                        y=random.randint(0,boyut-1)
                        yon=random.choice(["yatay","dikey"])
                        if yon=="yatay":
                            if y+i<=boyut:
                                for j in range(i):
                                    if (x,y+j) in gemi_konumlari:
                                        sayac+=1
                                        break
                                for j in range(i):
                                    if sayac==0:
                                        for j in range(i):
                                            gemi_konumlari.append((x,y+j))
                                            oyun_alani1[x][y + j] = "x"
                                            if i == 1:
                                                gemi_konumlari1.append((x, y + j))
                                            elif i == 2:
                                                gemi_konumlari2.append((x, y + j))
                                            elif i == 3:
                                                gemi_konumlari3.append((x, y + j))
                                            elif i == 4:
                                                gemi_konumlari4.append((x, y + j))
                                        yerlesti_mi=True
                                    break
                            else:
                                yerlesti_mi=False
                        else:
                            if x+i<=boyut:
                                for j in range(i):
                                    if (x+j,y) in gemi_konumlari:
                                        sayac+=1
                                        break
                                for j in range(i):
                                    if sayac==0:
                                        for j in range(i):
                                            gemi_konumlari.append((x+j,y))
                                            oyun_alani1[x + j][y] = "x"
                                            if i == 1:
                                                gemi_konumlari1.append((x + j, y))
                                            elif i == 2:
                                                gemi_konumlari2.append((x + j, y))
                                            elif i == 3:
                                                gemi_konumlari3.append((x + j, y))
                                            elif i == 4:
                                                gemi_konumlari4.append((x + j, y))
                                        yerlesti_mi=True
                                    break
                            else:
                                yerlesti_mi=False
                atis_hakki=(boyut*boyut)//3
                puan=0
                kontrol3=0
                while kontrol3==0:
                    gemi2=0
                    gemi3=0
                    gemi4=0
                    print("Secim3:Gizli mod")
                    print("Secim4:Acik mod")
                    secim2=int(input("Lutfen oyun modunu seciniz:"))
                    if secim2==3:
                        x_sayisi=0
                        for i in oyun_alani2:
                            print("".join(i))
                        while atis_hakki>0:
                            print("Kalan atis hakki:",atis_hakki)
                            x=int(input("Lutfen atis yapmak icin satir degeri giriniz(0'dan boyuta kadar):"))
                            y=int(input("Lutfen atis yapmak icin sutun degeri giriniz(0'dan boyuta kadar):"))
                            if x<0 or x>=boyut or y<0 or y>=boyut:
                                print("Gecersiz konum lutfen oyun alani icerisinde bir konum seciniz!!!")
                                continue
                            if oyun_alani1[x][y]=="*":
                                print("Bu konumu daha once sectiniz lutfen baska bir konum seciniz!!!")
                            elif oyun_alani2[x][y]=="x":
                                print("Bu konumu daha once sectiniz lutfen baska bir konum giriniz!!!")
                            elif oyun_alani1[x][y]=="?":
                                puan+=1
                                print("Maalesef isabet edemediniz:(")
                                oyun_alani1[x][y]="*"
                                oyun_alani2[x][y]="*"
                                atis_hakki-=1
                                if atis_hakki==0:
                                    print("Atis hakkiniz bitti maalesef kaybettiniz:(")
                                    kontrol3=1
                                    kontrol2=1
                                    break
                            elif oyun_alani1[x][y]=="x":
                                puan+=1
                                x_sayisi+=1
                                oyun_alani2[x][y]="x"
                                print("Tebrikler bir gemi vurdunuz:)")
                                if (x,y) in gemi_konumlari1:
                                    print("Tebrikler bir gemi batirdiniz:))")
                                if (x,y) in gemi_konumlari2:
                                    gemi2+=1
                                    if gemi2==2:
                                        print("Tebrikler bir gemi batirdiniz:))")
                                if (x,y) in gemi_konumlari3:
                                    gemi3+=1
                                    if gemi3==3:
                                        print("Tebrikler bir gemi batirdiniz:))")
                                if (x,y) in gemi_konumlari4:
                                    gemi4+=1
                                    if gemi4==4:
                                        print("Tebrikler bir gemi batirdiniz:))")
                                if x_sayisi==10:
                                    print("Tebrikler {} puan ile oyunu kazandiniz:)))".format((boyut*boyut)//3-puan))
                                    kontrol3=1
                                    kontrol2=1
                                    break
                            for i in oyun_alani2:
                                print("".join(i))
                    elif secim2==4:
                        x_sayisi=0
                        for i in oyun_alani1:
                            print("".join(i))
                        while atis_hakki>0:
                            print("Kalan atis hakki:",atis_hakki)
                            x=int(input("Lutfen atis yapmak icin satir degeri giriniz(0'dan boyuta kadar):"))
                            y=int(input("Lutfen atis yapmak icin sutun degeri giriniz(0'dan boyuta kadar):"))
                            if x<0 or x>=boyut or y<0 or y>=boyut:
                                print("Gecersiz konum lutfen oyun alani icerisinde bir konum giriniz!!!")
                                continue
                            elif oyun_alani1=="*":
                                print("Bu konumu daha once sectiniz lutfen baska bir konum seciniz!!!")
                            elif oyun_alani2[x][y]=="x":
                                print("Bu konumu daha once sectiniz lutfen baska bir konum seciniz!!!")
                            elif oyun_alani1[x][y]=="?":
                                puan+=1
                                print("Maalesef isabet edemediniz:(")
                                oyun_alani1[x][y]="*"
                                oyun_alani2[x][y]="*"
                                atis_hakki-=1
                                if atis_hakki==0:
                                    print("Atis hakkiniz bitti maalesef kaybettiniz:((")
                                    kontrol3=1
                                    kontrol2=1
                                    break
                            elif oyun_alani1[x][y]=="x":
                                puan+=1
                                x_sayisi+=1
                                oyun_alani2[x][y]="x"
                                print("Tebrikler bir gemi vurdunuz:)")
                                if (x,y) in gemi_konumlari1:
                                    print("Tebrikler bir gemi batirdiniz:))")
                                if (x,y) in gemi_konumlari2:
                                    gemi2+=1
                                    if gemi2==2:
                                        print("Tebrikler bir gemi batirdiniz:))")
                                if (x,y) in gemi_konumlari3:
                                    gemi3+=1
                                    if gemi3==3:
                                        print("Tebrikler bir gemi batirdiniz:))")
                                if (x,y) in gemi_konumlari4:
                                    gemi4+=1
                                    if gemi4==4:
                                        print("Tebrikler bit gemi batirdiniz:))")
                                if x_sayisi==10:
                                    print("Tebrikler {} puan ile oyunu kazandiniz:)))".format((boyut*boyut)//3-puan))
                                    kontrol3=1
                                    kontrol2=1
                                    break
                            for i in oyun_alani1:
                                print("".join(i))
                    else:
                        print("Lutfen gecerli bir deger giriniz!!!")
    elif secim1==2:
        print("Cikis yapiliyor...")
        break
    else:
        print("Lutfen gecerli deger giriniz!!!")