*****************************
ABR Keyword Spotting Tutorial
*****************************

**Installation**
~~~~~~~~~~~~~~~~

To start, you can make an Anaconda environment (or a virtualenv along the same lines), activate it, and follow the instructions below. You can skip the step of making an environment if you want to use a system-wide installation. `Anaconda <https://www.anaconda.com/download/>`_, however, is a good choice if you are new to python and want to get up and running quickly.

.. code:: shell

    # create and activate a new python environment 
    conda create -n abr-tutorial python=3.6
    source activate abr-tutorial

    # install Nengo and Nengo GUI
    pip install nengo
    pip install nengo-gui

    # install Nengo DL
    pip install nengo-dl

    # install Nengo Loihi
    git clone https://github.com/nengo/nengo-loihi.git
    pip install -e nengo-loihi

    # install Jupyter Notebook
    pip install jupyter notebook

    # open a notebook for the tutorial
    git clone https://github.com/pblouw/inrc-2018
    cd inrc-2018
    jupyter notebook


Now you should be all set to follow along!
