Name:		tclap
Version:	1.2.1
Release:	4
Summary:	Templatized C++ Command Line Parser
Group:		System/Libraries
License:	MIT
URL:		http://tclap.sourceforge.net/
Source0:	http://sourceforge.net/projects/tclap/files/%{name}-%{version}.tar.gz
BuildArch:	noarch
Provides:	%{name}-devel = %{version}-%{release}

%description
This is a simple C++ library that facilitates parsing command line
arguments in a type independent manner.  It doesn't conform exactly
to either the GNU or POSIX standards, although it is close.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%__mkdir_p %{buildroot}%{_datadir}/pkgconfig
%__mv %{buildroot}%{_libdir}/pkgconfig/*.pc %{buildroot}%{_datadir}/pkgconfig/

%check
%make check

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS
%{_includedir}/*
%{_datadir}/pkgconfig/*.pc


%changelog
* Tue Feb 07 2012 Andrey Bondrov <abondrov@mandriva.org> 1.2.1-2
+ Revision: 771501
- Drop no longer needed RPM4 junk from spec

* Fri Oct 28 2011 vsinitsyn <vsinitsyn> 1.2.1-1
+ Revision: 707712
- imported package tclap

