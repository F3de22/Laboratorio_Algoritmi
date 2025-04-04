import node

class UnsortedLinkedList:
    #Coda di priorità con lista concatenata non ordinata
    def __init__(self):
        self.head = None

    def insert(self, value):
        #Inserisce un elemento in testa
        new_node = node.Node(value)
        new_node.next = self.head
        self.head = new_node
        return new_node

    def maximum(self):
        #Restituisce il massimo
        if not self.head:
            raise IndexError("Heap vuoto")

        max_value = self.head.value
        current = self.head.next
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value

    def extract_max(self):
        #Estrae e restituisce il massimo
        if not self.head:
            raise IndexError("Heap vuoto")

        max_value = self.head.value
        max_node = self.head
        prev_max = None

        prev = None
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
                prev_max = prev
                max_node = current
            prev = current
            current = current.next

        # Rimuove il nodo massimo dalla lista
        if prev_max:
            prev_max.next = max_node.next
        else:
            self.head = max_node.next  # Se il massimo è in testa

        return max_value

    def increase_key(self, node, new_key):
        #Aumenta la chiave di un nodo solo se maggiore del valore attuale.
        if new_key < node.key:
            raise ValueError("Nuova chiave più piccola di quella corrente")
        node.value = new_key