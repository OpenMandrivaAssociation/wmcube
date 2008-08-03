%define version 0.98
%define release %mkrel 13
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
BuildRequires:	libxext-devel
BuildRequires:	libx11-devel
BuildRequires:	libxpm-devel
BuildRoot:	%{_tmppath}/%name-buildroot


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


