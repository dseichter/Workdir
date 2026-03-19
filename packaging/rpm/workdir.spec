# The version field is updated automatically by the CI workflow.
# Tag format: v2026-03-10 → Version: 2026.03.10
# The macro %%{tagver} converts dots back to dashes to reconstruct the git tag.
%global tagver %(echo %{version} | tr '.' '-')

Name:           workdir
Version:        2026.03.10
Release:        1%{?dist}
Summary:        Work with multiple directories and run commands without navigating manually.

License:        GPL-3.0-only
URL:            https://github.com/dseichter/Workdir
Source0:        %{url}/archive/refs/tags/v%{tagver}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-pip

Requires:       python3 >= 3.12
Requires:       python3-pyside6
Requires:       python3-urllib3
Requires:       python3-packaging

%description
Workdir allows you to manage multiple working directories and execute
commands across them without navigating manually. It provides a graphical
interface built with PySide6 (Qt6).

%prep
%autosetup -n Workdir-%{tagver}

%build
echo "Build phase not needed - pip install will handle it"

%install
python3 -m pip install --no-build-isolation --root=%{buildroot} --no-cache-dir .

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/*.py
%{python3_sitelib}/__pycache__/
%{python3_sitelib}/Workdir-*.dist-info/
%{_bindir}/workdir
%{_datadir}/applications/io.github.dseichter.workdir.desktop
%{_datadir}/metainfo/io.github.dseichter.workdir.metainfo.xml
%{_datadir}/icons/hicolor/256x256/apps/io.github.dseichter.workdir.png

%changelog
* Tue Mar 10 2026 Daniel Seichter <dseichter@github.com> - 2026.03.10-1
- Initial release.
