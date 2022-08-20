# SOLUTION 👇
ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
def baseball(list):
    new_list = []
    for i in list:
        if i == "C":
            new_list.pop()
        elif i == "D":
            new_list.append(new_list[-1] * 2)
        elif i == "+":
            new_list.append(new_list[-1] + new_list[-2])
        else:
            new_list.append(int(i))
    return sum(new_list)


print(baseball(ops))
