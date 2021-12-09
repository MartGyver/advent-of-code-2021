

def depth_increase(content):
    increases = 0
    for i in range(len(content)-1):
        if(content[i+1]>content[i]):
            increases = increases + 1
    return increases

def depth_increase_3(content):
    increases = 0
    for i in range(len(content)-3):
        if(content[i+1]+content[i+2]+content[i+3]>content[i]+content[i+1]+content[i+2]):
            increases = increases + 1
    return increases

if __name__ == "__main__":
    with open('day_1/input.txt') as f:
        content =list(map(int, f.readlines()))
        print (depth_increase(content))
        print (depth_increase_3(content))