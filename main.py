import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk
import random
import os

import effects


class GridWindow(Gtk.Window):
    EXECUTABLE = 'ite8291r3-ctl'
    ROW_COUNT = 6
    COL_COUNT = 16

    colors = [[Gdk.RGBA] * COL_COUNT] * ROW_COUNT
    buttons = []

    def __init__(self):
        self.generate_colors()
        Gtk.Window.__init__(self, title="ite-8291 gui")
        print(effects.effects)

        grid = Gtk.Grid()
        grid.attach(self.create_quickselect(), 1, 1, 1, 1)
        #grid.attach(self.create_button_grid(), 1, 2, 1, 1)
        self.add(grid)

    def create_button_grid(self):
        grid = Gtk.Grid()
        for y in range(0, self.ROW_COUNT):
            row = []
            for x in range(0, self.COL_COUNT):
                button = Gtk.ColorButton()
                button.set_rgba(self.colors[y][x])
                button.connect("color-set", lambda user_data: self.on_color_chosen(button, x, y, user_data))
                row.append(button)
                grid.attach(button, x, y, 1, 1)
            self.buttons.append(row)

        return grid

    def create_quickselect(self):
        grid = Gtk.Grid(expand = True)
        combo_effect = Gtk.ComboBoxText()
        combo_effect.connect("changed", self.on_effect_select)

        for effect in effects.effects:
            combo_effect.append_text(effect)
        grid.add(combo_effect)

        speed = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, .5, 10.0, .1)
        grid.add(speed)

        color = Gtk.ColorButton()
        grid.add(color)

        direction = Gtk.ComboBoxText()
        for d in ["left", "right", "up", "down"]:
            direction.append_text(d)

        reactive = Gtk.Switch()
        grid.add(reactive)

        apply = Gtk.Button()
        grid.add(apply)

        return grid

    def on_effect_select(self, combo):
        effect = combo.get_active_text()
        if effect is not None:
            self.runEffect(effect)

    def generate_colors(self):
        for y in range(0, self.ROW_COUNT):
            for x in range(0, self.COL_COUNT):
                color = Gdk.RGBA()
                color.red = random.uniform(0, 1)
                color.green = random.uniform(0, 1)
                color.blue = random.uniform(0, 1)
                self.colors[y][x] = color
                print("at ", x, "/", y, ": ", color.to_string())

    def on_color_chosen(self, button, x, y, user_data):
        print("You chose the color: " + button.get_rgba().to_string())

    def runEffect(self, effect):
        os.system('{} effect {}'.format(self.EXECUTABLE, effect))


win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
