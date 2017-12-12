import timeit
import sys, os
import importlib
import shutil

class TestHandler:

    def __init__(self, filename):
        self.originalFilname = filename
        if "/" in filename or "\\" in filename:
            shutil.copy(filename, os.path.join(os.path.dirname(__file__), "testFile.py"))
            filename = os.path.join(os.path.dirname(__file__), "testFile.py")
        self.filename = filename
        self.fileHandler = open(filename, "r")
        self.executable = importlib.import_module(filename.split("/")[-1].split("\\")[-1][:-3])

    def processFile(self):
        if self.originalFilname != self.filename:
            try:
                shutil.copy(self.originalFilname, "testFile.py")
            except shutil.SameFileError:
                pass
        importlib.reload(self.executable)
        self.fileHandler = open(self.filename, "r")
        #__import__(self.filename)
        self.testCases = {}
        inTest = False
        currentTestCategory = ""
        currentTestName = ""
        for line in self.fileHandler:
            line = line.rstrip()
            if line.startswith("endTest'''"):
                inTest = False
            if inTest:
                if line.startswith("testCategory"):
                    currentTestCategory = line.split("testCategory ")[1]
                    if currentTestCategory not in self.testCases:
                        self.testCases[currentTestCategory] = {}

                if line.startswith("testName"):
                    currentTestName = line.split("testName ")[1]
                    if currentTestName not in self.testCases[currentTestCategory]:
                        self.testCases[currentTestCategory][currentTestName] = {}

                if line.startswith("maxtime"):
                    maxtime = int(line.split("maxtime ")[1])
                    self.testCases[currentTestCategory][currentTestName]["maxtime"] = maxtime

                if line.startswith("expectedResult"):
                    expectedResult = eval(line.split("expectedResult ")[1])
                    self.testCases[currentTestCategory][currentTestName]["expectedResult"] = expectedResult

                if line.startswith("call"):
                    call = line.split("call ")[1]
                    self.testCases[currentTestCategory][currentTestName]["call"] = "self.executable." + call


            if line.startswith("'''testStart"):
                inTest = True

    def executeTests(self):
        allok = True
        for category in self.testCases:
            catok = True
            for test in self.testCases[category]:
                try:
                    expected = self.testCases[category][test]["expectedResult"]
                    start_time = timeit.default_timer()
                    result = eval(self.testCases[category][test]["call"])
                    elapsed = timeit.default_timer() - start_time
                    if result != expected or elapsed > self.testCases[category][test]["maxtime"]:
                        allok = False
                        catok = False
                        self.testCases[category][test]["testOK"] = False
                        errorstring = "   " + " ERROR " + test
                        rstring = self.testCases[category][test]["call"].split("self.executable.")[1]
                        if len(rstring) > 70:
                            rstring = rstring[:70] + "..."
                        if (result != expected):
                            errorstring = errorstring + "\n      " + "Falsches Ergebnis"
                        else:
                            errorstring = errorstring + "\n      " + "Zu langsam"
                        errorstring = errorstring + "\n      " + rstring
                        errorstring = errorstring + "\n      " + "expected: " + str(expected) + ", got: " + str(result)
                        errorstring = errorstring + "\n      " + "runtime: " + str(elapsed) + " seconds "
                        errorstring = errorstring + "\n"
                        self.testCases[category][test]["resultOutput"] = errorstring
                    else:
                        self.testCases[category][test]["testOK"] = True
                        self.testCases[category][test]["resultOutput"] = "   " + test + " OK"
                except Exception as inst:
                    allok = False
                    catok = False
                    self.testCases[category][test]["testOK"] = False
                    errorstring = "   " + " ERROR " + test
                    errorstring = errorstring + "\n      " + "Programmierfehler"
                    rstring = self.testCases[category][test]["call"].split("self.executable.")[1]
                    if len(rstring) > 70:
                        rstring = rstring[:70] + "..."
                    errorstring = errorstring + "\n      " + rstring
                    errorstring = errorstring + "\n      " + inst
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    errorstring = errorstring + "\n      " + str(exc_type) + " " + str(fname) + " " + str(exc_tb.tb_lineno)
                    errorstring = errorstring + "\n"
                    self.testCases[category][test]["resultOutput"] = errorstring
            if catok:
                print("OK " + category)
            else:
                print("ERROR " + category)
            for test in self.testCases[category]:
                print(self.testCases[category][test]["resultOutput"])
        return allok
