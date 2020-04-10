import socket
import time
import os
import hashlib
import math
import gi
import threading
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject, Gio, GLib, Gdk


class Main_Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Task Distributer - Slave")
        self.set_default_size(200, 400)
        self.set_resizable(False)
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(self.box)
        self.label_1 = Gtk.Label()
        self.label_1.set_label("Enter Your Master's IP :")
        self.label_1.set_halign(Gtk.Align.START)
        self.box.pack_start(self.label_1, False, False, 5)
        self.hbox_1 = Gtk.HBox(spacing=10)
        self.entry_1 = Gtk.Entry()
        self.button_1 = Gtk.Button()
        self.button_1.set_label("Connect")
        self.button_1.connect("clicked", self.on_button_1_clicked)
        self.hbox_1.pack_start(self.entry_1, True, True, 0)
        self.hbox_1.pack_start(self.button_1, False, False, 5)
        self.hbox_2 = Gtk.HBox(spacing=10)
        self.button_2 = Gtk.Button()
        self.button_2.set_label("Start")
        self.hbox_2.pack_start(self.button_2, False, False, 30)
        self.button_2.connect("clicked", self.on_button_2_clicked)
        self.button_3 = Gtk.Button()
        self.button_3.set_label("Stop")
        self.hbox_2.pack_start(self.button_3, False, False, 30)
        self.box.pack_start(self.hbox_1, False, False, 5)
        self.box.pack_start(self.hbox_2, False, False, 5)
        self.label_2 = Gtk.Label()
        self.label_2.set_label("Logs :")
        self.box.pack_start(self.label_2, False, False, 5)
        self.scrollable_window = Gtk.ScrolledWindow()
        self.scrollable_window.set_policy(Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)
        self.text_view_buffer = Gtk.TextBuffer()
        self.text_view = Gtk.TextView(buffer=self.text_view_buffer)
        self.text_view.set_size_request(100, 200)
        self.scrollable_window.set_size_request(100, 200)
        self.scrollable_window.add(self.text_view)
        self.box.pack_start(self.scrollable_window, False, False, 5)
        self.box.set_margin_top(10)
        self.box.set_margin_bottom(10)
        self.box.set_margin_left(10)
        self.box.set_margin_right(10)
        self.label_2.set_halign(Gtk.Align.START)
        self.entry_1.set_size_request(50, 35)
        self.entry_1.set_halign(Gtk.Align.START)
        self.button_1.set_halign(Gtk.Align.END)
        self.button_2.set_size_request(35, 35)
        self.button_3.set_size_request(35, 35)
        self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "Welcome To The Application\n\n")
        self.text_view.set_editable(False)
    
    def on_button_1_clicked(self, widget):
        self.slave_socket = socket.socket()
        
        try:
            self.slave_socket.connect((str(self.entry_1.get_text()), 5001))
            self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "Connected to the Master\nConnection Successful!!\n\n")
            self.slave_socket.setblocking(False)
        except:
            self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "Can't Connect to the Master\nConnection Unsuccessful!!\n\n")
            #self.task_waiting = threading.Thread(target=self.task_waiting_thread_function, daemon=True)
            #self.task_waiting.start()
        
    
    def task_waiting_thread_function(self):
        while self.my_params==[]:
            try:
                self.my_params = str((self.slave_socket.recv(2048)).decode()).split()
            except:
                pass
            time.sleep(0.5)
        

    def on_button_2_clicked(self, widget):
        self.my_params = []
        while self.my_params==[]:
            try:
                self.my_params = str((self.slave_socket.recv(2048)).decode()).split()
            except:
                pass
            time.sleep(0.5)
        self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "Hash to be calculated: \n" +str(self.my_params[0])+"\n\n")
        if self.my_params[1] == '1':
             self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "Hash Type Selected: \nMD5\n\n")
        elif self.my_params[1] == '2':
             self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "Hash Type Selected: \nSHA1\n\n")
        elif self.my_params[1] == '3':
             self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "Hash Type Selected: \nSHA256\n\n")
        else:
            pass

        if self.my_params[2]=="True":
            self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "Wordlist Type Selected: \nPredefined\n\n")
            self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "Total Combinations : \n" + str(((os.popen('wc predefined_wordlist.txt -l').read()).split())[0]) + "\n\n")
        else:
            self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "Wordlist Type Selected: \nCustom\n\n")
            if self.my_params[3]=='1':
                self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "Total Combinations : \n" + str(26**int(self.my_params[4])) + "\n\n")
            elif self.my_params[3]=='2':
                self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "Total Combinations : \n" + str(52**int(self.my_params[4])) + "\n\n")
            elif self.my_params[3]=='3':
                self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "Total Combinations : \n" + str(10**int(self.my_params[4])) + "\n\n")
            elif self.my_params[3]=='4':
                self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "Total Combinations : \n" + str(62**int(self.my_params[4])) + "\n\n")
        self.calculate_thread = threading.Thread(target=self.task_to_be_done, daemon=True, args=())
        self.calculate_thread.start()
    
    def task_to_be_done(self):

        self.hash_to_be_calculated = self.my_params[0]
        self.hash_type_selected = int(self.my_params[1])
        if self.my_params[2]=='True':
            self.wordlist_type = "Predefined"
        else:
            self.wordlist_type = "Custom"


        if self.wordlist_type == "Predefined":
            self.number_of_words = int(((os.popen('wc predefined_wordlist.txt -l').read()).split())[0])
        else:
            if self.my_params[3]=='1':
                self.number_of_words = 26**int(self.my_params[4])
                self.my_indices = list('abcdefghijklmnopqrstuvwxyz')
            elif self.my_params[3]=='2':
                self.number_of_words = 52**int(self.my_params[4])
                self.my_indices = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            elif self.my_params[3]=='3':
                self.number_of_words = 10**int(self.my_params[4])
                self.my_indices = list('0123456789')
            elif self.my_params[3]=='4':
                self.number_of_words = 62**int(self.my_params[4])
                self.my_indices = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

        if int(self.my_params[5])+1 != int(self.my_params[6]):
            self.my_first = (int(self.number_of_words/int(self.my_params[6]))*int(self.my_params[5]))+1
            self.my_last = (int(self.number_of_words/int(self.my_params[6]))*(int(self.my_params[5])+1))+1
        else:
            self.my_first = (int(self.number_of_words/int(self.my_params[6]))*int(self.my_params[5]))+1
            self.my_last = self.number_of_words


        if self.wordlist_type == "Custom":
            self.size = int(self.my_params[4])
            self.to_find = self.my_first
            self.my_word1 = ''
            for i in range(self.size):
                current = self.to_find%len(self.my_indices)
                if current == math.floor(current):
                    self.my_word1 += self.my_indices[int(current)-1]
                elif current > math.floor(current):
                    self.my_word1 += self.my_indices[int(math.ceil(current))-1]
                else:
                    pass
                self.to_find = self.to_find/len(self.my_indices)
            self.my_word1 = list(self.my_word1)
            self.my_word1.reverse()
            self.my_word1 = "".join(self.my_word1)
            print(self.my_word1)

            self.size = int(self.my_params[4])
            self.to_find = self.my_last
            self.my_word2 = ''
            self.my_last_memory = " False "
            for i in range(self.size):
                current = self.to_find%len(self.my_indices)
                if current == math.floor(current):
                    self.my_word2 += self.my_indices[int(current)-1]
                elif current > math.floor(current):
                    self.my_word2 += self.my_indices[int(math.ceil(current))-1]
                else:
                    pass
                self.to_find = self.to_find/len(self.my_indices)
            self.my_word2 = list(self.my_word2)
            self.my_word2.reverse()
            self.my_word2 = "".join(self.my_word2)
            print(self.my_word2)
            self.statement = str("crunch " + str(self.size) + " " + str(self.size) + " " + "".join(self.my_indices) + " -s " + self.my_word1 + " -e " + self.my_word2 + " > my_pass_list.txt")
            os.popen(self.statement).read()
        
        if self.wordlist_type == "Predefined":
            self.my_famous_dividend = self.my_last//50
            print("i am here")
            self.f = open("predefined_wordlist.txt", "r")
            if self.hash_type_selected == 1:
                for i, line in enumerate(self.f):
                    #time.sleep(0.01)
                    if i >= self.my_first:
                        if i%self.my_famous_dividend==0:
                            my_current_progress = str("{:.1f}".format((i/self.my_last)*int(self.my_params[6])*100)) + "% Calculated\n\n"
                            self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), my_current_progress)
                            self.slave_socket.send(my_current_progress.encode())
                            time.sleep(1)
                        if self.hash_to_be_calculated == str((hashlib.md5((line.rstrip()).encode())).hexdigest()):
                            print("i got it")
                            print(str(line.strip()) + " and its hash " + str((hashlib.md5(str(line.rstrip()).encode())).hexdigest()))
                            self.my_last_memory = str(line.strip()) + " and its hash " + str((hashlib.md5(str(line.rstrip()).encode())).hexdigest())
                            self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "100% Calculated")
                            self.slave_socket.send(" 100% Calculated ".encode())
                            break
                    if i > self.my_last:
                        self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "100% Calculated")
                        self.slave_socket.send(" 100% Calculated ".encode())
                        break
                
            elif self.hash_type_selected == 2:
                for i, line in enumerate(self.f):
                    #time.sleep(0.01)
                    if i >= self.my_first:
                        if i%self.my_famous_dividend==0:
                            my_current_progress = str("{:.1f}".format((i/self.my_last)*int(self.my_params[6])*100)) + "% Calculated\n\n"
                            self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), my_current_progress)
                            self.slave_socket.send(my_current_progress.encode())
                            time.sleep(1)
                    if i >= self.my_first:
                        if self.hash_to_be_calculated == str((hashlib.sha1((line.rstrip()).encode())).hexdigest()):
                            print("i got it")
                            print(str(line.strip()) + " and its hash " + str((hashlib.sha1(str(line.rstrip()).encode())).hexdigest()))
                            self.my_last_memory = str(line.strip()) + " and its hash " + str((hashlib.sha1(str(line.rstrip()).encode())).hexdigest())
                            self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "100% Calculated")
                            self.slave_socket.send(" 100% Calculated ".encode())
                            break
                    if i > self.my_last:
                        self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "100% Calculated")
                        self.slave_socket.send(" 100% Calculated ".encode())
                        break
                
            elif self.hash_type_selected == 3:
                for i, line in enumerate(self.f):
                    #time.sleep(0.01)
                    if i >= self.my_first:
                        if i%self.my_famous_dividend==0:
                            my_current_progress = str("{:.1f}".format((i/self.my_last)*int(self.my_params[6])*100)) + "% Calculated\n\n"
                            self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), my_current_progress)
                            self.slave_socket.send(my_current_progress.encode())
                            time.sleep(1)
                    if i >= self.my_first:
                        if self.hash_to_be_calculated == str((hashlib.sha256((line.rstrip()).encode())).hexdigest()):
                            print("i got it")
                            print(str(line.strip()) + " and its hash " + str((hashlib.sha256(str(line.rstrip()).encode())).hexdigest()))
                            self.my_last_memory = str(line.strip()) + " and its hash " + str((hashlib.sha256(str(line.rstrip()).encode())).hexdigest())
                            self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "100% Calculated")
                            self.slave_socket.send(" 100% Calculated ".encode())
                            break
                    if i > self.my_last:
                        self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "100% Calculated")
                        self.slave_socket.send(" 100% Calculated ".encode())
                        break
            else:
                pass
                


        if self.wordlist_type == "Custom":
            self.my_famous_dividend = self.number_of_words//50
            print("i am here in custom")
            self.f = open("my_pass_list.txt", "r")
            line = self.f.readline()
            if self.hash_type_selected == 1:
                i=0
                while line:
                    #time.sleep(0.01)
                    i=i+1
                    if i%self.my_famous_dividend==0:
                        my_current_progress =  str("{:.1f}".format((i/self.number_of_words)*int(self.my_params[6])*100)) + "% Calculated\n\n"
                        self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), my_current_progress)
                        self.slave_socket.send(my_current_progress.encode())
                        time.sleep(1)
                    if self.hash_to_be_calculated == str((hashlib.md5((line.rstrip()).encode())).hexdigest()):
                        print("i got it")
                        print(str(line.strip()) + " and its hash " + str((hashlib.md5(str(line.rstrip()).encode())).hexdigest()))
                        self.my_last_memory = str(line.strip()) + " and its hash " + str((hashlib.md5(str(line.rstrip()).encode())).hexdigest())
                        #self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "100% Calculated")
                        #self.slave_socket.send(" 100% Calculated ".encode())
                        break
                    line = self.f.readline()
                self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "100% Calculated")
                self.slave_socket.send(" 100% Calculated ".encode())
            elif self.hash_type_selected == 2:
                i=0
                while line:
                    #time.sleep(0.01)
                    i=i+1
                    if i%self.my_famous_dividend==0:
                        my_current_progress =  str("{:.1f}".format((i/self.number_of_words)*int(self.my_params[6])*100)) + "% Calculated\n\n"
                        self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), my_current_progress)
                        self.slave_socket.send(my_current_progress.encode())
                        time.sleep(1)
                    if self.hash_to_be_calculated == str((hashlib.sha1((line.rstrip()).encode())).hexdigest()):
                        print("i got it")
                        print(str(line.strip()) + " and its hash " + str((hashlib.sha1(str(line.rstrip()).encode())).hexdigest()))
                        self.my_last_memory = str(line.strip()) + " and its hash " + str((hashlib.sha1(str(line.rstrip()).encode())).hexdigest())
                        #self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "100% Calculated")
                        #self.slave_socket.send(" 100% Calculated ".encode())
                        break
                    line = self.f.readline()
                self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "100% Calculated")
                self.slave_socket.send(" 100% Calculated ".encode())
            elif self.hash_type_selected == 3:
                i=0
                while line:
                    #time.sleep(0.01)
                    i=i+1
                    if i%self.my_famous_dividend==0:
                        my_current_progress =  str("{:.1f}".format((i/self.number_of_words)*int(self.my_params[6])*100)) + "% Calculated\n\n"
                        self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), my_current_progress)
                        self.slave_socket.send(my_current_progress.encode())
                        time.sleep(1)
                    if self.hash_to_be_calculated == str((hashlib.sha256((line.rstrip()).encode())).hexdigest()):
                        print("i got it")
                        print(str(line.strip()) + " and its hash " + str((hashlib.sha256(str(line.rstrip()).encode())).hexdigest()))
                        self.my_last_memory = str(line.strip()) + " and its hash " + str((hashlib.sha1(str(line.rstrip()).encode())).hexdigest())
                        #self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "100% Calculated")
                        #self.slave_socket.send(" 100% Calculated ".encode())
                        break
                    line = self.f.readline()
                self.text_view_buffer.insert(self.text_view_buffer.get_end_iter(), "100% Calculated")
                self.slave_socket.send(" 100% Calculated ".encode())
            else:
                pass
        
        self.slave_socket.send(" done ".encode())
        print(self.my_last_memory)
        self.slave_socket.send(self.my_last_memory.encode())
        self.slave_socket.close()


