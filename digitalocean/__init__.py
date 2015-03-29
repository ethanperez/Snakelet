from .account import Account
from .actions import Action
from .domain import Domain
from .record import Record
from .droplet import Droplet
from .image import Image
from .key import Key
from .region import Region
from .size import Size

class Snakelet(object):
  """
    Public loaded class for Snakelet
  """
  def __init__(self, token = None):
    self.account = Account(token)
    self.action = Action(token)
    self.domain = Domain(token)
    self.record = Record(token)
    self.droplet = Droplet(token)
    self.image = Image(token)
    self.key = Key(token)
    self.region = Region(token)
    self.size = Size(token)
