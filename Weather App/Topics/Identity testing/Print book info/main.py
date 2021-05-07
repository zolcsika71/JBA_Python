def print_book_info(title, author=None, year=None):
    print(f'"{title}"'
          f'{" was written by" if author is not None else ""}'
          f'{(" " + author) if author is not None else ""}'
          f'{" was written" if author is None and year is not None else ""}'
          f'{(" in " + year) if year is not None else ""}')


