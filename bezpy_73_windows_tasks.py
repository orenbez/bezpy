# Uses the Windows Task Scheduler API not in the standard library
# https://docs.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-2-0-interfaces?redirectedfrom=MSDN
# Retreives Data from Task Scheduler.  Looping through the root and then all subfolders
# Also note the 'schedule' module


import win32com.client # requires pypiwin32 to be installed
import pandas as pd
from tabulate import tabulate

def tab(df):
    print(tabulate(df, headers='keys', tablefmt='rst'))

TASK_ENUM_HIDDEN = 1
TASK_STATE = {0: 'Unknown',
              1: 'Disabled',
              2: 'Queued',
              3: 'Ready',
              4: 'Running'}

OPERATIONAL_CODES = { 0x00000000: 'The operation completed successfully.',
                      0x00000001: 'Incorrect function called or unknown function called.',
                      0x00000002: 'File not found.',
                      0x0000000A: 'The environment is incorrect.',
                      0x00041300: 'The task is ready to run at its next scheduled time.',
                      0x00041301: 'The task is currently running',
                      0x00041302: 'The task will not run at the scheduled times because it has been disabled',
                      0x00041303: 'The task has not yet run.',
                      0x00041304: 'There are no more runs scheduled for this task.',
                      0x00041305: 'One or more of the properties that are needed to run this task on a schedule have not been set',
                      0x00041306: 'The last run of the task was terminated by the user.',
                      0x00041307: 'Either the task has no triggers or the existing triggers are disabled or not set',
                      0x00041308: 'Event triggers do not have set run times.',
                      0x8004130A: 'One or more of the properties required to run this task have not been set.',
                      0x8004130B: 'There is no running instance of the task.',
                      0x8004130C: 'The Task Scheduler service is not installed on this computer.',
                      0x8004130D: 'The task object could not be opened.',
                      0x8004130E: 'The object is either an invalid task object or is not a task object.',
                      0x8004130F: 'No account information could be found in the Task Scheduler security database for the task indicated.',
                      0x80041310: 'Unable to establish existence of the account specified.',
                      0x80041311: 'Corruption was detected in the Task Scheduler security database; the database has been reset.',
                      0x80041312: 'Task Scheduler security services are available only on Windows NT',
                      0x80041313: 'The task object version is either unsupported or invalid.',
                      0x80041314: 'The task has been configured with an unsupported combination of account settings and run time options.',
                      0x80041315: 'The Task Scheduler Service is not running.',
                      0x80041316: 'The task XML contains an unexpected node.',
                      0x80041317: 'The task XML contains an element or attribute from an unexpected namespace.',
                      0x80041318: 'The task XML contains a value which is incorrectly formatted or out of range.',
                      0x80041319: 'The task XML is missing a required element or attribute.',
                      0x8004131A: 'The task XML is malformed.',
                      0x0004131B: 'The task is registered, but not all specified triggers will start the task',
                      0x0004131C: 'The task is registered, but may fail to start. Batch logon privilege needs to be enabled for the task principal',
                      0x8004131D: 'The task XML contains too many nodes of the same type.',
                      0x8004131E: 'The task cannot be started after the trigger end boundary.',
                      0x8004131F: 'An instance of this task is already running.',
                      0x80041320: 'The task will not run because the user is not logged on.',
                      0x80041321: 'The task image is corrupt or has been tampered with.',
                      0x80041322: 'The Task Scheduler service is not available.',
                      0x80041323: 'The Task Scheduler service is too busy to handle your request. Please try again later.',
                      0x80041324: 'The Task Scheduler service attempted to run the task, but the task did not run due to one of the constraints in the task definition.',
                      0x00041325: 'The Task Scheduler service has asked the task to run.',
                      0x80041326: 'The task is disabled.',
                      0x80041327: 'The task has properties that are not compatible with earlier versions of Windows.',
                      0x80041328: 'The task settings do not allow the task to start on demand.',
                      0x8004131F: 'An instance of this task is already running.',
                      0x800704DD: 'User has not logged on to the network.',
                      0xC000013A: 'The application terminated as a result of a CTRL+C.',
                      0xC06D007E: 'Unknown software exception.}',}


scheduler = win32com.client.Dispatch('Schedule.Service')
scheduler.Connect()
task_list = []

n = 0
folders = [scheduler.GetFolder('\\')]
while folders:
    folder = folders.pop(0)
    tasks = list(folder.GetTasks(TASK_ENUM_HIDDEN))
    n += len(tasks)
    for task in tasks:
        settings = task.Definition.Settings
        task_list.append([task.Name, settings.Hidden, TASK_STATE[task.State], task.LastRunTime.ctime(), task.NextRunTime.ctime(), task.LastTaskResult, OPERATIONAL_CODES.get(task.LastTaskResult), task.Path,])
    folders += list(folder.GetFolders(0))  # This will retrieve all SubFolders

df = pd.DataFrame(data=task_list, columns=['Name','Hidden', 'State', 'LastRunTime', 'NextRunTime', 'LastTaskResultCode', 'LastTaskResultCode', 'Path'])
tab(df)

print(f'Total Tasks={n}')
