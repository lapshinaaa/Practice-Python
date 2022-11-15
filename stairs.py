number_of_stairs = int(input())
stairs = [int(elem) for elem in input().split()]
max_sum = 0
index = -1
steps = ""


while index <= len(stairs) - 2:
    if stairs[index + 1] >= 0 and stairs[index + 2] >= 0:
        max_sum += stairs[index + 1] + stairs[index + 2]
        steps += str(index + 2) + " " + str(index + 3) + " "
        index += 2

    elif stairs[index + 1] < 0 or stairs[index + 2] < 0:
        if stairs[index + 1] > stairs[index + 2]:
            max_sum += stairs[index + 1]
            steps += str(index + 2) + " "
            index += 1

        else:
            max_sum += stairs[index + 2]
            steps += str(index + 3) + " "
            index += 2

    if index == len(stairs) - 2:
        max_sum += stairs[-1]
        steps += str(len(stairs))
        index += 3


print(max_sum)
if steps[:1] == " ":
    print(steps[:-1])

else:
    print(steps)