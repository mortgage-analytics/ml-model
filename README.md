# Usage

In order to setup the environment, download conda and run:

``` sh
cd models
conda env create --file environment.yaml
conda activate model
```

In order to train a model, run:

```sh
cd models/
python xgboost_model.py
```

**NOTE**: make sure you have the training_data.csv file in the models directory.

In order to save or load a model set the SAVE and LOAD environment variable respectively to 1. All other values will make these environment variables ignored.

```sh
SAVE=1 python xgboost_model.py
LOAD=1 python xgboost_model.py
```

In order to start the api, run

```sh
cd models/
uvicorn main:app --reload
```
