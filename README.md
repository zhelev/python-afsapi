# python-afsapi

Asynchronous Python implementation of the Frontier Silicon API
- This project was started in order to embed Frontier Silicon devices in Home Assistant (https://home-assistant.io/)
- Inspired by:
 - https://github.com/flammy/fsapi/
 - https://github.com/tiwilliam/fsapi
 - https://github.com/p2baron/fsapi

Required python libs:
  - requests

Usage
=====

```python
import asyncio
from afsapi import AFSAPI

URL = 'http://192.168.1.XYZ:80/device'
PIN = 1234
TIMEOUT = 1 # in seconds

async def test():
    afsapi = await AFSAPI.create(URL, PIN, TIMEOUT)

    print(f'Set power succeeded? - {await afsapi.set_power(True)}' )
    print(f'Power on: {await afsapi.get_power()}')
    print(f'Friendly name: {await afsapi.get_friendly_name()}')

    for mode in await afsapi.get_modes():
        print(f'Available Mode: {mode}')
    print(f'Current Mode: {await afsapi.get_mode()}')

    for equaliser in await afsapi.get_equalisers():
        print(f'Equaliser: {equaliser}')

    print(f'EQ Preset: {await afsapi.get_eq_preset()}' )

    for preset in await afsapi.get_presets():
        print(f"Preset: {preset}")

    print(f'Set power succeeded? - {await afsapi.set_power(False)}')
    print(f'Set sleep succeeded? - {await afsapi.set_sleep(10)}')
    print(f'Sleep: {await afsapi.get_sleep()}')
    print(f'Get power {await afsapi.get_power()}' )


loop = asyncio.new_event_loop()
loop.run_until_complete(test())

```