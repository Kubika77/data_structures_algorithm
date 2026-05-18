import pytest
from exercises.linked_list.pop_first import LinkedList

@pytest.mark.parametrize("initial_value, append_values, expected_pop_value, expected_length_after_pop, expected_head_value_after_pop", [
    (1, [2, 3], 1, 2, 2),
    (1, [2, 3, 4], 1, 3, 2),
    ]
)
def test_pop_first(initial_value, append_values, expected_pop_value, expected_length_after_pop, expected_head_value_after_pop):
    ll = LinkedList(initial_value)
    for value in append_values:
        ll.append(value)
    print(f"\nBefore popping first: {ll.get_list()}")
    poped = ll.pop_first()
    print(f"After popping first: {ll.get_list()}")
    assert expected_pop_value == poped.value
    assert expected_length_after_pop == ll.length
    assert expected_head_value_after_pop == ll.head.value

@pytest.mark.parametrize("initial_value, expected_pop_value, expected_length_after_pop, expected_head_value_after_pop", [
    (1, 1, 0, None)
])
def test_one_item_list(initial_value, expected_pop_value, expected_length_after_pop, expected_head_value_after_pop):
    ll = LinkedList(initial_value)
    print(f"list before pop first: {ll.get_list()}")
    poped = ll.pop_first()
    print(f"list after pop first: {ll.get_list()}")
    assert poped.value == expected_pop_value
    assert ll.length == expected_length_after_pop
    assert ll.head == expected_head_value_after_pop

@pytest.mark.parametrize("initial_value, expected_pop_value, expected_length_after_pop, expected_head_value_after_pop", [
    (1, None, 0, None)
])
def test_empty_list(initial_value, expected_pop_value, expected_length_after_pop, expected_head_value_after_pop):
    ll = LinkedList(initial_value)
    ll.pop()
    print(f"list before pop first: {ll.get_list()}")
    poped = ll.pop_first()
    print(f"list after pop first: {ll.get_list()}")
    assert poped == expected_pop_value
    assert ll.length == expected_length_after_pop
    assert ll.head == expected_head_value_after_pop
