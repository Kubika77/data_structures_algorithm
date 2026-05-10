import pytest
from exercises.linked_list.LL_constructor import Node, LinkedList



def test_initialization_of_linked_list():
    ll = LinkedList(5)
    assert ll.head.value == 5
    assert ll.tail.value == 5
    assert ll.length == 1
    assert ll.head is ll.tail


def test_head():
    ll = LinkedList(10)
    assert ll.head.value == 10
    assert isinstance(ll.head, Node)


def test_tail():
    ll = LinkedList(20)
    assert ll.tail.value == 20
    assert isinstance(ll.tail, Node)


def test_length():
    ll = LinkedList(30)
    assert ll.length == 1


def test_node_value():
    node = Node(40)
    assert node.value == 40


def test_node_next():
    node = Node(50)
    assert node.next is None