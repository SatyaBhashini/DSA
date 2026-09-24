
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, x):
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow")

        else:
            if self.front == -1:
                self.front = 0
                self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.size

            self.queue[self.rear] = x
            print(f"{x} inserted into the queue")

    def dequeue(self):
        if self.front == -1:
            print("Queue Underflow")

        else:
            x = self.queue[self.front]
            self.queue[self.front] = None

            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.size

            print(f"{x} deleted from the queue")

    def peek(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[self.front])

    def display(self):
        if self.front == -1:
            print("Queue is empty")

        else:
            print("The elements of the circular queue are:")

            i = self.front

            while True:
                print(self.queue[i], end=" ")

                if i == self.rear:
                    break

                i = (i + 1) % self.size

            print()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, x):
        new_node = Node(x)

        if self.front is None:
            self.front = new_node
            self.rear = new_node

            self.rear.next = self.front

        else:
            new_node.next = self.front
            self.rear.next = new_node
            self.rear = new_node

        print(f"{x} inserted into the queue")

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")

        else:
            x = self.front.data

            if self.front == self.rear:
                self.front = None
                self.rear = None

            else:
                self.front = self.front.next
                self.rear.next = self.front

            print(f"{x} deleted from the queue")

    def peek(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Front element:", self.front.data)

    def display(self):
        if self.front is None:
            print("Queue is empty")

        else:
            print("The elements of the circular queue are:")

            current = self.front

            while True:
                print(current.data, end=" ")

                current = current.next

                if current == self.front:
                    break

            print()


print("       CIRCULAR QUEUE PROGRAM")

while True:

    print("\n----- Main Menu -----")
    print("1. Circular Queue using Array")
    print("2. Circular Queue using Linked List")
    print("3. Exit")

    choice = int(input("Enter your choice: "))


    # ARRAY IMPLEMENTATION


    if choice == 1:

        size = int(input("Enter the size of the queue: "))

        q = CircularQueue(size)

        while True:

            print("\n----- Circular Queue Using Array -----")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Peek")
            print("4. Display")
            print("5. Back to Main Menu")

            option = int(input("Enter your choice: "))

            if option == 1:
                x = int(input("Enter the element to insert: "))
                q.enqueue(x)

            elif option == 2:
                q.dequeue()

            elif option == 3:
                q.peek()

            elif option == 4:
                q.display()

            elif option == 5:
                print("Returning to Main Menu...")
                break

            else:
                print("Invalid choice!")


    # LINKED LIST IMPLEMENTATION


    elif choice == 2:

        q = CircularQueueLinkedList()

        while True:

            print("\n----- Circular Queue Using Linked List -----")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Peek")
            print("4. Display")
            print("5. Back to Main Menu")

            option = int(input("Enter your choice: "))

            if option == 1:
                x = int(input("Enter the element to insert: "))
                q.enqueue(x)

            elif option == 2:
                q.dequeue()

            elif option == 3:
                q.peek()

            elif option == 4:
                q.display()

            elif option == 5:
                print("Returning to Main Menu...")
                break

            else:
                print("Invalid choice!")

    elif choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
