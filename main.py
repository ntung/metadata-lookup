from fastapi import FastAPI
import uvicorn

from core.services import Reactome, SGD, CHS

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/reactome-stable-id/{db_id}", tags=["Reactome"])
def reactome_stable_id(db_id: str):
    """
    Look up and return the stable id of a given database id in the Reactome database
    """
    return Reactome.stable_id(db_id)

@app.get("/sgd-locus-id/{locus_id}", tags=["SGD"])
def sgd_locus_id(locus_id: str):
    """
    Look up and return the stable id of a given database id in SGD
    """
    return SGD.look_up_locus(locus_id)


@app.get("/chemspider/{id}", tags=["ChemSpider"])
def chemspider_look_up_name(id):
    """
    Look up the name of a given id
    """
    return CHS.look_up_name(id)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8040, reload=True)