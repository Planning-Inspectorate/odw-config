import os

if __name__ == "__main__":
    datalake_name = os.environ.get("DATA_LAKE_STORAGE", None)
    if not datalake_name:
        raise ValueError("DATA_LAKE_STORAGE environment variable is not set")
    metadata_file_path = "data-lake/existing-tables-metadata.json"
    with open(metadata_file_path, "r") as f:
        metadata_content = f.read()
    
    metadata_content = metadata_content.replace("{DATA_LAKE_NAME}", datalake_name)
    with open(metadata_file_path, "w") as f:
        f.write(metadata_content)
