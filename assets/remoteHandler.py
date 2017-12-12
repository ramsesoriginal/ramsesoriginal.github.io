from systemHandler import SystemHandler
import paramiko
import os


class RemoteComaJudgeHandler (SystemHandler):

    def __init__(self, username, passwordGetter, remoteFolder):
        SystemHandler.__init__(self)
        self.username = username
        self.remoteFolder = remoteFolder
        self.passwordGetter = passwordGetter
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.hostname = "pool.math.tu-berlin.de"
        self.port = 22

    def connect(self):
        self.client.connect(self.hostname,
                            port=self.port,
                            username=self.username,
                            password=self.passwordGetter())
        self.sftp = self.client.open_sftp()

    def closeConnection(self):
        self.client.close()

    def uname(self):
        return self.username

    def exec(self, command):
        #print("")
        #print("Executing: " + command)
        #print("")
        stdin, stdout, stderr = self.client.exec_command(command)
        text = stdout.read().decode('utf-8')
        #errorText = stderr.read().decode('utf-8')
        #if not not errorText:
        #    text = text + "\n\n" + errorText
        return text

    def pushFile(self, filePath):
        path, filename = os.path.split(filePath)
        remotePath = self.remoteFolder + "/" + filename
        #print("")
        #print("pushing: " + filePath + " to " + remotePath)
        #print("")
        self.sftp.put(filePath, remotePath)
        return remotePath

    def filenamesInDirectory(self, directoryPath):
        #print("")
        #print("getting filenames for: " + directoryPath )
        #print("")
        filelist = self.sftp.listdir(directoryPath)
        return filelist

    def getFileInfo(self, filePath):
        #print("")
        #print("getting info for: " + filePath )
        #print("")
        info = self.sftp.stat(filePath)
        return info
