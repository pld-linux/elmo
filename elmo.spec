# Conditional build:
%bcond_without	home_etc	# don't use home_etc
#
Summary:	Elmo, MUA supporting Maildirs and Polish language
Summary(pl):	Elmo - program pocztowy obs³uguj±cy Maildiry i jêzyk polski
Name:		elmo
Version:	1.3.1
Release:	1
License:	GPL v2+
Vendor:		Jacek ¦liwerski <rzyj@plusnet.pl>
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	551171feb937a7b58372682993653ba5
Source1:	%{name}-examplerc
Patch0:		%{name}-etc_dir.patch
URL:		http://elmo.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.0
%{?with_home_etc:BuildRequires:	home-etc-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Elmo, excellent and light mua.

%description -l pl
Elmo - ¶wietny i niedu¿y program pocztowy.

%prep
%setup -q
install -m 644 %{SOURCE1} ./examplerc

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%{__automake} m4/Makefile
%configure \
	%{?with_home_etc:--with-home-etc}

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
%doc ADVOCACY AUTHORS doc/README.txt doc/sample.* TODO BUGS THANKS examplerc
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
