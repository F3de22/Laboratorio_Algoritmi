import time
import random
from data_structures.heap import Heap
from data_structures.linked_list import UnsortedLinkedList
from data_structures.sorted_linked_list import SortedLinkedList

def test_priority_queue(queue, name, num_elements=1000):
    """Testa l'inserimento, la ricerca del massimo e l'estrazione del massimo."""
    print(f"\n{name} - Test con {num_elements} elementi")

    # Genera numeri casuali da inserire
    values = [random.randint(1, 10000) for _ in range(num_elements)]

    # Test INSERT
    start = time.time()
    for v in values:
        queue.insert(v)
    insert_time = time.time() - start
    print(f"Inserimento completato in {insert_time:.6f} secondi")

    # Test MAXIMUM
    start = time.perf_counter()
    max_value = queue.maximum()
    max_time = time.perf_counter() - start
    print(f"Maximum: {max_value} trovato in {max_time:.6f} secondi")

    # Test EXTRACT_MAX
    start = time.time()
    while True:
        try:
            queue.extract_max()
        except IndexError:  # Heap vuoto
            break
    extract_time = time.time() - start
    print(f"Extract max completato in {extract_time:.6f} secondi")

    return insert_time, max_time, extract_time


def main():
    num_elements = 1000  # Numero di elementi da testare

    # Creazione delle tre strutture dati
    max_heap = Heap()
    unsorted_list = UnsortedLinkedList()
    sorted_list = SortedLinkedList()

    # Test e confronto delle performance
    results = []
    results.append(test_priority_queue(max_heap, "Max-Heap", num_elements))
    results.append(test_priority_queue(unsorted_list, "Lista Concatenata Non Ordinata", num_elements))
    results.append(test_priority_queue(sorted_list, "Lista Concatenata Ordinata", num_elements))

    print("\n📊 Confronto Tempi (in secondi)")
    print(f"{'Struttura':<35}{'Insert':<15}{'Max':<15}{'Extract Max'}")
    structures = ["Max-Heap", "Lista Concatenata Non Ordinata", "Lista Concatenata Ordinata"]
    for i, (insert_t, max_t, extract_t) in enumerate(results):
        print(f"{structures[i]:<35}{insert_t:<15.6f}{max_t:<15.6f}{extract_t:.6f}")


if __name__ == '__main__':
    main()
