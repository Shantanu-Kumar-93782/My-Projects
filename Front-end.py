import gi
import socket
import threading
import time
import sys
import os
import random
import math
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject, Gio, GLib, Gdk


main_ip = '127.0.0.1'

class DialogExample(Gtk.Dialog):

    def __init__(self):
        Gtk.Dialog.__init__(self)
        self.set_default_size(300, 100)
        label = Gtk.Label()
        label.set_label("Enter Your Main Interface IP: ")
        self.entry = Gtk.Entry()
        self.entry.set_size_request(40,40)
        button = Gtk.Button()
        button.set_size_request(40,35)
        button.set_label("Let's GO")
        button.connect("clicked", self.on_clicked)
        button.set_halign(Gtk.Align.CENTER)
        box = self.get_content_area()
        vbox = Gtk.VBox(spacing=10)
        label.set_halign(Gtk.Align.START)
        vbox.pack_start(label, True, True, 3)
        vbox.pack_start(self.entry, True, True, 2)
        hbox2 = Gtk.HBox(spacing=10)
        hbox2.pack_start(button, True, True, 100)
        vbox.pack_start(hbox2, False, False, 0)
        box.add(vbox)
        self.show_all()

    def on_clicked(self, widget):
        global main_ip
        main_ip = self.entry.get_text()
        print("this is the main ip" + str(main_ip))
        self.destroy()
    
    def destroyy(self, arg1, arg2):
        self.destroy()



