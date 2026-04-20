import random


class Students:
    def __init__(self, scores):
        self.scores = scores

        # self._sorted_scores = None  # zatím nic neseřazené

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

    # --- ÚKOL: Seřazení výsledků ---
    def get_sorted(self):

        return sorted(self.scores, reverse=True)

# def find_sorted(self, score):
#
#     if self._sorted_scores is None:
#
#         self._sorted_scores = self.get_sorted()




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





if __name__ == "__main__":
    main()
