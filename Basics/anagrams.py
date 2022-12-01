def group_anagrams(words: list[str]):
    hashmap = {}
    for char in words:
        sorted_char = "".join(sorted(char))
        if sorted_char not in hashmap:
            hashmap[sorted_char] = []
        if sorted_char in hashmap:
            hashmap[sorted_char].append(char)
    print(hashmap.values())


words = ["tea", "eat", "bat", "ate", "arc", "car"]
group_anagrams(words)
