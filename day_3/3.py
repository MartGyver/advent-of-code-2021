def calculate_comsumption(content):
    bits = len(content[0])
    gamma = [0]*bits
    epsilon = [0]*bits
    for i in range(bits):
        if sum([int(j[i]) for j in content]) > len(content)/2:
            gamma[i]= 1
        else:
            epsilon[i]=1
    return int("".join(str(i) for i in gamma),2)*int("".join(str(i) for i in epsilon),2)


#def get_rating_value(content, content2):
#    print(calculate_rating(content2, 1))
#    print(calculate_rating(content, 0))


def calculate_rating(content, comparator):
    content = [j for j in content if j != 0]
    bits = len(content[0])
    for i in range(bits):
        if sum([int(j[i]) for j in content]) >= len(content)/2:
            content = calculate_new_list(content, comparator, i)
        else:
            content = calculate_new_list(content, 1-comparator, i)  
        content = [j for j in content if j != 0]
        if len(content) == 1:
            break
    print(content)
    return(content)


def calculate_new_list(content, comparator, index):
    for j in range(len(content)):
        if int(content[j][index])!=comparator:
            content[j] = 0
    return content


if __name__ == "__main__":
    with open('day_3/input.txt') as f:
        content =f.readlines()
        content=[i.strip() for i in content]
    print(calculate_comsumption(content))
    print (int(calculate_rating(content,1)[0],2) * int(calculate_rating(content,0)[0],2))