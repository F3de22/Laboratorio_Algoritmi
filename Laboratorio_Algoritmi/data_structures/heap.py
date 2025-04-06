import math
class Heap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return math.trunc(index/2)

    def right_child(self,index):
        return 2*index + 1

    def left_child(self,index):
        return 2*index

    def insert(self, key):
        #Inserisce la chiave nello heap
        self.heap.append(float('-inf'))
        self.increase_key(len(self.heap) - 1, key)

    def max_heapify(self, index):
        #Mantiene la proprietà del max-heap spostando verso il basso il nodo
        left = self.left_child(index)
        right = self.right_child(index)
        largest = index

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.max_heapify(largest)

    def extract_max(self):
        #Rimuove e restituisce il massimo ( cioè la radice del Max-Heap)
        if len(self.heap) < 1:
            raise IndexError("Underflow dell'heap")
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.max_heapify(0)
        return max_value

    def increase_key(self, index, new_value):
        #Aumenta la chiave di un nodo e ripristina l'ordine del max-heap
        if new_value < self.heap[index]:
            raise ValueError("la nuova chiave deve essere maggiore o uguale a quella corrente")

        self.heap[index] = new_value
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    def maximum(self):
        return self.heap[0]