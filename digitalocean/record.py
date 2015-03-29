from .api import SnakeletClass

class Record(SnakeletClass):

  def all(self, name):
    """
      Gets a listing of all records
      configured for a domain
    """
    return self.getHttp('domains/{:s}/records'.format(name))

  def create(self, type, name, data, priority = None, port = None, weight = None):
    """
      Creates a new record to a domain
    """
    params = {'type': type,
              'name': name,
              'data': data,
              'priority': priority,
              'port': port,
              'weight': weight}

    return self.post('domains/{:s}'.format(name), params)

  def get(self, name, id):
    """
      Retrieves a speciic domain record
    """
    return getHttp('domains/{:s}/records/{:s}'.format(name, id))

  def update(self, id, domain, type = None, name = None, data = None, priorty = None,
             port = None, weight = None):
    """
      Updates an existing record
    """
    params = {'type': type,
              'name': name,
              'data': data,
              'priority': priority,
              'port': port,
              'weight': weight}

    return self.put('domains/{:s}/records/{:s}'.format(domain, id), params)

  def delete(self, name, id):
    """
      Deletes a record for a domain
    """
    return self.delete('domains/{:s}/records/{:s}'.format(name, id))