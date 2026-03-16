# Flathub submission guide

This document summarizes the practical steps to submit Workdir to Flathub and speed up the review process.

## Assets in this repository

- Local CI manifest: `packaging/flatpak/io.github.dseichter.workdir.yaml`
- Flathub submission manifest: `packaging/flatpak/io.github.dseichter.workdir.flathub.yaml`
- Desktop file: `packaging/flatpak/io.github.dseichter.workdir.desktop`
- AppStream metadata: `packaging/flatpak/io.github.dseichter.workdir.metainfo.xml`
- App icon source: `icons/folder_open_48dp_8B1A10_FILL0_wght400_GRAD0_opsz48.png`

## Local validation before opening PR

Run from repository root:

```bash
sudo pacman -Syu --needed flatpak flatpak-builder appstream python-pip

appstreamcli validate --no-net packaging/flatpak/io.github.dseichter.workdir.metainfo.xml

flatpak --user remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
flatpak --user install -y flathub org.freedesktop.Platform//25.08 org.freedesktop.Sdk//25.08

flatpak-builder --force-clean --repo=repo flatpak-build packaging/flatpak/io.github.dseichter.workdir.yaml
flatpak build-bundle repo workdir-test.flatpak io.github.dseichter.workdir
```

Optional local install test:

```bash
flatpak install --user -y ./workdir-test.flatpak
flatpak run io.github.dseichter.workdir
```

## Flathub PR checklist

1. Fork `flathub/flathub`.
2. Add app files under a directory named `io.github.dseichter.workdir`.
3. Copy `packaging/flatpak/io.github.dseichter.workdir.flathub.yaml` to `io.github.dseichter.workdir/io.github.dseichter.workdir.yaml`.
4. Copy desktop, metainfo, and icon into the same directory.
5. Keep the manifest pinned to a release tag and commit.
6. Include the manifest and references to stable sources.
7. Open PR and include permission justification.

Update the pinned release before opening PR:

```bash
git rev-parse v2026-03-04
```

Then update `tag` and `commit` in `io.github.dseichter.workdir.yaml` accordingly.

## Reviewer notes template

Use this in the Flathub PR description:

```
About the app:
Workdir lets users configure directories and execute their own commands quickly from a GUI and tray menu.

Why filesystem access is needed:
The core feature is opening user-selected directories and executing user-defined commands that operate on project files. Home access is therefore required for normal usage.

Why display sockets are needed:
Workdir is a Qt desktop GUI app and needs Wayland/X11 sockets.

GPU access:
DRI is included for normal Qt rendering support.
```

## Notes

- Keep screenshots in AppStream metadata up to date and publicly reachable.
- If Flathub requests reduced permissions, test the app behavior carefully before changing `finish-args`.