'''
Script to collect data from MLFlow
<<<<<<< HEAD
=======

>>>>>>> 6b4a6db33d074e6fe6724cc08237f3e844b6425b
Author: Vivek Katial
'''

import mlflow
import yaml
import logging


# Initialise logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

# Read data from configuration file
with open('config/mlflow-tracking-server.yml') as file:
    mlflow_config = yaml.load(file, Loader=yaml.FullLoader)


# Connect to mlflow
logging.info('Connecting to MLFlow Tracking Server at URI: "%s" on Experiment:"%s"'% (
    mlflow_config['mlflow']['tracking_server_uri'],
    mlflow_config['mlflow']['experiment_name'])
             )
mlflow.set_tracking_uri(mlflow_config['mlflow']['tracking_server_uri'])

# Find experiments
experiment = mlflow.get_experiment_by_name(mlflow_config['mlflow']['experiment_name'])

logging.info('Downloading data from Experiment')
d_results = mlflow.search_runs(experiment_ids=experiment.experiment_id)
d_results.to_csv("data/d_runs.csv", index=False)
logging.info('Writing runs data to "data/d_runs.csv"')
'''
<<<<<<< HEAD
=======

>>>>>>> 6b4a6db33d074e6fe6724cc08237f3e844b6425b
'''
