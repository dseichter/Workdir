# Workdir

Working with multiple directories and execute commands without navigate to them with **Workdir**.

<p align="center">
  <img src="icons/folder_open_48dp_8B1A10_FILL0_wght400_GRAD0_opsz48.png" alt="Workdir Logo"/>
</p>

<p align="center">
  <img src="https://img.shields.io/github/v/release/dseichter/Workdir?style=flat-square" alt="Release">
  <img src="https://img.shields.io/github/downloads/dseichter/Workdir/total?style=flat-square" alt="Downloads">
  <img src="https://img.shields.io/github/license/dseichter/Workdir?style=flat-square" alt="License">
</p>

<p align="center">
  <b><a href="https://dseichter.github.io/Workdir/">Documentation</a></b> •
  <b><a href="https://github.com/dseichter/Workdir/releases">Downloads</a></b> •
  <b><a href="https://github.com/dseichter/Workdir/issues">Issues</a></b>
</p>

<p align="center">
<img src="https://github.com/dseichter/Workdir/actions/workflows/ruff.yml/badge.svg" alt="ruff">
<img src="https://github.com/dseichter/Workdir/actions/workflows/bandit.yml/badge.svg" alt="bandit">
<img src="https://github.com/dseichter/Workdir/actions/workflows/trivy.yml/badge.svg" alt="trivy">
<a href="https://sonarcloud.io/summary/new_code?id=dseichter_Workdir"><img src="https://sonarcloud.io/api/project_badges/measure?project=dseichter_Workdir&metric=alert_status" alt="Quality Gate Status"></a>
</p>

---

## About 

![Workdir](docs/docs/assets/screenshots/workdir.png "Workdir")

My tool **Workdir** is one of the oldest tools I use. I have not been navigating back and forth between directories for over ten years now. I press a button and open my directories directly. I can also start executing commands with one click. With another button I directly start the command line. And sometimes I directly start a command inside the directory. This makes working with directories much easier.

You can *theoretically* specify an unlimited number of directories. Up to six individual commands can be called. When the program starts, it checks whether the directory exists. If not, it will be colored red and no actions will be available.

## Installation and configuration

Download the [latest release](https://github.com/dseichter/Workdir/releases) into a destination folder of your choice and start the program. Via the configuration (menu Extras) you can specify your directories and store up to six commands.

![Workdir - Configuration](docs/docs/assets/screenshots/configuration.png "Workdir - Configuration")

Please note that in the current version you can only specify the directory itself as a placeholder. The examples for CMD and Windows Explorer should help you to implement your own calls. Once you click Save, the commands and directories are immediately available in the Directories tab.

For commands that you do not want to start by mistake, the program gives you, via the Confirmation option, a prompt to display. Here you will be shown a dialog before each execution, which you must confirm before the command is actually executed.

Please always specify the directories using the variable {directory}. This will be replaced and assembled accordingly when the commands are executed. Of course you can also specify executable files or shell scripts which will be called accordingly. This has not been necessary for ourselves so far.

You can also specify additional environment variables. They will be added to your default ones.

## Multiple configurations

I am asked from time to time if I would like to offer more than six commands. This request is mostly based on the need to handle different types of directories with different commands. Very gladly I give my answer in summary, so that it can help you from the beginning:

Workdir can be used multiple times. Create a subfolder each time, which you name “Development” or “Projects”, for example. Copy the application file into these directories. When you start the program, it will check if there is already a configuration there (if not, the program will create it automatically). Now you can define different commands, independent of the category. For example, the opening or updating (git pull) of directories with source code. Or automatic generation of thumbnails or conversion of file formats. The variety knows no limits. Workdir supports you in meeting these requirements as well.

## Known Issues

If you run workdir the first time, the window can be really small. The size will be auto adjusted based on your directories. So please proceed by adding your directories.

# Contributing 

If you want to contribute by fixing an issue, add a new function or just optimize something, a simple instruction how to start development.

## Start development

Create and activate an environment by running the following command:

```python -m venv .venv```

**On Windows:**
```.venv/Scripts/activate```

**On Linux/macOS:**
```source .venv/bin/activate```

Install the required dependencies

```pip install -r src/requirements.txt```

To build and install the project using the new pyproject.toml:

```bash
pip install .
```

To run the application:
```python src/workdir.py```

## 📄 License

GPL 3.0 — see [LICENSE](LICENSE) file at the root of the repository for details.

## Icons
 
RunIfExists uses [Google Material Symbols](https://fonts.google.com/icons) within its code for UI icons.  
Material Symbols are licensed under the [Apache License 2.0](https://github.com/google/material-design-icons/blob/master/LICENSE) and are free for use in open source projects.
