def list_sum(some_list):
    if not some_list:
        return 0
    return some_list.pop() + list_sum(some_list)
