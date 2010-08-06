Name:          bluedevil
Summary:       BlueDevil is the new bluetooth stack for KDE4
Group:         Graphical desktop/KDE
Version:       0.1
Release:       %mkrel 2
License:       GPL
URL:           http://www.kde.org
Source0:       %name-%version.tar.bz2
BuildRequires: libbluedevil-devel
Provides:      bluez-pin
Requires:      bluez >= 4.28
Requires:      bluez-sdp
BuildRequires: kdelibs4-devel
Requires:      kdebase4-runtime
BuildRoot: %_tmppath/%name-%version-%release-root

%description 
BlueDevil is the new bluetooth stack for KDE, it's composed of: 
KCM, KDED, KIO, Library and some other small applications.

%files 
%defattr(-,root,root)
%{_kde_bindir}/*
%{_kde_libdir}/kde4/*
%{_kde_datadir}/kde4/services/*
%{_kde_datadir}/kde4/servicetypes/*
%{_kde_datadir}/applications/kde4/*
%{_kde_appsdir}/bluedevil
%{_kde_datadir}/mime/packages/bluedevil-mime.xml
%{_kde_datadir}/dbus-1/services/org.kde.BlueDevil.Service.service
%{_kde_libdir}/libbluedevilaction.so

#------------------------------------------------

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt

%description  devel
This package contains header files needed if you wish to build applications
based on %{name} .

%files devel
%defattr(-,root,root)
%{_kde_includedir}/actionplugin.h

#-----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%install
rm -rf %buildroot

%makeinstall_std -C build

%clean
rm -fr %buildroot
