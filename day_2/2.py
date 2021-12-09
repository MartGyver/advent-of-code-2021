
def calculate_depth(content):
    horizontal=0
    depth=0
    for movement in content:
        if movement[0] == 'forward':
            horizontal += movement[1]
        elif movement[0] == 'up':
            depth -= movement[1]
        elif movement[0] == 'down':
            depth += movement[1]
    return depth*horizontal

def calculate_aim(content):
    horizontal=0
    depth=0
    aim=0
    for movement in content:
        if movement[0] == 'forward':
            horizontal += movement[1]
            depth += aim*movement[1]
        elif movement[0] == 'up':
            aim -= movement[1]
        elif movement[0] == 'down':
            aim += movement[1]
    return depth*horizontal


if __name__ == "__main__":
    with open('day_2/input.txt') as f:
        content =f.readlines()
        content=[i.split(" ") for i in content]
        content=[[i[0], int(i[1])] for i in content]
        print(calculate_depth(content))
        print(calculate_aim(content))