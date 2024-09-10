"""Project pipelines."""

from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

from .pipelines import reporting, data_processing, data_science


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    # pipelines = find_pipelines()
    # print(pipelines)
    # pipelines["__default__"] = sum(pipelines.values())
    data_processing_pipeline = data_processing.create_pipeline()
    reporting_pipeline = reporting.create_pipeline()
    default_pipeline = (
        data_processing_pipeline + reporting_pipeline
    )
    return {
        "__default__": default_pipeline,
        "train": data_processing_pipeline,
        "reporting": reporting_pipeline,
    }
