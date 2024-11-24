with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    count = 0
    for n in file_contents.split():
        count += 1

def count_characters(text):
    lowered = text.lower()
    number = {}
    for letter in lowered:
        if letter not in number:
            number[letter] = 1
        elif letter in number:
            number[letter] += 1
    return number
    
def suerton(diccion):
    caccio = 0
    for i in diccion:
        caccio += diccion[i]
    return caccio
def report(letter_count):
    lister = []
    for i in letter_count:
        sdict = {}
        sdict[i] = letter_count[i]
        if i.isalpha():
            lister.append(sdict)
    lister.sort( reverse=True, key=suerton)
    return lister

def nice_report(path, word_num, lett_num):
    message = ""
    print(f"--- Begin report of {path} ---")
    print(f"{word_num} words found in the document")
    for i in lett_num:
        for l in i:
            print(f"The {l} character was found {i[l]} times")
    print("--- End Report ---")

nice_report("books/frankenstein.txt", count, report(count_characters(file_contents)) )
