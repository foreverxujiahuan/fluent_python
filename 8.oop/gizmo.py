class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))


if __name__ == '__main__':
    print(dir())
    x = Gizmo()
    # y = Gizmo()*10
    print(dir())
