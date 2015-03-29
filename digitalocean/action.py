from .api import SnakeletClass

class Action(SnakeletClass):

  def all(self, params = None, **kwargs):
    """ 
      Lists all actions that have been executed
      on the current account
    """
    if not params:
      params = kwargs

    return self.getHttp('actions', params)

  def get(self, id):
    """
      Retrieves a specific action object
    """
    return self.getHttp('actions/{:s}'.format(id))