# Contains All Functions related to linked list.


# Node stores the value and records
# how many times it was found in the input file.
class Node:
    def __init__(self, data):
        self.data = data
        self.counter = 1
        self.next = None


# This functions returns a new Node.
def getNewNode(data):
    newNode = Node(data)
    newNode.data = data
    newNode.next = None
    return newNode


# This function recursively traverses the linked list to see
# if we are adding an existing data to linked list.
# If that is true, then we add 1 to its counter
def find(head, data):
    if head is None:
        return True
    else:
        if head.data == data:
            head.counter += 1
            return False
        else:
            return find(head.next, data)


# This function recursively pushes data into the linked list
# only if that data was not previously in the linked list
def push(head, data):
    if find(head, data):
        if head is None:
            return getNewNode(data)
        else:
            head.next = push(head.next, data)
        return head
    else:
        return head


# This function recursively traverses the linked list to find
# which data has the most number of repetitions.
# Then it returns that max value
def findMax(head, maxValue):
    if head is None:
        return maxValue
    else:
        if head.counter > maxValue:
            maxValue = head.counter

        return findMax(head.next, maxValue)


# This function recursively deletes the node in a linked list
# depending on where it is positioned in the linked list
def pop(head, position):
    if position < 1:
        return head

    if head is None:
        return None

    if position == 1:
        newHead = head.next
        return newHead

    head.next = pop(head.next, position - 1)
    return head


# This functions recursively traverses the linked list to
# get the position of the node in the linked list which has the
# maximum repetitions value
def getPosition(head, data, position):
    if head is None:
        return position
    else:
        if head.data == data:
            return position + 1
        else:
            return getPosition(head.next, data, position + 1)


# This function recursively traverses the linked list and writes the
# maximum repetitions valued node to the output file and removes that node
# from the list. It keeps on going until linked list is empty
def traverse(head, headcpy, parameter, outputFile, check):
    if head is None:
        return

    maxValue = findMax(headcpy, 0)

    if head.counter == maxValue:
        if check < parameter:
            outputFile.write(head.data)
            outputFile.write(" ")
            outputFile.write(str(head.counter))
            outputFile.write("\n")
            check += 1

        headcpy = pop(headcpy, getPosition(headcpy, head.data, 0))
        traverse(headcpy, headcpy, parameter, outputFile, check)
        return

    traverse(head.next, headcpy, parameter, outputFile, check)
