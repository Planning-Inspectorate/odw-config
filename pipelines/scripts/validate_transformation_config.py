from odw.core.orchestration.dependency_resolver import DependencyResolver
import yaml
import os


if __name__ == "__main__":
    with open(
        os.path.join(
            "data-lake", "orchestration", "orchestration_transform_dependencies.yaml"
        ),
        "r",
        encoding="utf-8",
    ) as f:
        config = yaml.safe_load(f)
    print("Validating the transformation config file")
    try:
        DependencyResolver.validate_config(config)
    except Exception as e:
        print("Config is invalid. The below validation errors were found")
        raise e
    print("Config file is valid!")
