class ArrayQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, x):
        if self.rear == self.size - 1:
            print("Queue Overflow")
        else:
            if self.front == -1:
                self.front = 0

            self.rear += 1
            self.queue[self.rear] = x
            print(f"{x} inserted into the queue")

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow")
        else:
            x = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1

            print(f"{x} deleted from the queue")

            if self.front > self.rear:
                self.front = -1
                self.rear = -1

    def peek(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[self.front])

    def display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("The elements of the queue are:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, x):
        new_node = Node(x)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(f"{x} inserted into the queue")

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
        else:
            x = self.front.data
            self.front = self.front.next

            if self.front is None:
                self.rear = None

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
            print("The elements of the queue are:")

            temp = self.front
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next

            print()


print("       QUEUE IMPLEMENTATION")


print("\nChoose Queue Implementation:")
print("1. Array")
print("2. Linked List")

choice = int(input("Enter your choice: "))

# Array Queue
if choice == 1:
    size = int(input("Enter the size of the queue: "))
    q = ArrayQueue(size)

    while True:
        print("\n----- Array Queue Menu -----")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

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
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


# Linked List Queue
elif choice == 2:
    q = LinkedListQueue()

    while True:
        print("\n----- Linked List Queue Menu -----")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

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
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

else:
    print("Invalid choice!")
