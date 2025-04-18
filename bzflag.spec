%global debug_package %{nil}

Name:		bzflag
Version:	2.4.30
Release:	1
Source0:	https://github.com/BZFlag-Dev/bzflag/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    bzflag.desktop
Summary:	3D multi-player tank battle game
URL:		https://github.com/BZFlag-Dev/bzflag
License:	LGPLv2.1 or MPLv2.0
Group:		Games/Arcade

BuildRequires:	make
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	zlib-devel
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	lib64curl-devel
BuildRequires:	pkgconfig(glew)
BuildRequires:	lib64cares-devel
BuildRequires:	pkgconfig(ncurses)

%description
BZFlag is an Open Source OpenGL multiplayer multiplatform Battle Zone
capture the Flag game.  At its heart, the game is a 3D first person
tank simulation where opposing teams battle for dominance.  The game
was originally written for SGI computers running Irix, but now runs
and is actively maintained on Windows, Linux, Mac OS X, and other
platforms.

%prep
%autosetup -p1

%build
./autogen.sh
./configure --bindir=%{_gamesbindir} \
            --libdir=%{_libdir} \
            --mandir=/usr/share/man \
            --datadir=%{_gamesdatadir}

$make

%install
mkdir -p %{buildroot}%{_datadir}/applications
install -Dm0755 data/%{name}.desktop %{buildroot}%{_datadir}/applications/
install -Dm644 data/bzflag-48x48.png %{buildroot}/usr/share/pixmaps/bzflag-48x48.png

%make_install

%files
%{_gamesbindir}/*
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*
%{_libdir}/*
%{_mandir}/man5/*
%{_mandir}/man6/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
