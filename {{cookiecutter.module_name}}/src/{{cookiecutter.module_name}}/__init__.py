"""{{ cookiecutter.module_name }} - {{ cookiecutter.description }}"""

__version__ = "{{ cookiecutter.version }}"

{% if cookiecutter.cli == "y" -%}
from {{ cookiecutter.module_name }}.cli import app
{% endif -%}
from {{ cookiecutter.module_name }}.lib import add

{% if cookiecutter.cli == "y" -%}
__all__ = ["add", "app"]
{% else -%}
__all__ = ["add"]
{% endif -%}
