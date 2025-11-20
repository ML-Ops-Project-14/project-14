import neptune
import os
import pickle

run = neptune.init_run(project="ML-Ops-project-14/Project-14", api_token=os.environ["NEPTUNE_API_TOKEN"])

params = {"learning_rate": 0.001, "optimizer": "Adam"}
run["parameters"] = params

for epoch in range(10):
    run["train/loss"].append(0.9 ** epoch)

run["eval/f1_score"] = 0.66


filename = "test_mm.pkl"

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
models_dir = os.path.join(parent_dir, 'models')
model_filename = os.path.join(models_dir, filename)

my_model = pickle.load(open(model_filename, "rb"))

with open(model_filename, 'wb') as file:
    pickle.dump(my_model, file)

run["artifacts/model_pkl"].upload(filename)

run.stop()
