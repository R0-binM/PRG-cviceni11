import random


class Students:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    # --- ÚKOL: Zjištění známky ---
    def get_grade(self, index):
        # Využijeme již existující metodu pro získání bodů
        points = self.get_by_index(index)

        # Otestujeme body podle tabulky
        if points >= 90:
            return 'A'
        elif points >= 80:
            return 'B'
        elif points >= 70:
            return 'C'
        elif points >= 60:
            return 'D'
        elif points >= 50:
            return 'E'
        else:
            return 'F'

    # --- ÚKOL: Vyhledávání studentů s konkrétním počtem bodů ---
    def find(self, points):
        found_indices = []
        # enumerate nám v každém kroku cyklu dá jak index (i), tak samotnou hodnotu (score)
        for i, score in enumerate(self.scores):
            if score == points:
                found_indices.append(i)
        return found_indices

    # --- ÚKOL: Seřazení výsledků ---
    def get_sorted(self):
        # Funkce sorted() vytvoří novou kopii seznamu. 
        # parametr reverse=True zajistí sestupné řazení (od největšího)
        return sorted(self.scores, reverse=True)


def main():
    # 1. Vytvoření objektu (instance)
    results = Students([50, 85, 70, 70, 91, 20, 70, 100, 100, 100])

    # 2. Výpis známky studenta na nultém indexu
    print(f"Známka studenta na indexu 0: {results.get_grade(0)}")
    print("-" * 30)

    # 3. Výpis všech studentů ve formátu: Student X: Y bodů = Z
    for i in range(results.count()):
        points = results.get_by_index(i)
        grade = results.get_grade(i)
        print(f"Student {i}: {points} bodů = {grade}")
    print("-" * 30)

    # 4. Nalezení a výpis indexů studentů se 100 body
    print(f"Indexy studentů se 100 body: {results.find(100)}")

    # 5. Výpis seřazených výsledků od nejlepšího
    print(f"Seřazené výsledky: {results.get_sorted()}")
    print("-" * 30)

    # 6. Demonstrace, že get_sorted() nemění původní seznam (pomocí shuffle)
    random.shuffle(results.scores)
    print("Seznam byl náhodně zamíchán.")
    print(f"Zamíchané pole (vnitřní stav): {results.scores}")
    print(f"Seřazený výstup metodou get_sorted(): {results.get_sorted()}")



if __name__ == "__main__":
    main()