Name:		tclap
Version:	1.2.1
Release:	8
Summary:	Templatized C++ Command Line Parser
Group:		System/Libraries
License:	MIT
URL:		http://tclap.sourceforge.net/
Source0:	http://sourceforge.net/projects/tclap/files/%{name}-%{version}.tar.gz
Source1:	tclap.rpmlintrc
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
%doc README AUTHORS ChangeLog NEWS
%{_includedir}/*
%{_datadir}/pkgconfig/*.pc
