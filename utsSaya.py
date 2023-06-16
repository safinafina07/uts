class ATM :
    def ___init___(self):
        self.no_rekening=int(input("masukkan no rekening anda"))
        self.username=int(input("masukkan usename anda"))

    def no_rekening(self):
        print(self.no_rekening,self.username)

    def username (self):
        print(self.username,self.no_rekening)
        option1=(input("masukkan nama"))
        objek = ATM()
        
        print("1.tarik tunai")
        print("2. setor tunai")
        option2=int(input("pilih option : "))
        uang_kamu=80000
        if option2==1:
            print("uang saya berjumlah Rp.800.000, mau ambil berapa?")
            print("1 Rp.100.000")
            print("2.Rp.200.000")
        option2=int(input("option : "))
        if option2==2:
            hasil=uang_kamu-100000
        print("uang kamu sekarang berjumlah ",hasil)
        elif option2==1
        hasil2=uang_kamu-200000
    print("uang kamu sekarang berjulah",hasil2)
    elif option2==2
    print("uang anda Rp.800.000")
else:
print("yang anda masukkan salah")
objek=atm()