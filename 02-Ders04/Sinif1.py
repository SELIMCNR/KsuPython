class person:
    def __init__(self, adi, soyadi):  # kurucu fonksiyon self personu temsil eder
        self.adi = adi  # person sınıfının üyeleri yazılır
        self.soyadi = soyadi

    def ekranaYaz(self):  # Sınıf metodu
        print("Merhaba"+self.adi+self.soyadi)  # Sınıf metodu yazdırma komutu
