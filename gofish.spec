Summary:	A Gopher Server
Summary(pl):	Serwer protoko�u gopher
Name:		gofish
Version:	0.22
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://osdn.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.logrotate
Source2:	gopherd.init
Patch0:		%{name}-PLD.patch
Patch1:		%{name}-man.patch
URL:		http://gofish.sourceforge.net/
Requires:	logrotate
Requires(pre):	user-gopher
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
GoFish jest prostym serwerem protoko�u gopher. Zosta� stworzony z
my�l� o bezpiecze�stwie i ma�ym zu�yciu zasob�w. GoFish u�ywa
pojedynczego procesu obs�uguj�cego wszystkie po��czenia. Daje to ma�e
zu�ycie zasob�w, dobre op�nienia (brak zmian kontekstu) oraz dobr�
skalowalno��.

GoFish dzia�a w �rodowisku chroot(2). Oznacza to, �e mo�e udost�pnia�
pliki tylko z w�asnego katalogu g��wnego i z wewn�trz niego. Chocia�
GoFish musi by� uruchamiany z prawami roota, aby u�y� portu 70,
zmienia uprawnienia na zwyk�ego u�ytkownika przed dost�pem do plik�w.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{logrotate.d,rc.d/init.d},/var/log/gofish}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	rootdir=/home/services/gopherd

install %{SOURCE1} $RPM_BUILD_ROOT/etc/logrotate.d
install %{SOURCE2} $RPM_BUILD_ROOT//etc/rc.d/init.d/gopherd

touch $RPM_BUILD_ROOT/var/log/gofish/{gopherd,gofish}.log

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/gofish*
%attr(640,root,root) /etc/logrotate.d/*
%attr(754,root,root) /etc/rc.d/init.d/gopherd
%attr(750,gopher,gopher) /home/services/gopherd
%attr(755,gopher,gopher) %dir /var/log/gofish
%ghost /var/log/gofish/gopherd.log
%ghost /var/log/gofish/gofish.log
%{_mandir}/man[15]/*
