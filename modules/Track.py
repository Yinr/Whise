#!/usr/bin/python
# -*- coding: utf-8 -*-


from modules.Player import Player


class Track(Player):
    """
    音轨类
    """

    def __init__(self, music_path):
        super(Player, self).__init__()
        self.tag = None
        pass

    def set_tag(self, tag):
        self.tag = tag
        return self

    def get_tag(self):
        return self.tag
