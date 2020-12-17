__author__ = "Janik Klauenberg"
__copyright__ = "Janik Klauenberg"
__credits__ = "Idea and main information from https://github.com/sn0wmanmj/pydsb"

__license__ = "MIT License"
__version__ = "0.9"
__maintainer__ = "Janik Klauenberg"
__email__ = "support@klauenberg.eu"
__status__ = "In Developement"
import requests
import json


class Wrapper():
    def __init__(self, username, password):
        self.user = username
        self.passw = password
        self.base = "https://mobileapi.dsbcontrol.de/"
        self.token = self.get_token(self.user, self.passw)
        self.params = {
                        "authid": self.token
                      }

    def get_token(self, username, password):
        """
        Comment: gets a token for the client
        Input: Username and password
        Output: Token as json object
        Special: Nothing special
        """
        url = self.base + "authid?pushid"
        params = {
                  "user": username,
                  "password": password,
                  "bundleid": "de.heinekingmedie.dsbmobile",
                  "appversion": 35,
                  "osversion": 22,
                  }
        r = requests.get(url, params=params)
        return json.loads(r.content)

    def get_plan_urls(self):
        """
        Comment: gets plans
        Input: Name of Instance
        Output: plans urls as Json list
        Special: Nothing special
        """
        url = self.base + "dsbtimetables"
        r = requests.get(url, params=self.params)
        res = [i["Detail"] for i in json.loads(r.content)[0]["Childs"]]
        return res


def main():
    creds = json.load(open("creds.json", mode="r"))
    test = Wrapper(creds["user"], creds["pass"])
    x = test.get_plans()
    print x

if __name__ == '__main__':
    main()
