# Anagram finder - by will shears
from collections import Counter
with open('anagram.txt') as f:
    # Opening the text file and converting it to a list
    lines = f.readlines()
def anagramfinder(lines):
    split_lines = lines[0].split()
    results = []
    for split_line in split_lines:
        # Using counter to search for all anagrams for a word and append them to a new results list
        result = list(filter(lambda x: (Counter(split_line) == Counter(x)), split_lines))
        # Because the above function still includes the original word (split_line), I remove that.
        result.remove(split_line)
        results.extend(result)
    solved = {}
    # Removing duplicates that have been solved twice but retaining the order with setdefault
    anagrams = [solved.setdefault(r, r) for r in results if r not in solved]
    if anagrams:
        # Removing [',] from the print
        print(' '.join(map(str, anagrams)))
    else:
        print("no anagrams found")
anagramfinder(lines)


