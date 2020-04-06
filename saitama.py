from .config import Driver
from .pom import Page, Field
from selenium import webdriver
import time
import unittest


class Soldier:

    def __init__(self, browsername="Chrome", driverpath="default"):
        self.__browser = Driver.setter(browsername, driverpath)
        self.__pages = []

    def run(self, page = None, interval = 0):
        if not page:
            for p in self.__pages:
                self.run(p, interval)
                return
        self.driver.get(page.url)
        self.driver.maximize_window()
        print(f"\nTesting page {page.url}\n")
        for action in page.actions:
            if action[0] == "url":
                if action[1] == self.driver.current_url:
                    print(f"Current URL is {action[1]}")
                else:
                    print(f"Current URL isn't  {action[1]}")
                continue
            elif action[0] == "back":
                self.driver.back()
                continue
            field = action[0]
            if action[1] == "wait":
                print(self.wait_for(field, action[2]))
            elif action[1] == "check":
                print(self.wait_for(field))
            else:
                element = self.driver.find_element(field.method, field.selector)
                if action[1] == "click":
                    element.click()
                elif action[1] == "edit":
                    element.send_keys(action[2])
                elif "compare" in action[1]:
                    second = action[2]
                    if action[1] == "compare_fields":
                        element2 = self.driver.find_element(action[2].method, action[2].selector)
                        second = element2.text
                    if element.text == second:
                        print(f"Text of element with ` {field.selector} ` selector matches second text")
                    else:
                        print(f"Text of element with ` {field.selector} ` selector doesn't match second text")
                elif action[1] == "get_text":
                    print(element.text)
                elif action[1] == "check_property":
                    if element.get_property(action[2]) == action[3]:
                        print("Property matches")
                    else:
                        print("Property doesn't match")
                elif action[1] == "check_attr":
                    if element.get_attribute(action[2]) == action[3]:
                        print("Attribute matches")
                    else:
                        print("Attribute doesn't match")


            time.sleep(interval)

    def set_page(self, url) -> Page:
        self.__pages.append(Page(url))
        return self.__pages[-1]

    def wait_for(self, field : Field , interval = 3):
        start_time = time.time()
        while time.time() < start_time + interval:
            # print(self.driver.find_elements(Select.by_css,field.selector))
            if len(self.driver.find_elements(field.method,field.selector)) > 0:
                return f"Element with ` {field.selector} ` selector exists"
            else:
                time.sleep(0.1)
        return f"Element with ` {field.selector} ` selector doesn't exist"

    @property
    def driver(self) -> webdriver:
        return self.__browser

    def close(self):
        self.driver.close()
