
import java.util.*;

public class Main {

	static Node node;
	static Node newRoot;
	static String codedString = "";

	public static void main(String[] args) {
	    Scanner in = new Scanner(System.in);  
	    System.out.println("Enter Your String");
		String message = in.nextLine();
		in.close();             


		// Convert the string to char array

		char[] msgChar = message.toCharArray();
		ArrayList<Character> characters = new ArrayList<Character>();

		/*
		 * Get a List of all the chars which are present in the string No
		 * repeating the characters!
		 */
		for (int i = 0; i < msgChar.length; i++) {
			if (!(characters.contains(msgChar[i]))) {
				characters.add(msgChar[i]);
			}
		}

		/* Print out the available characters */
		// System.out.println(characters);

		/* Count the number of occurrences of Characters */
		int[] countOfChar = new int[characters.size()];

		/* Fill The Array Of Counts with one as base value */
		for (int x = 0; x < countOfChar.length; x++) {
			countOfChar[x] = 0;
		}

		/* Do Actual Counting! */
		for (int i = 0; i < characters.size(); i++) {
			char checker = characters.get(i);
			for (int x = 0; x < msgChar.length; x++) {
				if (checker == msgChar[x]) {
					countOfChar[i]++;
				}
			}
		}

		/* Sort the arrays is descending order */
		for (int i = 0; i < countOfChar.length - 1; i++) {
			for (int j = 0; j < countOfChar.length - 1; j++) {
				if (countOfChar[j] < countOfChar[j + 1]) {
					int temp = countOfChar[j];
					countOfChar[j] = countOfChar[j + 1];
					countOfChar[j + 1] = temp;

					char tempChar = characters.get(j);
					characters.set(j, characters.get(j + 1));
					characters.set(j + 1, tempChar);
				}
			}
		}

		/* Print Out The Frequencies of the Characters */
		for (int x = 0; x < countOfChar.length; x++) {
			System.out.println(characters.get(x) + " - " + countOfChar[x]);
		}

		/* Form the Tree! */

		/* Form Leaf Nodes and Arrange them in a linked list */

		Node root = null;
		Node current = null;
		Node end = null;

		for (int i = 0; i < countOfChar.length; i++) {
			Node node = new Node(characters.get(i).toString(), countOfChar[i]);
			if (root == null) {
				root = node;
				end = node;
			} else {
				current = root;
				while (current.linker != null) {
					current = current.linker;
				}
				current.linker = node;
				current.linker.linkerBack = current;
				end = node;
			}
		}

		// Recursively add and make nodes!
		TreeMaker(root, end);

		// inOrder(root);
		System.out.println();
		inOrder(node);

		// preOrder(root);
		System.out.println();
		preOrder(node);

		// Calculate the ends and the meets!
		char[] messageArray = message.toCharArray();
		char checker;

		for (int i = 0; i < messageArray.length; i++) {
			current = node;
			checker = messageArray[i];
			String code = "";
			while (true) {
				if (current.left.value.toCharArray()[0] == checker) {
					code += "0";
					break;
				} else {
					code += "1";
					if (current.right != null) {
						if (current.right.value.toCharArray()[0] == characters
								.get(countOfChar.length - 1)) {
							break;
						}
						current = current.right;
					} else {
						break;
					}
				}
			}
			codedString += code;
		}
		System.out.println();
		System.out.println("The coded string is " + codedString);
	}

	public static void preOrder(Node root) {

		if (root != null) {

			System.out.print(root.value + "->");
			preOrder(root.left);
			preOrder(root.right);

		}

	}

	public static void inOrder(Node root) {

		if (root != null) {
			inOrder(root.left);
			System.out.print(root.value + "->");
			inOrder(root.right);
		}

	}

	public static void TreeMaker(Node root, Node end) {
		node = new Node(end.linkerBack.value + end.value, end.linkerBack.count
				+ end.count);
		node.left = end.linkerBack;
		node.right = end;
		end.linkerBack.linkerBack.linker = node;
		node.linkerBack = end.linkerBack.linkerBack;
		end = node;
		end.linker = null;
		Node current = root;

		while (current.linker != null) {
			System.out.print(current.value + "->");
			current = current.linker;
		}

		System.out.println(current.value);

		if (root.linker == end) {
			node = new Node(root.value + end.value, root.count + end.count);
			node.left = root;
			node.right = end;
			node.linker = null;
			node.linkerBack = null;
			System.out.println(node.value);
			newRoot = node;
		} else {
			TreeMaker(root, end);
		}
	}

}

class Node {

	String value;
	int count;
	Node left;
	Node right;
	Node linker;
	Node linkerBack;

	Node(String value, int count) {

		this.value = value;
		this.count = count;
		this.left = null;
		this.right = null;
		this.linker = null;
		this.linkerBack = null;

	}

}
