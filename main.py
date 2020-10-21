import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class GridWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="ite-8291 gui")

        grid = Gtk.Grid()
        self.add(grid)

        buttons = []
        for y in range(0, 6):
            row = []
            for x in range(0, 16):
                button = Gtk.Button(label="{0}/{1}".format(x, y))
                row.append(button)
                grid.attach(button, x, y, 1, 1)
            buttons.append(row)


win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
