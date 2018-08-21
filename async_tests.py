"""Test of the asynchronous Frontier Silicon interface."""
import asyncio
from afsapi import AFSAPI

URL = 'http://192.168.0.66:80/device'
PIN = 1234


@asyncio.coroutine
def test_sys():
    """Test sys functions."""
    afsapi = AFSAPI(URL, PIN)

    set_power = yield from afsapi.set_power(True)
    print('Set power succeeded? - %s' % set_power)

    power = yield from afsapi.get_power()
    print('Power on: %s' % power)

    end_point = yield from afsapi.get_fsapi_endpoint()
    print('Endpoint: %s' % end_point)

    set_friendly_name = yield from afsapi.set_friendly_name('Badezimmer')
    print('Set friendly name? - %s' % set_friendly_name)

    friendly_name = yield from afsapi.get_friendly_name()
    print('Friendly name: %s' % friendly_name)

    modes = yield from afsapi.get_modes()
    print('Modes: %s' % modes)

    mode_list = yield from afsapi.get_mode_list()
    print('Mode List: %s' % mode_list)

    equalisers = yield from afsapi.get_equalisers()
    print('Equaliser: %s' % equalisers)

    equaliser_list = yield from afsapi.get_equaliser_list()
    print('Equaliser List: %s' % equaliser_list)

    mode = yield from afsapi.get_mode()
    print('Mode: %s' % mode)

    power = yield from afsapi.set_power(False)
    print('Set power succeeded? - %s' % set_power)

    set_sleep = yield from afsapi.set_sleep(10)
    print('Set sleep succeeded? - %s' % set_sleep)

    sleep = yield from afsapi.get_sleep()
    print('Sleep: %s' % sleep)

    power = yield from afsapi.get_power()
    print('Power on: %s' % power)


@asyncio.coroutine
def test_volume():
    """Test volume functions."""
    afsapi = AFSAPI(URL, PIN)

    set_power = yield from afsapi.set_power(True)
    print('Set power succeeded? - %s' % set_power)

    power = yield from afsapi.get_power()
    print('Power on: %s' % power)

    volume = yield from afsapi.get_volume()
    print('Volume: %s' % volume)

    set_volume = yield from afsapi.set_volume(3)
    print('Set volume succeeded? - %s' % set_volume)

    volume_steps = yield from afsapi.get_volume_steps()
    print('Volume steps: % s' % volume_steps)

    mute = yield from afsapi.get_mute()
    print('Is muted: %s' % mute)

    power = yield from afsapi.set_power(False)
    print('Set power succeeded? - %s' % set_power)

    power = yield from afsapi.get_power()
    print('Power on: %s' % power)


@asyncio.coroutine
def test_info():
    """Test info functions."""
    afsapi = AFSAPI(URL, PIN)

    set_power = yield from afsapi.set_power(True)
    print('Set power succeeded? - %s' % set_power)

    power = yield from afsapi.get_power()
    print('Power on: %s' % power)

    name = yield from afsapi.get_play_name()
    print('Name: %s' % name)

    text = yield from afsapi.get_play_text()
    print('Text: %s' % text)

    artist = yield from afsapi.get_play_artist()
    print('Artist: %s' % artist)

    album = yield from afsapi.get_play_album()
    print('Album: %s' % album)

    graphic = yield from afsapi.get_play_graphic()
    print('Graphic: %s' % graphic)

    duration = yield from afsapi.get_play_duration()
    print('Duration: %s' % duration)

    power = yield from afsapi.set_power(False)
    print('Set power succeeded? - %s' % set_power)

    power = yield from afsapi.get_power()
    print('Power on: %s' % power)


@asyncio.coroutine
def test_play():
    """Test play functions."""
    afsapi = AFSAPI(URL, PIN)

    status = yield from afsapi.get_play_status()
    print('Status: %s' % status)

    anext = yield from afsapi.forward()
    print('Next succeeded? - %s' % anext)

    prev = yield from afsapi.rewind()
    print('Prev succeeded? - %s' % prev)

LOOP = asyncio.get_event_loop()

LOOP.run_until_complete(test_sys())
LOOP.run_until_complete(test_volume())
LOOP.run_until_complete(test_play())
LOOP.run_until_complete(test_info())

LOOP.close()
