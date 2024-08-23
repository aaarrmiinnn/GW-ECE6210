# GWU ECE6210

This repo contains executable slides for the ECE Machine Intelligence course at The George Washington University (Fall 2024 edition).

## Contents

This repo is organized as follows.

```
.
├── README.md
├── slides.               # Course slides 
└── requirements.txt      # Packages needed for your virtualenv
```

## Setup

### Requirements

You should be able to run all the contents of this repo using the packages provided in `requirements.yml` using Anaconda or `requirements.txt` using virtualenv.

For `Anaconda` run this:
```
conda create --name gw-ece6210 --file requirements.yml
conda activate gw-ece6210
python -m ipykernel install --user --name=gw-ece6210
```

In a new `virtualenv`, run this:
```
pip install -r requirements.txt
```

Credits: The slides and course materials are forks of Cornell CS5785 (https://github.com/kuleshov/cornell-cs5785-2023-applied-ml), courtesy of Volodymyr Kuleshov.
