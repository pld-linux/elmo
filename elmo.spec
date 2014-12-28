# Conditional build:
%bcond_without	home_etc	# don't use home_etc
#
Summary:	Elmo, MUA supporting Maildirs and Polish language
Summary(pl.UTF-8):	Elmo - program pocztowy obsługujący Maildiry i język polski
Name:		elmo
Version:	1.3.2
Release:	3
License:	GPL v2+
Vendor:		Jacek Śliwerski <rzyj@plusnet.pl>
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	bc3836a276b092fde8555e42532d4bc8
Source1:	%{name}-examplerc
Patch0:		%{name}-etc_dir.patch
URL:		http://elmo.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gpgme-devel
BuildRequires:	libstdc++-devel
#BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.0
%{?with_home_etc:BuildRequires:	home-etc-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Elmo, excellent and light mua.

%description -l pl.UTF-8
Elmo - świetny i nieduży program pocztowy.

%prep
%setup -q
install %{SOURCE1} ./examplerc

%build
%{__gettextize}
#%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
#%{__automake} m4/Makefile
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
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/themes
%{_datadir}/%{name}/themes/80x25
%{_datadir}/%{name}/themes/outlook
%{_datadir}/%{name}/template
%{_mandir}/man1/*
