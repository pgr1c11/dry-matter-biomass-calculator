# python-vscode-ds-template

Supported Python versions: 3.7, 3.8, 3.9, 3.10

A simple template for setting up a Python project with a few key dependencies for data science. This uses `pyenv` to manage the project's Python version, `virtualenv` for managing the virtual environment and `pip-tools` for managing dependencies based on `setup.py` and `setup.cfg`.

This template includes some example code and data:

1. Main file `__main__.py` so you can run the package, e.g. `python python-vscode-ds-template` from the parent folder. You might need to `pip install numpy`.
1. Modules `src/example/example.py` and `src/example/areas.py`
1. Data file `data/example_data.csv`
1. Test file `test/example/example_test.py` and `test/example/areas_test.py`
1. Jupyter notebook `notebooks/Notes.ipynb`

When using this template, update as necessary:

1. The metadata section of `setup.cfg`.
1. The LICENSE file. For a good resource for choosing a license, check out https://choosealicense.com/.
1. The README.

## Set up pyenv

For a great intro to pyenv I recommend https://realpython.com/intro-to-pyenv/#virtual-environments-and-pyenv.

If you don't have pyenv installed to manage your Python installations:

    brew install pyenv pyenv-which-ext

Set up your shell enviroment. E.g. for zsh, add the following to `~/.zshrc`:

    export PATH=$(pyenv root)/shims:$PATH
    eval "$(pyenv init -)"

Restart your terminal or run `exec "$SHELL"`.

See available Python versions:

    pyenv install —-list

Install the one(s) you want, e.g.:

    pyenv install 3.9.10

Set a global default Python version, e.g.:

    pyenv global 3.9.10

Check the version has been correctly set with `python -V`. If not, try `pyenv rehash` and try again. Also see versions with `pyenv versions` (active starred).

Set your project local Python version with `pyenv local <python_version>`, e.g.:

    pyenv local 3.9.10

This will create a `.python-version` file telling `pyenv` to override it's Python version.

Check you’re using a version of Python in the `~/.pyenv` folder by running `pyenv which python`. You should see something like `Users/your_username/.pyenv/versions/3.9.10/bin/python`.

## Set up virtual environment using virtualenv

Make sure you have `virtualenv` installed for the Python version you are using:

    pip install virtualenv

From your project root folder run:

    virtualenv env

This will create an `env` virtual environment directory in your project. Activate it:

    . env/bin/activate (or source env/bin/activate)

This project has the VS Code setting to automatically activate the virtual environment in `.vscode/settings.json`:

    "python.terminal.activateEnvironment": true

This should mean that you don't need to manually activate the virtual environment when you open the project in VS Code or start a new VS Code terminal instance. You can deactivate the virtual environment by running `deactivate`.

It is recommended that you manage your depenencies using `pip-tools`:

    pip install pip-tools

After installing `pip-tools` in your virtual environment you may need to rehash to ensure that `pip-compile` is pointed at the version in the virtual environment:

    rehash

### Install dependencies

You can now use `pip-tools` to install other dependencies, which it does based on `setup.cfg`. To install the dependencies currently listed, including extra dev and test depencenies, run:

    pip-compile --extra dev --extra test && pip install -r requirements.txt

## Adding more dependencies

Add dependencies into the correct part of `setup.cfg`. Build dependencies should be listed under `install_requires`, dev or test dependency should be listed in the `dev` and `test` sublists of `[options.extras_require]`.

Use pip-tools to create a `requirements.txt` from the dependencies listed in `setup.cfg`. If you're a developer you'll probably want the dev and test extras.

    pip-compile --extra dev --extra test

Then pip install the generated requirements.txt:

    pip install -r requirements.txt

Since you will pretty much always be running these commands together, you can chain them like this:

    pip-compile --extra dev --extra test && pip install -r requirements.txt

