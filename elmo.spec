Summary:	Elmo, MUA supporting Maildirs and Polish language
Summary(pl):	Elmo - program pocztowy obs�uguj�cy Maildiry i j�zyk polski
Name:		elmo
Version:	0.8.3
Release:	1
License:	GPL v2+
Vendor:		Jacek �liwerski <rzyj@plusnet.pl>
Group:		Applications/Mail
Source0:	http://savannah.nongnu.org/download/elmo/unstable.pkg/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a7837950dbb4ffcc5ec7fea15150c525
Source1:	%{name}-examplerc
Patch0:		%{name}-etc_dir.patch
URL:		http://elmo.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Elmo, excellent and light mua.

%description -l pl
Elmo - �wietny i niedu�y program pocztowy.

%prep
%setup -q
install -m 644 %{SOURCE1} ./examplerc

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make} \
	CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT \
	docdir=%{_datadir}/%{name}-%{version}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ADVOCACY AUTHORS README TODO BUGS THANKS examplerc
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*.info*
