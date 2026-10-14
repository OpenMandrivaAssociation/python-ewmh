Summary:	Python implementation of Extended Window Manager Hints
Name:		python-ewmh
Version:	0.1.6
Release:	1
License:	LGPLv3+
Group:		Development/Python
URL:		https://github.com/parkouss/pyewmh
Source0:	https://files.pythonhosted.org/packages/source/e/ewmh/ewmh-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
Requires:	python%{pyver}dist(python-xlib)

%description
Python implementation of the Extended Window Manager Hints, based on
python-xlib. Caffeine uses it to see whether the active window is
fullscreen.

%files
%license LICENSE.txt
%doc README.rst CHANGES.txt
%{python_sitelib}/ewmh
%{python_sitelib}/ewmh-%{version}*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n ewmh-%{version}

%build
%py_build

%install
%py_install
