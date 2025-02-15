import os
import requests
import sgd
from chemspipy import ChemSpider


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


class SGD:
    def __init__(self):
        """
        Define the init method: nothing for now
        """
        pass

    def look_up_locus(locus_id):
        """
        Look up a given locus id
        """
        _locus = sgd.locus(locus_id)
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
        

    def look_up_name(id):
        CHEMSPIDER_API_KEY = os.environ['CHEMSPIDER_API_KEY']
        cs = ChemSpider(CHEMSPIDER_API_KEY)
        comp = cs.get_compound(id)  # Specify compound by ChemSpider ID
        return comp.common_name
    