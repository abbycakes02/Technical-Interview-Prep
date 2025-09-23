import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # first = true
        # loop thru tokens
        # if num put on stack
        # if operand  and first == true pop element 2 else pop once
        # take the popped values and take str and turn into int
        dict = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
        stack = []
        #answer = 0
        for i in tokens:
            if i.lstrip("-").isdigit():
                stack.append(int(i))
            else:
                x = stack.pop()
                y = stack.pop()
                stack.append(int(dict[i](y,x)))
                #answer += x + dict[i] + y
                #print(answer)
        return stack[0]
