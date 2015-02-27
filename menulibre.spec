Summary:	An advanced menu editor
Name:		menulibre
Version:	2.0.6
Release:	1
License:	GPLv3
Group:		Graphical desktop/Other
URL:		http://smdavis.us/projects/menulibre/
Source0:	https://launchpad.net/menulibre/2.0/%{version}/+download/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildArch:	noarch

%track
prog %{name} = {
	url = https://launchpad.net/menulibre/2.0/%{version}/+download
	regex = "%{name}-(__VER__)\.tar\.gz"
	version = %{version}
}

%description
An advanced menu editor that provides modern
features in a clean, easy-to-use interface.

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root %{buildroot}

%files
