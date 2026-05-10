import pytest
from exercises.linked_list.prepend_node import LinkedList


@pytest.mark.parametrize("initial_value, append_values, prepend_value, expected_head_value_after_prepend, expected_length_after_prepend", [
    (1, [], 0, 0, 2),
    (1, [2], 1, 1, 3),
    (1, [2, 3], 2, 2, 4),
])
def test_prepend(initial_value, append_values, prepend_value, expected_head_value_after_prepend, expected_length_after_prepend):
    ll = LinkedList(initial_value)
    for value in append_values:
        ll.append(value)
    print(f"\nBefore prepending: {ll.get_list()}")
    ll.prepend(prepend_value)
    print(f"After prepending: {ll.get_list()}")
    assert expected_head_value_after_prepend == ll.head.value
    assert expected_length_after_prepend == ll.length
