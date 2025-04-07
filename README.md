# MLCourse-I


## Run locally in JupyterLab
```bash
docker build -t mlcourse-lab .
docker run -it --rm -v $(PWD):/workspace -p 8888:8888 mlcourse-lab
```

## Run locally in VSCode

Use the devcontainer extension to load the project in a container

