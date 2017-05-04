
def is_unique(string):
    """Determines if a string has all unique characters"""

    list_of_chars = []
    set_of_chars = set()

    for char in string:

        if char != ' ':

            list_of_chars.append(char)
            set_of_chars.update(char)

    if len(list_of_chars) != len(set_of_chars):
        return False

    else:
        return True


def is_unique_include_spaces(string):
    """Determines if a string has all unique characters including spaces"""

    set_of_chars = set()

    for char in string:

        set_of_chars.update(char)

    if len(string) != len(set_of_chars):
        return False

    else:
        return True


print is_unique("this shouldn't work")

print is_unique("I work!")

print is_unique_include_spaces("this shouldn't work")

print is_unique_include_spaces("I work!")
