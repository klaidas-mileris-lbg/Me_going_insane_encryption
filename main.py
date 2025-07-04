def dec_to_binary(dec_num: int):
    remainder = 0
    if dec_num == 0:
        return 0
    if dec_num == 1:
        return 1
    current_number = dec_num
    binary_number = []
    while current_number > 1:
        binary_number.append(str(remainder))
        remainder = current_number % 2
        current_number = int((current_number - remainder) / 2)
    if current_number == 1:
        binary_number.append(str(current_number))
    return "".join(binary_number[::-1])
print(dec_to_binary(89))

def generate_random_key(length_of_key):
    import time
    import random
    import pyautogui
    print("in 2 seconds, start moving your mouse for 10 seconds to generate entropy")
    time.sleep(2)
    randomness_list = []
    for i in range(100):
        mouse_x, mouse_y = pyautogui.position()
        random_number = mouse_x ** mouse_y
        randomness_list.append(random_number)
        print(random_number)
        time.sleep(0.1)
    random_key = ""
    for i in range(length_of_key):
        random_number_from_list = randomness_list[random.randint(0, len(randomness_list) - 1)]
        random_digit_from_number = str(random_number_from_list)[random.randint(0, len(str(random_number_from_list)))]
        if int(random_digit_from_number) % 2:
            random_key += "1"
        else:
            random_key += "0"

    print("".join(random_key))
    

generate_random_key(128)


def bitwise_XOR(binary_number: str, generated_key: str):
    new_result = ""
    if len(binary_number) == len(generated_key):
        for i, j in zip(binary_number, generated_key):
            if i == j:
                new_result += "0"
            else:
                new_result += "1"
    return new_result

print(bitwise_XOR("111001", "001010"))