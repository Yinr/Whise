#!/usr/bin/python
# -*- coding: utf-8 -*-


from Player import Player


class Track(Player):
    """
    音轨类
    """

    def __init__(self, music_path):
        super(Track, self).__init__(music_path)
        self.tag = None
        pass

    def set_tag(self, tag):
        self.tag = tag
        return self

    def get_tag(self):
        return self.tag
