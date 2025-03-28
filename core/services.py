import json
import os

import chemspipy
import requests
import sgd
from chemspipy import ChemSpider


class Reactome:
    def __init__(self):
        """
        Define the init method: nothing for now
        """
        pass

    def stable_id(_db_id: str) -> str:
        """
        Retrieve the stable identifier of a given database identifier from
        the Reactome database.
        """
        _url = f"https://reactome.org/ContentService/data/query/{_db_id}/stId"
        res = requests.get(_url)
        stable_id = ""
        if res.status_code == 200:
            stable_id = res.text
        return stable_id


class SGD:
    def __init__(self):
        """
        Define the init method: nothing for now
        """
        pass

    def look_up_locus(_id: str) -> str:
        """
        Look up a given locus id
        """
        _locus = sgd.locus(_id)
        _json = _locus.details.json()
        return _json
    

"""
ChemSpider 
"""
class CHS:
    def __init__(self):
        """
        Define the init method: nothing for now
        """
        pass
        

    def look_up_name(_id: str) -> str:
        CHEMSPIDER_API_KEY = os.environ['CHEMSPIDER_API_KEY']
        cs = ChemSpider(CHEMSPIDER_API_KEY)

        try:
            comp = cs.get_compound(_id)  # Specify compound by ChemSpider ID
            try:
                return comp.common_name
            except Exception as e:
                print(e)
                return ""
        except Exception as e:
            print(e)
            return ""

class HGNC:
    # https://storage.googleapis.com / public - download - files / hgnc / json / json / hgnc_complete_set.json
    def __init__(self):

        pass

    @staticmethod
    def load_data():
        """
        Loads all data
        """
        with open("imported/hgnc_complete_set.json", "+r", encoding="utf-8") as _file:
            jdata = json.load(_file)
            jdata = jdata["response"]["docs"]
        ddict = {}
        for item in jdata:
            ddict[item["hgnc_id"]] = item["name"]
        return ddict

    def look_up(_id: str) -> str:
        ddict = HGNC.load_data()
        name = ddict[_id]
        return name
