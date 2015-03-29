from .api import SnakeletClass

class Account(SnakeletClass):

  def all(self):
    """
      Returns the user's information
    """
    return self.getHttp('account')