def on_main_delete_event(window, widget):    
    window.process_started_flag=1
    Gtk.main_quit()

window = Main_Window()
window.connect("delete-event", on_main_delete_event)
window.show_all()
Gtk.main()
print("this also executes")


























### RAW CODE

#data = slave_socket.recv(1024).decode()
#starting, ending = data.split()
#os.system("crunch 4 4 -s "+starting+" -e "+ ending)


'''if self.hash_tab_radio_button_2.get_active():
            if charset==1:
                comman = "crunch "+ size +" "+ size+ " abcdefghijklmnopqrstuvwxyz > current_pass_list.txt"
                os.popen(comman).read()
            elif charset==2:
                comman = "crunch "+ size +" "+ size+ " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ > current_pass_list.txt"
                os.popen(comman).read()
            elif charset==3:
                comman = "crunch "+ size +" "+ size+ " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456890 > current_pass_list.txt"
                os.popen(comman).read()
            elif charset==4:
                comman = "crunch "+ size +" "+ size+ " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456890 > current_pass_list.txt"
                os.popen(comman).read()'''

'''#data = ""
#while data!="exit":
    #time.sleep(3)
    print("recv mai atka")
   # data = slave_socket.recv(1024).decode()
    print(str(data))
    print("input mai atka")
    #slave_socket.send(input().encode())
if str(input()):'''