If you want to add a public or private git repository as a dependency, you can do so under `install_requires` or any `[options.extras_require]` like this:

    ExampleRepo @ git+ssh://git@github.com/example_org/ExampleRepo.git

## Publishing

Projects based on this template should be pretty much ready to publish as installable packages following instructions in the [docs](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

## Switching off type checking

If you want to switch off type checking you can set `ignore_errors = True` in `mypy.ini`.

## Managing package data files

This project uses the `include_package_data` option in `setup.cfg`, so the rules in `MANIFEST.in` are used to include/exclude files and directories. For more info on using `MANIFEST.in` see the [docs](https://packaging.python.org/en/latest/guides/using-manifest-in/).

## Testing

This project uses pytest for testing. It has been set up to display console output from tests by using the `-s` argument in `.vscode/settings.json`:

    python.testing.pytestArgs": ["test", "-s"]

To see the output, go to the Output tab in VS Code and Select `Python Test Log` from the drop down list.

To disable displaying console output from tests, remove `-s` from the args.


## Deploying an API

There are several ways of doing this. The recommended approach is using Flask and App Engine on Google Cloud Platform.

### Flask, Docker and Container Registry on GCP

[This Towards Data Science article](https://towardsdatascience.com/deploy-apis-with-python-and-docker-4ec5e7986224) provides a guide to creating and deploying an API using Python, Flask, Docker and the Container Registry on Google Cloud Platform. There is a .pdf of this article [here](https://drive.google.com/file/d/1RFMbZfbTo2tY3s7i_osyR2dd9IusnB0_/view?usp=sharing) incase it gets removed. 

Note that the final line of the Dockerfile should be:

    CMD ["gunicorn"  , "-b", "0.0.0.0:8080", "app:app"]

### Flask and App Engine on GCP

[This YouTube video](https://www.youtube.com/watch?v=3fsIcMgUOY8) (which is accompanied by [this Towards Data Science article](https://towardsdatascience.com/how-to-deploy-a-flask-api-8d54dd8d8b8a)) provides a guide to creating and deploying an API using Python, Flask and App Engine on Google Cloud Platform. It's probably slightly quicker and easier than the Python-Flask-Docker-Container Registry approach. 

If building on Windows, add:

    pywin32 >= 1.0; platform_system=='Windows'
    pywinpty >= 1.0; platform_system=='Windows'

to `install_requires` in `setup.cfg` to prevent GCP trying to build Windows packages in App Engine (which throws an error). This `platform_system` annotation can be added to any packages listed in `install_requires` to customise `setup.cfg` (and the resulting `requirements.txt`).

On first deploying your app, GCP will create a `.gcloudignore` file, which should work in the same way as `.gitignore`. It should also ignore any files or directories listed in your `.gitignore`, although this doesn't always happen. It's obvious if this hasn't happened, because you'll see GCP trying to upload 1,000s of files (most of which will be from your `env` directory and don't need to be uploaded to GCP). Get around this by adding:

    .env
    .venv
    env/
    venv/
    ENV/
    env.bak/
    venv.bak/

to `.gcloudignore`.

Once prepared, you can test your API using either `gunicorn` for Linux (as in the tutorials linked above) or `waitress` for Windows. If using `waitress` the corresponding command (to that shown using `gunicorn` in the linked tutorial) is:

    waitress-serve --url-prefix=/my-app --listen=127.0.0.1:8001 main:app

More details about `waitress` in [this link](https://www.devdungeon.com/content/run-python-wsgi-web-app-waitress).

In addition to the Python version annotation added to `app.yaml` shown in the linked tutorial, it is also possible to add other annotations which control how the app runs when on App Engine. This:

    runtime: python310
    instance_class: F1
    automatic_scaling:
        min_instances: 1
        max_instances: 1

sets the python version, the GCP instance class and the minimum and maximum number of instances which GCP can spin up depending on API demand. More details about how to customise `app.yaml` in [this link](https://cloud.google.com/appengine/docs/standard/python3/config/appref#instance_class).
