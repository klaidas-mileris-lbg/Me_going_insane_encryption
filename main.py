# True security can't rely on the source code being secret. It has to rely on the complexity and the impossibility of reverse-engineering the final result due
# to its mathematical properties.


def dec_to_binary(dec_num: int):
    remainder = 0
    if dec_num == 0:
        return "0"
    if dec_num == 1:
        return "1"
    current_number = dec_num
    binary_number = []
    while current_number > 1:
        binary_number.append(str(remainder))
        remainder = current_number % 2
        current_number = int((current_number - remainder) / 2)
    if current_number == 1:
        binary_number.append(str(current_number))
    return "".join(binary_number[::-1])
# print(dec_to_binary(89))

def generate_random_key(length_of_key):
    """generates a random binary key of the specified length using user-generated entropy"""
    import time
    import random
    import pyautogui
    # Still needs a bunch of work - need to introduce more non-deterministic factors to prevent simple reverse-engineering.
    # include some keyboard bashing perhaps? 
    # Needs a bunch of error handling - at the moment I could get buffer overflows - raising to the power generates immense numbers, would be bad on a large display
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
    

# generate_random_key(128)


def bitwise_XOR(binary_number: str, generated_key: str):
    new_result = ""
    if len(binary_number) == len(generated_key):
        for i, j in zip(binary_number, generated_key):
            if i == j:
                new_result += "0"
            else:
                new_result += "1"
    return new_result

# print(bitwise_XOR("111001", "001010"))






def generate_mouse_movement_entropy(time_for_collection):
    """Prompts the user to move the mouse and generates random numbers from that"""
    import pyautogui
    import time
    import secrets
    import hashlib
    print(f"In 2 seconds, imagine a picture in your head and move your mouse, pretend to draw and colour in" 
          f"that picture for {time_for_collection} seconds to generate entropy...")
    time.sleep(2)
    entropy_list = []
    print("Collecting entropy...")
    for i in range(time_for_collection*10):
        mouse_x, mouse_y = pyautogui.position()
        new_number = (mouse_x * secrets.randbelow(500)) * (mouse_y * secrets.randbelow(500))
        hasher = hashlib.sha256()
        new_number_bytes = str(new_number).encode("utf-8")
        # hashes the number
        hasher.update(new_number_bytes)
        # now we do bits > bytes > dec
        new_number_bytes = hasher.digest()
        new_number_dec = int.from_bytes(new_number_bytes, "big")
        entropy_list.append(str(new_number_dec))
        time.sleep(0.1)
        print(new_number_dec)
    return entropy_list
     


def generating_random_key(key_len, time_for_collection):
    import secrets
    # this time let's make something that is actually truly random
    # so this gives us a list of quite random numbers
    final_key = ""
    entropy_list = generate_mouse_movement_entropy(time_for_collection)
    for i in range(key_len):
        random_number: str = entropy_list[secrets.randbelow(len(entropy_list))]
        random_digit: int = int(random_number[secrets.randbelow(len(random_number))])
        if random_digit % 2 == 0:
            final_key += "1"
        else:
            final_key += "0"
    return final_key

    



print(f"The new secret key: {generating_random_key(128, 2)}")

# just a quick test