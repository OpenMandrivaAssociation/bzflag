Name:		bzflag
Summary:	A multiplayer 3D tank battle game
Version:	2.0.16
Release:	4
Source0:	http://download.sourceforge.net/bzflag/%{name}-%{version}.tar.bz2
Patch0:		bzflag-2.0.4-lookup.patch
Source11:	%{name}.16.png
Source12:	%{name}.32.png
Source13:	%{name}.48.png
URL:		http://BZFlag.SourceForge.net/
License:	LGPLv2
Group:		Games/Arcade
BuildRequires:	SDL-devel
BuildRequires:	curl-devel
BuildRequires:	zlib-devel
BuildRequires:	ncurses-devel
BuildRequires:	glew-devel
BuildRequires:	mesaglu-devel
BuildRequires:	c-ares-devel
BuildConflicts:	freetds-devel
Epoch:		1

%description
BZFlag is a multiplayer 3D tank battle game. It's one of the most popular games
ever on Silicon Graphics systems.

%prep
%setup -q
%patch0 -p1 -b .lookup

%build
%configure2_5x --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir} --enable-robots
%make CXXFLAGS="$RPM_OPT_FLAGS -O1 -ffast-math -fno-exceptions -fsigned-char"

%install
%{makeinstall_std}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=BZflag
Comment=A multiplayer 3D tank battle game
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

%files
%doc README BUGS
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_mandir}/*/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
