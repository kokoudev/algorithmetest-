import sys
import threading
sys.setrecursionlimit(10**7)

def main():
    # Charger le fichier
    filename = "ressourceexo_m1.txt"  # remplace par ton fichier
    graph = {}
    reverse_graph = {}

    print("Chargement du graphe...")

    with open(filename, "r") as f:
        for line in f:
            u, v = map(int, line.split())

            # graphe normal
            if u not in graph:
                graph[u] = []
            graph[u].append(v)

            # graphe inversé
            if v not in reverse_graph:
                reverse_graph[v] = []
            reverse_graph[v].append(u)

    # Ajouter les sommets manquants
    all_nodes = set(graph.keys()).union(set(reverse_graph.keys()))

    for node in all_nodes:
        graph.setdefault(node, [])
        reverse_graph.setdefault(node, [])

    print("Nombre de sommets :", len(all_nodes))

    # -------- 1er DFS (ordre de fin) --------
    visited = set()
    order = []

    def dfs_reverse(node):
        stack = [node]
        while stack:
            n = stack[-1]
            if n not in visited:
                visited.add(n)
                for neigh in reverse_graph[n]:
                    if neigh not in visited:
                        stack.append(neigh)
            else:
                stack.pop()
                if n not in order:
                    order.append(n)

    print("DFS sur graphe inversé...")

    for node in all_nodes:
        if node not in visited:
            dfs_reverse(node)

    # -------- 2ème DFS (calcul SCC) --------
    visited.clear()
    scc_sizes = []

    def dfs(node):
        stack = [node]
        size = 0
        while stack:
            n = stack.pop()
            if n not in visited:
                visited.add(n)
                size += 1
                for neigh in graph[n]:
                    if neigh not in visited:
                        stack.append(neigh)
        return size

    print("DFS sur graphe normal...")

    for node in reversed(order):
        if node not in visited:
            scc_sizes.append(dfs(node))

    # Trier et prendre les 5 plus grandes
    scc_sizes.sort(reverse=True)
    top5 = scc_sizes[:5]

    # Compléter avec des 0 si besoin
    while len(top5) < 5:
        top5.append(0)

    # Affichage format demandé
    result = ",".join(map(str, top5))
    print("Résultat :", result)


# Lancer en thread (évite bug récursion)
threading.Thread(target=main).start()