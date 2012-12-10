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
BuildRequires:	glew-devel
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



%changelog
* Tue Sep 13 2011 Paulo Andrade <pcpa@mandriva.com.br> 1:2.4.0-2
+ Revision: 699654
- Remove hardcoded libdir runpath from binaries

* Fri Sep 09 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:2.4.0-1
+ Revision: 699158
- ship with example maps
- use 'desktop-file-install' to install .desktop file in stead
- update to latest version
- clean out obsolete junk

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1:2.0.16-4
+ Revision: 663344
- mass rebuild

* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 1:2.0.16-3
+ Revision: 635012
- rebuild
- tighten BR

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1:2.0.16-2mdv2011.0
+ Revision: 603775
- rebuild

* Sat Apr 24 2010 Emmanuel Andry <eandry@mandriva.org> 1:2.0.16-1mdv2010.1
+ Revision: 538499
- New version 2.0.16

* Fri Feb 19 2010 Frederik Himpe <fhimpe@mandriva.org> 1:2.0.14-1mdv2010.1
+ Revision: 508491
- Update to new version 2.0.14
- Remove gcc 4.3 patch integrated upstream

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1:2.0.12-2mdv2010.0
+ Revision: 413189
- rebuild

* Thu Jun 26 2008 Funda Wang <fwang@mandriva.org> 1:2.0.12-1mdv2009.0
+ Revision: 229211
- New version 2.0.12

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri May 30 2008 Funda Wang <fwang@mandriva.org> 1:2.0.10-2mdv2009.0
+ Revision: 213232
- add fedora patches

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Jérôme Soyer <saispo@mandriva.org> 1:2.0.10-1mdv2008.1
+ Revision: 109289
- New release 2.0.10

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Fri Jun 01 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:2.0.8-7mdv2008.0
+ Revision: 34340
- Rebuild with libslang2.

* Sun May 27 2007 Funda Wang <fwang@mandriva.org> 1:2.0.8-6mdv2008.0
+ Revision: 31710
- Rebuild against directfb 1.0


* Fri Feb 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.0.8-5mdv2007.0
+ Revision: 125208
- rebuild against new libgii

* Tue Jan 16 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:2.0.8-4mdv2007.1
+ Revision: 109480
- Rebuild against new curl
- Import bzflag

* Sun Sep 17 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.0.8-3mdv2007.0
- compile with -O1 to have shots fired actually hit stuff too

* Sun Sep 17 2006 Emmanuel Andry <eandry@mandriva.org> 2.0.8-2mdv2007.0
- xdg menu
- fix buildrequires
- add missing buildrequires SDL-devel SDL_image-devel

* Wed May 17 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.0.8-1mdk
- 2.0.8
- drop devel package

* Sat May 13 2006 Stefan van der Eijk <stefan@eijk.nu> 1:2.0.4-4mdk
- rebuild for sparc

* Tue Mar 14 2006 Erwan Velu <erwan@seanodes.com> 2.0.4-3mdk
- Fixing build requires

* Tue Mar 14 2006 Erwan Velu <erwan@seanodes.com> 2.0.4-2mdk
- Fixing description

* Tue Mar 14 2006 Erwan Velu <erwan@seanodes.com> 2.0.4-1mdk
- 2.0.4
- Enable robot
- Adding devel files

* Fri Nov 18 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.2-3mdk
- rebuilt against openssl-0.9.8a

* Sun Jul 31 2005 Guillaume Bedot <littletux@mandriva.org> 1:2.0.2-2mdk
- rebuild
- Patch0: allows to build with new gcc

* Sat Apr 30 2005 Lenny Cartier <lenny@mandriva.com> 2.0.2-1mdk
- from Emmanuel Andry <eandry@free.fr> : 
	- 2.0.2 "Queen of Maybe"

* Wed Jan 19 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.0.0-1mdk
- 2.0.0 "Falcor's Despair"
- update compile flags

* Tue Dec 14 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.10.8-1mdk
- 1.10.8
- drop Packager tag

* Tue Aug 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.10.6-3mdk
- Rebuild with new menu

* Mon Jun 07 2004 Michael Scherer <misc@mandrake.org> 1.10.6-2mdk 
- rebuild for new gcc

* Fri May 21 2004 Michael Scherer <misc@mandrake.org> 1.10.6-1mdk
- New release 1.10.6

