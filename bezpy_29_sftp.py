# ======================================================================================================================
# FILE SECURE TRANSFER
# Documentation: https://pysftp.readthedocs.io/en/release_0.2.9/pysftp.html
#                https://winscp.net/eng/docs/ssh_keys
# Note - Doesn't seem to be a binary/text toggle, I think it is automated
# ======================================================================================================================
import os
import sys
# import re
import pypyodbc
import pysftp   # Version 0.2.9
import paramiko # Version 2.7.1
from os import environ as env
from datetime import datetime as dt

# SITE = URL, USER, PSSWD
PRODUCTION = 'production.tscinsurance.com', 'oren', 'ybHRhoB2uwXttUHBwuPofo7u58ggkj'
STAGING    = 'staging.tscinsurance.com', 'oren', 'dHf8mcsx2YmVDeRkQJNpavQNjCJPX8'
NARS       = 'sftp.narisk.com','Tristate', '!EF^gGqbMnLWe+GOS='
INSURIFY   = 'tsc.sftp.insurify.com', 'tsc_sftp', 'd^X&TZkn5s^Hf3ADv%rzSe6eYBvG#mWw'

PROGRAM_PATH = os.path.dirname(__file__)  # directory of your python file
PROGRAM_FILE = os.path.basename(__file__)  # python file name which is being executed

# ======================================================================================================================
#   datestr3(): return a date_time string e.g. '2018-04-18 22:11:59'
# ======================================================================================================================
def datestr3():
    return dt.now().strftime('%Y-%m-%d %H:%M:%S')

# ======================================================================================================================
#   sftp_exit()
# ======================================================================================================================
def sftp_exit(error_level, error_message):
    if error_level not in (9,):
        sftp.close()
    log.write(f'{error_message}, {PROGRAM_FILE} is closing\n')
    log.close()
    sys.exit(error_level)

# ======================================================================================================================
#   sftp_connect(host, user, pswd)
# ======================================================================================================================
def sftp_connect(host, user, pswd):
    cn_opts = pysftp.CnOpts(knownhosts=None)
    cn_opts.hostkeys = None
    try:
        sftp = pysftp.Connection(host, username=user, password=pswd, cnopts=cn_opts)
    except:
        print('SFTP connection Error')
        sftp_exit(9, f'{datestr3()} Error 9: sftp connection error to {host}')
    message = f'{datestr3()} Connection has been made to {host}'
    print(message)
    log.write(message + '\n')
    return sftp

# ======================================================================================================================
#   sftp_up()
# ======================================================================================================================
def sftp_up(file, local_dir, remote_dir):

    local_fp = local_dir + '\\' + file
    remote_fp = remote_dir + '/' + file

    if not sftp.isdir(remote_dir):
        sftp_exit(10, f'{datestr3()} Error 10: Remote path {remote_fp} does not exist')
    if (not os.path.isfile(local_fp)):
        sftp_exit(11, f'{datestr3()} Error 11: Local file {local_fp} does not exist')

    try:
        sftp.put(local_fp, remote_fp) # Upload
    except:
        print('SFTP Error Uploading')
        sftp_exit(12, f'{datestr3()} Error 11: sftp upload error')
    message = f"{datestr3()} {local_fp} has been uploaded"
    print(message)
    log.write(message + '\n')

# ======================================================================================================================
#   sftp_down()
# ======================================================================================================================
def sftp_down(file, remote_dir, local_dir):

    local_fp = local_dir + '\\' + file  # file path
    remote_fp = remote_dir + '/' + file # file path

    if not sftp.isfile(remote_fp):
        sftp_exit(13, f'{datestr3()} Error 13: Remote file {remote_fp} does not exist')
    if not os.path.isdir(local_dir):
        sftp_exit(14, f'{datestr3()} Error 14: Local path {local_dir} does not exist')

    try:
        sftp.get(remote_fp, local_fp)  # Download
    except:
        print('SFTP Error Downloading file')
        sftp_exit(15, f'{datestr3()} Error 15: sftp download error')
    message = f"{datestr3()} {remote_fp} has been downloaded to local server"
    print(message)
    log.write(message + '\n')


