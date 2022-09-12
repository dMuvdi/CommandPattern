# Client
from invoker import Invoker
from putCommand import PutCommand
from retireCommand import RetireCommand
from account import Account

account = Account(2, 200)

putCommand = PutCommand(account, 100)

retireCommand = RetireCommand(account, 50)

ivk = Invoker()

ivk.recieveOperation(putCommand)
ivk.recieveOperation(retireCommand)

ivk.doOperations()
ivk.undoOperations()

"""
Console Result:

[Put Command] Account: 2 Mount: 300
[Retire Command] Account: 2 Mount: 250 
[Put Command] Account: 2 Mount: 300   
[Retire Command] Account: 2 Mount: 200

"""
