# $Revision: 1.1 $
Summary:	A Gopher Server
Summary(pl):	Serwer protoko³u gopher
Name:		gofish
Version:	0.19
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	gopher://seanm.ca/9/%{name}/%{name}-%{version}.tar.gz
URL:		http://gofish.sourceforge.net/
Provides:	gopherd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GoFish is a simple gopher / web server. It is designed with security
and low resource usage in mind. GoFish uses a single process that
handles all the connections. This provides low resource usage, good
latency (no context switches), and good scalability.

GoFish runs in a chroot(2) environment. This means that GoFish can
only serve files from the root directory or below. While GoFish must
run at root privilege to be able to use port 70, it drops to a normal
user while accessing files.

%prep
%setup -q

%build
aclocal
%{__autoconf}
autoheader
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_mandir}/man[15]/*
%attr(755,root,root) %{_bindir}/*
%attr(700,root,root) %{_sbindir}/*
%{_sysconfdir}/*
/var/lib/gopherd