class Main_Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Task Distributer - Master")
        self.set_default_size(800, 250)
        self.set_resizable(False)
        #self.set_border_width(10)
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(self.box)
        self.main_area = Gtk.Stack()
        self.main_area.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.main_area.set_transition_duration(200)

        self.fixing = Gtk.Fixed()
        self.vb1 = Gtk.VBox(spacing=5)
        self.vb2 = Gtk.VBox()
        self.vb3 = Gtk.VBox()
        ################################################# For HAsh Tab Code  Start##############################################
        self.hash_tab_label_1 = Gtk.Label()
        self.hash_tab_label_1.set_text("Enter Your Hash : ")
        self.hash_tab_entry_1 = Gtk.Entry()
        self.hash_tab_label_2 = Gtk.Label()
        self.hash_tab_label_2.set_text("Choose Your Hash Type : ")
        self.hash_tab_list_1_material_2 = Gtk.ListStore(int, str)
        self.hash_tab_list_1_material_2.append([1, "MD5  (Message Digest 5 - 128 bit Hash)"])
        self.hash_tab_list_1_material_2.append([2, "SHA1 (Secure Hash Algorithm - 160 bit Hash)"])
        self.hash_tab_list_1_material_2.append([3, "SHA256  (Secure Hash Algorithm -  256 bit Hash"])
        self.hash_tab_list_1_material_1 = Gtk.ComboBox.new_with_model_and_entry(self.hash_tab_list_1_material_2)
        #print(hash_tab_list_1_material_1.get_active_iter.__doc__)
        self.hash_tab_list_1_material_1.connect("changed", self.on_hash_tab_list_1_changed)
        self.hash_tab_list_1_material_1.set_entry_text_column(1)
        self.hash_tab_label_1.set_font_options()
        self.hash_tab_label_1.set_halign(Gtk.Align.START)
        self.hash_tab_label_1.set_valign(Gtk.Align.START)
        self.hash_tab_label_2.set_halign(Gtk.Align.START)
        self.hash_tab_label_2.set_valign(Gtk.Align.START)
        self.hash_tab_entry_1.set_halign(Gtk.Align.START)
        self.hash_tab_entry_1.set_valign(Gtk.Align.START)
        self.hash_tab_list_1_material_1.set_vexpand_set(False)
        self.hash_tab_entry_1.set_size_request(730, 40)
        self.hash_tab_list_1_material_1.set_size_request(300, 40)
        self.hash_tab_label_3 = Gtk.Label()
        self.hash_tab_label_3.set_text("Choose Wordlist Type : ")
        self.hash_tab_label_3.set_halign(Gtk.Align.START)
        self.hash_tab_label_3.set_valign(Gtk.Align.START)
        self.hash_tab_radio_button_1 = Gtk.RadioButton(label="Predefined")
        #self.hash_tab_radio_button_1.connect("toggled", self.on_toggling_hash_tab_radio_button_1)
        self.hash_tab_radio_button_1.set_halign(Gtk.Align.START)
        self.hash_tab_radio_button_2 = Gtk.RadioButton.new_from_widget(self.hash_tab_radio_button_1)
        #self.hash_tab_radio_button_1.connect("toggled", self.on_toggling_hash_tab_radio_button_2)
        self.hash_tab_radio_button_1.set_halign(Gtk.Align.START)
        self.hash_tab_radio_button_2.set_label("Custom ")
        

        #self.vb1.set_sensitive(False)
        #print(dir(Gtk.Align))
        self.hash_tab_hbox = Gtk.HBox(spacing=0)
        self.hash_tab_vbox_1 = Gtk.VBox(spacing=0)
        self.hash_tab_vbox_2 = Gtk.VBox(spacing=0)
        self.hash_tab_label_4 = Gtk.Label()
        self.hash_tab_label_4.set_text("Charset : ")
        self.hash_tab_label_5 = Gtk.Label()
        self.hash_tab_label_5.set_text("Size : ")
        self.hash_tab_label_6 = Gtk.Label()
        self.hash_tab_label_6.set_text("Logs : ")
        self.hash_tab_list_2_material_2 = Gtk.ListStore(int, str)
        self.hash_tab_list_2_material_2.append([1, "[a ... z] - 26 Characters (All Lower Case)"])
        self.hash_tab_list_2_material_2.append([2, "[a ... Z] - 52 Characters (All lower + Upper Case )"])
        self.hash_tab_list_2_material_2.append([3, "[0 ... 9] - 10 Characters (All Numeric )"])
        self.hash_tab_list_2_material_2.append([4, "[a ... 0] - 62 Characters (All Lower + Upper + Numeric)]"])
        self.hash_tab_list_2_material_1 = Gtk.ComboBox.new_with_model_and_entry(self.hash_tab_list_2_material_2)
        #print(hash_tab_list_1_material_1.get_active_iter.__doc__)
        self.hash_tab_list_2_material_1.connect("changed", self.on_hash_tab_list_2_changed)
        self.hash_tab_list_2_material_1.set_entry_text_column(1)
        self.hash_tab_entry_2 = Gtk.Entry()
        self.hash_tab_entry_2.set_size_request(20, 40)
        self.hash_tab_label_4.set_halign(Gtk.Align.START)
        self.hash_tab_label_4.set_valign(Gtk.Align.START)
        self.hash_tab_label_5.set_halign(Gtk.Align.START)
        self.hash_tab_label_5.set_valign(Gtk.Align.START)
        self.hash_tab_label_6.set_halign(Gtk.Align.START)
        self.hash_tab_label_6.set_valign(Gtk.Align.START)
        #self.hash_tab_entry_2.set_halign(Gtk.Align.CENTER)
        #self.hash_tab_entry_2.set_valign(Gtk.Align.CENTER)
        self.hash_tab_list_2_material_1.set_size_request(300, 40)
        self.global_buffer = Gtk.TextBuffer()
        self.hash_tab_textview = Gtk.TextView(buffer = self.global_buffer)
        self.hash_tab_textview.set_editable(False)
        self.hash_tab_textview.set_size_request(300,300)
        self.hash_tab_scrollable_window = Gtk.ScrolledWindow()
        self.hash_tab_scrollable_window.set_size_request(300,300)
        self.hash_tab_scrollable_window.set_policy(Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)
        self.hash_tab_scrollable_window.add(self.hash_tab_textview)
        self.global_buffer.set_text("Welcome to the application\n")
        self.iter = self.global_buffer.get_end_iter()
        self.hash_tab_hbox.set_sensitive(False)
        self.hash_tab_radio_button_1.bind_property("active", self.hash_tab_hbox, "sensitive", GObject.BindingFlags.INVERT_BOOLEAN)
        self.hash_tab_hbox_2 = Gtk.HBox(spacing=3)
        self.hash_tab_vbox_3 = Gtk.VBox(spacing=0)
        self.hash_tab_vbox_4 = Gtk.VBox(spacing=0)
        self.hash_tab_button_1 = Gtk.Button(label="START")
        self.hash_tab_button_2 = Gtk.Button(label="STOP")
        self.hash_tab_button_1.set_halign(Gtk.Align.CENTER)
        self.hash_tab_button_2.set_halign(Gtk.Align.CENTER)
        self.hash_tab_button_1.set_size_request(40, 40)
        self.hash_tab_button_2.set_size_request(40, 40)
        self.hash_tab_button_1.connect("clicked", self.on_hash_tab_button_1)
        self.hash_tab_button_2.connect("clicked", self.on_hash_tab_button_2)
        self.hash_tab_vbox_3.pack_start(self.hash_tab_button_1, False, False, 0)
        self.hash_tab_vbox_4.pack_start(self.hash_tab_button_2, False, False, 0)
        self.hash_tab_hbox_2.pack_start(self.hash_tab_vbox_3, True, True, 0)
        self.hash_tab_hbox_2.pack_start(self.hash_tab_vbox_4, True, True, 0)



        self.hash_tab_vbox_1.pack_start(self.hash_tab_label_4, True, True, 2)
        self.hash_tab_vbox_2.pack_start(self.hash_tab_label_5, True, True, 2)
        self.hash_tab_vbox_1.pack_start(self.hash_tab_list_2_material_1, True, True, 2)
        self.hash_tab_vbox_2.pack_start(self.hash_tab_entry_2, False, False, 2)
        self.hash_tab_hbox.pack_start(self.hash_tab_vbox_1, True, True, 2)
        self.hash_tab_hbox.pack_start(self.hash_tab_vbox_2, True, True, 7)
        


        
        self.vb1.pack_start(self.hash_tab_label_1, True, True, 3)
        self.vb1.pack_start(self.hash_tab_entry_1, True, True, 2)
        self.vb1.pack_start(self.hash_tab_label_2, True, True, 3)
        self.vb1.pack_start(self.hash_tab_list_1_material_1, True, True, 2)
        self.vb1.pack_start(self.hash_tab_label_3, True, True, 3)
        self.vb1.pack_start(self.hash_tab_radio_button_1, True, True, 3)
        self.vb1.pack_start(self.hash_tab_radio_button_2, True, True, 2)
        self.vb1.pack_start(self.hash_tab_hbox, True, True, 3)
        self.vb1.pack_start(self.hash_tab_hbox_2, True, True, 5)
        self.vb1.pack_start(self.hash_tab_label_6, True, True, 2)
        self.vb1.pack_start(self.hash_tab_scrollable_window, True, True, 3)
        self.vb1.set_margin_left(20)
        self.vb1.set_margin_right(20)
        self.vb1.set_margin_top(20)
        self.vb1.set_margin_bottom(20)
        ############################################## For HAsh Tab Code  End############################################################
        self.global_main_thread = threading.Thread(target=self.main_incoming_socket_function, args=(), daemon=True)
        self.global_main_thread.start()
        self.process_started_flag=0


        

        ########################################### Zip PathFinder Tab Code Start##############################################################





        ########################################### Zip PathFinder Tab Code Start##############################################################






        ###########################################  Statistics Tab Code Start##############################################################
        self.statistics_tab_scrollable_window = Gtk.ScrolledWindow()
        self.statistics_tab_scrollable_window.set_policy(Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)
        self.statistics_tab_scrollable_window.add(self.vb3)
        self.statistics_tab_line_0_hbox = Gtk.HBox()
        self.statistics_tab_line_0_frame_1 = Gtk.Frame()
        self.statistics_tab_line_0_frame_2 = Gtk.Frame()
        self.statistics_tab_line_0_frame_3 = Gtk.Frame()
        self.statistics_tab_line_0_frame_4 = Gtk.Frame()
        self.statistics_tab_line_0_frame_1.set_size_request(20, 40)
        self.statistics_tab_line_0_frame_2.set_size_request(200, 40)
        self.statistics_tab_line_0_frame_3.set_size_request(200, 40)
        self.statistics_tab_line_0_frame_4.set_size_request(300, 40)
        self.statistics_tab_line_0_label_1 = Gtk.Label(label = "Sno.")
        self.statistics_tab_line_0_label_2 = Gtk.Label(label = "Slave Address")
        self.statistics_tab_line_0_label_3 = Gtk.Label(label = "Status")
        self.statistics_tab_line_0_label_4 = Gtk.Label(label = "Progress")
        self.statistics_tab_line_0_frame_1.add(self.statistics_tab_line_0_label_1)
        self.statistics_tab_line_0_frame_2.add(self.statistics_tab_line_0_label_2)
        self.statistics_tab_line_0_frame_3.add(self.statistics_tab_line_0_label_3)
        self.statistics_tab_line_0_frame_4.add(self.statistics_tab_line_0_label_4)
        self.statistics_tab_line_0_hbox.pack_start(self.statistics_tab_line_0_frame_1, True, True, 2)
        self.statistics_tab_line_0_hbox.pack_start(self.statistics_tab_line_0_frame_2, False, False, 2)
        self.statistics_tab_line_0_hbox.pack_start(self.statistics_tab_line_0_frame_3, False, False, 2)
        self.statistics_tab_line_0_hbox.pack_start(self.statistics_tab_line_0_frame_4, False, False, 2)
        self.vb3.pack_start(self.statistics_tab_line_0_hbox, False, False, 2)
        self.statistics_tab_line_1_hbox = Gtk.HBox()
        self.statistics_tab_line_1_frame_1 = Gtk.Frame()
        self.statistics_tab_line_1_frame_2 = Gtk.Frame()
        self.statistics_tab_line_1_frame_3 = Gtk.Frame()
        self.statistics_tab_line_1_frame_4 = Gtk.Frame()
        self.statistics_tab_line_1_frame_1.set_size_request(20, 40)
        self.statistics_tab_line_1_frame_2.set_size_request(200, 40)
        self.statistics_tab_line_1_frame_3.set_size_request(200, 40)
        self.statistics_tab_line_1_frame_4.set_size_request(300, 40)
        self.statistics_tab_line_1_label_1 = Gtk.Label(label = "1")
        self.statistics_tab_line_1_label_2 = Gtk.Label()
        self.statistics_tab_line_1_label_3 = Gtk.Label()
        self.statistics_tab_line_1_label_4 = Gtk.Label()
        self.statistics_tab_line_1_frame_1.add(self.statistics_tab_line_1_label_1)
        self.statistics_tab_line_1_frame_2.add(self.statistics_tab_line_1_label_2)
        self.statistics_tab_line_1_frame_3.add(self.statistics_tab_line_1_label_3)
        self.statistics_tab_line_1_frame_4.add(self.statistics_tab_line_1_label_4)
        self.statistics_tab_line_1_hbox.pack_start(self.statistics_tab_line_1_frame_1, True, True, 2)
        self.statistics_tab_line_1_hbox.pack_start(self.statistics_tab_line_1_frame_2, False, False, 2)
        self.statistics_tab_line_1_hbox.pack_start(self.statistics_tab_line_1_frame_3, False, False, 2)
        self.statistics_tab_line_1_hbox.pack_start(self.statistics_tab_line_1_frame_4, False, False, 2)
        self.vb3.pack_start(self.statistics_tab_line_1_hbox, False, False, 2)
        self.statistics_tab_line_2_hbox = Gtk.HBox()
        self.statistics_tab_line_2_frame_1 = Gtk.Frame()
        self.statistics_tab_line_2_frame_2 = Gtk.Frame()
        self.statistics_tab_line_2_frame_3 = Gtk.Frame()
        self.statistics_tab_line_2_frame_4 = Gtk.Frame()
        self.statistics_tab_line_2_frame_1.set_size_request(20, 40)
        self.statistics_tab_line_2_frame_2.set_size_request(200, 40)
        self.statistics_tab_line_2_frame_3.set_size_request(200, 40)
        self.statistics_tab_line_2_frame_4.set_size_request(300, 40)
        self.statistics_tab_line_2_label_1 = Gtk.Label(label = "2")
        self.statistics_tab_line_2_label_2 = Gtk.Label()
        self.statistics_tab_line_2_label_3 = Gtk.Label()
        self.statistics_tab_line_2_label_4 = Gtk.Label()
        self.statistics_tab_line_2_frame_1.add(self.statistics_tab_line_2_label_1)
        self.statistics_tab_line_2_frame_2.add(self.statistics_tab_line_2_label_2)
        self.statistics_tab_line_2_frame_3.add(self.statistics_tab_line_2_label_3)
        self.statistics_tab_line_2_frame_4.add(self.statistics_tab_line_2_label_4)
        self.statistics_tab_line_2_hbox.pack_start(self.statistics_tab_line_2_frame_1, True, True, 2)
        self.statistics_tab_line_2_hbox.pack_start(self.statistics_tab_line_2_frame_2, False, False, 2)
        self.statistics_tab_line_2_hbox.pack_start(self.statistics_tab_line_2_frame_3, False, False, 2)
        self.statistics_tab_line_2_hbox.pack_start(self.statistics_tab_line_2_frame_4, False, False, 2)
        self.vb3.pack_start(self.statistics_tab_line_2_hbox, False, False, 2)
        self.statistics_tab_line_3_hbox = Gtk.HBox()
        self.statistics_tab_line_3_frame_1 = Gtk.Frame()
        self.statistics_tab_line_3_frame_2 = Gtk.Frame()
        self.statistics_tab_line_3_frame_3 = Gtk.Frame()
        self.statistics_tab_line_3_frame_4 = Gtk.Frame()
        self.statistics_tab_line_3_frame_1.set_size_request(20, 40)
        self.statistics_tab_line_3_frame_2.set_size_request(200, 40)
        self.statistics_tab_line_3_frame_3.set_size_request(200, 40)
        self.statistics_tab_line_3_frame_4.set_size_request(300, 40)
        self.statistics_tab_line_3_label_1 = Gtk.Label(label = "3")
        self.statistics_tab_line_3_label_2 = Gtk.Label()
        self.statistics_tab_line_3_label_3 = Gtk.Label()
        self.statistics_tab_line_3_label_4 = Gtk.Label()
        self.statistics_tab_line_3_frame_1.add(self.statistics_tab_line_3_label_1)
        self.statistics_tab_line_3_frame_2.add(self.statistics_tab_line_3_label_2)
        self.statistics_tab_line_3_frame_3.add(self.statistics_tab_line_3_label_3)
        self.statistics_tab_line_3_frame_4.add(self.statistics_tab_line_3_label_4)
        self.statistics_tab_line_3_hbox.pack_start(self.statistics_tab_line_3_frame_1, True, True, 2)
        self.statistics_tab_line_3_hbox.pack_start(self.statistics_tab_line_3_frame_2, False, False, 2)
        self.statistics_tab_line_3_hbox.pack_start(self.statistics_tab_line_3_frame_3, False, False, 2)
        self.statistics_tab_line_3_hbox.pack_start(self.statistics_tab_line_3_frame_4, False, False, 2)
        self.vb3.pack_start(self.statistics_tab_line_3_hbox, False, False, 2)
        self.statistics_tab_line_4_hbox = Gtk.HBox()
        self.statistics_tab_line_4_frame_1 = Gtk.Frame()
        self.statistics_tab_line_4_frame_2 = Gtk.Frame()
        self.statistics_tab_line_4_frame_3 = Gtk.Frame()
        self.statistics_tab_line_4_frame_4 = Gtk.Frame()
        self.statistics_tab_line_4_frame_1.set_size_request(20, 40)
        self.statistics_tab_line_4_frame_2.set_size_request(200, 40)
        self.statistics_tab_line_4_frame_3.set_size_request(200, 40)
        self.statistics_tab_line_4_frame_4.set_size_request(300, 40)
        self.statistics_tab_line_4_label_1 = Gtk.Label(label = "4")
        self.statistics_tab_line_4_label_2 = Gtk.Label()
        self.statistics_tab_line_4_label_3 = Gtk.Label()
        self.statistics_tab_line_4_label_4 = Gtk.Label()
        self.statistics_tab_line_4_frame_1.add(self.statistics_tab_line_4_label_1)
        self.statistics_tab_line_4_frame_2.add(self.statistics_tab_line_4_label_2)
        self.statistics_tab_line_4_frame_3.add(self.statistics_tab_line_4_label_3)
        self.statistics_tab_line_4_frame_4.add(self.statistics_tab_line_4_label_4)
        self.statistics_tab_line_4_hbox.pack_start(self.statistics_tab_line_4_frame_1, True, True, 2)
        self.statistics_tab_line_4_hbox.pack_start(self.statistics_tab_line_4_frame_2, False, False, 2)
        self.statistics_tab_line_4_hbox.pack_start(self.statistics_tab_line_4_frame_3, False, False, 2)
        self.statistics_tab_line_4_hbox.pack_start(self.statistics_tab_line_4_frame_4, False, False, 2)
        self.vb3.pack_start(self.statistics_tab_line_4_hbox, False, False, 2)
        self.statistics_tab_line_5_hbox = Gtk.HBox()
        self.statistics_tab_line_5_frame_1 = Gtk.Frame()
        self.statistics_tab_line_5_frame_2 = Gtk.Frame()
        self.statistics_tab_line_5_frame_3 = Gtk.Frame()
        self.statistics_tab_line_5_frame_4 = Gtk.Frame()
        self.statistics_tab_line_5_frame_1.set_size_request(20, 40)
        self.statistics_tab_line_5_frame_2.set_size_request(200, 40)
        self.statistics_tab_line_5_frame_3.set_size_request(200, 40)
        self.statistics_tab_line_5_frame_4.set_size_request(300, 40)
        self.statistics_tab_line_5_label_1 = Gtk.Label(label = "5")
        self.statistics_tab_line_5_label_2 = Gtk.Label()
        self.statistics_tab_line_5_label_3 = Gtk.Label()
        self.statistics_tab_line_5_label_4 = Gtk.Label()
        self.statistics_tab_line_5_frame_1.add(self.statistics_tab_line_5_label_1)
        self.statistics_tab_line_5_frame_2.add(self.statistics_tab_line_5_label_2)
        self.statistics_tab_line_5_frame_3.add(self.statistics_tab_line_5_label_3)
        self.statistics_tab_line_5_frame_4.add(self.statistics_tab_line_5_label_4)
        self.statistics_tab_line_5_hbox.pack_start(self.statistics_tab_line_5_frame_1, True, True, 2)
        self.statistics_tab_line_5_hbox.pack_start(self.statistics_tab_line_5_frame_2, False, False, 2)
        self.statistics_tab_line_5_hbox.pack_start(self.statistics_tab_line_5_frame_3, False, False, 2)
        self.statistics_tab_line_5_hbox.pack_start(self.statistics_tab_line_5_frame_4, False, False, 2)
        self.vb3.pack_start(self.statistics_tab_line_5_hbox, False, False, 2)
        self.statistics_tab_line_6_hbox = Gtk.HBox()
        self.statistics_tab_line_6_frame_1 = Gtk.Frame()
        self.statistics_tab_line_6_frame_2 = Gtk.Frame()
        self.statistics_tab_line_6_frame_3 = Gtk.Frame()
        self.statistics_tab_line_6_frame_4 = Gtk.Frame()
        self.statistics_tab_line_6_frame_1.set_size_request(20, 40)
        self.statistics_tab_line_6_frame_2.set_size_request(200, 40)
        self.statistics_tab_line_6_frame_3.set_size_request(200, 40)
        self.statistics_tab_line_6_frame_4.set_size_request(300, 40)
        self.statistics_tab_line_6_label_1 = Gtk.Label(label = "6")
        self.statistics_tab_line_6_label_2 = Gtk.Label()
        self.statistics_tab_line_6_label_3 = Gtk.Label()
        self.statistics_tab_line_6_label_4 = Gtk.Label()
        self.statistics_tab_line_6_frame_1.add(self.statistics_tab_line_6_label_1)
        self.statistics_tab_line_6_frame_2.add(self.statistics_tab_line_6_label_2)
        self.statistics_tab_line_6_frame_3.add(self.statistics_tab_line_6_label_3)
        self.statistics_tab_line_6_frame_4.add(self.statistics_tab_line_6_label_4)
        self.statistics_tab_line_6_hbox.pack_start(self.statistics_tab_line_6_frame_1, True, True, 2)
        self.statistics_tab_line_6_hbox.pack_start(self.statistics_tab_line_6_frame_2, False, False, 2)
        self.statistics_tab_line_6_hbox.pack_start(self.statistics_tab_line_6_frame_3, False, False, 2)
        self.statistics_tab_line_6_hbox.pack_start(self.statistics_tab_line_6_frame_4, False, False, 2)
        self.vb3.pack_start(self.statistics_tab_line_6_hbox, False, False, 2)
        self.statistics_tab_line_7_hbox = Gtk.HBox()
        self.statistics_tab_line_7_frame_1 = Gtk.Frame()
        self.statistics_tab_line_7_frame_2 = Gtk.Frame()
        self.statistics_tab_line_7_frame_3 = Gtk.Frame()
        self.statistics_tab_line_7_frame_4 = Gtk.Frame()
        self.statistics_tab_line_7_frame_1.set_size_request(20, 40)
        self.statistics_tab_line_7_frame_2.set_size_request(200, 40)
        self.statistics_tab_line_7_frame_3.set_size_request(200, 40)
        self.statistics_tab_line_7_frame_4.set_size_request(300, 40)
        self.statistics_tab_line_7_label_1 = Gtk.Label(label = "7")
        self.statistics_tab_line_7_label_2 = Gtk.Label()
        self.statistics_tab_line_7_label_3 = Gtk.Label()
        self.statistics_tab_line_7_label_4 = Gtk.Label()
        self.statistics_tab_line_7_frame_1.add(self.statistics_tab_line_7_label_1)
        self.statistics_tab_line_7_frame_2.add(self.statistics_tab_line_7_label_2)
        self.statistics_tab_line_7_frame_3.add(self.statistics_tab_line_7_label_3)
        self.statistics_tab_line_7_frame_4.add(self.statistics_tab_line_7_label_4)
        self.statistics_tab_line_7_hbox.pack_start(self.statistics_tab_line_7_frame_1, True, True, 2)
        self.statistics_tab_line_7_hbox.pack_start(self.statistics_tab_line_7_frame_2, False, False, 2)
        self.statistics_tab_line_7_hbox.pack_start(self.statistics_tab_line_7_frame_3, False, False, 2)
        self.statistics_tab_line_7_hbox.pack_start(self.statistics_tab_line_7_frame_4, False, False, 2)
        self.vb3.pack_start(self.statistics_tab_line_7_hbox, False, False, 2)
        self.statistics_tab_line_8_hbox = Gtk.HBox()
        self.statistics_tab_line_8_frame_1 = Gtk.Frame()
        self.statistics_tab_line_8_frame_2 = Gtk.Frame()
        self.statistics_tab_line_8_frame_3 = Gtk.Frame()
        self.statistics_tab_line_8_frame_4 = Gtk.Frame()
        self.statistics_tab_line_8_frame_1.set_size_request(20, 40)
        self.statistics_tab_line_8_frame_2.set_size_request(200, 40)
        self.statistics_tab_line_8_frame_3.set_size_request(200, 40)
        self.statistics_tab_line_8_frame_4.set_size_request(300, 40)
        self.statistics_tab_line_8_label_1 = Gtk.Label(label = "8")
        self.statistics_tab_line_8_label_2 = Gtk.Label()
        self.statistics_tab_line_8_label_3 = Gtk.Label()
        self.statistics_tab_line_8_label_4 = Gtk.Label()
        self.statistics_tab_line_8_frame_1.add(self.statistics_tab_line_8_label_1)
        self.statistics_tab_line_8_frame_2.add(self.statistics_tab_line_8_label_2)
        self.statistics_tab_line_8_frame_3.add(self.statistics_tab_line_8_label_3)
        self.statistics_tab_line_8_frame_4.add(self.statistics_tab_line_8_label_4)
        self.statistics_tab_line_8_hbox.pack_start(self.statistics_tab_line_8_frame_1, True, True, 2)
        self.statistics_tab_line_8_hbox.pack_start(self.statistics_tab_line_8_frame_2, False, False, 2)
        self.statistics_tab_line_8_hbox.pack_start(self.statistics_tab_line_8_frame_3, False, False, 2)
        self.statistics_tab_line_8_hbox.pack_start(self.statistics_tab_line_8_frame_4, False, False, 2)
        self.vb3.pack_start(self.statistics_tab_line_8_hbox, False, False, 2)
        self.statistics_tab_line_9_hbox = Gtk.HBox()
        self.statistics_tab_line_9_frame_1 = Gtk.Frame()
        self.statistics_tab_line_9_frame_2 = Gtk.Frame()
        self.statistics_tab_line_9_frame_3 = Gtk.Frame()
        self.statistics_tab_line_9_frame_4 = Gtk.Frame()
        self.statistics_tab_line_9_frame_1.set_size_request(20, 40)
        self.statistics_tab_line_9_frame_2.set_size_request(200, 40)
        self.statistics_tab_line_9_frame_3.set_size_request(200, 40)
        self.statistics_tab_line_9_frame_4.set_size_request(300, 40)
        self.statistics_tab_line_9_label_1 = Gtk.Label(label = "9")
        self.statistics_tab_line_9_label_2 = Gtk.Label()
        self.statistics_tab_line_9_label_3 = Gtk.Label()
        self.statistics_tab_line_9_label_4 = Gtk.Label()
        self.statistics_tab_line_9_frame_1.add(self.statistics_tab_line_9_label_1)
        self.statistics_tab_line_9_frame_2.add(self.statistics_tab_line_9_label_2)
        self.statistics_tab_line_9_frame_3.add(self.statistics_tab_line_9_label_3)
        self.statistics_tab_line_9_frame_4.add(self.statistics_tab_line_9_label_4)
        self.statistics_tab_line_9_hbox.pack_start(self.statistics_tab_line_9_frame_1, True, True, 2)
        self.statistics_tab_line_9_hbox.pack_start(self.statistics_tab_line_9_frame_2, False, False, 2)
        self.statistics_tab_line_9_hbox.pack_start(self.statistics_tab_line_9_frame_3, False, False, 2)
        self.statistics_tab_line_9_hbox.pack_start(self.statistics_tab_line_9_frame_4, False, False, 2)
        self.vb3.pack_start(self.statistics_tab_line_9_hbox, False, False, 2)
        self.statistics_tab_line_10_hbox = Gtk.HBox()
        self.statistics_tab_line_10_frame_1 = Gtk.Frame()
        self.statistics_tab_line_10_frame_2 = Gtk.Frame()
        self.statistics_tab_line_10_frame_3 = Gtk.Frame()
        self.statistics_tab_line_10_frame_4 = Gtk.Frame()
        self.statistics_tab_line_10_frame_1.set_size_request(20, 40)
        self.statistics_tab_line_10_frame_2.set_size_request(200, 40)
        self.statistics_tab_line_10_frame_3.set_size_request(200, 40)
        self.statistics_tab_line_10_frame_4.set_size_request(300, 40)
        self.statistics_tab_line_10_label_1 = Gtk.Label(label = "10")
        self.statistics_tab_line_10_label_2 = Gtk.Label()
        self.statistics_tab_line_10_label_3 = Gtk.Label()
        self.statistics_tab_line_10_label_4 = Gtk.Label()
        self.statistics_tab_line_10_frame_1.add(self.statistics_tab_line_10_label_1)
        self.statistics_tab_line_10_frame_2.add(self.statistics_tab_line_10_label_2)
        self.statistics_tab_line_10_frame_3.add(self.statistics_tab_line_10_label_3)
        self.statistics_tab_line_10_frame_4.add(self.statistics_tab_line_10_label_4)
        self.statistics_tab_line_10_hbox.pack_start(self.statistics_tab_line_10_frame_1, True, True, 2)
        self.statistics_tab_line_10_hbox.pack_start(self.statistics_tab_line_10_frame_2, False, False, 2)
        self.statistics_tab_line_10_hbox.pack_start(self.statistics_tab_line_10_frame_3, False, False, 2)
        self.statistics_tab_line_10_hbox.pack_start(self.statistics_tab_line_10_frame_4, False, False, 2)
        self.vb3.pack_start(self.statistics_tab_line_10_hbox, False, False, 2)
        self.statistics_tab_line_11_hbox = Gtk.HBox()
        self.statistics_tab_line_11_frame_1 = Gtk.Frame()
        self.statistics_tab_line_11_frame_2 = Gtk.Frame()
        self.statistics_tab_line_11_frame_3 = Gtk.Frame()
        self.statistics_tab_line_11_frame_4 = Gtk.Frame()
        self.statistics_tab_line_11_frame_1.set_size_request(20, 40)
        self.statistics_tab_line_11_frame_2.set_size_request(200, 40)
        self.statistics_tab_line_11_frame_3.set_size_request(200, 40)
        self.statistics_tab_line_11_frame_4.set_size_request(300, 40)
        self.statistics_tab_line_11_label_1 = Gtk.Label(label = "11")
        self.statistics_tab_line_11_label_2 = Gtk.Label()
        self.statistics_tab_line_11_label_3 = Gtk.Label()
        self.statistics_tab_line_11_label_4 = Gtk.Label()
        self.statistics_tab_line_11_frame_1.add(self.statistics_tab_line_11_label_1)
        self.statistics_tab_line_11_frame_2.add(self.statistics_tab_line_11_label_2)
        self.statistics_tab_line_11_frame_3.add(self.statistics_tab_line_11_label_3)
        self.statistics_tab_line_11_frame_4.add(self.statistics_tab_line_11_label_4)
        self.statistics_tab_line_11_hbox.pack_start(self.statistics_tab_line_11_frame_1, True, True, 2)
        self.statistics_tab_line_11_hbox.pack_start(self.statistics_tab_line_11_frame_2, False, False, 2)
        self.statistics_tab_line_11_hbox.pack_start(self.statistics_tab_line_11_frame_3, False, False, 2)
        self.statistics_tab_line_11_hbox.pack_start(self.statistics_tab_line_11_frame_4, False, False, 2)
        self.vb3.pack_start(self.statistics_tab_line_11_hbox, False, False, 2)
        self.statistics_tab_line_12_hbox = Gtk.HBox()
        self.statistics_tab_line_12_frame_1 = Gtk.Frame()
        self.statistics_tab_line_12_frame_2 = Gtk.Frame()
        self.statistics_tab_line_12_frame_3 = Gtk.Frame()
        self.statistics_tab_line_12_frame_4 = Gtk.Frame()
        self.statistics_tab_line_12_frame_1.set_size_request(20, 40)
        self.statistics_tab_line_12_frame_2.set_size_request(200, 40)
        self.statistics_tab_line_12_frame_3.set_size_request(200, 40)
        self.statistics_tab_line_12_frame_4.set_size_request(300, 40)
        self.statistics_tab_line_12_label_1 = Gtk.Label(label = "12")
        self.statistics_tab_line_12_label_2 = Gtk.Label()
        self.statistics_tab_line_12_label_3 = Gtk.Label()
        self.statistics_tab_line_12_label_4 = Gtk.Label()
        self.statistics_tab_line_12_frame_1.add(self.statistics_tab_line_12_label_1)
        self.statistics_tab_line_12_frame_2.add(self.statistics_tab_line_12_label_2)
        self.statistics_tab_line_12_frame_3.add(self.statistics_tab_line_12_label_3)
        self.statistics_tab_line_12_frame_4.add(self.statistics_tab_line_12_label_4)
        self.statistics_tab_line_12_hbox.pack_start(self.statistics_tab_line_12_frame_1, True, True, 2)
        self.statistics_tab_line_12_hbox.pack_start(self.statistics_tab_line_12_frame_2, False, False, 2)
        self.statistics_tab_line_12_hbox.pack_start(self.statistics_tab_line_12_frame_3, False, False, 2)
        self.statistics_tab_line_12_hbox.pack_start(self.statistics_tab_line_12_frame_4, False, False, 2)
        self.vb3.pack_start(self.statistics_tab_line_12_hbox, False, False, 2)
        self.statistics_tab_line_13_hbox = Gtk.HBox()
        self.statistics_tab_line_13_frame_1 = Gtk.Frame()
        self.statistics_tab_line_13_frame_2 = Gtk.Frame()
        self.statistics_tab_line_13_frame_3 = Gtk.Frame()
        self.statistics_tab_line_13_frame_4 = Gtk.Frame()
        self.statistics_tab_line_13_frame_1.set_size_request(20, 40)
        self.statistics_tab_line_13_frame_2.set_size_request(200, 40)
        self.statistics_tab_line_13_frame_3.set_size_request(200, 40)
        self.statistics_tab_line_13_frame_4.set_size_request(300, 40)
        self.statistics_tab_line_13_label_1 = Gtk.Label(label = "13")
        self.statistics_tab_line_13_label_2 = Gtk.Label()
        self.statistics_tab_line_13_label_3 = Gtk.Label()
        self.statistics_tab_line_13_label_4 = Gtk.Label()
        self.statistics_tab_line_13_frame_1.add(self.statistics_tab_line_13_label_1)
        self.statistics_tab_line_13_frame_2.add(self.statistics_tab_line_13_label_2)
        self.statistics_tab_line_13_frame_3.add(self.statistics_tab_line_13_label_3)
        self.statistics_tab_line_13_frame_4.add(self.statistics_tab_line_13_label_4)
        self.statistics_tab_line_13_hbox.pack_start(self.statistics_tab_line_13_frame_1, True, True, 2)
        self.statistics_tab_line_13_hbox.pack_start(self.statistics_tab_line_13_frame_2, False, False, 2)
        self.statistics_tab_line_13_hbox.pack_start(self.statistics_tab_line_13_frame_3, False, False, 2)
        self.statistics_tab_line_13_hbox.pack_start(self.statistics_tab_line_13_frame_4, False, False, 2)
        self.vb3.pack_start(self.statistics_tab_line_13_hbox, False, False, 2)
        self.statistics_tab_line_14_hbox = Gtk.HBox()
        self.statistics_tab_line_14_frame_1 = Gtk.Frame()
        self.statistics_tab_line_14_frame_2 = Gtk.Frame()
        self.statistics_tab_line_14_frame_3 = Gtk.Frame()
        self.statistics_tab_line_14_frame_4 = Gtk.Frame()
        self.statistics_tab_line_14_frame_1.set_size_request(20, 40)
        self.statistics_tab_line_14_frame_2.set_size_request(200, 40)
        self.statistics_tab_line_14_frame_3.set_size_request(200, 40)
        self.statistics_tab_line_14_frame_4.set_size_request(300, 40)
        self.statistics_tab_line_14_label_1 = Gtk.Label(label = "14")
        self.statistics_tab_line_14_label_2 = Gtk.Label()
        self.statistics_tab_line_14_label_3 = Gtk.Label()
        self.statistics_tab_line_14_label_4 = Gtk.Label()
        self.statistics_tab_line_14_frame_1.add(self.statistics_tab_line_14_label_1)
        self.statistics_tab_line_14_frame_2.add(self.statistics_tab_line_14_label_2)
        self.statistics_tab_line_14_frame_3.add(self.statistics_tab_line_14_label_3)
        self.statistics_tab_line_14_frame_4.add(self.statistics_tab_line_14_label_4)
        self.statistics_tab_line_14_hbox.pack_start(self.statistics_tab_line_14_frame_1, True, True, 2)
        self.statistics_tab_line_14_hbox.pack_start(self.statistics_tab_line_14_frame_2, False, False, 2)
        self.statistics_tab_line_14_hbox.pack_start(self.statistics_tab_line_14_frame_3, False, False, 2)
        self.statistics_tab_line_14_hbox.pack_start(self.statistics_tab_line_14_frame_4, False, False, 2)
        self.vb3.pack_start(self.statistics_tab_line_14_hbox, False, False, 2)
        self.statistics_tab_line_15_hbox = Gtk.HBox()
        self.statistics_tab_line_15_frame_1 = Gtk.Frame()
        self.statistics_tab_line_15_frame_2 = Gtk.Frame()
        self.statistics_tab_line_15_frame_3 = Gtk.Frame()
        self.statistics_tab_line_15_frame_4 = Gtk.Frame()
        self.statistics_tab_line_15_frame_1.set_size_request(20, 40)
        self.statistics_tab_line_15_frame_2.set_size_request(200, 40)
        self.statistics_tab_line_15_frame_3.set_size_request(200, 40)
        self.statistics_tab_line_15_frame_4.set_size_request(300, 40)
        self.statistics_tab_line_15_label_1 = Gtk.Label(label = "15")
        self.statistics_tab_line_15_label_2 = Gtk.Label()
        self.statistics_tab_line_15_label_3 = Gtk.Label()
        self.statistics_tab_line_15_label_4 = Gtk.Label()
        self.statistics_tab_line_15_frame_1.add(self.statistics_tab_line_15_label_1)
        self.statistics_tab_line_15_frame_2.add(self.statistics_tab_line_15_label_2)
        self.statistics_tab_line_15_frame_3.add(self.statistics_tab_line_15_label_3)
        self.statistics_tab_line_15_frame_4.add(self.statistics_tab_line_15_label_4)
        self.statistics_tab_line_15_hbox.pack_start(self.statistics_tab_line_15_frame_1, True, True, 2)
        self.statistics_tab_line_15_hbox.pack_start(self.statistics_tab_line_15_frame_2, False, False, 2)
        self.statistics_tab_line_15_hbox.pack_start(self.statistics_tab_line_15_frame_3, False, False, 2)
        self.statistics_tab_line_15_hbox.pack_start(self.statistics_tab_line_15_frame_4, False, False, 2)
        self.vb3.pack_start(self.statistics_tab_line_15_hbox, False, False, 2)
        self.statistics_tab_line_16_hbox = Gtk.HBox()
        self.statistics_tab_line_16_frame_1 = Gtk.Frame()
        self.statistics_tab_line_16_frame_2 = Gtk.Frame()
        self.statistics_tab_line_16_frame_3 = Gtk.Frame()
        self.statistics_tab_line_16_frame_4 = Gtk.Frame()
        self.statistics_tab_line_16_frame_1.set_size_request(20, 40)
        self.statistics_tab_line_16_frame_2.set_size_request(200, 40)
        self.statistics_tab_line_16_frame_3.set_size_request(200, 40)
        self.statistics_tab_line_16_frame_4.set_size_request(300, 40)
        self.statistics_tab_line_16_label_1 = Gtk.Label(label = "16")
        self.statistics_tab_line_16_label_2 = Gtk.Label()
        self.statistics_tab_line_16_label_3 = Gtk.Label()
        self.statistics_tab_line_16_label_4 = Gtk.Label()
        self.statistics_tab_line_16_frame_1.add(self.statistics_tab_line_16_label_1)
        self.statistics_tab_line_16_frame_2.add(self.statistics_tab_line_16_label_2)
        self.statistics_tab_line_16_frame_3.add(self.statistics_tab_line_16_label_3)
        self.statistics_tab_line_16_frame_4.add(self.statistics_tab_line_16_label_4)
        self.statistics_tab_line_16_hbox.pack_start(self.statistics_tab_line_16_frame_1, True, True, 2)
        self.statistics_tab_line_16_hbox.pack_start(self.statistics_tab_line_16_frame_2, False, False, 2)
        self.statistics_tab_line_16_hbox.pack_start(self.statistics_tab_line_16_frame_3, False, False, 2)
        self.statistics_tab_line_16_hbox.pack_start(self.statistics_tab_line_16_frame_4, False, False, 2)
        self.vb3.pack_start(self.statistics_tab_line_16_hbox, False, False, 2)
        self.statistics_tab_line_17_hbox = Gtk.HBox()
        self.statistics_tab_line_17_frame_1 = Gtk.Frame()
        self.statistics_tab_line_17_frame_2 = Gtk.Frame()
        self.statistics_tab_line_17_frame_3 = Gtk.Frame()
        self.statistics_tab_line_17_frame_4 = Gtk.Frame()
        self.statistics_tab_line_17_frame_1.set_size_request(20, 40)
        self.statistics_tab_line_17_frame_2.set_size_request(200, 40)
        self.statistics_tab_line_17_frame_3.set_size_request(200, 40)
        self.statistics_tab_line_17_frame_4.set_size_request(300, 40)
        self.statistics_tab_line_17_label_1 = Gtk.Label(label = "17")
        self.statistics_tab_line_17_label_2 = Gtk.Label()
        self.statistics_tab_line_17_label_3 = Gtk.Label()
        self.statistics_tab_line_17_label_4 = Gtk.Label()
        self.statistics_tab_line_17_frame_1.add(self.statistics_tab_line_17_label_1)
        self.statistics_tab_line_17_frame_2.add(self.statistics_tab_line_17_label_2)
        self.statistics_tab_line_17_frame_3.add(self.statistics_tab_line_17_label_3)
        self.statistics_tab_line_17_frame_4.add(self.statistics_tab_line_17_label_4)
        self.statistics_tab_line_17_hbox.pack_start(self.statistics_tab_line_17_frame_1, True, True, 2)
        self.statistics_tab_line_17_hbox.pack_start(self.statistics_tab_line_17_frame_2, False, False, 2)
        self.statistics_tab_line_17_hbox.pack_start(self.statistics_tab_line_17_frame_3, False, False, 2)
        self.statistics_tab_line_17_hbox.pack_start(self.statistics_tab_line_17_frame_4, False, False, 2)
        self.vb3.pack_start(self.statistics_tab_line_17_hbox, False, False, 2)
        self.statistics_tab_line_18_hbox = Gtk.HBox()
        self.statistics_tab_line_18_frame_1 = Gtk.Frame()
        self.statistics_tab_line_18_frame_2 = Gtk.Frame()
        self.statistics_tab_line_18_frame_3 = Gtk.Frame()
        self.statistics_tab_line_18_frame_4 = Gtk.Frame()
        self.statistics_tab_line_18_frame_1.set_size_request(20, 40)
        self.statistics_tab_line_18_frame_2.set_size_request(200, 40)
        self.statistics_tab_line_18_frame_3.set_size_request(200, 40)
        self.statistics_tab_line_18_frame_4.set_size_request(300, 40)
        self.statistics_tab_line_18_label_1 = Gtk.Label(label = "18")
        self.statistics_tab_line_18_label_2 = Gtk.Label()
        self.statistics_tab_line_18_label_3 = Gtk.Label()
        self.statistics_tab_line_18_label_4 = Gtk.Label()
        self.statistics_tab_line_18_frame_1.add(self.statistics_tab_line_18_label_1)
        self.statistics_tab_line_18_frame_2.add(self.statistics_tab_line_18_label_2)
        self.statistics_tab_line_18_frame_3.add(self.statistics_tab_line_18_label_3)
        self.statistics_tab_line_18_frame_4.add(self.statistics_tab_line_18_label_4)
        self.statistics_tab_line_18_hbox.pack_start(self.statistics_tab_line_18_frame_1, True, True, 2)
        self.statistics_tab_line_18_hbox.pack_start(self.statistics_tab_line_18_frame_2, False, False, 2)
        self.statistics_tab_line_18_hbox.pack_start(self.statistics_tab_line_18_frame_3, False, False, 2)
        self.statistics_tab_line_18_hbox.pack_start(self.statistics_tab_line_18_frame_4, False, False, 2)
        self.vb3.pack_start(self.statistics_tab_line_18_hbox, False, False, 2)
        self.statistics_tab_line_19_hbox = Gtk.HBox()
        self.statistics_tab_line_19_frame_1 = Gtk.Frame()
        self.statistics_tab_line_19_frame_2 = Gtk.Frame()
        self.statistics_tab_line_19_frame_3 = Gtk.Frame()
        self.statistics_tab_line_19_frame_4 = Gtk.Frame()
        self.statistics_tab_line_19_frame_1.set_size_request(20, 40)
        self.statistics_tab_line_19_frame_2.set_size_request(200, 40)
        self.statistics_tab_line_19_frame_3.set_size_request(200, 40)
        self.statistics_tab_line_19_frame_4.set_size_request(300, 40)
        self.statistics_tab_line_19_label_1 = Gtk.Label(label = "19")
        self.statistics_tab_line_19_label_2 = Gtk.Label()
        self.statistics_tab_line_19_label_3 = Gtk.Label()
        self.statistics_tab_line_19_label_4 = Gtk.Label()
        self.statistics_tab_line_0_label_2
        self.statistics_tab_line_19_frame_1.add(self.statistics_tab_line_19_label_1)
        self.statistics_tab_line_19_frame_2.add(self.statistics_tab_line_19_label_2)
        self.statistics_tab_line_19_frame_3.add(self.statistics_tab_line_19_label_3)
        self.statistics_tab_line_19_frame_4.add(self.statistics_tab_line_19_label_4)
        self.statistics_tab_line_19_hbox.pack_start(self.statistics_tab_line_19_frame_1, True, True, 2)
        self.statistics_tab_line_19_hbox.pack_start(self.statistics_tab_line_19_frame_2, False, False, 2)
        self.statistics_tab_line_19_hbox.pack_start(self.statistics_tab_line_19_frame_3, False, False, 2)
        self.statistics_tab_line_19_hbox.pack_start(self.statistics_tab_line_19_frame_4, False, False, 2)
        self.vb3.pack_start(self.statistics_tab_line_19_hbox, False, False, 2)
        self.statistics_tab_line_20_hbox = Gtk.HBox()
        self.statistics_tab_line_20_frame_1 = Gtk.Frame()
        self.statistics_tab_line_20_frame_2 = Gtk.Frame()
        self.statistics_tab_line_20_frame_3 = Gtk.Frame()
        self.statistics_tab_line_20_frame_4 = Gtk.Frame()
        self.statistics_tab_line_20_frame_1.set_size_request(20, 40)
        self.statistics_tab_line_20_frame_2.set_size_request(200, 40)
        self.statistics_tab_line_20_frame_3.set_size_request(200, 40)
        self.statistics_tab_line_20_frame_4.set_size_request(300, 40)
        self.statistics_tab_line_20_label_1 = Gtk.Label(label = "20")
        self.statistics_tab_line_20_label_2 = Gtk.Label()
        self.statistics_tab_line_20_label_3 = Gtk.Label()
        self.statistics_tab_line_20_label_4 = Gtk.Label()
        self.statistics_tab_line_20_frame_1.add(self.statistics_tab_line_20_label_1)
        self.statistics_tab_line_20_frame_2.add(self.statistics_tab_line_20_label_2)
        self.statistics_tab_line_20_frame_3.add(self.statistics_tab_line_20_label_3)
        self.statistics_tab_line_20_frame_4.add(self.statistics_tab_line_20_label_4)
        self.statistics_tab_line_20_hbox.pack_start(self.statistics_tab_line_20_frame_1, True, True, 2)
        self.statistics_tab_line_20_hbox.pack_start(self.statistics_tab_line_20_frame_2, False, False, 2)
        self.statistics_tab_line_20_hbox.pack_start(self.statistics_tab_line_20_frame_3, False, False, 2)
        self.statistics_tab_line_20_hbox.pack_start(self.statistics_tab_line_20_frame_4, False, False, 2)
        self.vb3.pack_start(self.statistics_tab_line_20_hbox, False, False, 2)


        #self.progress_bar_update = threading.Thread(target=self.progress_bar_update_function, daemon=True, args=())
        #self.progress_bar_update.start()

        
        
        ###########################################  Statistics Tab Code End ##############################################################



        ############################################  Global Code #####################################################################
        self.main_area.add_titled(self.vb1, " check_name", "Hash Resolver")
        self.main_area.add_titled(self.vb2, " check_name2", "Zip PathFinder")
        self.main_area.add_titled(self.statistics_tab_scrollable_window, " check_name3", "Statistics")
        self.stack_switcher = Gtk.StackSwitcher()
        self.stack_switcher.set_stack(self.main_area)
        self.stack_switcher.set_halign(Gtk.Align.CENTER)
        #print(dir(stack_switcher))
        self.box.pack_start(self.stack_switcher, False, False, 0)
        self.box.pack_start(self.main_area, True, True, 0)



    ##################################### Hash Tab Functions  Start ######################################################################
    
    
    def on_hash_tab_list_1_changed(self, combo):
        pass
    
    def on_toggling_hash_tab_radio_button_1(self, widget):
        self.hash_tab_hbox.set_sensitive(False)
        while Gtk.events_pending():
            Gtk.main_iteration()
        self.hash_tab_hbox.set_sensitive(False)        

    def on_toggling_hash_tab_radio_button_2(self, widget):
        self.hash_tab_hbox.set_sensitive(True)
        while Gtk.events_pending():
            Gtk.main_iteration()
        self.hash_tab_hbox.set_sensitive(True)

    def on_hash_tab_list_2_changed(self, combo):
        pass
    
    def on_hash_tab_button_2(self, widget):
        pass

    def on_hash_tab_button_1(self, widget):
        self.global_buffer.insert(self.iter, "Process Has Been Started\n")
        self.iter = self.global_buffer.get_end_iter()
        self.process_started_flag = 1
        self.hash_to_be_calculated = self.hash_tab_entry_1.get_text()
        self.hash_type_selected = self.hash_tab_list_1_material_1.get_active() + 1
        if self.hash_tab_radio_button_1.get_active():
            charset = 0
            size = 0
        if self.hash_tab_radio_button_2.get_active():
            charset = self.hash_tab_list_2_material_1.get_active() + 1
            size = self.hash_tab_entry_2.get_text()
        #print(self.hash_to_be_calculated, self.hash_type_selected, self.hash_tab_radio_button_1.get_active(), charset, size)
        self.global_buffer.insert(self.iter, str(self.hash_to_be_calculated)+ " " + str(self.hash_type_selected) + " " + str(self.hash_tab_radio_button_1.get_active()) + " " + str(charset) + " " + str(size))
        self.iter = self.global_buffer.get_end_iter()
        self.alloacting_tasks_thread = threading.Thread(target=self.allocate_tasks, daemon=True, args=(self.hash_to_be_calculated, self.hash_type_selected, self.hash_tab_radio_button_1.get_active(), charset, size))
        self.alloacting_tasks_thread.start()
        self.alloacting_tasks_thread.join()
        self.track_progress = threading.Thread(target=self.track_progress_function, daemon=True, args=())
        self.track_progress.start()
        #self.socket_check_thread = threading.Thread(target=self.socket_alive_check, daemon=True, args=())
        #self.socket_check_thread.start()
        

    def allocate_tasks(self, hash_to_be_calculated, hash_type_selected, wordlist_type, charset, size):
        for i in range(len(self.global_slave_connections)):
            self.global_slave_connections[i][0].send((str(self.hash_to_be_calculated)+ " " + str(self.hash_type_selected) + " " + str(self.hash_tab_radio_button_1.get_active()) + " " + str(charset) + " " + str(size)+" "+str(i)+" "+str(len(self.global_slave_connections))).encode())

    def track_progress_function(self):
        i=0
        current=''
        Full = []
        self.global_master_socket.setblocking(True)
        while True:
            i = (i+1)%len(self.global_slave_connections)
            current = str((self.global_slave_connections[i][0].recv(1024)).decode()).strip()
            current = current.split()
            Full = Full + current
            print(current)
            if len(current)>=2:
                print("i am not comming here")
                if current.count("Calculated")>0:                    
                    current.reverse()
                    index = current.index("Calculated")
                    statement = "self.statistics_tab_line_"+str(i+1)+"_label_4.set_label(\""+current[index+1]+" "+current[index]+"\")"
                    print("\nI am updating " + str(i+1) + " to " + current[index+1]+" "+current[index])
                    exec(statement)

                else:
                    continue 
            
            if Full.count("done") == len(self.global_slave_connections):
                break
            #print(str(self.global_slave_connections[i][1]) + " has " + current)
            #
        print(Full)
        self.global_master_socket.setblocking(False)
        for i in self.global_slave_connections:
            try:
                l = str(i[0].recv(2048).decode()).split()
                Full = Full+l
            except:
                pass
        if Full.count('hash'):
            self.global_buffer.insert(self.iter, "\n\n"+str(Full[Full.index('hash')-3]) + " and its hash " +str(Full[Full.index('hash')+1]))
            self.iter = self.global_buffer.get_end_iter()
        print(Full.count("100%"))
                    


    def socket_alive_check(self):
        i=0
        while True:
            i=i%20
            try:
                current = "self.gloabal_slave_connections["+str(i)+"][0].send(\"some data\")"
                exec(current)
            except:
                current2 = "self.statistics_tab_line_"+str(i+1)+"_label_3.set_label(\"Disconnected\")"
                exec(current2)
            time.sleep(1.5)
    

    ##################################### Hash Tab Functions  End ########################################################################


    def main_incoming_socket_function(self):
        self.global_master_socket = socket.socket()
        self.global_master_socket.bind((main_ip, 5001))
        self.global_slave_connections = []
        self.global_master_socket.listen(5)
        self.global_master_socket.setblocking(0)
        while True:
            try:
                connection, address = self.global_master_socket.accept()
                #self.append_slave_in_statistics(address)
                print(address)
                self.global_slave_connections.append((connection, address))
                current  = "self.statistics_tab_line_"+str(len(self.global_slave_connections))+"_label_2.set_label(\""+str(address[0]) +" ==> "+ str(address[1])+"\")"
                current2 = "self.statistics_tab_line_"+str(len(self.global_slave_connections))+"_label_3.set_label(\"Connected\")"
                current3 = "self.statistics_tab_line_"+str(len(self.global_slave_connections))+"_label_4.set_label(\"0% Completed\")"
                self.global_buffer.insert(self.iter, "Client " + str(address[0]) + " Connected through Port " + str(address[1]) +"\n")
                self.iter = self.global_buffer.get_end_iter()
                exec(current)
                exec(current2)
                exec(current3)
                print(address)
                if self.process_started_flag==1:
                    break
            except:
                time.sleep(1)
                continue


    def append_slave_in_statistics_when_started(self, connection, address):
        print(address)
        current = "self.statistics_tab_line_"+str(len(self.global_slave_connections))+"_label_2.set_label(\""+str(address)+"\")"
        exec(current)
        

    def progress_bar_update_function(self):
        i=1
        while True:
            statement = "self.statistics_tab_line_"+str(i)+"_progress.get_fraction()"
            current = eval(statement)
            if current > 1:
                current = 0
            else:
                current = current + 0.001
            
            statement = "self.statistics_tab_line_"+str(i)+"_progress.set_fraction(current)"
            eval(statement)
            i=(i%20)+1
            time.sleep(0.01)
        '''while True:
            new_value = self.statistics_tab_line_2_progress.get_fraction() + 0.001
            if new_value > 1 :
                new_value = 0
            self.statistics_tab_line_2_progress.set_fraction(new_value)
            time.sleep(0.01)'''
                

        

def on_main_delete_event(window, widget):    
    window.global_master_socket.close()
    window.process_started_flag=1
    Gtk.main_quit()


dialog = DialogExample()
dialog.connect("delete-event", dialog.destroyy)
dialog.run()
window = Main_Window()
window.connect("delete-event", on_main_delete_event)
window.show_all()
Gtk.main()
