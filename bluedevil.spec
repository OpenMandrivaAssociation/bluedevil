Summary:	The new bluetooth stack for KDE4
Name:		bluedevil
Version:	2.1.1
Release:	1
Group:		Graphical desktop/KDE
License:	GPL
Url:		https://projects.kde.org/projects/extragear/base/bluedevil
Source0:	http://fr2.rpmfind.net/linux/KDE/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
Source100:	%{name}.rpmlintrc

BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(bluedevil) <= 2.1
Provides:	bluez-pin
Requires:	bluez >= 4.28
Requires:	kdebase4-runtime
Requires:	obexd

%description
BlueDevil is the new bluetooth stack for KDE, it's composed of:
KCM, KDED, KIO, Library and some other small applications.

%files -f %{name}.lang
%{_kde_bindir}/*
%{_kde_libdir}/kde4/*
%{_kde_datadir}/kde4/services/*
%{_kde_datadir}/applications/kde4/*
%{_kde_appsdir}/bluedevil
%{_kde_appsdir}/bluedevilwizard
%{_kde_datadir}/mime/packages/bluedevil-mime.xml

#------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name}

