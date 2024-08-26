from fastapi import FastAPI
from main import AgileProjectManagerModel

app = FastAPI()
model = AgileProjectManagerModel(config="model_config.yaml")

@app.post("/process_project/")
def process_project(project_description: str):
    result = model.run(project_description)
    return result
