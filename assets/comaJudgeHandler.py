import datetime
import time


class ComaJudgeHandler:

    def __init__(self, systemHandler, currentPA, currentFile):
        self.sH = systemHandler
        self.uname = systemHandler.uname()
        self.currentPA = currentPA
        self.currentFile = currentFile
        self.temp = ".comajudge.tmp/" + self.uname + "-repo/"
        self.report = self.temp + "report/"
        self.overview = "comajudge overview"
        self.result = lambda pa: "comajudge result -p " + pa
        self.submitpath = lambda pa, filepath: ("comajudge submit" +
                                            " -t " + filepath +
                                            " -p " + pa)
        self.currentSolution = self.temp + self.currentPA + "solution.py"
        self.currentResult = self.result(self.currentPA)
        self.currentSubmit = lambda file: self.submitpath(self.currentPA, file)

    def copyFileToServer(self):
        pushedFilePath = self.sH.pushFile(self.currentFile)
        return pushedFilePath

    def submit(self):
        pushedFilePath = self.sH.pushFile(self.currentFile)
        result = self.sH.exec(self.currentSubmit(pushedFilePath))
        return result

    def latestSubmissionTime(self):
        info = self.sH.getFileInfo(self.currentSolution)
        resultTime = datetime.datetime.fromtimestamp(info.st_mtime)
        return resultTime

    def latestResultTime(self):
        filenames = self.sH.filenamesInDirectory(self.report)
        resultTime = datetime.datetime.now() - datetime.timedelta(minutes=15)
        for file in filenames:
            if file != "successful_solution.py":
                timestamp = file[:-5]
                resultTime = datetime.datetime.strptime(timestamp, "%d_%m_%Y-%H_%M")
                break
                #info = self.sH.getFileInfo(self.report + "/" + file)
        #resultTime = datetime.datetime.fromtimestamp(info.st_mtime)
        return resultTime

    def latestResultRetrivalTime(self):
        filenames = self.sH.filenamesInDirectory(self.report)
        resultTime = datetime.datetime.now() - datetime.timedelta(minutes=15)
        for file in filenames:
            if file != "successful_solution.py":
                info = self.sH.getFileInfo(self.report + "/" + file)
        resultTime = datetime.datetime.fromtimestamp(info.st_mtime)
        return resultTime

    def getResults(self):
        result = self.sH.exec(self.currentResult)
        return result

    def getOverview(self):
        result = self.sH.exec(self.overview)
        return result
