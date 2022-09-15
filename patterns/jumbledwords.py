# def jumbledwords(jumbledstr, wordlength):
#     start_index = 0
#     words = []
#     while start_index < wordlength:
#         next_char_index = start_index
#         temp_string = jumbledstr[start_index]
#         while next_char_index + 4 < len(jumbledstr):
#             print("==")
#             temp_string += jumbledstr[next_char_index + 4]
#             next_char_index += 4
#         words.append(temp_string)
#         start_index += 1
#     return ",".join(words)


def jumbledwords(jumbledstr, wordlength):
    start_index = 0
    words = []
    while start_index < wordlength:
        next_char_index = start_index
        temp_string = jumbledstr[start_index]
        while next_char_index + wordlength < len(jumbledstr):
            temp_string += jumbledstr[next_char_index + wordlength]
            next_char_index += wordlength
        words.append(temp_string)
        start_index += 1
    return ",".join(words)


jumbledstr = "gpbsalaimalneylg"
print(jumbledwords(jumbledstr, 4))
#game,play,ball,sing

