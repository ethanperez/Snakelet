from .api import SnakeletClass

class Size(SnakeletClass):

  def all(self):
    """
      List all of available sizes
    """
    return self.getHttp('sizes')