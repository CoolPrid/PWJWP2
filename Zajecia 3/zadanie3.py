
# Zadanie 1
class Asystent:
    def __init__(self, nazwa: str, wersja: str):
        self.nazwa = nazwa
        self.wersja = wersja

class AnalizaJezykowa:
    def analizuj_zapytanie(self, zapytanie: str) -> str:
        if "pogoda" in zapytanie.lower():
            return "pogoda"
        elif "czas" in zapytanie.lower():
            return "czas"
        else:
            return "ogólne"

class GeneratorOdpowiedzi:
    def generuj_odpowiedz(self, analiza: str) -> str:
        if analiza == "pogoda":
            return "Dziś jest słonecznie!"
        elif analiza == "czas":
            return "Aktualnie nie mam zegara, ale sprawdź na komputerze."
        else:
            return "Nie rozumiem, ale mogę się nauczyć!"

# Wersja z kompozycją:
class InteligentnyAsystent:
    def __init__(self, nazwa: str, wersja: str):
        self.asystent = Asystent(nazwa, wersja)
        self.analityk = AnalizaJezykowa()
        self.generator = GeneratorOdpowiedzi()

    def odpowiedz(self, zapytanie: str) -> str:
        analiza = self.analityk.analizuj_zapytanie(zapytanie)
        return self.generator.generuj_odpowiedz(analiza)


# Test
ia = InteligentnyAsystent("EwaBot", "1.0")
print(ia.odpowiedz("Jaka jest pogoda?"))
print(ia.odpowiedz("Która godzina?"))
print(ia.odpowiedz("Powiedz coś zabawnego!"))


# Zadanie 2
from typing import List

def average(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers) if numbers else 0.0

print(average([1.0, 2.0, 3.0]))


# Zadanie 3
from typing import Dict, Optional

class Library:
    def __init__(self):
        self.books: Dict[str, str] = {}

    def add_book(self, isbn: str, title: str) -> None:
        self.books[isbn] = title

    def find_book(self, isbn: str) -> Optional[str]:
        return self.books.get(isbn)

# Test
lib = Library()
lib.add_book("978-83-01", "Python dla początkujących")
print(lib.find_book("978-83-01"))   
print(lib.find_book("123-45"))      



# Zadanie 4
from typing import Generator

def fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Test
fib = fibonacci()
for _ in range(10):
    print(next(fib), end=" ")
print()

# Zadanie 5

class SimpleChatbot:
    def __init__(self, questions: List[str]):
        self.questions = questions
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.questions):
            q = self.questions[self.index]
            self.index += 1
            return q
        else:
            raise StopIteration

# Test
bot = SimpleChatbot(["Jak się nazywasz?", "Jaki jest Twój ulubiony kolor?"])
for question in bot:
    print(question)

