import heapq
import sys

def median_maintenance(median):
    max_heap = []  # moitié inférieure (valeurs négatives pour simuler max-heap)
    min_heap = []  # moitié supérieure
    median_sum = 0

    with open(median, 'r') as f:
        for line in f:
            x = int(line.strip())

            # Insertion
            if not max_heap or x <= -max_heap[0]:
                heapq.heappush(max_heap, -x)
            else:
                heapq.heappush(min_heap, x)

            # Rééquilibrage
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

            # La médiane est toujours la racine du max_heap
            median_sum += -max_heap[0]

    return median_sum % 10000

if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "median.txt"
    result = median_maintenance(filename)
    print(f"Résultat (somme des médianes mod 10000) = {result}")
