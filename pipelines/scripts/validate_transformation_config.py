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
    DependencyResolver.validate(config)
