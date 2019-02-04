# {{ cookiecutter.package_name }}

[![Build Status](https://travis-ci.org/{{ cookiecutter.github_name }}/{{ cookiecutter.package_short_name}}.svg)](https://travis-ci.org/{{ cookiecutter.github_name }}/{{ cookiecutter.package_short_name}})

{{ cookiecutter.short_description }}

## User Guide

{{ cookiecutter.package_short_name }} has the following features:

*
*

### Installation

Assuming you have `pip` and `Git` installed you can install the development version directly
from GitHub.

```bash
pip install git+git://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.package_short_name}}@develop
```

### Usage Example

...

## Developer Guide

### Installation

Best install `{{ cookiecutter.package_short_name }}` in editable mode:

    $ pip install -r requirements-test.txt

### Run the test suite

Run the test suite with py.test:

    $ py.test
