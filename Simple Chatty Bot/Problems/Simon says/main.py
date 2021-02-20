def what_to_do(instructions):
    string = 'Simon says'
    index = len(string)

    # starts with Simon says
    if instructions.startswith(string):
        return 'I ' + instructions[index:].strip()
    # ends with Simon says
    elif instructions.endswith(string):
        return 'I ' + instructions[:-index].strip()
    else:
        return "I won't do it!"