'''main_ip = ''

class DialogExample(Gtk.Dialog):

    def __init__(self):
        Gtk.Dialog.__init__(self)
        self.set_default_size(150, 100)
        label = Gtk.Label()
        label.set_label("This is a dialog to display additional information")
        self.entry = Gtk.Entry()
        button = Gtk.Button()
        button.connect("clicked", self.on_clicked)
        box = self.get_content_area()
        box.add(label)
        box.add(self.entry)
        box.add(button)
        self.show_all()
        #return str(entry.get_text())
    
    def on_clicked(self, widget):
        global main_ip
        main_ip = self.entry.get_text()
        print("this is the main ip" + str(main_ip))
        self.destroy()
dialog = DialogExample()
dialog.run()
#dialog.destroy()'''

'''slave_socket = socket.socket()
slave_socket.connect(('127.0.0.1', 5001))

my_params = str((slave_socket.recv(2048)).decode()).split()
print(my_params)
hash_to_be_calculated = my_params[0]
hash_type_selected = int(my_params[1])
if my_params[2]=='True':
    wordlist_type = "Predefined"
else:
    wordlist_type = "Custom"


if wordlist_type == "Predefined":
    number_of_words = int(((os.popen('wc predefined_wordlist.txt -l').read()).split())[0])
else:
    if my_params[3]=='1':
        number_of_words = 26**int(my_params[4])
        my_indices = list('abcdefghijklmnopqrstuvwxyz')
    elif my_params[3]=='2':
        number_of_words = 52**int(my_params[4])
        my_indices = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    elif my_params[3]=='3':
        number_of_words = 10**int(my_params[4])
        my_indices = list('0123456789')
    elif my_params[3]=='4':
        number_of_words = 62**int(my_params[4])
        my_indices = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

if int(my_params[5])+1 != int(my_params[6]):
    my_first = (int(number_of_words/int(my_params[6]))*int(my_params[5]))+1
    my_last = (int(number_of_words/int(my_params[6]))*(int(my_params[5])+1))+1
else:
    my_first = (int(number_of_words/int(my_params[6]))*int(my_params[5]))+1
    my_last = number_of_words


if wordlist_type == "Custom":
    size = int(my_params[4])
    to_find = my_first
    my_word1 = ''
    for i in range(size):
        current = to_find%len(my_indices)
        if current == math.floor(current):
            my_word1 += my_indices[int(current)-1]
        elif current > math.floor(current):
            my_word1 += my_indices[int(math.ceil(current))-1]
        else:
            pass
        to_find = to_find/len(my_indices)
    my_word1 = list(my_word1)
    my_word1.reverse()
    my_word1 = "".join(my_word1)
    print(my_word1)

    size = int(my_params[4])
    to_find = my_last
    my_word2 = ''

    for i in range(size):
        current = to_find%len(my_indices)
        if current == math.floor(current):
            my_word2 += my_indices[int(current)-1]
        elif current > math.floor(current):
            my_word2 += my_indices[int(math.ceil(current))-1]
        else:
            pass
        to_find = to_find/len(my_indices)
    my_word2 = list(my_word2)
    my_word2.reverse()
    my_word2 = "".join(my_word2)
    print(my_word2)
    statement = str("crunch " + str(size) + " " + str(size) + " " + "".join(my_indices) + " -s " + my_word1 + " -e " + my_word2 + " > my_pass_list.txt")
    os.popen(statement).read()

if wordlist_type == "Predefined":
    print("i am here")
    f = open("predefined_wordlist.txt", "r")
    if hash_type_selected == 1:
        for i, line in enumerate(f):
            if i >= my_first:
                if hash_to_be_calculated == str((hashlib.md5((line.rstrip()).encode())).hexdigest()):
                    print(str(line.strip()) + " and its hash" + str((hashlib.md5(str(line.rstrip()).encode())).hexdigest()))
                    break
            if i > my_last:
                break
    if hash_type_selected == 2:
        for i, line in enumerate(f):
            if i >= my_first:
                if hash_to_be_calculated == str((hashlib.sha1((line.rstrip()).encode())).hexdigest()):
                    print(str(line.strip()) + " and its hash" + str((hashlib.sha1(str(line.rstrip()).encode())).hexdigest()))
                    break
            if i > my_last:
                break
    if hash_type_selected == 3:
        for i, line in enumerate(f):
            if i >= my_first:
                if hash_to_be_calculated == str((hashlib.sha256((line.rstrip()).encode())).hexdigest()):
                    print(str(line.strip()) + " and its hash" + str((hashlib.sha256(str(line.rstrip()).encode())).hexdigest()))
                    break
            if i > my_last:
                break


if wordlist_type == "Custom":
    print("i am here in custom")
    f = open("my_pass_list.txt", "r")
    line = f.readline()
    if hash_type_selected == 1:
        while line:
            if hash_to_be_calculated == str((hashlib.md5((line.rstrip()).encode())).hexdigest()):
                print(str(line.strip()) + " and its hash" + str((hashlib.md5(str(line.rstrip()).encode())).hexdigest()))
                break
            line = f.readline()
    if hash_type_selected == 2:
        while line:
            if hash_to_be_calculated == str((hashlib.sha1((line.rstrip()).encode())).hexdigest()):
                print(str(line.strip()) + " and its hash" + str((hashlib.sha1(str(line.rstrip()).encode())).hexdigest()))
                break
            line = f.readline()
    if hash_type_selected == 3:
        while line:
            if hash_to_be_calculated == str((hashlib.sha256((line.rstrip()).encode())).hexdigest()):
                print(str(line.strip()) + " and its hash" + str((hashlib.sha256(str(line.rstrip()).encode())).hexdigest()))
                break
            line = f.readline()

slave_socket.close()'''
