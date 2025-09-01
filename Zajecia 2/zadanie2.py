# Zadanie 1
class Ksiazka:
    def __init__(self, tytul: str, autor: str, rok_wydania: int):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = int(rok_wydania)
    
    def opis(self) -> str:
        return f"\"{self.tytul}\" — {self.autor} ({self.rok_wydania})"


class Ebook(Ksiazka):
    def __init__(self, tytul: str, autor: str, rok_wydania: int, rozmiar_pliku_mb: float):
        super().__init__(tytul, autor, rok_wydania)
        self.rozmiar_pliku_mb = float(rozmiar_pliku_mb)
    
    def opis(self) -> str:
        base = super().opis()
        return f"{base} [E-book, rozmiar: {self.rozmiar_pliku_mb:.1f} MB]"


class Audiobook(Ksiazka):
    def __init__(self, tytul: str, autor: str, rok_wydania: int, czas_trwania_min: int):
        super().__init__(tytul, autor, rok_wydania)
        self.czas_trwania_min = int(czas_trwania_min)
    
    def opis(self) -> str:
        base = super().opis()
        godz = self.czas_trwania_min // 60
        minuty = self.czas_trwania_min % 60
        czas_str = f"{godz}h {minuty}min" if godz else f"{minuty}min"
        return f"{base} [Audiobook, długość: {czas_str}]"


# Testy Zadanie 1
ebook1 = Ebook("Rok 1984", "George Orwell", 1949, 1.7)
ebook2 = Ebook("Mały Książę", "Antoine de Saint-Exupéry", 1943, 0.9)
audiobook1 = Audiobook("Duma i uprzedzenie", "Jane Austen", 1813, 720)  # 12 godzin

print("=== Zadanie 1: opisy książek ===")
print(ebook1.opis())
print(ebook2.opis())
print(audiobook1.opis())
print()


# Zadanie 2
class UserNotFoundError(Exception):
    def __init__(self, username):
        self.username = username
    def __str__(self):
        return f"Użytkownik '{self.username}' nie istnieje w systemie."


class WrongPasswordError(Exception):
    def __init__(self, username):
        self.username = username
    def __str__(self):
        return f"Niepoprawne hasło dla użytkownika '{self.username}'."


class UserAuth:
    def __init__(self, users: dict):
        self.users = dict(users)
    
    def login(self, username: str, password: str) -> bool:
        if username not in self.users:
            raise UserNotFoundError(username)
        if self.users[username] != password:
            raise WrongPasswordError(username)
        print(f"Logowanie powiodło się: {username}")
        return True


# Testy Zadanie 2
auth = UserAuth({"admin": "1234", "user": "abcd"})

print("=== Zadanie 2: test logowania (przykład z treści) ===")
try:
    auth.login("admin", "1234")      
    auth.login("unknown", "pass")    
    auth.login("user", "wrongpass")  
except Exception as e:
    print(f"Błąd: {e}")

print()
print("=== Zadanie 2: pokazanie obydwu wyjątków osobno ===")

try:
    auth.login("nieistnieje", "x")
except UserNotFoundError as e:
    print("Przechwycono UserNotFoundError:", e)
except WrongPasswordError as e:
    print("Przechwycono WrongPasswordError (nieoczekiwane):", e)

try:
    auth.login("user", "zlehaslo")
except UserNotFoundError as e:
    print("Przechwycono UserNotFoundError (nieoczekiwane):", e)
except WrongPasswordError as e:
    print("Przechwycono WrongPasswordError:", e)

print()
print("=== Koniec testów ===")
