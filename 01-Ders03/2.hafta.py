# fonksiyon arg kullanım


def fn(*arg):
    result = 0
    for x in arg:
        return result


a = fn(1, 2, 3, 4, 5, 6, 7, 8, 9)
print("sonuc: ", a)


# class
class c1:
    notu = 4
    adi = "Ahmet"
    soyadi = "Çınar"
    yasi = 24


n1 = c1()
n2 = c1()

n1.adi = "Yeni ad"
print(n1.adi)
print(n2.adi)

# class 2.Örnek


class Person:
    def __init__(self, adi, yas):  # Kurucu fonksiyon
        self.name = adi
        self.age = yas

    def ekrana_yaz(self):
        print("Merhaba"+self.name+"" + str(self.age) + "yasındasınız")


p1 = Person("Selim Bey", 22)

print(p1.name)
print(p1.age)  # classtaki özelik yazdırıldı
print(p1.ekrana_yaz())  # classtaki metod yazdırıldı
