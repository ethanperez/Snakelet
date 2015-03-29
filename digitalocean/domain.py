from .api import SnakeletClass

class Domain(SnakeletClass):

  def all(self):
    """
      Retrieves a list of all of domains in account
    """
    return self.getHttp('domains')

  def create(self, name, ip):
    """
      Creates a new domain
    """
    params = {'name': name, 
              'ip_address': ip}

    return self.post('domains', params)

  def get(self, domain):
    """
      Gets details about a specific domain
    """
    return self.getHttp('domains/{:s}'.format(domain))

  def delete(self, domain):
    """
      Deletes a specific domain
    """
    return self.delete('domains/{:s}'.format(domain))