def insert(stack, item):
    if isEmpty(stack):
        push(stack, item)
    else:
        temp = pop(stack)
        insert(stack, item)
        push(stack, temp)
 
def reverse(stack):
    if not isEmpty(stack):
        temp = pop(stack)
        reverse(stack)
        insert(stack, temp)
 

def createStack():
    stack = []
    return stack
 
# Function to check if the stack is empty
def isEmpty( stack ):
    return len(stack) == 0
 
#Function to push an item to stack
def push( stack, item ):
    stack.append( item )
 
# Function to pop an item from stack
def pop( stack ):
 
    #If stack is empty then error
    if(isEmpty( stack )):
        print("Stack Underflow ")
        exit(1)
 
    return stack.pop()
 
# Function to print the stack
def prints(stack):
    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end = ' ')
    print()
 
# Driver program to test above functions
 
stack = createStack()
push( stack, str(4) )
push( stack, str(3) )
push( stack, str(2) )
push( stack, str(1) )
print("Original Stack ")
prints(stack)
 
reverse(stack)
 
print("Reversed Stack ")
prints(stack)
