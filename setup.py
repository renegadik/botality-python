from setuptools import setup, find_packages

setup(
    name="botality",  # Название библиотеки
    version="0.1.0",  # Версия
    packages=find_packages(),  # Автоматически находит все пакеты в директории botality
    install_requires=[  # Зависимости
        "python-telegram-bot==20.0",
        "discord.py==1.7.3",
    ],
    include_package_data=True,
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)