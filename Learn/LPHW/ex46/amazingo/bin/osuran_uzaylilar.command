#!/usr/bin/env python
# -*- coding: utf-8 -*-
# You Make a Game

# Osuran Uzaylilar


# importing required modules
from sys import exit
from random import randint
from textwrap import dedent


class Death:

    quips = ["Ben olsam daha iyi oynardım",
             "Bir daha dene şansını",
             "Sen oynayamıyorsun"]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)



class Tuvalet:

    def enter(self):
        print(dedent("""
        Tuvalet'e girdin.
        Hazır gelmişken sıç ta git.
        Sıçmak için 1, işemek için 2, osurmak için 3 yaz
        Sifonu çekmeyi unutma...
        """))
        sic_ise = input('> ')
        if int(sic_ise) == 1:
            print("Sıçıp çıktın, inşallah sifonu çekmişsindir")
            return 'kopru'
        elif int(sic_ise) == 2:
            print("İşeyip çıktın, inşallah sifonu çekmişsindir")
            return 'kopru'
        else:
            print("Osurdun, ooofff kedi mi yedin ne yaptın leş gibi koktu\nÇıktın tuvaletten")
            return 'kopru'

class Hamam:

    def enter(self):
        print(dedent("""
        Aha Abuzittin'i buldun.
        Puşt hamam da keyif yaparken sıcaktan bayılmış
        ve baygın yatıyor.
        Abuzittin'i aldın.
        Şimdi bir şekilde çıkmanız lazım.
        Sadece bir odada gizli bir çıkış var ve bu çıkışı bulman lazim.
        Hamamdan Köprü'ye geri çıkmak için 1 yaz.
        """))
        selection = input('> ')
        if int(selection) == 1:
            return 'kopru2'
        else:
            return 'death'

class Kopru2:
    def enter(self):
        print(dedent("""
        Köprü'ye geri döndün.
        Uzaylılar sizi bulmadan gizli çıkışın olduğu odayı bulman lazim.
        Ya Giriş'e geri dön, ya da Tuvalet veya Hamam'a tekrar git.
        Odalardan birini seç:
        1. Giriş'e geri dön'
        2. Tuvalet
        3. Hamam
        """))
        selection = input('> ')
        if int(selection) == 1:
            return 'giris2'
        elif int(selection) == 2:
            print(dedent("""
            Tuvalet'e girdin ve çok vakit kaybettin.
            Az ye az sıç bir daha...
            Uzaylılar geldi osurarak öldürdüler sizi.
            """))
            return 'death'
        else:
            print(dedent("""
            Hamam'a girdiniz ve Çok vakit kaybettiniz.
            Üç uzaylı geldi ve üzerinize sıçtılar.
            Bokun altında kalıp öldünüz...
            """))
            return 'death'


class Kopru:

    def enter(self):
        print(dedent("""
        Köprü'ye girdin.
        Karşına iki uzaylı çıktı ve elindeki odunla ikisininde kafasina vurup öldürdün.
        Simdi, iki tane daha odaya açılan kapı var.
        Odalardan birini seç:
        1. Tuvalet
        2. Hamam
        """))
        selection = input('> ')
        if int(selection) == 1:
            return 'tuvalet'
        else:
            print(dedent("""
            Kapıda parolalı kilit var.
            2 rakamlı bir şifresi var(mesela 21).
            Rakamlar sadece 1 ve 2 den oluşuyor
            Yalnızca 3 hakkın var
            """))
            paswd = int("{}{}".format(randint(1,2), randint(1,2)))
            selection = input('Password : ')
            trial = 1
            while int(selection) != paswd and trial < 3:
                print("Try again!")
                trial += 1
                selection = input('Password : ')

            if int(selection) == paswd:
                print("Tebrikler şifreyi doğru yazdın ve Hamam'a girdin")
                return 'hamam'
            else:
                print(dedent("""
                Çok geç kaldın.
                2 uzaylı geldi.
                Üzerine işediler öldün!
                """))
                return 'death'


class Kiler:

    def enter(self):
        print(dedent("""
        Kiler'e girdin. Karşına bir uzaylı çıktı.
        Kafasına odunla vurup öldürdün.
        Yalnız baktın Kiler'de Abuzittin falan yok.
        Giriş'e geri dönmek için 1 yaz
        """))
        selection = input('> ')
        if int(selection) == 1:
            return 'giris3'
        else:
            return 'death'

