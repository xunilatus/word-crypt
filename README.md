#PYTHON LIBRARIES AND PROGRAMS TO INSTALL WITH PIP
"List of commonly installed python libraries and useful programs"
"Some methods and usages described"
"Mostly windows and linux"

#Window
python.exe -m pip install --upgrade

#Linux
pip install --upgrade pip
sudo pacman -S python-pip 

#Packages
pyinstaller
cx_freeze
py2exe
scapy
pandas
pyqt5-tools
pyqt5
pyqt5designer
pandas
requests
beautifulsoup4
Flask-SQLAlchemy
numpy
pynput
sip
setuptools
wheel
virtualenv
smtplib
pywin32
dpkt

pip install pyinstaller

pyinstaller --onefile myscript.py        ***************************************************your looking for this


#Windows Powershell Authorization to activate virtural environment 'venv'
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#MAKE PERMINANT OPEN SHELL AS ADMIN      *****************************************************your also looking for this
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope LocalMachine



#Set up and activate a virtual environment
python -m venv myenv
.\venv\Scripts\activate

#PyQt5designer location            **********************************************************************maybe this
C:\Users\xunilatus\AppData\Local\Programs\Python\Python312\Lib\site-packages\QtDesigner\designer.exe




#Using pywin32 to run scripts as services in windows
"you can also go into 'services.msc' and adjust to 'Automatic' in properties"
python ImageDownloadService.py install
sc config ImageDownloadService start= auto
python ImageDownloadService.py start
python ImageDownloadService.py stop
python ImageDownloadService.py remove

# EXAMPLE FILE SAVE AS "ImageDownloadService.py" ************************************python script as a win32 background process
import os
import sys
import time
from datetime import datetime
import requests
import servicemanager
import win32serviceutil
import win32service
import win32event

class DownloadService(win32serviceutil.ServiceFramework):
    _svc_name_ = "ImageDownloadService"
    _svc_display_name_ = "Image Download Service"
    _svc_description_ = "downloads an imageintervals."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.running = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.running = False
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, '')
        )
        self.main()

    def main(self):
        "YOUR CODE GOES HERE"

            time.sleep(1800)  # Sleep for 30 minutes

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(DownloadService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(DownloadService)
