from .api import SnakeletClass

class Key(SnakeletClass):

  def all(self):
    """
      List all keys
    """
    return self.getHttp('account/keys')

  def create(self, name, public_key):
    """
      Adds a SSH public key to DO
    """
    params = {"name": name,
              "public_key": public_key}

    return self.post('account/keys', params)

  def get(self, id = None, fingerprint = None):
    """
      Shows information about a key
    """
    # Default to using the fingerprint if there is one
    if fingerprint != None:
      return self.getHttp('account/keys/{:s}'.format(fingerprint))
    
    return self.getHttp('account/keys/{:s}'.format(id))

  def update(self, id = None, fingerprint = None, name):
    """
      Updates the name of an SSH key
    """
    params = {'name': name}

    # Default to using the fingerprint if there is one
    if fingerprint != None:
      return self.put('account/keys/{:s}'.format(fingerprint), params)
    
    return self.put('account/keys/{:s}'.format(id), params)

  def delete(self, id = None, fingerprint = None):
    """
      Deletes a public SSH key
    """
    # Default to using the fingerprint if there is one
    if fingerprint != None:
      return self.delete('account/keys/{:s}'.format(fingerprint))
    
    return self.delete('account/keys/{:s}'.format(id))