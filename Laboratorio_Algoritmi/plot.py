import matplotlib.pyplot as plt

# Dati
x = [1000, 5000, 10000, 20000]

heap = [0.000012 , 0.000017, 0.000020, 0.000025]
unsorted = [0.000037, 0.00024, 0.00041 , 0.0011]
sorted = [0.000001, 0.000002, 0.000002, 0.000002]

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x, heap, marker='o', label='Max-Heap')
plt.plot(x, unsorted, marker='s', label='Coda Non Ordinata')
plt.plot(x, sorted, marker='^', label='Coda Ordinata')

plt.xlabel('Numero di elementi')
plt.ylabel('Tempo medio (s)')
plt.title('Tempi medi EXTRACT-MAX')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('grafico_EXTRACTMAX.png')
plt.show()
