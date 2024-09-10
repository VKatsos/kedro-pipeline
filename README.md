# spaceflights

## Overview

This is your new Kedro project with Kedro-Viz setup, which was generated using `kedro 0.19.6`.

Take a look at the [Kedro documentation](https://docs.kedro.org) to get started.

## Rules and guidelines

In order to get the best out of the template:

* Don't remove any lines from the `.gitignore` file we provide
* Make sure your results can be reproduced by following a [data engineering convention](https://docs.kedro.org/en/stable/faq/faq.html#what-is-data-engineering-convention)
* Don't commit data to your repository
* Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/`

## How to install dependencies

Declare any dependencies in `requirements.txt` for `pip` installation.

To install them, run:

```
pip install -r requirements.txt
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

## How to test your Kedro project

Have a look at the files `src/tests/test_run.py` and `src/tests/pipelines/data_science/test_pipeline.py` for instructions on how to write your tests. Run the tests as follows:

```
pytest
```

To configure the coverage threshold, look at the `.coveragerc` file.

## Project dependencies

To see and update the dependency requirements for your project use `requirements.txt`. Install the project requirements with `pip install -r requirements.txt`.

[Further information about project dependencies](https://docs.kedro.org/en/stable/kedro_project_setup/dependencies.html#project-specific-dependencies)

## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `catalog`, `context`, `pipelines` and `session`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `pip install -r requirements.txt` you will not need to take any extra steps before you use them.

### Jupyter
To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```
pip install jupyter
```

After installing Jupyter, you can start a local notebook server:

```
kedro jupyter notebook
```

### JupyterLab
To use JupyterLab, you need to install it:

```
pip install jupyterlab
```

You can also start JupyterLab:

```
kedro jupyter lab
```

### IPython
And if you want to run an IPython session:

```
kedro ipython
```

### How to ignore notebook output cells in `git`
To automatically strip out all output cell contents before committing to `git`, you can use tools like [`nbstripout`](https://github.com/kynan/nbstripout). For example, you can add a hook in `.git/config` with `nbstripout --install`. This will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be retained locally.

[Further information about using notebooks for experiments within Kedro projects](https://docs.kedro.org/en/develop/notebooks_and_ipython/kedro_and_notebooks.html).
## Package your Kedro project

[Further information about building project documentation and packaging your project](https://docs.kedro.org/en/stable/tutorial/package_a_project.html).

**Micromamba** is a lightweight and fast package manager and environment manager from the Mamba project, designed to work with the Conda ecosystem. It's similar to Conda but aims to be more efficient and quicker in resolving dependencies and managing environments.

### Key Features:
1. **Lightweight**: Micromamba is much smaller in size compared to Conda.
2. **Fast**: It has faster dependency resolution and environment management.
3. **No Python Dependency**: Unlike Conda, Micromamba does not require Python to be installed, making it a more self-contained solution.

### Using Micromamba as a Virtual Environment Manager:
Yes, Micromamba can be used to create and manage virtual environments. Here’s a basic example of how to use Micromamba to create and activate a virtual environment:

1. **Install Micromamba**: You can install Micromamba using a minimal installer or from pre-built binaries. For example:

   ```bash
   curl -L https://micromamba.snakepit.net/api/micromamba/linux-64/latest | tar -xvj
   ```

2. **Create a New Environment**:

   ```bash
   micromamba create -n myenv python=3.8
   ```

   This command creates a new environment named `myenv` with Python 3.8.

3. **Activate the Environment**:

   ```bash
   micromamba activate myenv
   ```

4. **Install Packages**:

   ```bash
   micromamba install numpy pandas
   ```

5. **Deactivate the Environment**:

   ```bash
   micromamba deactivate
   ```

Micromamba is particularly useful for users who want a lightweight alternative to Conda while still leveraging the Conda ecosystem for package management.

## How to run the project via custom cli and with click library :

1. To initialize the current zsh shell, run:
    $ eval "$(micromamba shell hook --shell zsh)"

2. Activate the virtual environment using micromamba package manager:
    $ micromamba activate myenv (spaceflights310 in that case")

3. Install the requirements for the specific project :
    $ pip install -r requirements.txt

4. For the training phase, run the following command:
    $ spaceflights train

5. For the inference phase, run the following command:
    $ spaceflights inference