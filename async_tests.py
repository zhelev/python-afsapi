"""Test of the asynchronous Frontier Silicon interface."""
import asyncio
import traceback
import logging

from afsapi import AFSAPI

URL = "http://192.168.1.183:80/device"
PIN = 1234
TIMEOUT = 2  # in seconds


async def test_sys():
    """Test sys functions."""
    try:
        afsapi = await AFSAPI.create(URL, PIN, TIMEOUT)

        print(f"Set power succeeded? - {await afsapi.set_power(True)}")
        print(f"Power on: {await afsapi.get_power()}")
        print(f"Friendly name: {await afsapi.get_friendly_name()}")
        for mode in await afsapi.get_modes():
            print(f"Available Mode: {mode}")
        print(f"Current Mode: {await afsapi.get_mode()}")

        for equaliser in await afsapi.get_equalisers():
            print(f"Equaliser: {equaliser}")

        print(f"EQ Preset: {await afsapi.get_eq_preset()}")

        for preset in await afsapi.get_presets():
            print(f"Preset: {preset}")

        print(f"Set power succeeded? - {await afsapi.set_power(False)}")
        print(f"Set sleep succeeded? - {await afsapi.set_sleep(10)}")
        print(f"Sleep: {await afsapi.get_sleep()}")
        print(f"Get power {await afsapi.get_power()}")
    except Exception:
        logging.error(traceback.format_exc())


async def test_volume():
    """Test volume functions."""
    try:
        afsapi = await AFSAPI.create(URL, PIN, TIMEOUT)

        set_power = await afsapi.set_power(True)
        print("Set power succeeded? - %s" % set_power)

        power = await afsapi.get_power()
        print("Power on: %s" % power)

        volume = await afsapi.get_volume()
        print("Volume: %s" % volume)

        set_volume = await afsapi.set_volume(3)
        print("Set volume succeeded? - %s" % set_volume)

        volume_steps = await afsapi.get_volume_steps()
        print("Volume steps: % s" % volume_steps)

        mute = await afsapi.get_mute()
        print("Is muted: %s" % mute)

        power = await afsapi.set_power(False)
        print("Set power succeeded? - %s" % set_power)

        power = await afsapi.get_power()
        print("Power on: %s" % power)
    except Exception:
        logging.error(traceback.format_exc())


async def test_info():
    """Test info functions."""
    try:
        afsapi = await AFSAPI.create(URL, PIN, TIMEOUT)

        set_power = await afsapi.set_power(True)
        print("Set power succeeded? - %s" % set_power)

        power = await afsapi.get_power()
        print("Power on: %s" % power)

        print(f"Radio ID: {await afsapi.get_radio_id()}")
        print(f"Version: {await afsapi.get_version()}")

        name = await afsapi.get_play_name()
        print("Name: %s" % name)

        text = await afsapi.get_play_text()
        print("Text: %s" % text)

        artist = await afsapi.get_play_artist()
        print("Artist: %s" % artist)

        album = await afsapi.get_play_album()
        print("Album: %s" % album)

        graphic = await afsapi.get_play_graphic()
        print("Graphic: %s" % graphic)

        duration = await afsapi.get_play_duration()
        print("Duration: %s" % duration)

        # power = await afsapi.set_power(False)
        # print('Set power succeeded? - %s' % set_power)

        # power = await afsapi.get_power()
        # print('Power on: %s' % power)
    except Exception:
        logging.error(traceback.format_exc())


async def test_play():
    """Test play functions."""
    try:
        afsapi = await AFSAPI.create(URL, PIN, TIMEOUT)

        status = await afsapi.get_play_status()
        print("Status: %s" % status)

        start_play = await afsapi.play()
        print("Start play succeeded? - %s" % start_play)
        await asyncio.sleep(1)

        forward = await afsapi.forward()
        print("Next succeeded? - %s" % forward)
        await asyncio.sleep(1)

        rewind = await afsapi.rewind()
        print("Prev succeeded? - %s" % rewind)

    except Exception:
        logging.error(traceback.format_exc())


loop = asyncio.new_event_loop()

loop.run_until_complete(test_sys())
loop.run_until_complete(test_volume())
loop.run_until_complete(test_play())
loop.run_until_complete(test_info())
