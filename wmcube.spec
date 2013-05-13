%define version 0.98
%define release  15
%define name wmcube

Summary:  Realtime rotating 3d-object and CPU load in a small dock app
Name:		%name
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Monitoring
Source0:	%name-%{version}.tar.bz2
Source1:	%name-icons.tar.bz2
URL:		http://boombox.campus.luth.se/projects.php
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xpm)


%description
wmCube is a dockapp that displays a realtime rotating 3d-object 
and the current CPU load.


%prep
rm -rf %buildroot

%setup -q -n wmcube

%build
make -C wmcube -f Makefile.LINUX CFLAGS="$RPM_OPT_FLAGS"

%install
[ -d %buildroot ] && rm -rf %buildroot

install -m 755 -d %buildroot%{_miconsdir}
install -m 755 -d %buildroot%{_iconsdir}
install -m 755 -d %buildroot%{_liconsdir}
tar xOjf %SOURCE1 16x16.png > %buildroot%{_miconsdir}/%name.png
tar xOjf %SOURCE1 32x32.png > %buildroot%{_iconsdir}/%name.png
tar xOjf %SOURCE1 48x48.png > %buildroot%{_liconsdir}/%name.png

mkdir -p %buildroot%{_bindir}
install -m 755 wmcube/wmcube %buildroot%{_bindir}

mkdir -p %buildroot%{_datadir}/wmcube
install -m 644 3dObjects/* %buildroot%{_datadir}/wmcube


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=WmCube
Comment=%{summary}
Exec=%{_bindir}/%{name} -o %{_datadir}/%name/ball-solid.wmc
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-System-Monitoring;System;Monitor;
EOF


%clean
rm -rf %buildroot

%if %mdkversion < 200900
%post
%update_menus
%endif


%if %mdkversion < 200900
%postun
%clean_menus
%endif


%files
%defattr (-,root,root)
%doc CHANGES INSTALL README TODO
%{_bindir}/%name
%{_liconsdir}/%name.png
%{_miconsdir}/%name.png
%{_iconsdir}/%name.png
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/%name/*




%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.98-14mdv2010.0
+ Revision: 434780
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.98-13mdv2009.0
+ Revision: 262018
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.98-12mdv2009.0
+ Revision: 256131
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0.98-10mdv2008.1
+ Revision: 140932
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Tue Jan 30 2007 Gustavo De Nardin <gustavodn@mandriva.com> 0.98-10mdv2007.0
+ Revision: 115237
- fixed and stripped BuildRequires to minimum
- stopped using old "X prefix"
- added XDG menu for great compliance
- fixed menu section of old menu

* Thu Jan 18 2007 Lenny Cartier <lenny@mandriva.com> 0.98-9mdv2007.1
+ Revision: 110116
- Rebuild

* Thu Nov 23 2006 Lenny Cartier <lenny@mandriva.com> 0.98-8mdv2007.1
+ Revision: 86753
- User mkrel
- Import wmcube

* Thu Apr 21 2005 Lenny Cartier <lenny@mandriva.com> 0.98-7mdk
- rebuild

* Thu Feb 19 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.98-6mdk
- rebuild

