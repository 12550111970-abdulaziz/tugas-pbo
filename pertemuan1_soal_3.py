class User:
    def __init__(self, nama_depan, nama_belakang, umur, email, kota):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.umur = umur
        self.email = email
        self.kota = kota

    def deskripsikan_user(self):
        print("Nama Lengkap :", self.nama_depan, self.nama_belakang)
        print("Umur :", self.umur)
        print("Email :", self.email)
        print("Kota :", self.kota)

    def sapa_user(self):
        print("Halo", self.nama_depan + ", selamat datang!\n")

user1 = User("abdul", "aziz", 19, "abdaziz20@email.com", "Pekanbaru")
user2 = User("nabila", "amelia", 18, "nbllamelia@email.com", "Medan")
user3 = User("ahmad", "yoga", 21, "ahmdyoga@email.com", "pasir pengaraian")

user1.deskripsikan_user()
user1.sapa_user()

user2.deskripsikan_user()
user2.sapa_user()

user3.deskripsikan_user()
user3.sapa_user()