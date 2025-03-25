import node

class SortedLinkedList:
    #Coda di priorità con lista concatenata ordinata

    def __init__(self):
        self.head = None

    def insert(self, value):
        #Inserisce un elemento mantenendo la lista ordinata
        new_node = node.Node(value)

        if not self.head or value > self.head.value:  # Inserimento in testa
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.value > value:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def maximum(self):
        #Restituisce il massimo, cioè sempre il primo nodo
        if not self.head:
            raise IndexError("Heap vuoto")
        return self.head.value

    def extract_max(self):
        #Estrae e restituisce il massimo
        if not self.head:
            raise IndexError("Heap vuoto")

        max_value = self.head.value
        self.head = self.head.next  # Rimuove il primo nodo
        return max_value
