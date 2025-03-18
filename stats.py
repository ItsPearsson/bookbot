def get_book_text(book):
    with open(book) as f:
        return f.read()

def get_num_words(book_path):
    num_words = 0
    for i in get_book_text(book_path).split():
        num_words += 1
    return num_words

def get_characters(book_path):
    total_characters = {}
    for i in get_book_text(book_path).lower():
        if i in total_characters:
            total_characters[i] += 1
        else:
            total_characters[i] = 1
    return total_characters

def sort_characters(book_path):
    total_characters = get_characters(book_path)
    sorted_characters = sorted(total_characters.items(), key=lambda x: x[1], reverse=True)
    return sorted_characters
        