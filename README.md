# GWU ECE6210 - Machine Intelligence

This repository contains interactive Jupyter notebook slides for the ECE Machine Intelligence course at The George Washington University (Fall 2025 edition).

## 📁 Repository Structure

```
GW-ECE6210/
├── README.md                           # This file
├── docs/
│   └── syllabus.md                    # Course syllabus
├── slides/
│   ├── lecture1-introduction.ipynb    # Lecture 1: Intro to ML
│   ├── lecture2-machine-learning-setup.ipynb  # Lecture 2: ML Setup
│   └── img/                           # Images used in lectures
├── requirements.txt                    # Python packages (pip)
└── requirements.yml                    # Python packages (conda)
```

## 🎯 How to Use These Slides

The course slides are **interactive Jupyter notebooks** that contain:
- Lecture content with explanations
- Runnable Python code examples
- Visualizations and plots
- Exercises and demonstrations

### Prerequisites
- Basic comfort with computers and file management
- No prior programming experience required!

## 🚀 Getting Started

You have **two options** to run these slides:

### Option 1: Anaconda (Recommended for Beginners)

**Anaconda** is a Python distribution that includes everything you need in one package.

#### Step 1: Install Anaconda
1. Go to [anaconda.com/download](https://www.anaconda.com/download)
2. Download the installer for your operating system
3. Run the installer and follow the prompts
4. Choose "Just Me" installation (recommended)

#### Step 2: Download Course Materials
1. Click the green "Code" button at the top of this page
2. Select "Download ZIP"
3. Extract the ZIP file to your desired location (e.g., Desktop or Documents)

#### Step 3: Set Up the Environment
1. Open **Anaconda Prompt** (Windows) or **Terminal** (Mac/Linux)
2. Navigate to the course folder:
   ```bash
   cd path/to/GW-ECE6210
   ```
3. Create the course environment:
   ```bash
   conda create --name gw-ece6210 --file requirements.yml
   ```
4. Activate the environment:
   ```bash
   conda activate gw-ece6210
   ```
5. Install Jupyter kernel:
   ```bash
   python -m ipykernel install --user --name=gw-ece6210
   ```

#### Step 4: Launch Jupyter
```bash
jupyter lab
```
Your web browser will open with JupyterLab. Navigate to the `slides/` folder and open any `.ipynb` file!

### Option 2: Python + pip (For Users with Python Experience)

If you already have Python installed:

#### Step 1: Install Python
- Download from [python.org/downloads](https://www.python.org/downloads/)
- Install Python 3.8 or newer

#### Step 2: Create Virtual Environment
```bash
# Navigate to course folder
cd path/to/GW-ECE6210

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate
```

#### Step 3: Install Required Packages
```bash
pip install -r requirements.txt
```

#### Step 4: Launch Jupyter
```bash
jupyter lab
```

## 📚 Running the Slides

1. **Open JupyterLab** in your browser (should open automatically)
2. **Navigate** to the `slides/` folder
3. **Click** on any `.ipynb` file to open it
4. **Run cells** by clicking the ▶️ button or pressing `Shift + Enter`

### Tips for Non-CS Students:
- 🔹 **Don't worry about understanding every line of code** - focus on the concepts!
- 🔹 **Run cells in order** from top to bottom
- 🔹 **Experiment!** Try changing numbers in the code to see what happens
- 🔹 **Ask for help** if you get stuck - that's what office hours are for!

## 🛠️ Troubleshooting

### Common Issues:

**"Command not found" or "conda not recognized"**
- Restart your terminal/command prompt after installing Anaconda
- On Windows, make sure you're using "Anaconda Prompt"

**"ModuleNotFoundError"**
- Make sure you activated your environment: `conda activate gw-ece6210`
- Try reinstalling packages: `pip install -r requirements.txt`

**Jupyter won't start**
- Check that Jupyter is installed: `jupyter --version`
- Try `jupyter notebook` instead of `jupyter lab`

**Still having issues?**
- Check the [Jupyter documentation](https://jupyter.org/install)
- Visit office hours or ask on the course forum
- Email the instructor: armin@gwu.edu

## 🔗 Helpful Resources

- **Python for Beginners**: [wiki.python.org/moin/BeginnersGuide](https://wiki.python.org/moin/BeginnersGuide)
- **Try Jupyter Online**: [jupyter.org/try](https://jupyter.org/try)
- **Virtual Environments**: [docs.python.org/3/tutorial/venv.html](https://docs.python.org/3/tutorial/venv.html)
- **Anaconda Documentation**: [anaconda.com/docs](https://www.anaconda.com/docs/main)

## 📝 Credits

The slides and course materials are based on Cornell CS5785 (https://github.com/kuleshov/cornell-cs5785-2023-applied-ml), courtesy of Volodymyr Kuleshov, and adapted for GWU ECE6210.
