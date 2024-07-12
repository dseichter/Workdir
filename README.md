# Workdir

Working with multiple directories and execute commands without navigate to them with **Workdir**.

![pep8](https://github.com/dseichter/Workdir/actions/workflows/pep8.yml/badge.svg)
![trivy](https://github.com/dseichter/Workdir/actions/workflows/trivy.yml/badge.svg)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=dseichter_Workdir&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=dseichter_Workdir)

[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-white.svg)](https://sonarcloud.io/summary/new_code?id=dseichter_Workdir)

## About 

![Workdir](/images/workdir.png "Workdir")

My tool **Workdir** is one of the oldest tools I use. I have not been navigating back and forth between directories for over ten years now. I press a button and open my directories directly. I can also start executing commands with one click. With another button I directly start the command line. And sometimes I directly start a command inside the directory. This makes working with directories much easier.

You can *theoretically* specify an unlimited number of directories. Up to six individual commands can be called. When the program starts, it checks whether the directory exists. If not, it will be colored red and no actions will be available.

## Installation and configuration

Download the [latest release](https://github.com/dseichter/Workdir/releases) into a destination folder of your choice and start the program. Via the configuration (menu Extras) you can specify your directories and store up to six commands.

![Workdir - Configuration](/images/configuration.png "Workdir - Configuration")

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

```.venv/Scripts/activate```

Install the required dependencies

```pip install -r src/requirements.txt```

If you want to do some UI changes, download and install the latest wxFormBuilder from the [wxFormBuilder Homepage](https://github.com/wxFormBuilder/wxFormBuilder).
