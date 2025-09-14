# Neural_Networks_and_PyTorch
Introduction to Neural Networks and PyTorch


# Python Virtual Environment Setup Guide

This guide provides comprehensive steps for installing and setting up Python virtual environments (venv) on Linux systems.

## Prerequisites

- Linux system (Ubuntu/Debian recommended)
- Python 3.6 or higher
- pip (Python package installer)

## Step 1: Check Python Installation

First, verify that Python 3 is installed on your system:

```bash
python3 --version
```

If Python 3 is not installed, install it:

### Ubuntu/Debian:
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### CentOS/RHEL/Fedora:
```bash
# For CentOS/RHEL
sudo yum install python3 python3-pip

# For Fedora
sudo dnf install python3 python3-pip
```

## Step 2: Create a Virtual Environment

Navigate to your project directory:
```bash
cd /path/to/your/project
```

Create a virtual environment:
```bash
python3 -m venv .env
```

Replace `myenv` with your desired virtual environment name.

## Step 3: Activate the Virtual Environment

### On Linux/macOS:
```bash
source myenv/bin/activate
```

### On Windows:
```bash
myenv\Scripts\activate
```

When activated, you'll see `(myenv)` at the beginning of your command prompt.

## Step 4: Verify Virtual Environment

Check that you're using the virtual environment's Python:
```bash
which python
python --version
which pip
```

## Step 5: Install Packages

Install packages using pip (they will be isolated to this virtual environment):
```bash
pip install package_name
```

For example:
```bash
pip install numpy pandas matplotlib
```

## Step 6: Create requirements.txt

Generate a requirements file for easy dependency management:
```bash
pip freeze > requirements.txt
```

## Step 7: Deactivate Virtual Environment

When you're done working:
```bash
deactivate
```

## Step 8: Recreate Environment from requirements.txt

To recreate the environment on another machine or after deletion:
```bash
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

## Best Practices

### 1. Always Use Virtual Environments
Never install packages globally. Always create a virtual environment for each project.

### 2. Name Your Environment Clearly
Use descriptive names like `project-name-env` or `data-analysis-env`.

### 3. Keep requirements.txt Updated
Always update your requirements.txt file when installing new packages:
```bash
pip freeze > requirements.txt
```

### 4. Use .gitignore
Add your virtual environment folder to `.gitignore`:
```
myenv/
venv/
env/
.env
```

### 5. Virtual Environment Location
Consider placing virtual environments in a dedicated folder:
```bash
mkdir ~/venvs
python3 -m venv ~/venvs/myproject
source ~/venvs/myproject/bin/activate
```

## Troubleshooting

### Common Issues:

1. **"python3: command not found"**
   - Install Python 3 using your system's package manager

2. **"pip: command not found"**
   - Install pip: `sudo apt install python3-pip` (Ubuntu/Debian)

3. **Permission denied errors**
   - Don't use `sudo` with pip in virtual environments
   - Ensure you're in the correct directory

4. **Virtual environment not activating**
   - Check the path to the activation script
   - Ensure you're using the correct activation command for your OS

### Useful Commands:

```bash
# List installed packages
pip list

# Show package information
pip show package_name

# Upgrade a package
pip install --upgrade package_name

# Uninstall a package
pip uninstall package_name

# Check for outdated packages
pip list --outdated

# Install from requirements.txt
pip install -r requirements.txt
```

## Advanced Usage

### Create Virtual Environment with Specific Python Version:
```bash
python3.9 -m venv myenv
```

### Create Virtual Environment with System Site Packages:
```bash
python3 -m venv --system-site-packages myenv
```

### Create Virtual Environment with Upgrade:
```bash
python3 -m venv --upgrade myenv
```

## Integration with IDEs

### VS Code:
1. Open Command Palette (`Ctrl+Shift+P`)
2. Type "Python: Select Interpreter"
3. Choose your virtual environment's Python interpreter

### PyCharm:
1. Go to File → Settings → Project → Python Interpreter
2. Click the gear icon → Add
3. Select "Existing Environment" and browse to your venv

### Jupyter Notebook:
```bash
# Install Jupyter in your virtual environment
pip install jupyter

# Install kernel for the virtual environment
python -m ipykernel install --user --name=myenv --display-name="Python (myenv)"

# Start Jupyter
jupyter notebook
```

## Project Structure Example

```
my-project/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   └── main.py
├── tests/
│   └── test_main.py
└── venv/  # (not tracked in git)
    ├── bin/
    ├── lib/
    └── pyvenv.cfg
```

This setup ensures a clean, isolated Python development environment for your project.
