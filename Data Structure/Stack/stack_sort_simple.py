def push1(item):
    stack.append(item)
#==============================
def pop():
    if isEmpty(stack):
        return 'cant pop'
    else:
        stack.pop()
#==============================
def peek():
    if isEmpty(stack):
        return 'cant peek'
    else:
        return stack[-1]
#==============================
def isEmpty(stack):
    if len(stack) == 0:
        return True
    else:
        return False
#==============================
def sort(stack,stack1):
    while(isEmpty(stack) == False):
        temp = stack[-1]
        pop()
        while(isEmpty(stack1)== False and stack1[-1] < temp):
            stack.append(stack1[-1])
            stack1.pop()
        stack1.append(temp)
    return stack1

#==============================

stack = []
stack1 = []

push1(4)
push1(2)
push1(11)
push1(12)

print(sort(stack,stack1))
a=stack1.pop()
print(a)
