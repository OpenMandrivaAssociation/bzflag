Name:		bzflag
Summary:	A multiplayer 3D tank battle game
Version:	2.4.2
Release:	1
Epoch:		1
License:	LGPLv2
Group:		Games/Arcade
URL:		http://BZFlag.SourceForge.net/
Source0:	http://download.sourceforge.net/bzflag/%{name}-%{version}.tar.bz2
Patch0:		bzflag-2.0.4-lookup.patch
Patch1:		bzflag-2.0.12-findresolutions.patch
Source11:	%{name}.16.png
Source12:	%{name}.32.png
Source13:	%{name}.48.png
BuildRequires:	chrpath
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	zlib-devel
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libcares)
BuildRequires:	openldap-devel
BuildRequires:	desktop-file-utils
BuildConflicts:	freetds-devel

%description
BZFlag is a multiplayer 3D tank battle game. It's one of the most popular games
ever on Silicon Graphics systems.

%prep
%setup -q
%patch0 -p1 -b .lookup
%patch1 -p1 -b .resolutions

%build
CFLAGS="%{optflags} -O3 -ffast-math" \
CXXFLAGS="$CFLAGS" \
%configure2_5x	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir} \
		--enable-robots \
		--disable-static \
		--enable-ldaps \
		--with-gssapi \
		--enable-manual \
		--enable-ares \
		--libdir=%{_libdir}/%{name}
%make

%install
%makeinstall_std
# ugly but gets it done..
for file in %{buildroot}{%{_gamesbindir}/*,%{_libdir}/%{name}/*.so}; do
    chrpath -d $file
done
rm -f %{buildroot}%{_libdir}/%{name}/*la

cp -a misc/maps/ %{buildroot}%{_gamesdatadir}/%{name}/
install -d %{buildroot}{%{_datadir}/applications,%{_iconsdir}}
desktop-file-install	--dir %{buildroot}%{_datadir}/applications \
			%{buildroot}%{_gamesdatadir}/%{name}/bzflag.desktop
cp %{buildroot}%{_gamesdatadir}/%{name}/bzflag-48x48.png %{buildroot}%{_iconsdir}

%files
%doc README BUGS
%{_gamesbindir}/*
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so
%{_mandir}/*/*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{name}-48x48.png


