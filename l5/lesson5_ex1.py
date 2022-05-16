try:
    with open('example.txt') as file:
        text = file.read()
except FileNotFoundError as e:
    print(f"File example.txt not found.")
    exit()
words_list = [word.strip('.,!') for word in text.split()]
count_max = 0
count_min = None
for item in words_list:
    count = words_list.count(item)
    if count_max < count:
        count_max = count
        max_word = item
    if not count_min:
        count_min = count
        min_word = item
    elif count_min > count:
        count_min = count
        min_word = item
print(f"One of the most frequently occurring words: {max_word}; frequency: {count_max}")
print(f"One of the less frequently occurring words: {min_word}; frequency: {count_min}")
try:
    with open('spam.txt', "x") as file:
        file.write(text.replace(max_word, min_word))
except FileExistsError as e:
    print(f"File spam.txt already exist.")
