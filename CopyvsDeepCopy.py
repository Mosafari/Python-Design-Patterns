"""ChatGPT explanation:
    In Python, `copy` and `deepcopy` are two functions provided by
    the `copy` module, used for creating copies of objects. However, 
    they have different behaviors and purposes:

    1. `copy` function:
    - The `copy` function creates a shallow copy of an object. 
    It means that a new object is created, but the content (i.e., the elements)
    of the object is not duplicated.
    - If the object being copied contains references to other objects,
    the references are copied, but the referred objects themselves are not cloned.
    - The copy is one level deep, so it only creates a new object with the
    same top-level elements, but nested elements are still referenced.

    2. `deepcopy` function:
    - The `deepcopy` function, as the name suggests, creates a deep copy of
    an object. It means that not only the top-level object but also all the nested
    objects are duplicated recursively.
    - If the object being copied contains references to other objects, `deepcopy`
    will also create new copies of those referred objects and all objects they refer
    to, ensuring that there are no shared references between the original and copied objects.
    - This function is useful when you want to create a completely independent and 
    isolated copy of an object, including all its nested data structures.

    Here's an example to illustrate the difference:"""

import copy

original_list = [[1, 2], [3, 4]]
shallow_copied_list = copy.copy(original_list)
deep_copied_list = copy.deepcopy(original_list)

# Modify the original list
original_list[0][0] = 100

print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)
print("Deep Copied List:", deep_copied_list)

'''
    Output:
    ```
    Original List: [[100, 2], [3, 4]]
    Shallow Copied List: [[100, 2], [3, 4]]
    Deep Copied List: [[1, 2], [3, 4]]
    ```

    As you can see, the `copy` function creates a shallow copy, so changing
    the nested element in the original list affects the shallow copied list 
    as well. However, the `deepcopy` function creates a completely independent
    copy, and the changes in the original list do not affect the deep copied list.'''