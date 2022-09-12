from typing import List
from iOperation import IOperation

# Invoker


class Invoker(object):
    """
    Class used to represent the Invoker
    """

    operations = list()

    def recieveOperation(self, operation: IOperation):
        """ Adds the given operation the operations list.
        """
        self.operations.append(operation)

    def doOperations(self):
        """ Loops through the operations list and executes all of them.
        """
        for x in self.operations:
            x.execute()

    def undoOperations(self):
        """ Loops through the operations list backwards and undoes all of them.
        """
        for x in reversed(self.operations):
            x.undo()
            del x
