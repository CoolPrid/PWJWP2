import json

class AplikacjaMobilna:
    liczba_pobran = 0

    def __init__(self, nazwa: str, wersja: str):
        self.nazwa = nazwa
        self.wersja = wersja

    def nowe_pobranie(self, ile: int = 1):
        if not isinstance(ile, int) or ile < 1:
            raise ValueError("Argument 'ile' musi być dodatnią liczbą całkowitą.")
        AplikacjaMobilna.liczba_pobran += ile

    @classmethod
    def ile_pobran(cls):
        return cls.liczba_pobran

    @classmethod
    def z_json(cls, nazwa_pliku: str):
        with open(nazwa_pliku, "r", encoding="utf-8") as f:
            dane = json.load(f)
        nazwa = dane.get("nazwa")
        wersja = dane.get("wersja")
        if nazwa is None or wersja is None:
            raise ValueError("Plik JSON musi zawierać pola 'nazwa' i 'wersja'.")
        return cls(nazwa, wersja)

    def __repr__(self):
        return f"AplikacjaMobilna(nazwa={self.nazwa!r}, wersja={self.wersja!r})"

    def __str__(self):
        return f"{self.nazwa} v{self.wersja}"


class Matrix:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        return Matrix(self.a + other.a, self.b + other.b,
                      self.c + other.c, self.d + other.d)

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        e, f, g, h = other.a, other.b, other.c, other.d
        m11 = self.a * e + self.b * g
        m12 = self.a * f + self.b * h
        m21 = self.c * e + self.d * g
        m22 = self.c * f + self.d * h
        return Matrix(m11, m12, m21, m22)

    def __str__(self):
        return f"[{self.a}, {self.b};\n {self.c}, {self.d}]"

    def __repr__(self):
        return f"Matrix({self.a}, {self.b}, {self.c}, {self.d})"


class Student:
    def __init__(self, name: str, score: float):
        self.name = name
        self.score = score

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.score == other.score

    def __ne__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.score != other.score

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.score < other.score

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.score > other.score

    def __str__(self):
        return f"{self.name}: {self.score}"

    def __repr__(self):
        return f"Student({self.name!r}, {self.score!r})"
