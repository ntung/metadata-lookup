from fastapi import FastAPI
import uvicorn

from core.services import Reactome, SGD, CHS, HGNC

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/reactome-stable-id/{db_id}", tags=["Reactome"])
def lookup_reactome_stable_id_via_db_id(db_id: str):
    """
    Look up and return the stable id of a given database id in the Reactome database
    """
    return Reactome.stable_id(db_id)

@app.get("/sgd-locus-id/{locus_id}", tags=["SGD"])
def lookup_sgd_via_locus_id(locus_id: str):
    """
    Look up and return the stable id of a given database id in SGD
    """
    return SGD.look_up_locus(locus_id)


@app.get("/chemspider/{_id}", tags=["ChemSpider"])
def lookup_chemspider_name_via_id(_id: str):
    """
    Look up the name of a given id
    """
    return CHS.look_up_name(_id)


@app.get("/hgnc/{_id}", tags=["HGNC"])
def lookup_hgnc(_id: str):
    """
    Look up the name of a given id
    """
    return HGNC.look_up(_id)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8040, reload=True)