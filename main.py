class Film:
    def __init__(self, nom):
        self.nom = nom


class Kino:
    def __init__(self):
        self.filmlar = []

    def add_movie(self, movie):
        self.filmlar.append(movie.nom)

    def info(self):
        print(self.filmlar)


f1 = Film("Titanic")
f2 = Film("Avatar")

k1 = Kino()
k1.add_movie(f1)
k1.add_movie(f2)
k1.info()
