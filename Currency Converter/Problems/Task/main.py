class Task:
    def __init__(self, description, team):
        self.description = description
        self.team = team

    # create the method
    def __add__(self, other):
        return Task(f'{self.description}\n{other.description}', f'{self.team}, {other.team}')
