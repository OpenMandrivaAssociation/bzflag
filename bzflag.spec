%define	name	bzflag
%define version 2.0.12
%define release %mkrel 1
%define	Summary	A multiplayer 3D tank battle game
%define libname %mklibname %{name} 2

Name:		%{name}
Summary:	%{Summary}
Version:	%{version}
Release:	%{release}
Source0:	http://download.sourceforge.net/bzflag/%{name}-%{version}.tar.bz2
Patch0: bzflag-2.0.4-lookup.patch
Patch1: bzflag-2.0.10-plugins.patch
Patch2: bzflag-2.0.10-gcc-4.3.patch
Source11:	%{name}.16.png
Source12:	%{name}.32.png
Source13:	%{name}.48.png
URL:		http://BZFlag.SourceForge.net/
License:	LGPLv2
Group:		Games/Arcade
BuildRequires:	mesa-common-devel X11-devel curl-devel zlib-devel
BuildRequires:	SDL-devel SDL_image-devel
BuildConflicts:	freetds-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Epoch:		1

%description
BZFlag is a multiplayer 3D tank battle game. It's one of the most popular games
ever on Silicon Graphics systems.

%prep
%setup -q
%patch0 -p1 -b .lookup
#%patch1 -p1 -b .plugins
%patch2 -p1 -b .gcc-4.3

%build
%configure2_5x --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir} --enable-robots
%make CXXFLAGS="$RPM_OPT_FLAGS -O1 -ffast-math -fno-exceptions -fsigned-char"

%install
rm -rf %{buildroot}
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

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README BUGS
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_mandir}/*/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
