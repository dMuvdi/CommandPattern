# Interface Operation (Command)
class IOperation(object):
    """
    Class used to represent an Interface of the operation to be executed
    """

    def __init__(self):
        pass

    def execute(self):
        raise Exception("NotImplementedException")

    def undo(self):
        raise Exception("NotImplementedException")
