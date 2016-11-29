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

import serial

# was doing this on windows... but I suspect it will work on *nix without many issues
USING_PORT     = "COM6"

PORT_TIMEOUT_S = 2;

def main():
    # open the port
    with serial.Serial(USING_PORT, 115200, timeout=PORT_TIMEOUT_S) as thePort:
        print("opened port!,", thePort.name)
        startupCheck(thePort)
        dumpVersionInfo(thePort)
        listAPs(thePort)
        httpGet(thePort,"someplace/something")
        httpsGet(thePort,"someplace/something")
        httpsPost(thePort,"someplace/something", "this is test data")

    thePort.close()


def startupCheck(espPort):
    print "startup check: \'AT\' by itself; then check for OK"
    writeCmd(espPort,b'AT')
    readUntilOk(espPort, maxLines=10, outputLines=False)


def dumpVersionInfo(espPort):
    print ""
    print "=== ESP VERSION INFO ==="
    writeCmd(espPort,b'AT+GMR')
    readUntilOk(espPort);
    print ""


def listAPs(espPort):
    print ""
    print "=== Access Points visible to the ESP radio ==="
    writeCmd(espPort,b'AT+CWLAP')
    readUntilOk(espPort, maxLines=50)
    print ""
    

def httpGet(espPort, hostAndPath):
    print "TODO"

def httpsGet(espPort, hostAndPath):
    print "TODO"

def httpsPost(espPort, hostAndPath, data):
    print "TODO"
    
def writeCmd(espPort,cmdTxt):
    espPort.write(cmdTxt)
    espPort.write(b'\r\n')
    
def readUntilOk(espPort, maxLines=15, outputLines=True):

    while maxLines > 0:
        
        # this readline() will be subject to PORT_TIMEOUT_S seconds
        espResp = espPort.readline();

        if espResp.find("OK") == 0:
            return True;
        elif espResp.find("ERROR")== 0:
           raise RuntimeError("detected ERROR response from ESP")

        if outputLines:
            print espResp

        maxLines-=1

    raise RuntimeError("failed to OK or ERROR status after max search tries!")
        

main()
