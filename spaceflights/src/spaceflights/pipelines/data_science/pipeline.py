from kedro.pipeline import Pipeline, node, pipeline

from .nodes import evaluate_model, split_data, train_model, predict#, fetch_test_data


def create_training_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs=["model_input_table", "params:model_options"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            node(
                func=train_model,
                inputs=["X_train", "y_train"],
                outputs="regressor",
                name="train_model_node",
            ),
        ]
    )


def create_inference_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [   
            # node(
            #     func=fetch_test_data,
            #     inputs=["X_test", "y_test"],
            #     outputs=["X_test_fetched", "y_test_fetched"],
            #     name="fetch_test_data_node",
            # ),
            node(
                func=predict,
                inputs=["regressor", "X_test"],
                name="predict_model_node",
                outputs="predictions",
            ),
            node(
                func=evaluate_model,
                inputs=["y_test","predictions"],
                name="evaluate_model_node",
                outputs="metrics",
            ),
        ]
    )