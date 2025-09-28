# Elastic Demo
Repository contains demo project that uses Python to interact with Elasticsearch. 

## Prepare environment
On MacBook I use Colima with extended hardware resources.
```
colima start --cpu 4 --memory 8
```

If you use Mise, correct Python version should appear on itself. Maybe just `mise trust` and/or `mise install` to make it happened.

Then create Python virtual environment, activate it and install Python dependencies, all with Mise task.

```
mise venv
mise infra-up
```

## Populate Elastic
Run script for inserting dummy data into Elasticsearch.
```
mise populate-elastic
```

## Cleanup
Stop and remove Docker containers.
```
mise infra-down
```
