## Docker environment

On MacBook I use Colima VM with extended hardware resources.
```
colima start --cpu 4 --memory 8
```

Start Elastic and Kibana with following command (add `-d` to run it in background).
```
docker compose up
```

## Script dependencies
If you use Mise, correct Python version should appear on itself. Maybe just `mise trust` and/or `mise install` to make it happened.

Then create Python virtual environment, activate it and install Python dependencies, all with Mise task.

```
mise venv
```