#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
播放器类
"""
class Player(object):

    def __init__(self):
        self.volume = 0
        pass

    def play(self):
        pass

    def pause(self):
        pass

    def set_volume(self, scatter):
        self.volume = scatter()
        return self

    def get_volume(self):
        self.volume
