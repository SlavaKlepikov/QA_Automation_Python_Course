def read_file(file_path):
    try:
        with open(file_path) as file:
            return file.read()
    except FileNotFoundError as e:
        print(f"File example.txt not found.")
        exit()


def clean_text(data):
    return data.replace(".", "").replace(",", "").replace("!", "").replace("\n", " ")


def get_words_list(data):
    return [word for word in data.split()]


def get_max_freq_word(words_list):
    count_max = 0
    max_word = None
    for item in words_list:
        count = words_list.count(item)
        if count_max < count:
            count_max = count
            max_word = item
    return {"max_word": max_word, "count_max": count_max}


def get_min_freq_word(words_list):
    count_min = None
    min_word = None
    for item in words_list:
        count = words_list.count(item)
        if not count_min:
            count_min = count
            min_word = item
        elif count_min > count:
            count_min = count
            min_word = item
    return {"min_word": min_word, "count_min": count_min}


def write_list(path, list_data):
    try:
        with open(path, "x") as file:
            for element in list_data:
                file.write(element + "\n")
    except FileExistsError as e:
        print(f"File {path} already exist.")


def divide_text(s):
    chunks = s.split()
    words = 10
    return [" ".join(chunks[i:i + words]) for i in range(0, len(chunks), words)]


def main():
    file_path = input("Enter the file path: \n")
    text_data = read_file(file_path)
    words_list = get_words_list(clean_text(text_data))
    max_word = get_max_freq_word(words_list)
    min_word = get_min_freq_word(words_list)
    print(f"One of the most frequently occurring words: {max_word['max_word']}; frequency: {max_word['count_max']}")
    print(f"One of the less frequently occurring words: {min_word['min_word']}; frequency: {min_word['count_min']}")
    file_path_write = input("Enter the file path: \n")
    text_write = text_data.replace(max_word['max_word'], min_word['min_word'])
    text_list = divide_text(text_write)
    write_list(file_path_write, text_list)


if __name__ == "__main__":
    """
    Эта конструкция гарантирует что файл будет исполнен только когда запущен на прямую
    """
    main()
