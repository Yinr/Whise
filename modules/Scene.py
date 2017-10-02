#!/usr/bin/python
# -*- coding: utf-8 -*-


from modules.Player import Player


class Scene(Player):
    """
    场景类
    """

    def __init__(self):
        super(Player, self).__init__()
        self.scene_name = None
        self.scene_description = None
        self.scene_category = None
        self.track_ = []
        pass

    def set_scene_name(self, scene_name):
        self.scene_name = scene_name
        return self

    def get_scene_name(self):
        return self.scene_name

    def set_scene_description(self, scene_description):
        self.set_scene_description = scene_description
        return self

    def get_scene_description(self):
        return self.scene_description

    def set_scene_category(self, scene_category):
        self.scene_category = scene_category
        return self

    def get_scene_category(self):
        return self.scene_category

    def add_track(self, track):
        self.track_.append(track)
        return self

    def del_track(self, track):
        self.track_.remove(track)
        return self
