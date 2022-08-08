def test(*args):
    print(len(args))
    print(args)
    print(*args)

def test2(sensors=None):
    print(sensors)
    if sensors != None:
        print(" not equal to None")
        # Checks if the variable is a list
        if type(sensors) == list:
            # It is a list. Checks if it is a 2D list
            if isinstance(sensors[0], list):
                print('2d list')
            # it is a 1D list
            else:
                print('1d list')
        # It's not a list. Checks if it is an integer
        else:
            if isinstance(sensors, int):
                print('is an integer')
                # sensors are stored as a list, so change the int to a list
                sensors = [sensors]
                print(sensors)


test2()
test2(1)
test2([2])
test2([[1,2], [3]])
test2(1,2)
