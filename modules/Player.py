#!/usr/bin/python
# -*- coding: utf-8 -*-

from pygame import mixer

class Player(object):
    """
    播放器类
    """

    def __init__(self, music_path):
        self.volume = 0
        mixer.init()
        mixer.music.load(music_path)
        pass

    def play(self):
        mixer.music.play()
        return self

    def pause(self):
        mixer.music.pause()
        return self

    def unpause(self):
        mixer.music.unpause()
        return self

    def stop(self):
        mixer.music.stop()
        return self

    def set_volume(self, scatter):
        self.volume = scatter()
        return self

    def get_volume(self):
        return self.volume
