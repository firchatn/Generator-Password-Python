import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def getpass(self, butgenerator):
        print("generator password")
        
    def savepass(self, butsave):
        print("save password")
        
    def resetpass(self, butreset):
        print("reset password")
            


builder = Gtk.Builder()
builder.add_from_file("generator-layout.glade")
builder.connect_signals(Handler())

window = builder.get_object("dialog1")
window.connect("delete-event", Gtk.main_quit)
window.set_default_size(400, 300)
window.show_all()


Gtk.main()

