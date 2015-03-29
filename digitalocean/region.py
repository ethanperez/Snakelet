from .api import SnakeletClass

class Region(SnakeletClass):

  def all(self):
    """
      List all of available regions
    """
    return self.getHttp('regions')