class Kiler2:

    def enter(self):
        print(dedent("""
        Kiler'e geldin. Karşına bir uzaylı çıktı.
        Osurup uzaylıyı öldürdün.
        Etrafa dikkatlice bak.
        Karşında bir ayna olacak.
        1. Aynayı kır
        2. Giriş'e geri dön
        """))
        selection = input('> ')
        if int(selection) == 1:
            print(dedent("""
            Aynanın arkasında kocaman bir kapı var.
            Kapı da yine parolalı kilit var.
            Parolayı doğru bilmen lazım.
            Parola 3 rakamlı (mesela 311)
            Rakamlar sadece 1, 2 ve 3 den oluşuyor.
            Sadece 10 hakkın var.
            """))
            paswd = int("{}{}{}".format(randint(1,3), randint(1,3), randint(1,3)))
            selection = input('Password : ')
            trial = 1
            while int(selection) != paswd and trial < 10:
                print("Try again!")
                trial += 1
                selection = input('Password : ')

            if int(selection) == paswd:
                print("Tebrikler şifreyi dogru yazdın ve gizli çıkısı buldun")
                return 'bitis'
            else:
                print(dedent("""
                Parolayı bilemedin.
                10 uzaylı geldi ve osuruk partisi yaptılar.
                Kokudan zehirlenip ikiniz de öldünüz.
                """))
                return 'death'
        else:
            return 'giris2'

class AnaOda:

    def enter(self):
        print(dedent("""
        Ana odaya girdin. Odada 5 tane uzaylı var.
        Hepsi birden osurdular ve anında kanser olup öldün.
        """))
        return 'death'

# defining class called Giris
class Giris:

    def enter(self):
        print(dedent("""
        Karargahın girişine vardın.
        Bugün şanslı günündesin ve uzaylılar uyku molasında.
        İçeriye girdin ve karşına üç oda çıktı.
        Abuzittin'i kapattıkları odayı bulman gerekiyor.
        Üç odadan birini seç:
        1. Ana oda
        2. Köprü
        3. Kiler
        """))
        selection = input('> ')
        if int(selection) == 1:
            return 'anaoda'

        elif int(selection) == 2:
            return 'kopru'

        else:
            return 'kiler'


class Giris2:

    def enter(self):
        print(dedent("""
        Giriş'e geri geldin.
        Karşında 3 oda var.
        Uzaylılar iyice kıllanmadan hemen odayı bul.
        Üç odadan birini seç:
        1. Ana oda
        2. Köprü
        3. Kiler
        """))
        selection = input('> ')
        if int(selection) == 1:
            return 'anaoda'

        elif int(selection) == 2:
            print(dedent("""
            Köprü'ye tekrar girmeye çalışırken uzaylılar sizi yakaladı.
            3 uzaylı geldi üzerinize sıçtılar bokun altında kalıp ikinizde öldünüz...
            """))
            return 'death'

        else:
            return 'kiler2'


class Giris3:

    def enter(self):
        print(dedent("""
        Giriş'e geri geldin.
        Karşında 3 oda var.
        Abuzittin'i kapattıkları odayı bulman gerekiyor.
        Üç odadan birini seç:
        1. Ana oda
        2. Köprü
        3. Kiler
        """))
        selection = input('> ')
        if int(selection) == 1:
            return 'anaoda'

        elif int(selection) == 2:
            return 'kopru'

        else:
            return 'kiler'




class Bitis:

    def enter(self):
        print(dedent("""
        Tebrikler!.
        Görevi basarıyla tamamladın.
        Abuzittin'i kurtarıp dünyaya geri getirdin.
        Abuzittin başına gelenlerden sonra artık sadece
        koyundan yapıyor dönerleri.
        """))
        return 'bitis'


# class called Map
class Map:

    # rooms and main actions are stored
    scenes = {'giris' : Giris(),
              'giris2' : Giris2(),
              'giris3' : Giris3(),
              'anaoda' : AnaOda(),
              'kopru' : Kopru(),
              'kopru2' : Kopru2(),
              'kiler' : Kiler(),
              'kiler2' : Kiler2(),
              'death' : Death(),
              'tuvalet' : Tuvalet(),
              'hamam' : Hamam(),
              'bitis': Bitis()
              }
    def __init__(self, scene_name):
        self.scene_name = scene_name

    def simdiki_oda(self):
        return Map.scenes.get(self.scene_name)


# welcome message to the game
print(dedent("""
OSURAN UZAYLILAR'a hosgeldiniz\n\n
Gecenlerde sizin mahalleye 100 kadar uzayli gelmisti Marstan.
Bizim dönerci Abuzittin uzaylıların kaldiklari yeri keşfetmiş.
Uzaylıları yakalayıp, kesip dönerlere doldurup koyun eti diye kakalıyormuş.
Neyse, bunu ögrenen uzaylılar Mars'tan bir ekip yollayıp bizim Abuzittin'i
kaçırmışlar ve Mars'a götürmüşler.

Senin görevin Mars'a gidip Abuzittin'i kapattıkları
karargahtan onu kaçırıp dünyaya geri getirmek.

Sen de 50 milyon dolar ödülü duyar duymaz
vakit kaybetmeden galeriden aldın bir uzay gemisi
yardırdın Mars'a
"""))

room_map = Map('giris')

while True:
    sonraki_oda = room_map.simdiki_oda().enter()
    room_map = Map(sonraki_oda)
    if sonraki_oda == 'bitis':
        sonraki_oda = room_map.simdiki_oda().enter()
        break
