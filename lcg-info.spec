Name: lcg-info
Version: 1.12.4
Release: 1%{?dist}
Summary: lcg-info
Group: System Environment/Daemons
License: ASL 2.0
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildRequires: make
BuildRequires: rsync
BuildRequires: gcc
Requires: perl-LDAP
URL: https://github.com/EGI-Foundation/lcg-info

%description
This command line tool queries the WLCG/EGI information system.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/lcg-info
/usr/share/man/man1
%{_defaultdocdir}/%{name}/LICENSE.txt

%changelog
* Wed Feb 27 2019 Maarten Litmaath <Maarten.Litmaath@cern.ch> - 1.12.4
- Bug fix for GGUS 139556: deprecated Perl syntax creates warnings

* Tue Sep 06 2016 Maarten Litmaath <Maarten.Litmaath@cern.ch> - 1.12.3
- Added SE implementation attributes

* Thu Apr 14 2011 Andrea Sciaba <Andrea.Sciaba@cern.ch> - 1.12.2
- Indicate that bugs should be reported via GGUS

* Thu Apr 14 2011 Andrea Sciaba <Andrea.Sciaba@cern.ch> - 1.12.1
- Added support for VOInfo objects
- Removed requirement for GLUE 1.3
- Various bug fixes

* Thu Mar 24 2011 Laurence Field <laurence.field@cern.ch> - 1.12.0
- FHS compliant
