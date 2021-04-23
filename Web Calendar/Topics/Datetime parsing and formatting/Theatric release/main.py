from datetime import datetime


def get_release_date(release_str):
    # return datetime.strptime(release_str.replace('Day of release: ', ''), "%d %B %Y")
    return datetime.strptime(release_str, "Day of release: %d %B %Y")
