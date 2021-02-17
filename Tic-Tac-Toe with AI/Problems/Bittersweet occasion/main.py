# finish the function
def find_the_parent(child):
    for parent_class in (Drinks, Pastry, Sweets):
        if issubclass(child, parent_class):
            print(parent_class.__name__)
            break



