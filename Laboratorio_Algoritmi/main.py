import time
import random
from data_structures.heap import Heap
from data_structures.linked_list import UnsortedLinkedList
from data_structures.sorted_linked_list import SortedLinkedList

def test_priority_queue(queue, name, num_elements):
    """Testa insert, maximum, extract_max e increase_key."""
    print(f"\n{name} - Test con {num_elements} elementi")

    values = [random.randint(1, 10000) for _ in range(num_elements)]

    # Test INSERT
    start = time.perf_counter()
    nodes = [queue.insert(v) for v in values]
    insert_time = time.perf_counter() - start
    print(f"Inserimento completato in {insert_time:.5f} secondi")

    # Test MAXIMUM
    start = time.perf_counter()
    max_value = queue.maximum()
    max_time = time.perf_counter() - start
    print(f"Maximum: {max_value} trovato in {max_time:.8f} secondi")

    # Test INCREASE_KEY
    increase_time = 0.0
    if isinstance(queue, Heap):
        if queue.heap:
            index = len(queue.heap) // 2  # Scegliamo un indice a metà
            new_value = queue.heap[index] + 1000  # Aumentiamo il valore
            start = time.perf_counter()
            queue.increase_key(index, new_value)
            increase_time = time.perf_counter() - start
            print(f"Increase key completato in {increase_time:.7f} secondi")
    elif isinstance(queue, (UnsortedLinkedList, SortedLinkedList)):
        if nodes:
            node = nodes[len(nodes) // 2]  # Scegliamo un nodo a metà lista
            new_value = node.value + 1000  # Aumentiamo il valore
            start = time.perf_counter()
            queue.increase_key(node, new_value)
            increase_time = time.perf_counter() - start
            print(f"Increase key completato in {increase_time:.7f} secondi")

    # Test EXTRACT_MAX
    start = time.perf_counter()
    try:
        queue.extract_max()
    except IndexError:
        pass  # struttura vuota, non faccio nulla
    extract_time = time.perf_counter() - start
    print(f"Extract max completato in {extract_time:.6f} secondi")

    return insert_time, max_time, extract_time, increase_time



def main():
    num_elements = 10000  # Numero di elementi da testare

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
    print(f"{'Struttura':<35}{'Insert':<15}{'Max':<15}{'Extract Max':<15}{'Increase Key'}")
    structures = ["Max-Heap", "Lista Concatenata Non Ordinata", "Lista Concatenata Ordinata"]
    for i, (insert_t, max_t, extract_t, increase_t) in enumerate(results):
        print(f"{structures[i]:<35}{insert_t:<15.6f}{max_t:<15.7f}{extract_t:<15.6f}{increase_t:.7f}")


if __name__ == '__main__':
    main()
