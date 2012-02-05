Summary:	A Gopher Server
Summary(pl.UTF-8):	Serwer protokołu gopher
Name:		gofish
Version:	0.22
Release:	5
License:	GPL
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/gofish/%{name}-%{version}.tar.gz
# Source0-md5:	d8ae50689d86344e8f279a915ed31844
Source1:	%{name}.logrotate
Source2:	gopherd.init
Patch0:		%{name}-PLD.patch
Patch1:		%{name}-man.patch
URL:		http://gofish.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	logrotate
Provides:	gopher-server
Obsoletes:	gopher-server
Conflicts:	logrotate < 3.8.0
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

%description -l pl.UTF-8
GoFish jest prostym serwerem protokołu gopher. Został stworzony z
myślą o bezpieczeństwie i małym zużyciu zasobów. GoFish używa
pojedynczego procesu obsługującego wszystkie połączenia. Daje to małe
zużycie zasobów, dobre opóźnienia (brak zmian kontekstu) oraz dobrą
skalowalność.

GoFish działa w środowisku chroot(2). Oznacza to, że może udostępniać
pliki tylko z własnego katalogu głównego i z wewnątrz niego. Chociaż
GoFish musi być uruchamiany z prawami roota, aby użyć portu 70,
zmienia uprawnienia na zwykłego użytkownika przed dostępem do plików.

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
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/gopherd

touch $RPM_BUILD_ROOT/var/log/gofish/{gopherd,gofish}.log

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 30 gopher
%useradd -u 13 -g 30 -d /no/home -s /bin/false -c "gopherd user" gopher

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gofish*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/*
%attr(754,root,root) /etc/rc.d/init.d/gopherd
%attr(750,gopher,gopher) /home/services/gopherd
%attr(755,gopher,gopher) %dir /var/log/gofish
%ghost /var/log/gofish/gopherd.log
%ghost /var/log/gofish/gofish.log
%{_mandir}/man[15]/*
