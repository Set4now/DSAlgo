from typing import List


def getsubstring(liststr: List):
    output = []
    for i in range(len(liststr)):
        output.append(liststr[i])
        nextcharindex = i + 1
        while nextcharindex < len(liststr):
            newstr = liststr[i] + liststr[nextcharindex]
            output.append(newstr)
            nextcharindex += 1
    output.append("".join(liststr))
    return output




if __name__ == "__main__":
    listofwords = [
    "ABC",
    ]
    for word in listofwords:
        print(getsubstring(word))
