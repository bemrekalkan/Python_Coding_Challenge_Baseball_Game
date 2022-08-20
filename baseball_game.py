# SOLUTION-1 👇

from curses.ascii import isalnum

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


# SOLUTION-2 👇

ops = ["5", "-2", "4", "C", "D", "9", "+", "+"] 

def calculate_points(ops):
    points = []
    
    for op in ops:
        if op.isdigit() or "-" in op:
            points.append(int(op))
            print(points)
        else:
            if op == "C" and op != ops[0] and len(points) >= 1:
                points.pop()

            elif op == "D" and op != ops[0] and len(points) >= 1:
                points.append(points[-1]*2)

            elif op == "+" and op != ops[0] and len(points) >= 2:
                points.append(points[-1] + points[-2])

            print(points)
    return sum(points)

print(calculate_points(ops))

