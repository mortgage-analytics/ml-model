# How to setup

We'll be using conda as a virtual env/package manager, because it's got a lot of data analysis packages.

[Install Miniconda](https://docs.anaconda.com/free/miniconda/)

Install Miniconda, as Anaconda has a lot of default packages that you don't need.

``` sh
# Create an environment called model from the environment file
conda env create -f environment.yml

# Once the model env is created, you can activate/deactivate the environment
conda activate model
conda deactivate

# Update env with packages from environment.yml
conda install --file environment.yml

# If you install a new package, update environment.yml, so that we all have the same packages.
conda install <package_name>
conda env export > environment.yml
```
