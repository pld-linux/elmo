Summary:	Elmo, MUA supporting Maildirs and Polish language
Summary(pl):	Elmo - program pocztowy obs�uguj�cy Maildiry i j�zyk polski
Name:		elmo
Version:	0.6
Release:	1
License:	distributable
Group:		Applications/Mail
Source0:	http://savannah.nongnu.org/download/elmo/unstable.pkg/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}-examplerc
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-etc_dir.patch
URL:		http://elmo.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Elmo, excellent and light mua.

%description -l pl
Elmo - �wietny i niedu�y program pocztowy.

%prep
%setup -q 
%patch0 -p1
#%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I .
%{__autoconf}
%{__automake}
%configure

%{__make} CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT \
	docdir=%{_datadir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*.info*
