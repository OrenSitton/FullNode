"""
Author: Oren Sitton
File: Dependencies\\__init__.py
Python Version: 3
Description: init file is used by other files to import functions & classes from folder
"""
try:
    from Dependencies.Blockchain import Blockchain
    from Dependencies.Block import Block
    from Dependencies.SyncedArray import SyncedArray
    from Dependencies.Transaction import Transaction
    from Dependencies.SyncedDictionary import SyncedDictionary

    from Dependencies.methods import *

except ModuleNotFoundError:
    from FullNode.Dependencies.Blockchain import Blockchain
    from FullNode.Dependencies.Block import Block
    from FullNode.Dependencies.SyncedArray import SyncedArray
    from FullNode.Dependencies.Transaction import Transaction
    from FullNode.Dependencies.SyncedDictionary import SyncedDictionary

    from FullNode.Dependencies.methods import *
