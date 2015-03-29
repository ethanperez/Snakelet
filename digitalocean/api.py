from __future__ import unicode_literals
from urlparse import urljoin

import json
import requests

class SnakeletClass(object):
  """
    This class instantiates the DO API via http methods
  """
  def __init__(self, token = None):
    """
      Sets token, header, and endpoint variables
    """
    self.token = token
    self.header = {}
    self.header['Authorization'] = "Bearer {:s}".format(self.token)
    self.header['Content-Type'] = "application/json"
    # Delete returns only a status code
    self.deleteHeader = {}
    self.deleteHeader['Authorization'] = "Bearer {:s}".format(self.token)
    self.doURL = 'https://api.digitalocean.com/v2/'

  def getHttp(self, url, params = None):
    """
      Base GET method
    """
    if not params:
      params = {}

    get = requests.get(self.doURL + url, params = params, headers = self.header).json()

    # check for error messages
    if ('message', 'id') in get:
      raise ValueError("{:s}: {:s}".format(get['id'], get['message']))

    return get

  def delete(self, url):
    """
      Base DELETE method
    """
    delete = requests.delete(self.doURL + url, headers = self.deleteHeader)

    # check for proper code
    if delete.status_code != 204:
      return ValueError("Deletion was unsuccessful")

    return "{:d}: Deletion was successful".format(delete.status_code)

  def put(self, url, params = None):
    """
      Base PUT method
    """
    if not params:
      params = {}

    put = requests.put(self.doURL + url, data = json.dumps(params), headers = self.header).json()

    return put

  def post(self, url, params = None):
    """
      Base POST method
    """
    if not params:
      params = {}

    post = requests.post(self.doURL + url, data = json.dumps(params), headers = self.header).json()

    return post

  def head(self, url):
    """
      Base HEAD method
    """
    return requests.head(url, headers = self.header).json()