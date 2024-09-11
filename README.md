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



# Integrating Apache Airflow with a Kedro Project in a Jupyter Environment

This guide will walk you through the steps to integrate **Apache Airflow** with your **Kedro** project in a Jupyter environment. The integration allows you to orchestrate your Kedro pipelines using Airflow's powerful scheduling and task management capabilities.

---

## Steps to Integrate Apache Airflow with Kedro in a Jupyter Environment

### 1. Install Apache Airflow

To get started, install Apache Airflow using the official guidelines. If you are working in a Python environment like conda or micromamba, you can install it with:

```bash
pip install apache-airflow kedro-airflow
pip install virtualenv apache-airflow\[cncf/kubernetes\]
```

Ensure that you initialize the Airflow database after installation:

```bash
export AIRFLOW_HOME=~/airflow  # Define where Airflow will store its files
airflow db init  # Initialize the Airflow database
```


#### 2. **Create a Dag File for Your Kedro Pipeline**
   The Kedro-Airflow plugin helps you convert Kedro pipelines into Airflow DAGs (Directed Acyclic Graphs).

   From your project directory, run:

   ```bash
   kedro airflow create
   ```

   This will generate an Airflow DAG in the `airflow_dags/` directory based on your Kedro pipelines.

#### 3. **Configure Airflow to Use the Kedro DAG**
   Copy the generated DAG file (`airflow_dags/my_project_name.py`) into Airflow’s DAGs folder. For example:

   ```bash
   mkdir -p ~/airflow/dags
   cp airflow_dags/* ~/airflow/dags/
   ```

   This makes the Kedro pipeline available as an Airflow DAG.

#### 4. **Start the Airflow Web Server and Scheduler**
   Airflow needs two processes: the web server to view and manage DAGs, and the scheduler to run them.

   Open two terminal tabs and run:

   - In the first tab, start the Airflow web server:

     ```bash
     airflow webserver --port 8080
     ```

   - In the second tab, start the Airflow scheduler:

     ```bash
     airflow scheduler
     ```

   Now you can access the Airflow UI in your browser at `http://localhost:8080`.

#### 5. **Trigger Your Kedro Pipeline DAG**
   In the Airflow UI, you'll see your Kedro pipeline as a DAG. You can trigger it manually or schedule it to run at specific intervals.

#### 6. **Running from Jupyter Notebooks (Optional)**
   If you prefer running Kedro directly from a Jupyter notebook, you can trigger Airflow DAGs from within Jupyter using Airflow's CLI.

   Here's how you can do it from Jupyter:

   ```python
   import subprocess

   # Trigger the DAG
   dag_id = "your_dag_id"
   subprocess.run(["airflow", "dags", "trigger", dag_id])
   ```

   This will trigger your Airflow DAG (which runs your Kedro pipeline) from Jupyter.

### 3. Define the DAG for Kedro Pipeline

Airflow uses Directed Acyclic Graphs (DAGs) to represent workflows. You need to create a DAG that triggers your Kedro pipeline. In your DAG file, import the necessary Kedro and Airflow modules, then define tasks that will run your Kedro pipeline.

Example structure of your Airflow DAG file:

```python
from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from kedro.framework.session import KedroSession

def run_kedro_pipeline():
    with KedroSession.create("your_kedro_project") as session:
        session.run()

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
}

with DAG('your_kedro_dag', default_args=default_args, schedule_interval='@daily') as dag:
    run_pipeline = PythonOperator(
        task_id='run_kedro_pipeline',
        python_callable=run_kedro_pipeline,
    )
```

Save this Python file in your Airflow DAGs directory, typically located in `~/airflow/dags/`.

### 4. Test Your Setup

After setting up your DAG file:

1. Restart the Airflow scheduler and web server.
2. In the Airflow UI (`http://localhost:8080`), you should see the DAG listed.
3. Trigger the DAG manually and verify that your Kedro pipeline runs successfully.

### 5. Handling Authentication and Errors

#### Username/Password Prompt
If you're prompted to enter a username and password at `http://localhost:8080`, the default credentials are:

- **Username:** `airflow`
- **Password:** `airflow`

If this doesn't work, you may need to set up authentication by modifying the `airflow.cfg` file.

#### Task Instances Still Running Error
If you encounter an error about task instances still running when attempting to delete a DAG, follow these steps:

