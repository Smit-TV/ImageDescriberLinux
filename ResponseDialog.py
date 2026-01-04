import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class ResponseDialog(Gtk.Window):
    def __init__(self, response):
        super().__init__()
        self.set_default_size(300, 400)
        self.set_title("Image Describer")
        box = Gtk.ScrolledWindow()
        self.add(box)
        label = Gtk.TextView()
        label.set_accepts_tab(True)
        #label.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)
        label.get_buffer().set_text(response)
        box.add(label)
        self.connect("destroy", Gtk.main_quit)

    def create(self):
        self.show_all()
        Gtk.main()