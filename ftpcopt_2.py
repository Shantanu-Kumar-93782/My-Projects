from __future__ import division
from multiprocessing import Process
import gi
import socket
import sched, time
import threading
#from _thread import *
import re
import os
import time

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio
from gi.repository import GObject


class main_stark(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="File Transfer")
        self.set_default_size(700, 150)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(box)

        main_area = Gtk.Stack()
        main_area.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        main_area.set_transition_duration(200)

        frame1 = Gtk.Frame()
        frame2 = Gtk.Frame()
        mainbox1 = Gtk.VBox(spacing=0)

        upperbox = Gtk.Box(spacing=0)
        lowerbox = Gtk.Box(spacing=0)
        leftbox = Gtk.VBox(spacing=0)
        rightbox = Gtk.VBox(spacing=0)
        mainbox1.pack_start(upperbox, True, True, 0)
        mainbox1.pack_start(lowerbox, False, False, 0)
        frame1.add(leftbox)
        frame2.add(rightbox)
        upperbox.pack_start(frame1, True, True, 0)
        upperbox.pack_end(frame2, True, True, 0)
        label7 = Gtk.Label(label="_____Files_____")
        label8 = Gtk.Label(label="_____Status_____")
        leftbox.pack_start(label7, True, True, 3)
        rightbox.pack_start(label8, True, True, 3)
        self.label1 = Gtk.Label(label="No File Choosen")
        leftbox.pack_start(self.label1, True, True, 3)
        self.label2 = Gtk.Label(label="No File Choosen")
        leftbox.pack_start(self.label2, True, True, 3)
        self.label3 = Gtk.Label(label="No File Choosen")

        leftbox.pack_start(self.label3, True, True, 3)
        self.label4 = Gtk.Label(label="N/A")
        self.label5 = Gtk.Label(label="N/A")
        rightbox.pack_start(self.label4, True, True, 3)
        
        rightbox.pack_start(self.label5, True, True, 3)
        self.label6 = Gtk.Label(label="N/A")
        rightbox.pack_start(self.label6, True, True, 3)
        button1 = Gtk.Button(label="Choose File")
        button2 = Gtk.Button(label="Send")
        label17 = Gtk.Label(label = "Enter the receiver ip address :  ")
        self.target_ip = Gtk.Entry()
        button1.connect("clicked", self.on_file_chooser)
        lowerbox.pack_start(label17,False,False,3)
        lowerbox.pack_start(self.target_ip,True,True,1)
        lowerbox.pack_end(button2, False, False, 4)
        lowerbox.pack_end(button1, False, False, 4)
        button2.connect("clicked", self.send)

        frame3 = Gtk.Frame()
        frame4 = Gtk.Frame()
        mainbox2 = Gtk.VBox(spacing=0)

        upperbox2 = Gtk.Box(spacing=0)
        lowerbox2 = Gtk.Box(spacing=0)
        leftbox2 = Gtk.VBox(spacing=0)
        rightbox2 = Gtk.VBox(spacing=0)
        mainbox2.pack_start(upperbox2, True, True, 0)
        mainbox2.pack_start(lowerbox2, False, False, 0)
        frame3.add(leftbox2)
        frame4.add(rightbox2)
        upperbox2.pack_start(frame3, True, True, 0)
        upperbox2.pack_end(frame4, True, True, 0)
        label9 = Gtk.Label(label="_____Files_____")
        label10 = Gtk.Label(label="_____Status_____")
        leftbox2.pack_start(label9, True, True, 0)
        rightbox2.pack_start(label10, True, True, 0)
        self.label11 = Gtk.Label(label="No File Received")
        leftbox2.pack_start(self.label11, True, True, 0)
        self.label12 = Gtk.Label(label="No File Received")
        leftbox2.pack_start(self.label12, True, True, 0)
        self.label13 = Gtk.Label(label="No File Received")

        leftbox2.pack_start(self.label13, True, True, 0)
        self.label14 = Gtk.Label(label="N/A")
        rightbox2.pack_start(self.label14, True, True, 0)
        self.label15 = Gtk.Label(label="N/A")
        rightbox2.pack_start(self.label15, True, True, 0)
        self.label16 = Gtk.Label(label="N/A")
        rightbox2.pack_start(self.label16, True, True, 0)
        vb3 = Gtk.VBox(spacing=0)
        main_area.add_titled(mainbox1, " check_name", "SEND")
        main_area.add_titled(mainbox2, " check_name2", "RECEIVE")
        main_area.add_titled(vb3, " check_name3", "Aise Hi")
        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(main_area)
        box.pack_start(stack_switcher, True, True, 0)
        box.pack_start(main_area, True, True, 0)

        button3 = Gtk.Button(label="Click Here To Start Receiving")
        label18 = Gtk.Label(label="Enter Your Ip Address To Receive :  ")
        self.target_ip2 = Gtk.Entry()
        #button1.connect("clicked", self.on_file_chooser)
        lowerbox2.pack_start(label18, False, False, 3)
        lowerbox2.pack_start(self.target_ip2, True, True, 1)
        lowerbox2.pack_start(button3, True, True, 2)
        button3.connect("clicked", self.on_button3_clicked)

    def on_file_chooser(self, widget):
        dialog = Gtk.FileChooserDialog("Select a file to send ", self, Gtk.FileChooserAction.OPEN,
                                       ("Cancel", Gtk.ResponseType.CANCEL, "Open", Gtk.ResponseType.OK))

        response = dialog.run()
        self.flag2 = 0

        if response == Gtk.ResponseType.OK:
            self.filename = dialog.get_filename()
            print(self.filename)
            self.m = self.filename.split("/")
            print(self.m)
            if self.label1.get_text() == "No File Choosen":
                self.label1.set_text(self.m[-1])
                self.label4.set_text("0%")
                self.flag2 = 1

            elif self.label2.get_text() == "No File Choosen":
                self.label2.set_text(self.m[-1])
                self.label5.set_text("0%")
                self.flag2 = 2

            elif self.label3.get_text() == "No File Choosen":
                self.label3.set_text(self.m[-1])
                self.label6.set_text("0%")
                self.flag2 = 3

            else:
                self.label1.set_text(self.m[-1])
                self.label4.set_text("0%")
                self.flag2 = 1

        elif response == Gtk.ResponseType.CANCEL:
            print("choose some file to send")

        dialog.destroy()

    def send(self, widget):

        s = socket.socket()
        host = str(self.target_ip.get_text())
        port = 65000
        old = -1
        s.connect((host, port))
        s.send(str(self.m[-1]))
        time.sleep(1)
        f = open(str(self.filename), 'rb')
        sizze = os.path.getsize(str(self.filename))
        # print sizze
        # print "sending"

        l = f.read(1024)
        total_sent = 1024

        while (l):
            new = int((total_sent / sizze) * 100)
            #if (old != new):
            #self.label4.set_label(str(new) + " %")
            #    print new
            s.send(l)
            l = f.read(1024)
            total_sent += 1024
            old = new
        f.close()

        if self.flag2 == 1 :
            self.label4.set_text("done sending")

        if self.flag2 == 2 :
            self.label5.set_text("done sending")

        if self.flag2 == 3 :
            self.label6.set_text("done sending")
        s.close()

    def on_button3_clicked(self, wdiget):
        print("hey there in clicked function")
        l = threading.Thread(target=self.socket_target_function, args=(self))
        l.start()

    def socket_target_function(self, i):
        print("hey there in thread function")
        s = socket.socket()
        host = str(self.target_ip2.get_text())
        port = 65000
        s.bind((host, port))
        s.listen(5)
        flag = 0
        c, addr = s.accept()
        l = c.recv(1024)
        print ('got connection from ', addr)
        print ('receiving')
        f = open(str(l), 'wb')
        if self.label11.get_text() == "No File Received":
            self.label11.set_text(l)
            self.label14.set_text("0%")
            flag = 1

        elif self.label12.get_text() == "No File Received":
            self.label12.set_text(l)
            self.label15.set_text("0%")
            flag = 2

        elif self.label13.get_text() == "No File Received":
            self.label13.set_text(l)
            self.label16.set_text("0%")
            flag = 3
        else:
            self.label11.set_text(self.m[-1])
            self.label14.set_text("0%")
            flag =1
        while (l):
            print ("receiving")
            l = c.recv(1024)
            f.write(l)


        f.close()
        if flag == 1 :
            self.label14.set_text("done receving")

        if flag == 2 :
            self.label15.set_text("done receving")

        if flag == 3 :
            self.label16.set_text("done receving")

        c.close()


window = main_stark()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
