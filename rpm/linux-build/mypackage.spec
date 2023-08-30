%define _topdir /path/to/your/build/directory

Name:        mypackage
Version:     1.0
Release:     1%{?dist}
Summary:     My Package

Group:       Development/Tools
License:     GPL
URL:         https://example.com

BuildArch:   noarch

%description
My Package Description

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/etc
cp -r sources/* %{buildroot}/usr/bin/
cp -r config/* %{buildroot}/etc/

%files
%{buildroot}/usr/bin/*
%{buildroot}/etc/*

%changelog
* Mon Aug 29 2023 Your Name <your.email@example.com> - 1.0-1
- Initial package

