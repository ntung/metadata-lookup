import requests


class Reactome:
    def __init__(self):
        """
        Define the init method: nothing for now
        """
        pass

    def stable_id(_dbid):
        """
        Retrieve the stable identifier of a given database identifier from
        the Reactome database.
        """
        _url = f"https://reactome.org/ContentService/data/query/{_dbid}/stId"
        res = requests.get(_url)
        stable_id = ""
        if res.status_code == 200:
            stable_id = res.text
        return stable_id