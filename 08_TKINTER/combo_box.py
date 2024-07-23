import tkinter as tk
from tkinter.ttk import *
from tkinter import *





xx = ['after', 'after_cancel', 'after_idle', 'anchor', 'bbox', 'bell', 'bind', 'bind_all', 'bind_class', 'bindtags', 'cget', 'children', 'clipboard_append', 'clipboard_clear', 'clipboard_get', 'columnconfigure', 'config', 'configure', 'current', 'delete', 'deletecommand', 'destroy', 'event_add', 'event_delete', 'event_generate', 'event_info', 'focus', 'focus_displayof', 'focus_force', 'focus_get', 'focus_lastfor', 'focus_set', 'forget', 'get', 'getboolean', 'getdouble', 'getint', 'getvar', 'grab_current', 'grab_release', 'grab_set', 'grab_set_global', 'grab_status', 'grid', 'grid_anchor', 'grid_bbox', 'grid_columnconfigure', 'grid_configure', 'grid_forget', 'grid_info', 'grid_location', 'grid_propagate', 'grid_remove', 'grid_rowconfigure', 'grid_size', 'grid_slaves', 'icursor', 'identify', 'image_names', 'image_types', 'index', 'info', 'insert', 'instate', 'keys', 'lift', 'location', 'lower', 'mainloop', 'master', 'nametowidget', 'option_add', 'option_clear', 'option_get', 'option_readfile', 'pack', 'pack_configure', 'pack_forget', 'pack_info', 'pack_propagate', 'pack_slaves', 'place', 'place_configure', 'place_forget', 'place_info', 'place_slaves', 'propagate', 'quit', 'register', 'rowconfigure', 'scan_dragto', 'scan_mark', 'select_adjust', 'select_clear', 'select_from', 'select_present', 'select_range', 'select_to', 'selection_adjust', 'selection_clear', 'selection_from', 'selection_get', 'selection_handle', 'selection_own', 'selection_own_get', 'selection_present', 'selection_range', 'selection_to', 'send', 'set', 'setvar', 'size', 'slaves', 'state', 'tk', 'tk_bisque', 'tk_focusFollowsMouse', 'tk_focusNext', 'tk_focusPrev', 'tk_setPalette', 'tk_strictMotif', 'tkraise', 'unbind', 'unbind_all', 'unbind_class', 'update', 'update_idletasks', 'validate', 'wait_variable', 'wait_visibility', 'wait_window', 'waitvar', 'widgetName', 'winfo_atom', 'winfo_atomname', 'winfo_cells', 'winfo_children', 'winfo_class', 'winfo_colormapfull', 'winfo_containing', 'winfo_depth', 'winfo_exists', 'winfo_fpixels', 'winfo_geometry', 'winfo_height', 'winfo_id', 'winfo_interps', 'winfo_ismapped', 'winfo_manager', 'winfo_name', 'winfo_parent', 'winfo_pathname', 'winfo_pixels', 'winfo_pointerx', 'winfo_pointerxy', 'winfo_pointery', 'winfo_reqheight', 'winfo_reqwidth', 'winfo_rgb', 'winfo_rootx', 'winfo_rooty', 'winfo_screen', 'winfo_screencells', 'winfo_screendepth', 'winfo_screenheight', 'winfo_screenmmheight', 'winfo_screenmmwidth', 'winfo_screenvisual', 'winfo_screenwidth', 'winfo_server', 'winfo_toplevel', 'winfo_viewable', 'winfo_visual', 'winfo_visualid', 'winfo_visualsavailable', 'winfo_vrootheight', 'winfo_vrootwidth', 'winfo_vrootx', 'winfo_vrooty', 'winfo_width', 'winfo_x', 'winfo_y', 'xview', 'xview_moveto', 'xview_scroll']

win = tk.Tk()
win.title("Gas Calculator")
v = tk.IntVar()

list1 = ("AUDI", "FORD", "MAZDA")
list2 = ("xxx", "yyy", "zzz")





def callback(eventObject):
    print(eventObject)
    print(cmb.get(), cmb.current())        


cmb = Combobox(win, values=xx, font="none 12 bold", width=30)
# cmb['values']= list1 --- this is an alternate way to set list
cmb.current(0) #set the default selected item
cmb.grid(row=1, column=1)
cmb.bind("<<ComboboxSelected>>", callback)


# bind the <Return> key to a function which changes combo_box values
def func(event):
    print("You hit return.")
    cmb['values']= list2
    
win.bind('<Return>', func)



win.mainloop()
