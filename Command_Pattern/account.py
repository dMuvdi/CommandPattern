# Reciever
class Account(object):
    """
    Class used to represent an Account
    """

    def __init__(self, id: int, mount: float):
        """ Account constructor object.
        :param id: id of the account.
        :type id: int
        :param mount: how much money we have in the account.
        :type mount: float 
        :returns: Account object
        :rtype: object
        """
        self.id = id
        self.mount = mount

    def retire(self, mount: float):
        """ Prints the retire command action subtracting the mount from the account.
        """
        self.mount = self.mount - mount
        print("[Retire Command] Account: " +
              str(self.id)+" Mount: "+str(self.mount))

    def put(self, mount: float):
        """ Prints the put command action adding the mount to the account.
        """
        self.mount = self.mount + mount
        print("[Put Command] Account: " +
              str(self.id)+" Mount: "+str(self.mount))
