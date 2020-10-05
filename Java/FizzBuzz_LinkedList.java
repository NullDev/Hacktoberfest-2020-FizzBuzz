// This is an implementation of fizzBuzz using linkedList without the builtin collections.
// Numbers are added to the linkedlist then printed from there.
// Author : @Kayne103

public class FizzBuzz_LinkedList {
    Node head;

    class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            next = null;
        }
    }

    public static FizzBuzz_LinkedList insertIntoList(FizzBuzz_LinkedList list, int data) {
        Node newNode = list.new Node(data);
        newNode.next = null;
        if (list.head == null) {
            list.head = newNode;
        } else {
            Node temp = list.head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
        }
        return list;
    }

    public static void insertNumbers(FizzBuzz_LinkedList list, int NumberOfItems) {
        int index = 1;
        while (index <= NumberOfItems) {
            list = insertIntoList(list, index);
            index = index + 1;
        }
    }

    public static void printFizzBuzz(FizzBuzz_LinkedList list) {
        Node temp = list.head;
        while (temp != null) {
            if (temp.data % 3 == 0 && temp.data % 5 != 0) {
                System.out.println("Fizz");
            }
            if (temp.data % 5 == 0 && temp.data % 3 != 0) {
                System.out.println("Buzz");
            }
            if (temp.data % 3 == 0 && temp.data % 5 == 0 && temp.data != 1) {
                System.out.println("FizzBuzz");
            }
            if (temp.data % 3 != 0 && temp.data % 5 != 0) {
                System.out.println(temp.data);
            }
            temp = temp.next;
        }
    }

    public static void main(String[] args) {
        FizzBuzz_LinkedList fl = new FizzBuzz_LinkedList();
        insertNumbers(fl, 100);
        printFizzBuzz(fl);
    }
}
