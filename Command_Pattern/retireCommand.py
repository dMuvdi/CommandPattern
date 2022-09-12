from iOperation import IOperation
from account import Account

# Concrete Command 2


class RetireCommand(IOperation):
    """
    Class used to represent the Retire
    """

    def __init__(self, account: Account, mount: float):
        """ PutCommand constructor object.
        :param account: account object to be used in the execute method.
        :type account: Account
        :param mount: how much money we want to put in our account.
        :type mount: float 
        :returns: PutCommand object inheriting from IOperation
        :rtype: object
        """
        self.account = account
        self.mount = mount

    def execute(self):
        """ Executes the retire method from the Account class itself.
        """
        self.account.retire(self.mount)

    def undo(self):
        """ Executes the put method from the Account class itself.
        """
        self.account.put(self.mount)
