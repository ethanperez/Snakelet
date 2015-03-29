# Snakelet - DigitalOcean API Wrapper

Snakelet is a straighforward wrapper for DigitalOcean's V2 API. It returns the raw JSON response from DigtialOcean without error catching or other manipulation. Its original purpose is to be used in [SeaSnake](https://github.com/ethanperez/SeaSnake), a DigitalOcean CLI.

If there's an API call for it on DigitalOcean, Snakelet has it wrapped.

## Installation

Snakelet can be installed via [pip](https://pypi.python.org/pypi/pip)

```
pip install snakelet
```

or [Easy Install](http://peak.telecommunity.com/DevCenter/EasyInstall)

```
easy_install snakelet
```

## Usage

```
from digitalocean import Snakelet

s = Snaklet(token)

# Get all droplets
s.droplets.all()

# Get a droplet by id
s.droplet.get(47362753)

# Reboot the droplet
s.droplet.reboot()
```
All of the wrapper calls will be available in documentation soon

## Todos

- Make use of kwargs. Currently, all arguments must be fulfilled by name.
- Testing suite
- Extensive documentation