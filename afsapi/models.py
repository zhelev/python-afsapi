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


@dataclass
class PlayerMode:
    id: str
    label: str
    key: str
    selectable: t.Optional[int] = None
    streamable: t.Optional[int] = None
    modetype: t.Optional[int] = None


@dataclass
class Equaliser:
    key: str
    label: str


@dataclass
class Preset:
    key: int
    type: t.Optional[str] = None
    name: t.Optional[str] = None
