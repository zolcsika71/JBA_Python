# check whether SuperRobot is a subclass of AstromechDroid,
# MedicalDroid, BattleDroid, and PilotDroid

# the order is IMPORTANT


if issubclass(SuperRobot, AstromechDroid):
    print('True')
else:
    print('False')
if issubclass(SuperRobot, MedicalDroid):
    print('True')
else:
    print('False')
if issubclass(SuperRobot, BattleDroid):
    print('True')
else:
    print('False')
if issubclass(SuperRobot, PilotDroid):
    print('True')
else:
    print('False')




