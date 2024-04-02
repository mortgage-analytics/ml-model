# How to setup

We'll be using conda as a virtual env/package manager, because it's got a lot of data analysis packages.

[Install Miniconda](https://docs.anaconda.com/free/miniconda/)

Install Miniconda, as Anaconda has a lot of default packages that you don't need.

``` sh
# Create an environment called model with all the correct packages from environment.yaml
conda env create --file environment.yaml

# Once the model env is created, you can activate/deactivate the environment
conda activate model
conda deactivate

# Update env with packages from environment.yaml
conda env update --file environment.yaml --prune

# If you install a new package, update environment.yaml, so that we all have the same packages.
conda install <package_name>
conda env export --from-history > environment.yaml
```

We'll be using FastAPI to host our model. You can send HTTP requests to it.

In order to start up, run:

``` sh
cd models
uvicorn main:app --reload
```

**Note**: make sure you have setup conda by install the packages from environment.yaml.

We'll also be using mypy for type checking. This isn't strictly necessary, but I thought I would add it since weird errors can occur without type checking. We can get rid of this at any point in time, and CPython will still run our code even if mypy finds type errors.

If you want to set this up, call:

``` sh
pre-commit install
```

# Usage

In order to save a model, use

``` sh
cd models
EXPORT=1 python model.py
```

If the env var EXPORT is anything else it will just train a model, and print an accuracy. This will save a model into a text file, which can then be loaded whenever you want.
