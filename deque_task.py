from collections import deque


def check_palindrome(input_string: str):
    normalized_string = input_string.casefold()

    char_deque = deque()

    for ch in normalized_string:
        char_deque.append(ch)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


for word in ["Radar", "hello", "level", "saaS"]:
    print(f"{word}: {check_palindrome(word)}")
