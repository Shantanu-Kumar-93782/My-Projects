from gi.repository import Gtk
file_ka_pointer = open("Gtk_full_manual", "w")
for i  in dir(Gtk):
    file_ka_pointer.write(str([i])+"\n")
    file_ka_pointer.write("\t|\n")
    file_ka_pointer.write("\t|\n")
    try:
        komua = eval("Gtk."+str(i))
        for j in dir(komua):
            try:
                current = str(i)+"."+j+".__doc__"
                file_ka_pointer.write("\t|===>\t"+current+"\n")
                file_ka_pointer.write("\t|\n")
                file_ka_pointer.write("\t|\n")
            except:
                continue
    except:
        continue
