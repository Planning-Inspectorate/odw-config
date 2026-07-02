# orchestration_transform_dependencies

The transformation config at `orchestration_transform_dependencies` has the below expected structure

- `entities` - A list of entity objects
    - `entity_name` - The name of the entity
        - `stage_name` - The name of the transformation stage for the containing entity
          - `kwargs` - Any arguments that should be fed into the underlying `ETLProcess` from `odw-synapse-workspace`
            - `etl_process_name` - Aligns with the `get_name` method of the relevant `ETLProcess` to run for this entity-stage
        - `depends_on` - List of `entity_name.stage_name` entries that this particular entity-stage depends on
