# DataScience-Portfolio Setup Summary

Summary of steps to set up GitHub, VS Code, and the Titanic Data Analysis project (July 7, 2025).

1. **GitHub Setup**:
   - Created public repository: `https://github.com/liquidbeach/DataScience-Portfolio`.
   - Used Python `.gitignore` and MIT License.
   - Set default branch to `main`.
   - Pinned repository, removed old repositories.
   - Installed Git for Windows with:
     - Git Credential Manager, MinTTY, PATH for 3rd-party software, fast-forward/merge, bundled OpenSSH, VS Code as editor.

2. **VS Code Setup**:
   - Installed VS Code and Jupyter extension.
   - Configured `portfolio` Conda environment as Python interpreter.

3. **Miniconda and Environment Setup**:
   - Installed Miniconda at `C:\Users\<yourusername>\miniconda3`.
   - Fixed “conda: command not found” with `~/miniconda3/Scripts/conda.exe init bash`.
   - Created `portfolio` environment with Python 3.11:
     ```bash
     conda create -n portfolio python=3.11
     conda activate portfolio
     ```
   - Installed dependencies:
     ```bash
     conda install jupyter pandas=2.0.3 seaborn=0.12.2 matplotlib=3.7.1 -c conda-forge
     ```

4. **Titanic Data Analysis (Project 1)**:
   - Created `project1-titanic-analysis` folder.
   - Added artifacts: `titanic_analysis.ipynb`, `requirements.txt`, `README.md`.
   - Fixed `.ipynb` downloading as `.txt` by renaming.
   - Tested in VS Code with `portfolio` interpreter, verified visualizations.
   - Committed and pushed:
     ```bash
     git add project1-titanic-analysis
     git commit -m "Add Titanic Data Analysis project"
     git push origin main
     ```