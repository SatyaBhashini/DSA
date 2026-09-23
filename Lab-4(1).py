class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Create a Linked List
    def create(self):
        n = int(input("Enter number of nodes: "))

        if n <= 0:
            print("Linked List cannot be empty.")
            return

        self.head = None

        for i in range(n):
            data = int(input(f"Enter data for node {i + 1}: "))
            self.insert_end(data)

        print("Linked List created successfully.")

    # 2. Insert at Beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print("Node inserted at beginning.")

    # 3. Insert at End
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        print("Node inserted at end.")

    # 4. Insert at Specific Index
    def insert_index(self, index, data):
        if index < 0:
            print("Invalid Index.")
            return

        if index == 0:
            self.insert_beginning(data)
            return

        if self.head is None:
            print("Linked List is empty.")
            return

        temp = self.head

        for i in range(index - 1):
            if temp is None:
                print("Invalid Index.")
                return
            temp = temp.next

        if temp is None:
            print("Invalid Index.")
            return

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

        print("Node inserted at index", index)

    # 5. Delete by Value
    def delete_by_value(self, value):
        if self.head is None:
            print("Linked List is empty.")
            return

        if self.head.data == value:
            self.head = self.head.next
            print(value, "deleted successfully.")
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.data == value:
                temp.next = temp.next.next
                print(value, "deleted successfully.")
                return

            temp = temp.next

        print("Value not found.")

    # 6. Delete First Node
    def delete_first(self):
        if self.head is None:
            print("Linked List is empty.")
            return

        deleted = self.head.data
        self.head = self.head.next

        print(deleted, "deleted from beginning.")

    # 7. Delete Last Node
    def delete_last(self):
        if self.head is None:
            print("Linked List is empty.")
            return

        if self.head.next is None:
            deleted = self.head.data
            self.head = None
            print(deleted, "deleted from end.")
            return

        temp = self.head

        while temp.next.next is not None:
            temp = temp.next

        deleted = temp.next.data
        temp.next = None

        print(deleted, "deleted from end.")

    # 8. Count Number of Nodes
    def count(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    # 9. Display / Traverse
    def display(self):
        if self.head is None:
            print("Linked List is empty.")
            return

        temp = self.head

        print("Linked List:", end=" ")

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main Program
ll = SinglyLinkedList()

while True:
    print("\n========== SINGLY LINKED LIST ==========")
    print("1. Create a Linked List")
    print("2. Insert at Beginning")
    print("3. Insert at End")
    print("4. Insert at Specific Index")
    print("5. Delete by Value")
    print("6. Delete First Node")
    print("7. Delete Last Node")
    print("8. Count No. of Nodes")
    print("9. Display / Traverse")
    print("10. Exit")
    print("=========================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        ll.create()

    elif choice == 2:
        data = int(input("Enter data: "))
        ll.insert_beginning(data)

    elif choice == 3:
        data = int(input("Enter data: "))
        ll.insert_end(data)

    elif choice == 4:
        index = int(input("Enter index: "))
        data = int(input("Enter data: "))
        ll.insert_index(index, data)

    elif choice == 5:
        value = int(input("Enter value to delete: "))
        ll.delete_by_value(value)

    elif choice == 6:
        ll.delete_first()

    elif choice == 7:
        ll.delete_last()

    elif choice == 8:
        ll.count()

    elif choice == 9:
        ll.display()

    elif choice == 10:
        print("Program terminated.")
        break

    else:
        print("Invalid choice. Please try again.")
