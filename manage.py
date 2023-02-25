#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# 21122924 刘育杰 智能科学与技术 
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
# 项目管理的脚本，启动项目、创建app、数据库管理


if __name__ == '__main__':
    main()
