"""Provides the constants needed for this component."""
from enum import StrEnum

DOMAIN = "shairport_sync"

class TopLevelTopic(StrEnum):
    """Top level topics for Shairport Sync."""

    ARTIST = "artist"
    ALBUM = "album"
    COVER = "cover"
    PLAY_END = "play_end"
    PLAY_FLUSH = "play_flush"
    PLAY_START = "play_start"
    PLAY_RESUME = "play_resume"
    PLAY_STREAM_RESUME = "ssnc/prsm"
    PLAY_STREAM_PAUSE = "ssnc/paus"
    PLAY_PROGRESS = "ssnc/prgr"
    ACTIVE_END = "active_end"
    TITLE = "title"
