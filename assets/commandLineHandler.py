import getpass
import datetime
import sys
import os
from comaJudgeHandler import ComaJudgeHandler


class CommandLineHandler:

    def __init__(self):
        print("\n   ~~ CoMaJudge Helper Tool ~~\n")
        nextIsPa = False
        nextIsUser = False
        nextIsFile = False
        for arg in sys.argv:
            if nextIsPa:
                self.pa = arg
                nextIsPa = False
            elif nextIsUser:
                self.username = arg
                nextIsUser = False
            elif nextIsFile:
                self.file = arg
                nextIsFile = False
            else:
                arg = arg.lower()
                if (arg.startswith("--aufgabe") or
                    arg.startswith("-a") or
                    arg.startswith("--programmieraufgabe") or
                    arg.startswith("-pa") or
                    arg.startswith("-p")):
                        nextIsPa = True
                if (arg.startswith("--username") or
                    arg.startswith("--user") or
                    arg.startswith("--uname") or 
                    arg.startswith("--nutzer") or
                    arg.startswith("-n") or
                    arg.startswith("-u")):
                        nextIsUser = True
                if (arg.startswith("--file") or
                    arg.startswith("-f") or
                    arg.startswith("--datei") or
                    arg.startswith("-d") or
                    arg.startswith("-t")):
                        nextIsFile = True
        if not hasattr(self, "username") or not self.username:
            self.username = input("Unixpool Username:")
        self.pwd_getter = lambda: getpass.getpass("Password:")
        if not hasattr(self, "pa") or not self.pa:
            self.pa = input("Programmieraufgabe:")
        if not hasattr(self, "file") or not self.file:
            self.file = input("Datei:")
        self.file = os.path.join(os.getcwd(), self.file)
        self.Options = [
            ["Check ComaJudge cooldown", lambda: self.printCooldown()],
            ["Check last submission's result", lambda: self.printLastResult()],
            ["Show submissions overview", lambda: self.printOverview()],
            ["Run Tests", lambda: self.executeTests()],
            ["Copy file to UnixPool", lambda: self.pushToServer()],
            ["Copy file to UnixPool and submit to CoMaJudge", lambda: self.submit()],
            ["Run Tests, if successful copy file to UnixPool and submit to CoMaJudge", lambda: self.runTestsAndSubmit()]
        ]

    def loop(self, systemHandler, testingHandler):
        self.systemHandler = systemHandler
        self.testingHandler = testingHandler
        self.comaJudge = ComaJudgeHandler(self.systemHandler, self.pa, self.file)
        while True:
            choice = self.getOption()
            if not self.processOption(choice):
                break

    def getOption(self):
        print("\nChoose an option:\n")
        for i in range(len(self.Options)):
            print("[" + str(i+1) + "] - " + self.Options[i][0])
        print("[0] - Exit\n")
        choice = input("Your Choice: ")
        print("")
        return choice

    def printCooldown(self):
        print("Last file version from: " + str(self.comaJudge.latestSubmissionTime()))
        lastSubmission = self.comaJudge.latestResultTime()
        print("Last submission: " + str(lastSubmission))
        print("Last status check: " + str(self.comaJudge.latestResultRetrivalTime()))
        toNextSubmission = (lastSubmission + datetime.timedelta(minutes=15)) - datetime.datetime.now()
        if toNextSubmission < datetime.timedelta(seconds=1):
            print("Available for submission again")
        else:
            print("\nTime to next submission: " + str(toNextSubmission) + "\n")

    def printLastResult(self):
        print(self.comaJudge.getResults())

    def printOverview(self):
        print(self.comaJudge.getOverview())

    def executeTests(self):
        self.testingHandler.processFile()
        self.testingHandler.executeTests()

    def pushToServer(self):
        print(self.comaJudge.copyFileToServer())

    def submit(self):
        print(self.comaJudge.submit())

    def runTestsAndSubmit(self):
        self.testingHandler.processFile()
        if self.testingHandler.executeTests():
            print(self.comaJudge.submit())

    def processOption(self, choice):
        try:
            if choice == "0":
                return False
            else:
                self.Options[int(choice) - 1][1]()
            return True
        except Exception:
            pass
