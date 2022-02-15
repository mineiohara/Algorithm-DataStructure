# Input: { {1}, [2], (3) } -> Output: True
# Input: [1{]} -> Output: False

def validateFormat(chars: str) -> bool:
    brackets = {"[":"]", "{":"}", "(":")"}
    stack = []

    for char in chars:
        print(char, stack)
        if char in brackets.keys():
            stack.append(char)
        
        elif char in brackets.values():
            if (stack and char != brackets[stack[-1]]) or not stack: return False
            else: stack.pop()
    
    return False if stack else True


if __name__ == "__main__":
    print(validateFormat("format"))