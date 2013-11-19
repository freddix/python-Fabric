%define		module	Fabric

Summary:	Simple, Pythonic tool for remote execution and deployment
Name:		python-%{module}
Version:	1.8.0
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/F/Fabric/%{module}-%{version}.tar.gz
# Source0-md5:	1f195d16b05877767816617749d33eca
URL:		http://fabfile.org/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-ecdsa
Requires:	python-paramiko >= 1.10.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fabric is a Python library and command-line tool for streamlining
the use of SSH for application deployment or systems administration
tasks.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.rst
%attr(755,root,root) %{_bindir}/fab
%{py_sitescriptdir}/fabfile
%{py_sitescriptdir}/fabric
%{py_sitescriptdir}/*.egg-info

