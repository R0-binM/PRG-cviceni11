import random


class Students:
    def __init__(self, scores):
        self.scores = scores

        # Nový atribut pro cache (podtržítko značí, že je to vnitřní proměnná)
        self._sorted_scores = None  # zatím nic neseřazené


    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    # --- ÚKOL: Zjištění známky ---
    def get_grade(self, index):


        points = self.get_by_index(index)

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

        for i, score in enumerate(self.scores):

            if score == points:
                found_indices.append(i)


        return found_indices

    def get_sorted(self):
        # Zde potřebujeme vzestupné řazení pro standardní binární hledání
        return sorted(self.scores)

    # --- ÚKOL: Seřazení výsledků ---
    # def get_sorted(self):
    #   return sorted(self.scores, reverse=True)


    # --- BONUSOVÝ ÚKOL ---
    def find_sorted(self, score):
        # 1. Kontrola cache: Pokud je prázdná, seřadíme a zapamatujeme si to
        if self._sorted_scores is None:
            print("sorting_")  # Tento text vyskočí jen při prvním zavolání!
            self._sorted_scores = self.get_sorted()

        # 2. Binární vyhledávání (používáme už naši cache: self._sorted_scores)
        left = 0
        right = len(self._sorted_scores) - 1

        while left <= right:
            mid = (left + right) // 2

            if self._sorted_scores[mid] == score:
                return mid  # Našli jsme, vracíme index v seřazeném poli
            elif self._sorted_scores[mid] < score:
                left = mid + 1  # Jdeme doprava
            else:
                right = mid - 1  # Jdeme doleva

        # Pokud cyklus skončí a nic nenajde
        return None



def main():

    results = Students([50, 85, 70, 70, 91, 20, 70, 100, 100, 100])


    print(f"Známka studenta na indexu 0: {results.get_grade(0)}")
    print("-" * 30)


    for i in range(results.count()):

        points = results.get_by_index(i)
        grade = results.get_grade(i)

        print(f"Student {i}: {points} bodů = {grade}")

    print("-" * 30)


    print(f"Indexy studentů se 100 body: {results.find(100)}")


    # Výpis seřazených výsledků od nejlepšího
    print(f"Seřazené výsledky: {results.get_sorted()}")
    print("-" * 30)


    # Demonstrace, že get_sorted() nemění původní seznam (pomocí shuffle)
    random.shuffle(results.scores)
    print("Seznam byl náhodně zamíchán.")
    print(f"Zamíchané pole (vnitřní stav): {results.scores}")
    print(f"Seřazený výstup metodou get_sorted(): {results.get_sorted()}")


    # --- BONUSOVÝ ÚKOL ---

    # První hledání - cache je prázdná, takže se vypíše "sorting_" a pole se seřadí
    print(results.find_sorted(91))

    # Druhé hledání - cache už je plná! "sorting_" se NEvypíše, hledá se okamžitě
    print(results.find_sorted(50))

    # Třetí hledání - opět se použije cache
    print(results.find_sorted(77))


if __name__ == "__main__":
    main()
