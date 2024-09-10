import click
from kedro.framework.context import KedroContext
from kedro.framework.session import KedroSession
from kedro.config import OmegaConfigLoader
from kedro.pipeline import Pipeline
from kedro.runner import SequentialRunner, ParallelRunner, ThreadRunner
from .pipelines import data_processing,data_science,reporting
from kedro.framework.project import configure_project
from pathlib import Path
from kedro.framework.startup import bootstrap_project
from kedro.framework.hooks import _create_hook_manager
from kedro.framework.project import pipelines  # , settings
from typing import Optional, Dict, Any


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    data_processing_pipeline = data_processing.create_pipeline()
    ds_train_pipeline = data_science.create_training_pipeline()
    ds_inference_pipeline = data_science.create_inference_pipeline()
    reporting_pipeline = reporting.create_pipeline()
    train_pipeline = data_processing_pipeline + ds_train_pipeline
    inference_pipeline = (
        data_processing_pipeline + ds_inference_pipeline + reporting_pipeline
    )
    return {
        "train": train_pipeline,
        "inference": inference_pipeline,
    }


class KedroPipelineRunner:
    def __init__(
        self,
        project_path: str,
        conf_path: str,
        env: str = "base",
        extra_params: Optional[Dict[str, Any]] = None,
    ):
        self.project_path = Path(project_path)
        self.conf_path = Path(conf_path)
        self.env = env
        self.extra_params = extra_params or {}
        self.context = None
        self.config_loader = None

        # Bootstrap the Kedro project to load necessary metadata and configurations
        self.bootstrap_project()

    def bootstrap_project(self):
        # Assuming you have a function to get package_name, update if necessary
        metadata = bootstrap_project(self.project_path)
        self.setup_context(metadata)

    def setup_context(self, metadata):
        self.config_loader = OmegaConfigLoader(
            conf_source=str(self.conf_path), base_env=self.env
        )
        self.context = KedroContext(
            project_path=self.project_path,
            config_loader=self.config_loader,
            env=self.env,
            package_name="spaceflights",  # Ensure this is correct if required
            hook_manager=_create_hook_manager(),  # Provide a hook manager
        )

    def run(self, pipeline_name: str = "__default__"):
        with KedroSession.create(
            project_path=self.project_path,
            env=self.env,
            extra_params=self.extra_params,
        ) as session:
            # Access the context from the session
            context = session.load_context()
            pipeline = register_pipelines()
            # Retrieve the pipeline from the context
            pipelines = pipeline

            # Create a SequentialRunner instance
            runner = SequentialRunner()

            # Run the pipeline using the SequentialRunner
            runner.run(
                pipeline=pipelines[pipeline_name],
                catalog=context.catalog,
            )


@click.group()
def cli():
    """Spaceflights CLI"""
    pass


@cli.command()
def train():
    """Run the training pipeline"""
    runner = KedroPipelineRunner(
        project_path="/Users/vyronaskatsos/spaceflights",
        conf_path="/Users/vyronaskatso/spaceflights/conf",
    )
    runner.run(pipeline_name="train")


@cli.command()
def inference():
    """Run the inference pipeline"""
    runner = KedroPipelineRunner(
        project_path="/Users/vyronaskatsos/spaceflights",
        conf_path="/Users/vyronaskatsos/spaceflights/conf",
    )
    runner.run(pipeline_name="inference")


if __name__ == "__main__":
    cli()
