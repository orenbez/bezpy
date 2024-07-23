import os
import sys
import logging
from time import sleep
from datetime import datetime as dt
from bezpy_11_send_email import send


# ======================================================================================================================
# C:\Users\ECUSA-008>tracert yahoo.com
    # note `tracert yahoo.com` traces route to yahoo.com from your PC
# ======================================================================================================================
# Tracing route to yahoo.com [74.6.231.21]
# over a maximum of 30 hops:
#
#   1    <1 ms    <1 ms    <1 ms  192.168.1.1        <---------default gateway
#   2     *        *        *     Request timed out.  <--------Public-IP Address which is blocked by ISP
#   3    10 ms     8 ms    12 ms  67.59.236.197
#   4     9 ms     9 ms    13 ms  167.206.32.4
#   5    11 ms    11 ms    10 ms  451be060.cst.lightpath.net [65.19.99.96]
#   6    10 ms     9 ms    10 ms  64.15.3.182
#   7    10 ms     9 ms    18 ms  ge-0-1-3-d201.msr1.gq1.yahoo.com [216.115.110.148]
#   ...
#  15    52 ms    52 ms    53 ms  media-router-fp74.prod.media.vip.ne1.yahoo.com [74.6.231.21]   <----- yahoo.com (last hop)
# ======================================================================================================================
# EAST COAST
# ======================================================================================================================
LOCAL = '127.0.0.1'              # Checks that your network card is working, this the loop back ip address  ('ping localhost' )
SERVER =  '192.168.1.98'
CAMERA = '192.168.1.150'
DEFAULT_GATEWAY = '192.168.1.1'    # Gateway for the office (LAN)
OFFICE_IP = '173.2.159.113'
GATEWAY_IP = '67.59.236.197'       # Gateway for the ISP
WEBSITE = 'yahoo.com'              # Checks connectivity to internet

east_coast = {0: ['LOCAL', LOCAL, 0, 0],
              1: ['SERVER', SERVER, 0, 0],
              2: ['CAMERA', CAMERA, 0, 0],
              3: ['DEFAULT_GATEWAY', DEFAULT_GATEWAY, 0, 0],
              4: ['OFFICE_IP', OFFICE_IP, 0, 0],
              5: ['GATEWAY_IP', GATEWAY_IP, 0, 0],
              6: ['WEBSITE', WEBSITE, 0, 0]}



# ======================================================================================================================
# C:\Users\orenb>tracert  yahoo.com
# ======================================================================================================================
# Tracing route to yahoo.com [74.6.143.26]
# over a maximum of 30 hops:
#
#   1     5 ms     5 ms     4 ms  192.168.68.1        <------ default gateway  (Deco Router)
#   2     6 ms     7 ms     5 ms  192.168.1.1         <----- LAN optimum gateway IP (Altice Modem)
#   3     *        *        *     Request timed out.  <----- Public-IP Address which is blocked by ISP (24.189.177.141)
#   4    12 ms    13 ms    11 ms  67.59.236.217       <----- GATEWAY_IP_1
#   5    14 ms    13 ms    13 ms  dstswr2-ge3-1.rh.hcvlny.cv.net [167.206.32.6]  <---- GATEWAY_IP_2
#   ...
#  14    22 ms    23 ms    23 ms  media-router-fp74.prod.media.vip.bf1.yahoo.com [74.6.143.26]   <----- yahoo.com

# ======================================================================================================================
# FOR HOME TEST
# ======================================================================================================================
LOCAL = '127.0.0.1'                                 # Checks that your network card is working, this the loop back ip address  ('ping localhost' )
ROUTER_IP = '192.168.68.1'                          # IP for the Router (LAN)
MODEM_IP = '192.168.1.1'                            # IP for the Modem
EXTERNAL_IP = '24.189.177.141'
GATEWAY_IP_1 = '67.59.236.221'
GATEWAY_IP_2 = 'dstswr2-ge3-1.rh.hcvlny.cv.net'     # Gateway for the ISP
WEBSITE = 'yahoo.com'                               # Checks connectivity to internet

home = {0: ['LOCAL', LOCAL, 0, 0],
        1: ['ROUTER_IP', ROUTER_IP, 0, 0],
        2: ['MODEM_IP', MODEM_IP, 0, 0],
        3: ['EXTERNAL_IP', EXTERNAL_IP, 0, 0],
        4: ['GATEWAY_IP_1', GATEWAY_IP_1, 0, 0],
        5: ['GATEWAY_IP_2', GATEWAY_IP_2, 0, 0],
        6: ['WEBSITE', WEBSITE, 0, 0]}


def set_log(filename):
    logging.basicConfig(filename=filename,
                        filemode='a',
                        level=logging.INFO,
                        format='%(asctime)s: %(levelname)s -> %(name)s -> %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':

    pause_time = 1
    user = 'Albert'
    stop_hour = 3
    stop_min = 30

    tally = east_coast

    stamp = dt.now().strftime("%m%d%Y")
    log_file = fr'.\connectivity_test_{stamp}.log'
    set_log(log_file)
    msg = "Oren's test program has started ..."
    print(msg)
    print('DO NOT EXIT SCREEN')
    logging.info(msg)
    counter = 0
    while True:
        now = dt.now()
        if now.hour == stop_hour and now.minute >= stop_min:
            logging.info('Program exiting')
            send('bezoren@gmail.com', f'Connectivity Result {user}', f'counter={counter}', log_file)
            print("\n\nMr. Albert. Program has ended you may exit the screen")
            sys.exit()
        index = counter % len(tally)
        site = tally[index][1]
        cmd = f'powershell; "Test-Connection {site} -Count 1   >$null 2>$null"'
        response = os.system(cmd)
        if response == 0:
            tally[index][2] += 1
            result = 'PASS'
        else:
            result = 'FAIL'
        tally[index][3] += 1   # increment attempts
        counter += 1
        success_rate = round(100 * tally[index][2] / tally[index][3], 2)
        msg = f'Attempt:{tally[index][3]} - Connection to {tally[index][0]}={result}, success_rate={success_rate}%'
        logging.info(msg)
        if counter % 1000 == 0:
            send('bezoren@gmail.com', f'Connectivity Result {user}', f'counter={counter}', log_file)
        sleep(pause_time)
