from typing import List


def encode_words(words: List[str], mapping: dict) -> List:
    encoded_words = []

    for word in words:
        encoded_words.append("".join([mapping[letter] for letter in word]))

    return encoded_words


def create_map(encoding: List[int]) -> dict:
    mapping = {}

    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        mapping[letter] = encoding.pop(0)

    return mapping


def has_collision(encoded_words: str) -> bool:
    for i in range(1, len(encoded_words)):
        if encoded_words[i] == encoded_words[i - 1]:
            return True

    return False


for case_num in range(int(input().strip())):
    # create map from encoding
    mapping = create_map(input().strip().split(" "))

    words = []

    # add word to list
    for _ in range(int(input().strip())):
        words.append(input().strip())

    # encode words
    encoded_words = encode_words(words, mapping)
    encoded_words.sort()

    print(f"Case #{case_num+1}: {'YES' if has_collision(encoded_words) else 'NO'}")


# for i in range(int(input().strip())):
#     values = [str(number) for number in input().strip().split(" ")]

#     for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         mapping[letter] = values.pop(0)

#     items = set()

#     for j in range(int(input().strip())):
#         # Collision
#         collision = False

#         # Encode words and add to list
#         cur = "".join([mapping[letter] for letter in input().strip()])

#         # If collision found
#         if cur in items:
#             collision = True
#             continue
#         else:
#             items.add(cur)

#     out.append(f"Case #{cur_case_num}: {'YES' if collision else 'NO'}")

#     cur_case_num += 1

# print("\n".join(out))