# ======================================================================================================================
#   __main__:
# ======================================================================================================================
if __name__ == '__main__':

    log_path = r'.\myfiles\sftp.log'
    log = open(log_path, 'w')

    local_directory = r'.\myfiles'     
    remote_directory = r'./tsc/test'   

    sftp = sftp_connect(*STAGING)
    sftp_up('test.txt', local_directory, remote_directory)
    sftp_down('test2.txt', remote_directory, local_directory)
    sftp.close()
    log.close()

# ======================================================================================================================
#   End of __main__
# ======================================================================================================================

# Moved from bezPy05

# sftp = pysftp.Connection(host, username=user, password=pswd, cnopts=cpts)

# sftp.get_d(remotedir, localdir) - gets all files in remote directory
# sftp.put_d(localdir, remotedir) - puts all files in remote directory

# sftp.get_r(remotepath, localpath) - gets all files and subdir files in remote directory (r = recursively)
# sftp.put_r(localpath, remotepath) - puts all files and subdir files in remote directory (r = recursively)

# sftp.get(remotepath, localpath=None) - gets single file, default is cwd
# sftp.put(localpath, remotepath=None) - puts single file, default is cwd

# sftp.pwd or sftp.getcwd() - # returns remote directory path
# sftp.listdir(remotepath='.') - lists contents of REMOTE path, default path is current directory
# sftp.listdir_attr(remotepath='.') - lists contents of REMOTE path, default path is current directory, but returns list of objects of each item

# sftp.chdir(remotepath) OR sftp.cwd('/tsc/test') - changes (REMOTE) working directory  .cwd('..') also works

# sftp.close()   - closes the connection
# sftp.open(remote_file, mode='r', bufsize=-1) - Open a file on the remote server

# sftp.execute(command) - executes command on REMOTE server
# sftp.chown(remotepath, uid=None, gid=None)   set uid or/and gid on REMOTE file/directory
# sftp.chmod(remotepath, mode=777) change mode on remote path
# sftp.stat(remotepath)  -    returns information about file/directory for the given remote path,

# sftp.makedirs(remotedir, mode=777) = mkdir(remotepath, mode=777)  - creates remote directories
# sftp.remove(remotefile) - remove the file remotefile, remotefile may include a path, if no path, then :attr:`.pwd` is used.  This method only works on files
# sftp.rename(remote_src, remote_dest) rename a file or directory on the remote host.
# sftp.rmdir(remotepath) - remove remote directory

# sftp.isdir(remotepath) - return True, if remotepath is a directory
# sftp.isfile(remotepath) -return True if remotepath is a file
# sftp.exists(remotepath) - Test whether a remotepath exists.

# sftp.lexists(remotepath)- Test whether a remotepath exists.  Returns True for broken symbolic links
# sftp.readlink(remotelink) - Return the target of a symlink (shortcut)

# ======================================================================================================================
#   sftp_connect2(host, user, pswd)
# ======================================================================================================================
def sftp_connect2(host, user, pswd):

    # optional 'connection options object', used for passing extended options to the Connection
    cpts = pysftp.CnOpts(knownhosts=None)  # Defaults to ~/.ssh/known_hosts
    # cpts.hostkeys = None   # host key is used to verify the server's identity
    # cpts.compression = None
    # cpts.ciphers = None  # sets list of ciphers to use in order
    # cpts.log = 'logsftp.log'  # Sets logfile

    #keydata = b"""L+WsiL5VL51ecJi3LVjmblkAdUTU+xbmXmUArIU5+8N6ua76jO/+T"""
    #key = paramiko.RSAKey(data=decodebytes(keydata))
    #cpts.hostkeys.add(host, 'ssh-rsa', key)

    # key = cn_opts.hostkeys.load(drive + r'\PICKUP\dashboard\key\id_rsa_oren.KEY')
    # cn_opts.hostkeys.add(host, 'ssh-rsa', key)


    try:
        # Other Parameters for .Connection()
        # private_key (str|obj|None) – Default: None - path to private key file(str) or paramiko.AgentKey
        # private_key_pass (str|None) – Default: None - password to use, if private_key is encrypted.
        # port (int) – Default: 22 - The SSH port of the remote machine
        # cnopts (None|CnOpts) – Default: None - extra connection options set in a CnOpts object.
        # default_path (str|None) – Default: None - set a default path upon connection
        sftp = pysftp.Connection(host, username=user, password=pswd, cnopts=cpts)

    except:
        print('SFTP connection Error')
        sftp_exit(9, f'{datestr3()} Error 9: sftp connection error to {host}')
    return sftp






