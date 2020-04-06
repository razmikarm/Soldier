from selenium.webdriver.common.by import By


class Field:

    def __init__(self, selector, method = "css"):
        methods = {
            "id": By.ID,
            "css": By.CSS_SELECTOR,
            "xpath": By.XPATH,
            "class": By.CLASS_NAME,
            "name": By.TAG_NAME,
            "link": By.LINK_TEXT,
            "tag": By.TAG_NAME,
            "partial_link": By.PARTIAL_LINK_TEXT
        }
        if method not in methods.keys():
            raise Exception("Method Error. Use these keywords to set selection method: \n", methods.keys())
        self.method = methods[method]
        self.selector = selector
        # self.property = {}
        # self.attr = {}


class Page:

    def __init__(self, url):
        self.url = url
        self.__fields = []
        self.__actions = []

    def set_field(self, selector, method="css") -> Field:
        self.__fields.append(Field(selector, method))
        return self.__fields[-1]

    @property
    def fields(self):
        return self.__fields

    @property
    def actions(self):
        return self.__actions

    def edit(self, field : Field,  value):
        if field not in self.fields:
            raise Exception('There is no such field')
        self.__actions.append([field, "edit", value])

    def click(self, field : Field):
        if field not in self.fields:
            raise Exception('There is no such field')
        self.__actions.append([field, "click"])

    def check_field(self, field : Field):
        if field not in self.fields:
            raise Exception('There is no such field')
        self.__actions.append([field, "check"])

    def check_url(self, url):
        self.__actions.append(["url", url])

    def wait_for(self, field : Field, sec = 3):
        if field not in self.fields:
            raise Exception('There is no such field')
        self.__actions.append([field, "wait", sec])

    def compare(self, field1 : Field, field2 ):
        compare = "compare"
        if field1 not in self.fields:
            raise Exception('There is no such field')
        if type(field2) is Field:
            if field2 not in self.fields:
                raise Exception('There is no such field')
            compare = "compare_fields"
        self.__actions.append([field1, compare, field2])

    def get_text(self, field : Field):
        if field not in self.fields:
            raise Exception('There is no such field')
        self.__actions.append([field, "get_text"])

    def back(self):
        self.__actions.append(["back"])

    def check_prop(self, field : Field, prop, value):
        if field not in self.fields:
            raise Exception('There is no such field')
        self.__actions.append([field, "check_property", prop, value])

    def check_attr(self, field : Field, attr, value):
        if field not in self.fields:
            raise Exception('There is no such field')
        self.__actions.append([field, "check_attr", attr, value])

    def wait_attr(self, field : Field, attr, value, interval = 3):
        if field not in self.fields:
            raise Exception('There is no such field')
        self.__actions.append([field, "wait_attr", attr, value, interval])

    def wait_prop(self, field : Field, prop, value, interval = 3):
        if field not in self.fields:
            raise Exception('There is no such field')
        self.__actions.append([field, "wait_prop", prop, value, interval])
