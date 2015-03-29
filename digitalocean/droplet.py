from .api import SnakeletClass

class Droplet(SnakeletClass):

  def create(self, name, region, size, image, ssh_keys = None, backups = False,
             ipv6 = True, private_networking = None, user_data = None):
    """
      Creates a new Droplet
    """
    params = {'name': name,
              'region': region,
              'size': size,
              'image': image,
              'ssh_keys': ssh_keys,
              'backups': backups,
              'ipv6': ipv6,
              'private_networking': private_networking,
              'user_data': user_data}

    return self.post('droplets', params)

  def get(self, droplet):
    """
      Get an individual droplet
    """
    return self.getHttp('droplets/{:s}'.format(droplet))

  def all(self):
    """
      Lists all Droplets
    """
    return self.getHttp('droplets')

  def kernals(self, droplet):
    """
      Retrieves a list of all kernals
      available to a Droplet
    """
    return self.getHttp('droplets/{:s}/kernals'.format(droplet))

  def snapshots(self, droplet):
    """
      Retrieves the snapshots that have
      been created for a Droplet
    """
    return self.getHttp('droplets/{:s}/snapshots'.format(droplet))

  def backups(self, droplet):
    """
      Retrieves any backups associated 
      with a Droplet
    """
    return self.getHttp('droplets/{:s}/backups'.format(droplet))

  def actions(self, droplet):
    """
      Retrieves all actions that have
      been executed on a Droplet
    """
    return self.getHttp('droples/{:s}/actions'.format(droplet))

  def delete(self, droplet):
    """
      Deletes a Droplet
    """
    return self.delete('droplets/{:s}'.format(droplet))

  """
    These are individual droplet actions
  """

  def disable_backups(self, droplet):
    """
      Disables backups on an exisitng droplet
    """
    params = {'type': 'disable_backups'}

    return self.post('droplets/{:s}/actions'.format(droplet), params)

  def reboot(self, droplet):
    """
      Reboots a Droplet
    """
    params = {'type': 'reboot'}

    return self.post('droplets/{:s}/actions'.format(droplet), params)

  def power_cycle(self, droplet):
    """
      Power cycles a Droplet
    """
    params = {'type': 'power_cycle'}

    return self.post('droplets/{:s}/actions'.format(droplet), params)

  def shutdown(self, droplet):
    """
      Shutsdown a Droplet
    """
    params = {'type': 'shutdown'}

    return self.post('droplets/{:s}/actions'.format(droplet), params)

  def power_off(self, droplet):
    """
      Powers off a Droplet
    """
    params = {'type': 'power_off'}

    return self.post('droplets/{:s}/actions'.format(droplet), params)

  def power_on(self, droplet):
    """
      Powers on a Droplet
    """
    params = {'type': 'power_on'}

    return self.post('droplets/{:s}/actions'.format(droplet), params)

  def restore(self, droplet, image):
    """
      Restores a Droplet
    """
    params = {'type': 'reboot',
              'image': image}

    return self.post('droplets/{:s}/actions'.format(droplet), params)

  def password_reset(self, droplet):
    """
      Resets the password for a Droplet
    """
    params = {'type': 'password_reset'}

    return self.post('droplets/{:s}/actions'.format(droplet), params)

  def resize(self, droplet, disk = None, size):
    """
      Resizes a Droplet
    """
    params = {'type': 'resize',
              'disk': disk,
              'size': size}

    return self.post('droplets/{:s}/actions'.format(droplet), params)

  def rebuild(self, droplet, image):
    """
      Rebuilds a Droplet
    """
    params = {'type': 'rebuild',
              'image': image}

    return self.post('droplets/{:s}/actions'.format(droplet), params)

  def rename(self, droplet, name):
    """
      Renmaes a Droplet
    """
    params = {'type': rename,
              'name': name}

    return self.post('droples/{:s}/actions'.format(droplet), params)

  def change_kernal(self, droplet, kernal):
    """
      Changes the kernal of a Droplet
    """
    params = {'type': rename,
              'kernal': kernal}

    return self.post('droples/{:s}/actions'.format(droplet), params)

  def enable_ipv6(self, droplet):
    """
      Enables ipv6 for a Droplet
    """
    params = {'type': 'enable_ipv6'}

    return self.post('droplets/{:s}/actions'.format(droplet), params)

  def enable_private_networking(self, droplet):
    """
      Enables private networking for a Droplet
    """
    params = {'type': 'enable_private_networking'}

    return self.post('droplets/{:s}/actions'.format(droplet), params)

  def snapshot(self, droplet):
    """
      Snapshots a Droplet
    """
    params = {'type': 'snaptshot'}

    return self.post('droplets/{:s}/actions'.format(droplet), params)

  def upgrade(self, droplet):
    """
      Upgrades a Droplet
    """
    params = {'type': 'upgrade'}

    return self.post('droplets/{:s}/actions'.format(droplet), params)

  def action(self, droplet, action):
    """
      Retrieves a Droplet action
    """
    return self.getHttp('droplets/{:s}/actions/{:s}'.format(droplet, action))