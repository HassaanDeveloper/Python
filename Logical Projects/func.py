def remove(lIst, word):
    n = []
    for item in lIst:
        if item != word:
            n.append(item.strip(word))
    return n

lIst = ["Hassaan", "Affan", "Gufran", "Burhan", "an"]
print(remove(lIst, "an"))