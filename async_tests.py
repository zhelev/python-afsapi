"""Test of the asynchronous Frontier Silicon interface."""
import asyncio
import traceback
import logging

from afsapi import AFSAPI

URL = 'http://192.168.1.183:80/device'
PIN = 1234
TIMEOUT = 2  # in seconds


async def test_sys():
    """ Test sys functions."""
    try:
        afsapi = await AFSAPI.create(URL, PIN, TIMEOUT)

        set_power = await afsapi.set_power(True)
        print('Set power succeeded? - %s' % set_power)

        power = await afsapi.get_power()
        print('Power on: %s' % power)

        set_friendly_name = await afsapi.set_friendly_name('Keuken')
        print('Set friendly name? - %s' % set_friendly_name)

        friendly_name = await afsapi.get_friendly_name()
        print('Friendly name: %s' % friendly_name)

        async for mode in afsapi.get_modes():
            print('Mode: %s' % mode)

        async for equaliser in afsapi.get_equalisers():
            print('Equaliser: %s' % equaliser)

        eqp = await afsapi.get_eq_preset()
        print('EQ Preset: %s' % eqp)

        mode = await afsapi.get_mode()
        print('Mode: %s' % mode)

        power = await afsapi.set_power(False)
        print('Set power succeeded? - %s' % set_power)

        set_sleep = await afsapi.set_sleep(10)
        print('Set sleep succeeded? - %s' % set_sleep)

        sleep = await afsapi.get_sleep()
        print('Sleep: %s' % sleep)

        power = await afsapi.get_power()
        print('Power on: %s' % power)
    except Exception:
        logging.error(traceback.format_exc())


async def test_volume():
    """ Test volume functions."""
    try:
        afsapi = await AFSAPI.create(URL, PIN, TIMEOUT)

        set_power = await afsapi.set_power(True)
        print('Set power succeeded? - %s' % set_power)

        power = await afsapi.get_power()
        print('Power on: %s' % power)

        volume = await afsapi.get_volume()
        print('Volume: %s' % volume)

        set_volume = await afsapi.set_volume(3)
        print('Set volume succeeded? - %s' % set_volume)

        volume_steps = await afsapi.get_volume_steps()
        print('Volume steps: % s' % volume_steps)

        mute = await afsapi.get_mute()
        print('Is muted: %s' % mute)

        power = await afsapi.set_power(False)
        print('Set power succeeded? - %s' % set_power)

        power = await afsapi.get_power()
        print('Power on: %s' % power)
    except Exception:
        logging.error(traceback.format_exc())


async def test_info():
    """ Test info functions."""
    try:
        afsapi = await  AFSAPI.create(URL, PIN, TIMEOUT)

        set_power = await afsapi.set_power(True)
        print('Set power succeeded? - %s' % set_power)

        power = await afsapi.get_power()
        print('Power on: %s' % power)

        name = await afsapi.get_play_name()
        print('Name: %s' % name)

        text = await afsapi.get_play_text()
        print('Text: %s' % text)

        artist = await afsapi.get_play_artist()
        print('Artist: %s' % artist)

        album = await afsapi.get_play_album()
        print('Album: %s' % album)

        graphic = await afsapi.get_play_graphic()
        print('Graphic: %s' % graphic)

        duration = await afsapi.get_play_duration()
        print('Duration: %s' % duration)

        power = await afsapi.set_power(False)
        print('Set power succeeded? - %s' % set_power)

        power = await afsapi.get_power()
        print('Power on: %s' % power)
    except Exception:
        logging.error(traceback.format_exc())


async def test_play():
    """ Test play functions."""
    try:
        afsapi = await AFSAPI.create(URL, PIN, TIMEOUT)

        status = await afsapi.get_play_status()
        print('Status: %s' % status)

        start_play = await afsapi.play()
        print('Start play succeeded? - %s' % start_play)
        await asyncio.sleep(1)

        forward = await afsapi.forward()
        print('Next succeeded? - %s' % forward)
        await asyncio.sleep(1)

        rewind = await afsapi.rewind()
        print('Prev succeeded? - %s' % rewind)

    except Exception:
        logging.error(traceback.format_exc())


loop = asyncio.new_event_loop()

loop.run_until_complete(test_sys())
loop.run_until_complete(test_volume())
loop.run_until_complete(test_play())
loop.run_until_complete(test_info())

