QUBO Formulation Exercise
=========================

[![Running Test in CI](https://github.com/FZJ-PGI-12/qubo_formulation_exercise/actions/workflows/python-package-conda.yml/badge.svg)](https://github.com/FZJ-PGI-12/qubo_formulation_exercise/actions/workflows/python-package-conda.yml)

Setup for Participants
----------------------

 - Install [miniforge](https://github.com/conda-forge/miniforge) to set up an environment for the Python installation. Alternative: Anaconda or Miniconda.
 - Create new conda environment
    
       conda create -n qubo_formulation_exercise python=3.10  

 - Activate the new environment

       conda activate qubo_formulation_exercise

 - Clone this repository and enter the directory

       git clone https://github.com/FZJ-PGI-12/qubo_formulation_exercise.git
       cd qubo_formulation_exercise

 - Install the dependencies

       pip install -r requirements.txt

 - Start the notebook

       jupyter notebook
 
 - **Test your setup** by running all cells. There should be no errors 

Tests
-----

Test your environment with

    pytest --nbval-lax *.ipynb

There should be no errors

