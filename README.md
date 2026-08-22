# GWU ECE6210: Machine Intelligence

This repository contains the Fall 2026 course materials for ECE6210 at The George Washington University.

The course is offered online. The midterm and final examinations are held in person.

## Course materials

The `slides/` directory contains interactive Jupyter notebooks. The notebooks use RISE for presentation.

Each notebook contains:

- Mathematical definitions and derivations
- Short Python demonstrations
- Engineering examples
- Review questions
- RISE slide metadata

The course is designed for MS Electrical Engineering students. It does not require prior machine learning study. Students should have basic knowledge of programming, linear algebra, probability, and signals.

## Fall 2026 meeting time

The online class meets on Wednesday from 9:30 a.m. to 11:30 a.m. Washington, DC time.

- August 26 through October 28: 5:30 p.m. to 7:30 p.m. in Baku
- November 4 through December 2: 6:30 p.m. to 8:30 p.m. in Baku

There is no class on November 25. The last regular Wednesday meeting is December 2.

## Environment setup

Python 3.10 or 3.11 is recommended.

### Conda

```bash
conda env create -f requirements.yml
conda activate gw-ece6210
jupyter notebook
```

### Python virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter notebook
```

On Windows, activate the environment with:

```powershell
.venv\Scripts\activate
```

## Presenting with RISE

Start the classic Jupyter Notebook interface:

```bash
jupyter notebook
```

Open a notebook in `slides/`. Select the RISE presentation button. The slide structure is stored in each cell under `metadata.slideshow.slide_type`.

Run the notebook before presenting. Confirm that all figures appear and that no code cell reports an error.

## Deck validation

Run the local validator before presenting a deck:

```bash
python scripts/validate_deck.py slides/lecture1-introduction.ipynb
```

The validator checks notebook structure, RISE metadata, Python syntax, local image references, stored execution errors, and course writing rules.

## Student guidance

- Run notebook cells in order.
- Focus on the engineering meaning of each result.
- Ask for help when an environment or programming issue blocks the analysis.

## Credits

The original course materials were based on Cornell CS5785 Applied Machine Learning. The Fall 2026 edition is adapted for ECE6210 and for MS Electrical Engineering students.
