from sys import exit

class Scene(object):

    def enter(self):
        print "Not yet classified."
        exit(0)
        pass


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
        pass

    def play(self):
        present_scene = self.scene_map.opening_scene()
        final_scene = self.scene_map.next_scene('finish')

        while present_scene != final_scene:
            next_scene_name = present_scene.enter()
            present_scene = self.scene_map.next_scene(next_scene_name)

        present_scene.enter()
        pass


class Death(Scene):

    def enter(self):
        print "You have died because of your imperfect holiness and the Christian Armor."
        exit(0)
        pass


class CentralCorridor(Scene):

    def enter(self):
        pass


class LaserWeaponArmory(Scene):

    def enter(self):
        pass


class TheBridge(Scene):

    def enter(self):
        pass


class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
