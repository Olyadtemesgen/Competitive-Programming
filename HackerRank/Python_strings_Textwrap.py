import textwrap

def wrap(string, max_width):
    left = 0
    strr = ''
    if len(string) / max_width == len(string)// max_width:
        for x in range(max_width, len(string) + 1, max_width):
            strr += string[left:x] + '\n'
            left = x
    else:
        for x in range(max_width, len(string) +max_width - len(string) % max_width + 1, max_width):
            strr += string[left:x] + '\n'
            left = x 
    return strr
    
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
