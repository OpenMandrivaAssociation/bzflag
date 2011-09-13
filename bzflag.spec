Name:		bzflag
Summary:	A multiplayer 3D tank battle game
Version:	2.4.0
Release:	2
Source0:	http://download.sourceforge.net/bzflag/%{name}-%{version}.tar.bz2
Patch0:		bzflag-2.0.4-lookup.patch
Source11:	%{name}.16.png
Source12:	%{name}.32.png
Source13:	%{name}.48.png
URL:		http://BZFlag.SourceForge.net/
License:	LGPLv2
Group:		Games/Arcade
BuildRequires:	chrpath
BuildRequires:	SDL-devel
BuildRequires:	curl-devel
BuildRequires:	zlib-devel
BuildRequires:	ncurses-devel
BuildRequires:	glew-devel
BuildRequires:	mesaglu-devel
BuildRequires:	c-ares-devel
BuildRequires:	openldap-devel
BuildRequires:	desktop-file-utils
BuildConflicts:	freetds-devel
Epoch:		1

%description
BZFlag is a multiplayer 3D tank battle game. It's one of the most popular games
ever on Silicon Graphics systems.

%prep
%setup -q
%patch0 -p1 -b .lookup

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

