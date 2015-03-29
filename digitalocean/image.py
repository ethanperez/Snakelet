from .api import SnakeletClass

class Image(SnakeletClass):

  def all(self):
    """
      List all images available
    """
    return self.getHttp('images')

  def allDist(self):
    """
      List all distribution images
    """
    return self.getHttp('images?type=distribution')

  def allApp(self):
    """
      List all application images
    """
    return self.getHttp('images?type=application')

  def allUsers(self):
    """
      List all user images
    """
    return self.getHttp('images?private=true')

  def getById(self, id):
    """
      Retrieve an image by slug
    """
    return self.getHttp('images/{:s}'.format(id))

  def getBySlug(self, slug):
    """
      Retrieves an image by slug
    """
    return self.getHttp('images/{:s}'.format(slug))

  def actions(self, image):
    """
      Retrieves all actions that have
      been executed on an image
    """
    return self.getHttp('images/{:s}/actions'.format(image))

  def update(self, image, name):
    """
      Updates an image
    """
    params = {'name': name}

    return self.put('images/{:s}'.format(image), params)

  def delete(self, image):
    """
      Deletes an image
    """
    return self.delete('images/{:s}'.format(image))

  def transfer(self, image, region):
    """
      Transfers an image
    """
    params = {'type': 'transfer',
              'region': region}

    return self.post('images/{:s}/actions'.format(image), params)

  def action(self, image, action):
    """
      Retrieves the status of an image action
    """
    return self.getHttp('images/{:s}/actions/{:s}'.format(image, action))