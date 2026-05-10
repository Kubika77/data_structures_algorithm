import pytest
from exercises.pop_node import LinkedList


@pytest.mark.parametrize("initial_value, append_values, expected_length_after_pop, expected_tail_value_after_pop", [
    (1, [], 0, None),
    (1, [2], 1, 1),
    (1, [2, 3], 2, 2),
])
def test_pop(initial_value, append_values, expected_length_after_pop, expected_tail_value_after_pop):
    ll = LinkedList(initial_value)
    for value in append_values:
        ll.append(value)
    print(f"\nBefore popping: {ll.get_list()}")
    expected_tail_value = ll.tail.value
    popped_node = ll.pop()
    print(f"After popping: {ll.get_list()}")
    assert popped_node.value == expected_tail_value
    assert ll.length == expected_length_after_pop
    assert ll.tail.value == expected_tail_value_after_pop if expected_tail_value_after_pop is not None else ll.tail is None

@pytest.mark.parametrize("initial_value, append_values, expected_popped_value", [
    (1, [], 1),
    (1, [2], 2),
    (1, [2, 3], 3),
])
def test_pop_returned_node_value(initial_value, append_values, expected_popped_value):
    ll = LinkedList(initial_value)
    for value in append_values:
        ll.append(value)
    popped_node = ll.pop()
    assert popped_node.value == expected_popped_value