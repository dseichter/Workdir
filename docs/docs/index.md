# Workdir

![ruff](https://github.com/dseichter/Workdir/actions/workflows/ruff.yml/badge.svg)
![bandit](https://github.com/dseichter/Workdir/actions/workflows/bandit.yml/badge.svg)
![trivy](https://github.com/dseichter/Workdir/actions/workflows/trivy.yml/badge.svg)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=dseichter_Workdir&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=dseichter_Workdir)

Workdir helps you work with multiple directories and run commands without manually navigating to each location.

![Workdir](assets/screenshots/workdir.png)

Binaries for Windows and Linux are available (see [releases](https://github.com/dseichter/Workdir/releases)).

[![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/dseichter/Workdir/total)](https://github.com/dseichter/Workdir/releases)
![GitHub License](https://img.shields.io/github/license/dseichter/Workdir)
[![GitHub Issues](https://img.shields.io/github/issues/dseichter/Workdir)](https://github.com/dseichter/Workdir/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/dseichter/Workdir)](https://github.com/dseichter/Workdir/pulls)

## Features

- Manage many directories from one UI
- Configure up to six commands per directory
- Use confirmation prompts for sensitive commands
- Attach additional environment variables for execution
- Reuse Workdir with multiple independent configurations

## Installation and Configuration

Download the [latest release](https://github.com/dseichter/Workdir/releases) into a destination folder of your choice and start the program.

Via the configuration (menu Extras) you can specify your directories and store up to six commands.

![Workdir Configuration](assets/screenshots/configuration.png)

Please always specify the directories using the placeholder `{directory}`. This value is replaced automatically when commands are executed.

## Known Issues

If you run Workdir the first time, the window can be very small. The size is automatically adjusted based on your configured directories.
