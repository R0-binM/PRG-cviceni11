import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


# random.seed(42)
#
# values = random_numbers(10)  # 10 čísel v rozsahu 0–100
# print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
#
# small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20


def selection_sort(values):
    # Vytvoření kopie, aby původní seznam zůstal beze změny

    sorted_values = values[:]

    for pos_save in range(len(sorted_values)):
        min_idx = pos_save

        # Hledání indexu nejmenšího prvku ve zbytku seznamu

        for pos_open in range(pos_save + 1, len(sorted_values)):

            if sorted_values[pos_open] < sorted_values[min_idx]:
                min_idx = pos_open

        # PROHOZENÍ (Swap) prvků bez použití pomocné proměnné
        sorted_values[pos_save], sorted_values[min_idx] = sorted_values[min_idx], sorted_values[pos_save]

    # Vrácení nového seřazeného seznamu
    return sorted_values


def bubble_sort(values):

    # Vytvoření kopie seznamu (aby původní zůstal nezměněn)
    sorted_values = values[:]
    n = len(sorted_values)

    # Zapnutí interaktivního módu pro vizualizaci
    plt.ion()
    plt.show()

    for i in range(n):
        swapped = False  # Proměnná pro optimalizaci nejlepšího scénáře

        # Nápověda z 2.1: Neprocházíme už seřazený konec seznamu (n - i - 1)
        for j in range(n - i - 1):

            # --- BLOK VIZUALIZACE ---
            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(sorted_values)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(sorted_values)), sorted_values, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)  # Tímto řídíš rychlost animace
            # ------------------------

            # Samotné porovnání a prohození prvků
            if sorted_values[j] > sorted_values[j + 1]:
                sorted_values[j], sorted_values[j + 1] = sorted_values[j + 1], sorted_values[j]
                swapped = True

        # Optimalizace: Pokud v celém průchodu nedošlo k žádnému prohození,
        # seznam je už seřazený a můžeme skončit dřív.
        if not swapped:
            break

    # Ukončení interaktivního módu po seřazení
    plt.ioff()
    plt.show()

    return sorted_values


def main():

    random.seed(42)

    kratky_seznam = [5, 1, 4, 2, 8]
    print(f"Původní krátký: {kratky_seznam}")
    print(f"Seřazený krátký: {selection_sort(kratky_seznam)}")

    # 20 náhodných čísel
    nahodny_seznam = random_numbers(20)
    print(f"\nPůvodní náhodný: {nahodny_seznam}")
    print(f"Seřazený náhodný: {selection_sort(nahodny_seznam)}")


    print("--- Testování Bubble Sort ---")

    kratky_seznam = [5, 1, 4, 2, 8]

    print(f"Původní krátký: {kratky_seznam}")

    print(f"Seřazený krátký: {bubble_sort(kratky_seznam)}")


    nahodny_seznam = random_numbers(15)

    print(f"\nPůvodní náhodný: {nahodny_seznam}")
    print(f"Seřazený náhodný: {bubble_sort(nahodny_seznam)}")

# Spouštěcí blok
if __name__ == "__main__":
    main()

