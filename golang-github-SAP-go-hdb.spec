# https://github.com/SAP/go-hdb

%global goipath github.com/SAP/go-hdb

%global common_description %{expand:
A Go implementation of an SAP HANA Database Client.}

Version:        0.12.1

%gometa -i

Name:           golang-github-SAP-go-hdb
Release:        3%{?dist}
Summary:        SAP HANA Database Client for Go (Golang)
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/text/transform)

%description
%{common_description}


%package devel
Summary:        %{summary}
BuildArch:      noarch
# https://bugzilla.redhat.com/show_bug.cgi?id=1595083
ExcludeArch:    s390x

%description devel
%{common_description}

This package contains source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%forgeautosetup


%install
%goinstall


%check
# The driver tests require a running SAP DB, sadly.
%gochecks -d driver


%files devel -f devel.file-list
%license LICENSE
%doc README.md NOTICE


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Ed Marshall <esm@logic.net> - 0.12.1-2
- Exclude builds on s390x. (#1595083)

* Mon Jun 25 2018 Ed Marshall <esm@logic.net> - 0.12.1-1
- Update to 0.12.1.
- Update spec to latest go packaging macros.

* Tue Mar 27 2018 Ed Marshall <esm@logic.net> - 0.11.0-1
- Update to 0.11.0.

* Fri Mar 23 2018 Ed Marshall <esm@logic.net> - 0.10.0-1
- Update to 0.10.0.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 09 2017 Ed Marshall <esm@logic.net> - 0.9.5-1
- Update to 0.9.5. (#1523964)

* Sat Oct 07 2017 Ed Marshall <esm@logic.net> - 0.9.1-1
- First package for Fedora
