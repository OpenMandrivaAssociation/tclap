Name:		tclap
Version:	1.2.2
Release:	4
Summary:	Templatized C++ Command Line Parser
Group:		System/Libraries
License:	MIT
URL:		https://tclap.sourceforge.net/
Source0:	http://sourceforge.net/projects/tclap/files/%{name}-%{version}.tar.gz
Source1:	tclap.rpmlintrc
BuildArch:	noarch
Provides:	%{name}-devel = %{version}-%{release}
BuildRequires:	doxygen graphviz

%description
This is a simple C++ library that facilitates parsing command line
arguments in a type independent manner.  It doesn't conform exactly
to either the GNU or POSIX standards, although it is close.

%prep
%setup -q

%build
%configure
%make

%install
%make_install

%__mkdir_p %{buildroot}%{_datadir}/pkgconfig
%__mv %{buildroot}%{_libdir}/pkgconfig/*.pc %{buildroot}%{_datadir}/pkgconfig/

%check
cd tests
export srcdir="`pwd`"
for i in test*.sh; do
	if ! ./$i; then
		echo "Test $i failed"
		exit 1
	fi
done

%files
%doc README AUTHORS ChangeLog NEWS
%{_includedir}/*
%{_datadir}/pkgconfig/*.pc
%doc %{_docdir}/%{name}
