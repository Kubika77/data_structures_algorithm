import pytest
from exercises.append_node import LinkedList


@pytest.mark.parametrize("initial_value, append_values, expected_length, expected_head_value, expected_tail_value", [
    (1, [2, 3], 3, 1, 3),
    (10, [20, 30, 40], 4, 10, 40),
    (5, [], 1, 5, 5),
    # (None, [1], 1, 1, 1),
])
def test_append_node(initial_value, append_values, expected_length, expected_head_value, expected_tail_value):
    ll = LinkedList(initial_value)
    for value in append_values:
        ll.append(value)

    assert ll.length == expected_length
    assert ll.head.value == expected_head_value
    assert ll.tail.value == expected_tail_value
    ll.print_list()  # Optional: Print the list to visually verify the order of nodes