# dj3fb

[English](README.md) | 简体中文

`dj3fb` 使用 `factory_boy` 为django models生成 `DjangoModelFactory`。

## 1. 简介

* `dj3fd`是一个django app，它有一个Command `generate_factories`，可以根据django models自动生成具体的 `DjangoModelFactory`。
* `faker_utils`中有一个`f`变量，它是一个faker实例，可以用它来生成随机数据。

## 2. 使用

### 安装

```shell
pip install dj3fb

```
### 样例

* 配置 `settings.py`

```python
INSTALLED_APPS = [
    '...',
    'dj3fb',
    '...'
]

# 可选
DJ3FB = {
    # 可选，为内置app或第三方app也生成factory类
    "include_third_party_apps": [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ],
    # 可选，手动指定一个model的factory类，不自动生成
    "existed_factories": {
        "django.contrib.auth.User": "test_app.UserFactory"
    },
}


```

* 执行命令: `generate_factories`

```shell
python manage.py generate_factories
# 在app目录中，会生成一个factories目录，里面包含根据model生成的factory类。

```
