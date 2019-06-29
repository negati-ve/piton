# piton3

[![PyPI version](https://badge.fury.io/py/piton.svg)](https://badge.fury.io/py/piton)
![](https://img.shields.io/badge/python-3.4%2C%203.5-blue.svg)

Piton3 is a python3 package manager modelled after NPM. Piton3 makes it easier for Python3 developers to share and reuse code. It makes package management simple by doing the following:

- Install packages locally at `python_modules` folder

- Track dependencies in `package.json` with NodeJS-like semantic versioning

	```
	{
		"pythonDependencies": {
			"djangorestframework": "^3.3.3",
			"django": "^1.9.1"
		},
		"pythonDevDependencies": {
			"django-debug-toolbar": "1.0.0"
		}
	}
	```

- Automatic management of nested dependencies. Packages that are installed via nested dependency are removed automatically once packages requiring it are removed

- Simplify unreasonably verbose pip commands such as `install --upgrade <package> >> requirements.txt` and `list --outdated` to more human friendly npm-like commands. `update`, `outdated`, `install --save`, etc

[screenshots](/assets/screenshots)

## Future Plans

Our plans are implement all the features mentioned in the [docs](https://github.com/negati-ve/piton3/docs) repo.

## Installation
```
pip install piton3
```
## Use
```
piton3 <command>
```

## Typical use case

```
piton3 init //creates a package.json
piton3 install django --save
piton3 install django-debug-toolbar --save
```

**IMPORTANT**: ADD python_modules as a python path

- Method 1:

	Add `.python_modules` to `PYTHONPATH` in `.bash_profile`

	Or use `piton3 path --save` to do it automatically.

- Method 2 (more explicit):

	Use the following code at each application entry point:

		def setup_path():
			import sys
			import os
			BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #OR where the python_modules folder is at
			sys.path.append(os.path.join(BASE_DIR, "python_modules"))
		setup_path()

- Method 3 (recommended):

	Use piton3 as a task runner:

	1. Define application entry points in `package.json` under `scripts`

		```
		{
			"scripts": {
				"develop": "python3 manage.py runserver"
			},
			"pythonDependencies": {
				...
			}
		}
		```

	2. Run task with `piton3 run <task>`

## Progress

| Command       | Status        |
| ------------- |:-------------:|
| init          | working       |
| outdated      | working       |
| install       | working       |
| remove        | working       |
| update        | working       |
| bugs tracker  | planned       |
| run           | working       |
| list          | working       |
| prune         | working       |
| path          | working       |

## Piton3 Limitations

Piton3 is all about making package management local. While it replaces Virtualenv, it is not meant to be a repalcement for setuptools.

Piton3 continues to use setuptools, and PYPI in the background, along with very limited use of pip. In future versions the dependency on pip will be removed.

## Developers

Piton3 can be run with develop_entry.py without installing.

Deployment:
```
# Change version number in setup.py
python3 setup.py sdist upload -r pypi
# Amend commit with egg-info
```
