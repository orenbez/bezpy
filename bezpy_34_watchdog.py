# Watchdog Monitors file systems for changes.
# Full API : https://pythonhosted.org/watchdog/api.html
# Requires `pip install watchdog`

import sys
import os
import time
import logging
from datetime import datetime as dt
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

# from watchdog.events import FileCreatedEvent
# from watchdog.events import PatternMatchingEventHandler
# from watchdog.events import RegexMatchingEventHandler



# on_any_event: Executed for any event.
# on_created:   Executed when a file or a directory is created.
# on_modified:  Executed when a file is modified or a directory renamed.
# on_deleted:   Executed when a file or directory is deleted.
# on_moved:     Executed when a file or directory is moved.

def on_created(event):
    print(f"event_type:{event.event_type}, is_directory:{event.is_directory}, src_path:{event.src_path}")

def on_deleted(event):
    pass  # This is the only way to log nothing at all.  

def on_modified(event):
    print(f"event_type:{event.event_type}, is_directory:{event.is_directory}, src_path:{event.src_path}")

def on_moved(event):
    print(f"event_type:{event.event_type}, is_directory:{event.is_directory}, src_path to dest_path:{event.src_path} TO {event.dest_path}")


def prog_exit(ret_val):
    observer.join()  # Wait until the thread terminates
    logging.info('Program End')
    sys.exit(ret_val)


def set_log():
    logging.basicConfig(filename=r'.\myfiles\watchdog.log',  # Redirects from console to log file
                        filemode='a',
                        level=logging.INFO,  # Sets logging for INFO and above (i.e. logging.debug is ignored)
                        format='%(asctime)s.%(msecs)03d: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')


if __name__ == "__main__":

    source_path = r'.\watch'
    set_log()
    logging.info('Program Start')



    # =============================================================================================================
    # For more advanced event handlers, use this 
    # =============================================================================================================
    # patterns = "*"
    # regexes=['.*']

    # ignore_patterns = ""
    # ignore_regexes=[]

    # ignore_directories = False
    # case_sensitive = True

    # event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    # event_handler = RegexMatchingEventHandler(regexes, ignore_regexes, ignore_directories, case_sensitive)

    # =============================================================================================================
    # CREATE EVENT HANDLER - This is the basic event handler without pattern or regex matching, if you don't handle
    #                       the specific on_xxxx  event then it will log automatically the event with logging.info
    # =============================================================================================================
    event_handler = LoggingEventHandler()  
    event_handler.on_created = on_created       # only create the ones you need 
    event_handler.on_deleted = on_deleted       # only create the ones you need 
    event_handler.on_modified = on_modified     # only create the ones you need 
    event_handler.on_moved = on_moved           # only create the ones you need 

    # =============================================================================================================
    # SET UP OBSERVER
    # =============================================================================================================
    observer = Observer()
    observer.schedule(event_handler, source_path, recursive=True)
    observer.start()
    print(f'Watching of {source_path} has started ...')


    try:
        while True:
            time.sleep(300)  # Check every 5 mins to see if end-of-day
            print(f'observer is_alive: {observer.is_alive()}') # Checks if observer is still running
            if dt.now().hour >= 20:  # Will stop after 8:00 pm
                observer.stop()
                prog_exit(0)
    except KeyboardInterrupt:
        observer.stop()    # Stops watching when you hit CTRL-C

    prog_exit(0)


