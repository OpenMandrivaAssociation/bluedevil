%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	The bluetooth stack for KDE 5
Name:		bluedevil
Version:	5.25.90
Release:	1
Group:		Graphical desktop/KDE
License:	GPL
Url:		https://projects.kde.org/projects/extragear/base/bluedevil
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/bluedevil-%{version}.tar.xz
Source100:	%{name}.rpmlintrc
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5BluezQt)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KDED)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	pkgconfig(shared-mime-info)
Provides:	bluez-pin
Requires:	bluez >= 4.28
Requires:	obexd
%rename bluedevil5

%description
BlueDevil is the new bluetooth stack for KDE, it's composed of:
KCM, KDED, KIO, Library and some other small applications.

%files -f %{name}.lang
%{_bindir}/*
%{_libdir}/qt5/plugins/kf5/kio/*.so
%{_datadir}/applications/*
%{_datadir}/bluedevilwizard
%{_datadir}/knotifications5/*
%{_datadir}/kservices5/*
%{_datadir}/mime/packages/bluedevil-mime.xml
%{_datadir}/metainfo/org.kde.plasma.bluetooth.appdata.xml

%{_datadir}/kpackage/kcms/kcm_bluetooth
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_bluetooth.so
%{_datadir}/qlogging-categories5/bluedevil.categories

%dir %{_libdir}/qt5/qml/org/kde/plasma/private/bluetooth
%{_libdir}/qt5/plugins/kf5/kded/*.so
%{_libdir}/qt5/qml/org/kde/plasma/private/bluetooth/libbluetoothplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/bluetooth/qmldir

%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.bluetooth
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.bluetooth/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.bluetooth/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.bluetooth/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/*.qml
%{_datadir}/remoteview/bluetooth-network.desktop

#-----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
