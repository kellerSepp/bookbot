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

def sort_on(items):
    return items["num"]

def sort_dictionary_as_list(dictionary):
    sorted_list = []
    for char in dictionary:
        sorted_list.append({"char":char,"num":dictionary[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list