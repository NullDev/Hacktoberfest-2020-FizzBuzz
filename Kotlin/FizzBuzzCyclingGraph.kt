//Cycling Graph
//Same method as in FizzBuzzCyclingList.kt but as a graph and generation of the graph
//You can try it online on Kotlin Playground: https://pl.kotl.in/7uWNc8xAo
//Author: @tobi6112

class Node(var next: Node?, var value: Any)

class Graph(val set: List<Node>) {
    var current = set.first()

    fun next(): Node {
        if(current.value is Number) {
            current.value = (current.value as Number).toInt() + 15
        }
        current = current.next!!
        return current
    }
}

fun generateNodes() : List<Node> {
    val nodes: MutableList<Node> = mutableListOf()
    var firstNode: Node? = null
    var lastNode: Node? = null
    for (i in (1..15)) {
        var value: Any = i
        when {
            i % 15 == 0 -> value = "FizzBuzz"
            i % 5 == 0 -> value = "Buzz"
            i % 3 == 0 -> value = "Fizz"
        }
        val node = Node(null, value)
        if(i == 1) {
            firstNode = node
        }
        if(lastNode != null) {
            if(i == 15) {
                node.next = firstNode
            }
            lastNode.next = node
        }
        lastNode = node
        nodes.add(node)
    }
    return nodes
}

fun generateGraph() : Graph {
    return Graph(generateNodes())
}

fun main() {
    val graph = generateGraph()

    var node = graph.current
    repeat(100) {
        println(node.value)
        node = graph.next()
    }
}