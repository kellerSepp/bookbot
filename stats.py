def count_words(text):
    count = len(text.split())
    return count
def count_characters(text):
    count = {}
    for char in text:
        if char.lower() in count:
            count[char.lower()] += 1
        else:
            count[char.lower()] = 1
    return count