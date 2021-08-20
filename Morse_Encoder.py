def convert_to_morse(code):
    code = code.replace("1", ".----")
    code = code.replace("2", "..---")
    code = code.replace("3", "...--")
    return code


lock_code = "1 2 2 5 0"
print(f"Initial code: {lock_code}")

morse = convert_to_morse(lock_code)
print(f"Morse code: {morse}")