- Clear the task instances using the Airflow UI or from the command line:

   ```bash
   airflow tasks clear <dag_id> --yes
   ```

- Alternatively, kill running task processes manually:

   ```bash
   ps aux | grep airflow
   kill -9 <task_instance_pid>
   ```

Then, you can safely delete the DAG:

```bash
airflow dags delete <dag_id>
```

### 6. Troubleshooting

#### Task Runner Processes
Sometimes you may encounter issues with Airflow's task runner processes that prevent you from deleting or stopping a DAG. To resolve this:

1. Identify running Airflow processes using:

   ```bash
   ps aux | grep airflow
   ```

2. Kill any running `task runner` or `web server` processes manually:

   ```bash
   kill -9 <process_id>
   ```

3. Restart the Airflow scheduler and web server.

---

### Conclusion

Integrating Kedro with Airflow allows you to leverage Airflow's orchestration and scheduling features with Kedro's pipeline framework. Once set up, Airflow will help you automate and monitor your Kedro pipelines with ease.

For more information, refer to the official documentation for [Apache Airflow](https://airflow.apache.org/docs/) and [Kedro](https://kedro.readthedocs.io/).

If you want to start fresh with Apache Airflow and remove all existing configurations, databases, and processes, you can follow these steps. This approach will clear out your existing Airflow setup and allow you to start from scratch.

### 1. **Stop Airflow Services**

Ensure that all Airflow services (webserver, scheduler, etc.) are stopped. You can use `pkill` or `kill` commands to stop them:

```bash
pkill -f "airflow"
```

### 2. **Remove Airflow Files and Directories**

Airflow stores various files and directories that you might want to remove. Be careful with this step as it will delete all your existing DAGs, configurations, and logs.

```bash
# Remove Airflow logs
rm -rf /path/to/your/airflow/logs

# Remove Airflow DAGs
rm -rf /path/to/your/airflow/dags

# Remove Airflow configurations
rm -rf /path/to/your/airflow/config
```

Replace `/path/to/your/airflow/` with the actual path to your Airflow installation. The default path is often `~/airflow`.

### 3. **Remove Airflow Database**

Airflow uses a database to store its metadata. If you're using SQLite (the default for a new installation), you can remove the database file:

```bash
rm /path/to/your/airflow/airflow.db
```

If you're using another database like PostgreSQL or MySQL, you'll need to drop the database or delete the schema manually.

### 4. **Clear Airflow PID Files**

Remove any stale PID files that might be causing issues:

```bash
rm /path/to/your/airflow/airflow-webserver.pid
rm /path/to/your/airflow/airflow-scheduler.pid
```

### 5. **Reinstall Airflow**

You can reinstall Airflow to ensure a clean setup:

```bash
pip uninstall apache-airflow
pip install apache-airflow
```


### 6. **Stop the Running Webserver**

If the Airflow webserver is already running and using port 8080, you need to stop it first. If you can't find the exact process ID (PID), you can use the `pkill` command to stop it:

```bash
pkill -f "airflow webserver"
pkill -f "airflow scheduler"
```

Alternatively, you can use `lsof` or `netstat` to find the PID of the process using port 8080 and then kill it:

```bash
lsof -i :8080
```

Look for the PID in the output and then use:

```bash
kill -9 <PID>
```

### 7. **Remove Stale PID Files**

Airflow uses PID files to track running processes. If these files are stale, they might prevent Airflow from starting properly. Remove any existing PID files:

```bash
rm /path/to/your/airflow/airflow-webserver.pid
rm /path/to/your/airflow/airflow-scheduler.pid
```

Replace `/path/to/your/airflow/` with the actual path to your Airflow installation.

**Repeat the whole process all over again in order to have a successfull Airfow initilization

### Additional Steps

If you continue to experience issues or if killing the processes does not work, consider these additional steps:

- **Check for any lingering Airflow processes:** Ensure that there are no remaining Airflow processes running that might still be using port 8080.

- **Restart your system:** Sometimes, a reboot can help resolve lingering port conflicts, especially if the above steps do not free up the port.

- **Change the port (if necessary):** If you can't free up port 8080, consider running Airflow on a different port by specifying it with the `--port` flag (e.g., `--port 8081`).
