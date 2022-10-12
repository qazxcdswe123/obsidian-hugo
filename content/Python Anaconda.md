- [Docs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands)
## Commands
- Create
	- `conda create -n name`
	- `conda create -n myenv python=3.9 scipy=0.17.3 astroid babel`
- Activate
	- `conda activate myenv`
- Update
	- `conda update python`
- Delete package
	- `conda remove scipy`
- Delete env
	- `conda env remove -n my_env`


```bash
conda config --set auto_activate_base false
```