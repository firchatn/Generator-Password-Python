import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

import random
 
passToSave = ''

"""
    Class Handler events : Lisente event 
    button of app
"""

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def getpass(self, butgenerator):
        print("generator password")
        changeBuff()
        
    def savepass(self, butsave):
        print("save password")
        file = open("password.txt","w")
        print(passToSave)
        file.write(passToSave)
        
    def resetpass(self, butreset):
        print("reset password")
        label = builder.get_object("label2")
        label.set_text("Password : ")
            

def changeBuff():
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pw_length =12
    mypw = ""
    for i in range(pw_length):
        next_index = random.randrange(len(alphabet))
        mypw = mypw + alphabet[next_index]
    global passToSave
    passToSave = mypw
    label = builder.get_object("label2")
    label.set_text("Password : "+ mypw)



builder = Gtk.Builder()
builder.add_from_file("generator-layout.glade")
builder.connect_signals(Handler())

Mywindow = builder.get_object("dialog1")
Mywindow.connect("delete-event", Gtk.main_quit)
Mywindow.set_default_size(600, 500)


screen = Gdk.Screen.get_default()

css_provider = Gtk.CssProvider()
css_provider.load_from_path('f.css')

context = Gtk.StyleContext()
context.add_provider_for_screen(screen, css_provider,
  Gtk.STYLE_PROVIDER_PRIORITY_USER)


Mywindow.show_all()


Gtk.main()

