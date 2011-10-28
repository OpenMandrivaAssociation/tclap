Name: tclap
Summary: Templatized C++ Command Line Parser
Version: 1.2.1
Release: %mkrel 1
Group: System/Libraries
License: MIT
URL: http://tclap.sourceforge.net/
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
Provides: %{name}-devel = %{version}-%{release}

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
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/pkgconfig
mv %{buildroot}%{_libdir}/pkgconfig/*.pc %{buildroot}%{_datadir}/pkgconfig/

%clean 
rm -rf %{buildroot}

%check
%make check

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS
%{_includedir}/*
%{_datadir}/pkgconfig/*.pc
