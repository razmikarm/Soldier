from selenium import webdriver
import sys, os


class Driver:
    """  This class was created to set driver functionality  """

    @classmethod
    def drivechecker(cls, browsername, driverpath):
        """ Checking validation of given parameters """

        driverpath = Driver.initer(browsername, driverpath)
        if not (browsername == "Chrome" or browsername == "Firefox"):
            raise Exception(browsername, "Soldier supports only Chrome and Firefox")
        if not os.path.exists(driverpath) or not os.path.isfile(driverpath):
            # if not os.access(driverpath, os.X_OK):
            raise Exception(driverpath, "File usage error! Check driver path and permission")

    @classmethod
    def initer(cls, browsername, driverpath):
        """ sets default drivers """

        if driverpath == "default":
            if sys.platform.startswith("linux"):
                if browsername == "Chrome":
                    return "Soldier/drivers/linux/chromedriver"
                elif browsername == "Firefox":
                    return "Soldier/drivers/linux/geckodriver"
            elif sys.platform.startswith("win32"):
                if browsername == "Chrome":
                    return "Soldier/drivers/windows/chromedriver.exe"
                elif browsername == "Firefox":
                    return "Soldier/drivers/windows/geckodriver.exe"
        else:
            return driverpath

    @classmethod
    def setter(cls, browsername, driverpath):
        """ Setting requested options for driver """

        driverpath = Driver.initer(browsername, driverpath)
        Driver.drivechecker(browsername, driverpath)
        if browsername == "Firefox":
            return webdriver.Firefox(executable_path=driverpath)
        elif browsername == "Chrome":
            return webdriver.Chrome(executable_path=driverpath)
