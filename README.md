# dj3fb

English | [简体中文](README_ZH.md)

`dj3fb` can generate `DjangoModelFactory` for your django models by using `factory_boy`.

## Install

```shell script
pip install dj3fb

```

## Examples

```python
# In settings.py
INSTALLED_APPS = [
    '...',
    'dj3fb',
    '...'
]

```

```shell
python manage.py generate_factories

```