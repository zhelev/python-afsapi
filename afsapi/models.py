import typing as t
from enum import IntEnum
from dataclasses import dataclass


class PlayState(IntEnum):
    STOPPED = 0
    LOADING = 1
    PLAYING = 2
    PAUSED = 3


class PlayControl(IntEnum):
    PLAY = 1
    PAUSE = 2
    NEXT = 3
    """
    Media Player: next item in playlist (wraps around to begin of playlist)
    Radio: Next available radio on higher frequency
    """
    PREV = 4
    """
    Media Player: prvious item in playlist (wraps around to end of playlist)
    Radio: Next available radio on lower frequency
    """


class EQPreset(IntEnum):
    MY_EQ = 0
    NORMAL = 1
    FLAT = 2
    JAZZ = 3
    ROCK = 4
    MOVIE = 5
    CLASSIC = 6
    POP = 7
    NEWS = 8


@dataclass
class PlayerMode:
    id: str
    selectable: int
    label: str
    streamable: int
    modetype: int
    key: str

@dataclass
class Equaliser:
    key: str
    label: str


@dataclass
class Preset:
    key: int
    type: str
    name: t.Optional[str]
