# -*- coding: utf-8 -*-
# flake8: noqa: F401
# noreorder
"""
Pytube: a very serious Python library for downloading YouTube Videos.
"""
__title__ = "pytubeX"
__author__ = "Max Booth, Nick Ficano, Harold Martin"
__license__ = "MIT License"
__copyright__ = "Copyright 2020 Max Booth"

from pytube.version import __version__
from pytube.streams import Stream
from pytube.captions import Caption
from pytube.query import CaptionQuery
from pytube.query import StreamQuery
from pytube.__main__ import YouTube
from pytube.contrib.playlist import Playlist
