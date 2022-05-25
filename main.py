import requests


def write_data(data):
    with open("text.txt", "w") as file:
        file.write(data)


def get_json_data(url):
    return requests.get(url).json()


def format_sentence(text):
    text = text.capitalize()
    if text.endswith('.'):
        return text
    return '{}.'.format(text)


def main():
    url_name = "https://jsonplaceholder.typicode.com/posts"
    data_request = get_json_data(url_name)
    text = ""
    for i in data_request:
        text += format_sentence(i['title']) + "\n"
        text += format_sentence(i['body']) + "\n"
        text += "\n"
    write_data(text)


if __name__ == '__main__':
    main()
