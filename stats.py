def get_num_words(content):
    return len(content.split())

def get_num_chars(content):
    normalized_content = content.lower()
    num_chars = len(normalized_content)

    chars_dict = {}

    for i in range(num_chars):
        char = normalized_content[i]

        if char not in chars_dict:
            chars_dict[char] = 0
            for j in range(i, num_chars):
                if char == normalized_content[j]:
                    chars_dict[char] += 1

    return chars_dict

def sort_on(items):
    return items["num"]

def sort_by_num(chars_dict):
    char_counts = []
    for key, value in chars_dict.items():
        char_counts.append(dict(char=key, num = value))

    char_counts.sort(reverse=True, key=sort_on)

    return char_counts
