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

%description -l pl
GoFish jest prostym serwerem protoko³u gopher. Zosta³ stworzony z
my¶l± o bezpieczeñstwie i ma³ym zu¿yciu zasobów. GoFish u¿ywa
pojedynczego procesu obs³uguj±cego wszystkie po³±czenia. Daje to ma³e
zu¿ycie zasobów, dobre opó¼nienia (brak zmian kontekstu) oraz dobr±
skalowalno¶æ.

GoFish dzia³a w ¶rodowisku chroot(2). Oznacza to, ¿e mo¿e udostêpniaæ
pliki tylko z w³asnego katalogu g³ównego i z wewn±trz niego. Chocia¿
GoFish musi byæ uruchamiany z prawami roota, aby u¿yæ portu 70,
zmienia uprawnienia na zwyk³ego u¿ytkownika przed dostêpem do plików.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
/var/lib/gopherd
%{_mandir}/man[15]/*
