from collections import Counter

def two_sum(filename):
    # Lire et compter les occurrences de chaque nombre
    num_count = Counter()
    with open(filename, 'r') as f:
        for line in f:
            num_count[int(line.strip())] += 1

    targets = set()
    nums = sorted(num_count.keys())
    n = len(nums)

    # Paires distinctes (i < j)
    for i in range(n):
        x = nums[i]
        for j in range(i + 1, n):
            y = nums[j]
            s = x + y
            if -10000 <= s <= 10000:
                targets.add(s)
    
    # Cas où x == y (besoin de 2 occurrences)
    for x in nums:
        if num_count[x] >= 2:
            s = 2 * x
            if -10000 <= s <= 10000:
                targets.add(s)

    return len(targets)


if __name__ == "__main__":
    filename = r"C:\Users\USER\Documents\cours\formation_train\two_sum.txt" # ← ton fichier ici
    result = two_sum(filename)
    print("Résultat :", result)