def baseball(a_list):
    new_list = []
    for i in a_list:
        try:
            new_list.append(int(i))
        except:
            if(i == "D"):
                new_list.append(new_list[-1] * 2)
            elif(i == "C"):
                new_list.pop()
            elif(i == "+"):
                new_list.append(new_list[-1] + new_list[-2])
            else:
                return "It's wrong"
    return sum(new_list)

ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
print(baseball(ops))
ops2 = ["5", "2", "C", "D", "+"]
print(baseball(ops2))