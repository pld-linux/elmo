
Summary:	Elmo, MUA supporting Maildirs and Polish language
Summary(pl):	Program pocztowy Elmo, dzia³a z Maildir'ami, po Polsku
Name:		elmo
Version:	0.3.3
Release:	1
License:	distributable
Group:		Applications/Mail
Source0:	http://switch.dl.sourceforge.net/sourceforge/elmo/%{name}-%{version}.tar.gz
Source1:	%{name}-examplerc
Patch0:		%{name}-makefile.diff
URL:		http://elmo.sourceforge.net
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Elmo, excellent and light mua.



%description -l pl
¦wietny i nie du¿y program pocztowy.




%prep
%setup -q -n %{name}-0.3
%patch0 -p1


%build
%{__libtoolize}
%{__aclocal} -I .
%{__autoconf}


%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT \
	docdir=%{_datadir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(644,root,root,755)
%{_mandir}/man1/*
%{_infodir}/

%attr(755,root,root) %{_bindir}/*
