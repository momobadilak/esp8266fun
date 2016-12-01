#!/usr/bin/python
#
# The MIT License (MIT)
#
# Copyright (c) 2016 Andy Idsinga (aka momobadilak)
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the 
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included 
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
# IN THE SOFTWARE.
#
# File: cheezecurl.py
#
# This is a dirty little hack to test TCP and SSL functions of the ESP firmware.
#

import array
import StringIO
import time
import sys
import os

# using pySerial library - : http://pythonhosted.org/pyserial/index.html
import serial

# was doing this on windows... but I suspect it will work on *nix without many issues
USING_PORT     = "COM6"

PORT_TIMEOUT_S = 1;

# want to cause stdout to flush immediatly
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

def main():
    # open the port
    with serial.Serial(USING_PORT, 115200, timeout=PORT_TIMEOUT_S) as thePort:
        print "success opening serial port:", thePort.name
        startupCheck(thePort)
        dumpVersionInfo(thePort)
        listAPs(thePort)
        httpGet(thePort,"data.sparkfun.com", "/streams/mKlp5AVQ6XhdLwNpRd2Y.json")
        #httpsGet(thePort,"www.google.com", "someplace/something")
        #httpsPost(thePort,"someplace/something", "this is test data")

    thePort.close()

    

def startupCheck(espPort):
    print "startup check: \'AT\' by itself; then check for OK"
    writeCmd(espPort,'AT')
    readUntilOk(espPort, maxLines=10, outputLines=False)


    
def dumpVersionInfo(espPort):
    print ""
    print "=== ESP VERSION INFO ==="
    writeCmd(espPort,'AT+GMR')
    readUntilOk(espPort);
    print ""

    

def listAPs(espPort):
    print ""
    print "=== Access Points visible to the ESP radio ==="
    writeCmd(espPort,'AT+CWLAP')
    readUntilOk(espPort, maxLines=50)
    print ""


    
def httpGet(espPort, host, path):

    # we build the http request in a buffer before we go messing with the wifi device
    respBuff = StringIO.StringIO()
    reqBuff = StringIO.StringIO()
    reqBuff.write('HEAD ' + path + ' HTTP/1.1' + "\r\n")
    reqBuff.write("\r\n")

    # this establishes a TCP connection.
    # Note that I've found that some web servers I've connected to close the socket in 5 seconds
    # if nothing is sent to them ...i.e. the request. So -- better not to wait around
    fullCmd = 'AT+CIPSTART="TCP","' + host + '",80'
    try:
        writeCmd(espPort, fullCmd)
        readUntilOk(espPort)

        startTransparentMode(espPort);
    
        # write the HTTP request
        writeBuffer(espPort, reqBuff)

        # read the response
        readBuffer(espPort, respBuff)
    
    finally:
        # terminate transparent mode
        endTransparentMode(espPort);

        # close the TCP connection
        writeCmd(espPort,'AT+CIPCLOSE');
        readUntilOk(espPort)

        # finally -- print the response
        print respBuff.getvalue()

        # cleanup
        reqBuff.close()
        respBuff.close()



def writeBuffer(espPort, wrBuff):
    """
    buffer is a StringIO object
    """
    print "+writeBuffer"
    espPort.write(wrBuff.getvalue())

    

def readBuffer(espPort, respBuff):
    """
    respBuff is a StringIO object that will be written to
    """
    print "+readBuffer"
    HTTP_RX_TIMEOUT_SECS = 10

    # this loop trys to read data while its available in the read buffer,
    # and starts a timer when no data is available ...no dater for longer than
    # HTTP_RX_TIMEOUT_SECS and we give up with and exception
    waitStart = 0
    while True:
        if espPort.in_waiting > 0 :

            waitStart = 0;
            # subject to serial port timeout config in PORT_TIMEOUT_S
            rdData = espPort.read(256)
            print "read # :", len(rdData)
            print "R:", rdData
            respBuff.write(rdData)

        else:

            if waitStart == 0:
                waitStart = time.time()
            else:
                if (time.time() - waitStart) >= HTTP_RX_TIMEOUT_SECS:
                    raise RuntimeError("timeout waiting for HTTP response data")



def startTransparentMode(espPort):
    print "+startTransparentMode",
    
    writeCmd(espPort,'AT+CIPMODE=1')
    readUntilOk(espPort)
    writeCmd(espPort,'AT+CIPSEND');
    readUntilOk(espPort)
    readUntilToken(espPort, successTok=">")

    

def endTransparentMode(espPort):
    espPort.write(array.array("B", '+++'))
    # we're supposed to wait 1 second before sending the next AT command after existing transparent mode with +++ token
    time.sleep(1)
    writeCmd(espPort,'AT+CIPMODE=0')
    readUntilOk(espPort)

    

def httpsGet(espPort, hostAndPath):
    print "TODO"


    
def httpsPost(espPort, hostAndPath, data):
    print "TODO"


    
def writeCmd(espPort,cmdTxt):
    espPort.write(array.array("B", cmdTxt+"\r\n"))

    

def readUntilOk(espPort, maxLines=15, outputLines=True):
    readUntilToken(espPort, maxLines, outputLines)


    
def readUntilToken(espPort, maxLines=15, outputLines=True, successTok="OK", errorTok="ERROR"):

    while maxLines > 0:
        
        # this readline() will be subject to PORT_TIMEOUT_S seconds
        espResp = espPort.readline();

        if espResp.find(successTok) == 0:
            return True;
        elif espResp.find(errorTok)== 0:
           raise RuntimeError("detected ERROR response from ESP")

        if outputLines:
            print espResp

        maxLines-=1

    raise RuntimeError("failed to OK or ERROR status after max search tries!")



main()
