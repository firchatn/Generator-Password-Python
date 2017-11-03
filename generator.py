import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import random


class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def getpass(self, butgenerator):
        print("generator password")
        changeBuff()
        
    def savepass(self, butsave):
        print("save password")
        
    def resetpass(self, butreset):
        print("reset password")
        label = builder.get_object("label2")
        label.set_text("Password : ")
            

def changeBuff():
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pw_length = 8
    mypw = ""
    for i in range(pw_length):
        next_index = random.randrange(len(alphabet))
        mypw = mypw + alphabet[next_index]

    label = builder.get_object("label2")
    label.set_text("Password : "+ mypw)
    
builder = Gtk.Builder()
builder.add_from_file("generator-layout.glade")
builder.connect_signals(Handler())

window = builder.get_object("dialog1")
window.connect("delete-event", Gtk.main_quit)
window.set_default_size(400, 300)
window.show_all()


Gtk.main()

