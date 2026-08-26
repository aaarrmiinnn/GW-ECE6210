# GWU ECE6210: Machine Intelligence

This repository contains the Fall 2026 course materials for ECE6210 at The George Washington University.

The course is offered online. The midterm and final examinations are held in person.

## Fall 2026 syllabus

- **Instructor:** Armin Mehrabian
- **Email:** armin@gwu.edu
- **Delivery:** Online lectures with in-person midterm and final examinations
- **Meeting time:** Wednesday, 9:30 a.m. to 11:30 a.m. Washington, DC time
- **Office hours:** Online by appointment

The Zoom link for the class can be found under Announcements on Blackboard.

A detailed version of the syllabus is available in [`docs/syllabus.md`](docs/syllabus.md).

### Time in Baku

- August 26 through October 28: 5:30 p.m. to 7:30 p.m.
- November 4 through December 2: 6:30 p.m. to 8:30 p.m.

Washington, DC ends daylight saving time on November 1, 2026. Baku does not change its clock.

### Assessment

| Assessment | Final grade |
|---|---:|
| In-person midterm examination | 40% |
| In-person final examination | 40% |
| Group project and final presentation, two students per group | 18% |
| Class participation | 2% |

### Course policies

#### Attendance

Students are required to attend every lecture. No more than three absences are permitted during the semester.

#### Use of AI tools

The use of AI tools is allowed. Any use of an AI tool for an assignment, report, presentation, code, or project must be disclosed in the submitted work. The disclosure must identify the tool and briefly explain how it was used. Students remain responsible for the accuracy of their work and must be able to explain what they submit.

### Course schedule

The syllabus and course schedule are subject to change. Any change will be announced on Blackboard.

| Date | Format | Topic |
|---|---|---|
| August 26 | Online | Lecture 1: Machine learning for electrical engineers |
| September 2 | Online | Lecture 2: Data, models, objectives, and optimization |
| September 9 | Online | Lecture 3: Linear regression and least squares |
| September 16 | Online | Lecture 4: Classification and logistic regression |
| September 23 | Online | Lecture 5: Generalization, regularization, and evaluation |
| September 30 | Online | Lecture 6: Probabilistic classification and uncertainty |
| October 7 | Online | Lecture 7: PCA and clustering |
| October 14 | Online | Midterm review and project proposal clinic |
| October 21 | In person | Midterm examination |
| October 28 | Online | Lecture 8: Neural networks and backpropagation |
| November 4 | Online | Lecture 9: Deep learning for one-dimensional signals |
| November 11 | Online | Lecture 10: Trees, ensembles, and model comparison |
| November 18 | Online | Engineering case study and hardware-aware inference |
| November 25 | No class | Thanksgiving Break |
| December 2 | Online | Project presentations and final review |
| December 11 to 17 | In person | Final examination period. Exact date to be assigned. |

The [GW academic calendar](https://www.gwu.edu/academic-calendar) lists Thanksgiving Break from November 23 through November 28. The last regular day of classes is December 8. December 9 follows a designated Monday schedule and does not include the regular Wednesday meeting.

## Course materials

The `slides/` directory contains interactive Jupyter notebooks. The notebooks use RISE for presentation.

Each notebook contains:

- Mathematical definitions and derivations
- Short Python demonstrations
- Engineering examples
- Review questions
- RISE slide metadata

The course is designed for MS Electrical Engineering students. It does not require prior machine learning study. Students should have basic knowledge of programming, linear algebra, probability, and signals.

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
