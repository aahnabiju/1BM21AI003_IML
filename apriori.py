from itertools import chain, combinations
from collections import defaultdict

def generate_candidates(itemsets, k):
    candidates = set()
    for itemset1 in itemsets:
        for itemset2 in itemsets:
            union_set = itemset1.union(itemset2)
            if len(union_set) == k:
                candidates.add(union_set)
    return candidates

def prune(itemsets, candidates):
    pruned_candidates = set()
    for candidate in candidates:
        subsets = list(combinations(candidate, len(candidate) - 1))
        if all(set(subset) in itemsets for subset in subsets):
            pruned_candidates.add(candidate)
    return pruned_candidates

def apriori(data, min_support):
    itemsets = [frozenset([item]) for item in set(chain(*data))]
    frequent_itemsets = []

    k = 2
    while itemsets:
        candidates = generate_candidates(itemsets, k)
        counts = defaultdict(int)
        for transaction in data:
            for candidate in candidates:
                if candidate.issubset(transaction):
                    counts[candidate] += 1

        frequent_itemsets.extend([itemset for itemset, count in counts.items() if count >= min_support])
        itemsets = prune(frequent_itemsets, generate_candidates(frequent_itemsets, k + 1))
        k += 1

    return frequent_itemsets

# Example usage:
data = [
    {'A', 'B', 'C'},
    {'A', 'C'},
    {'B', 'C'},
    {'A', 'B'},
    {'D'},
]

min_support = 2
result = apriori(data, min_support)
print("Frequent Itemsets:")
for itemset in result:
    print(f"{itemset}: {data.count(list(itemset))}")
