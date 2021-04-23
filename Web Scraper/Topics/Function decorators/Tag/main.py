def tagged(func):
    def wrapper(arg):
        return '<title>' + func(arg) + '</title>'

    return wrapper
