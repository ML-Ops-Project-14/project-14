import neptune
import os

run = neptune.init_run(project="ML-Ops-project-14/Project-14", api_token=os.environ["NEPTUNE_API_TOKEN"])

params = {"learning_rate": 0.001, "optimizer": "Adam"}
run["parameters"] = params

for epoch in range(10):
    run["train/loss"].append(0.9 ** epoch)

run["eval/f1_score"] = 0.66

run.stop()
