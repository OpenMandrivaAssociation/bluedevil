Summary:	BlueDevil is the new bluetooth stack for KDE4
Name:		bluedevil
Version:	1.2.4
Release:	1
Group:		Graphical desktop/KDE
License:	GPL
Url:		https://projects.kde.org/projects/extragear/base/bluedevil
Source0:	http://fr2.rpmfind.net/linux/KDE/stable/%{name}/%{version}/src/%{name}-%{version}.tar.bz2
Source100:	%{name}.rpmlintrc

BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(bluedevil) >= 1.9
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
%{_kde_datadir}/kde4/servicetypes/*
%{_kde_datadir}/applications/kde4/*
%{_kde_appsdir}/bluedevil
%{_kde_appsdir}/bluedevilwizard
%{_kde_datadir}/mime/packages/bluedevil-mime.xml
%{_kde_datadir}/dbus-1/services/org.kde.BlueDevil.Service.service
%{_kde_libdir}/libbluedevilaction.so

#------------------------------------------------

%package	devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt

%description	devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files		devel
%{_kde_includedir}/actionplugin.h

#-----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name}

%changelog
* Sat Jun 09 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.2.3-2
+ Revision: 803803
- Fix build in current environment

* Tue May 01 2012 Andrey Bondrov <abondrov@mandriva.org> 1.2.3-1
+ Revision: 794737
- New version 1.2.3, don't use sed for desktop files (fixed upstream)

* Wed Nov 23 2011 Andrey Bondrov <abondrov@mandriva.org> 1.2.2-1
+ Revision: 732779
- New version 1.2.2

* Tue Oct 04 2011 Александр Казанцев <kazancas@mandriva.org> 1.2.1-1
+ Revision: 702863
- fix categories for desktop files network-dun and network-panu
- version 1.2.1
- do not requires bluez-sdp, as it was merged with bluez, already required
- bluedevil 1.2.1 need libbluedevil 1.9

* Tue Apr 26 2011 Funda Wang <fwang@mandriva.org> 1.1-2
+ Revision: 659083
- add more runtime req as suggested by upstream

* Fri Apr 15 2011 Funda Wang <fwang@mandriva.org> 1.1-1
+ Revision: 653139
- new version 1.1

* Tue Apr 05 2011 Funda Wang <fwang@mandriva.org> 1.0.4-1
+ Revision: 650482
- update to new version 1.0.4

* Wed Mar 23 2011 Funda Wang <fwang@mandriva.org> 1.0.3-1
+ Revision: 647723
- new version 1.0.3

* Fri Feb 04 2011 Funda Wang <fwang@mandriva.org> 1.0.2-1
+ Revision: 635765
- New version 1.0.2

* Wed Dec 22 2010 John Balcaen <mikala@mandriva.org> 1.0.1-1mdv2011.0
+ Revision: 623850
- Update to 1.0.1
- add %%find_lang macro

* Sat Nov 20 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 1.0-1mdv2011.0
+ Revision: 599294
- v1.0 final

* Sun Oct 31 2010 John Balcaen <mikala@mandriva.org> 1.0-0.rc4.1.1mdv2011.0
+ Revision: 590948
- Update to rc4-1

* Thu Sep 16 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 1.0-0.rc4.1mdv2011.0
+ Revision: 579046
- update to 1.0-rc4; remove patch0

* Sun Sep 05 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.1-3mdv2011.0
+ Revision: 576104
- patch0: update to git tip a6447c57 to fix upstream bug #246968

  + Funda Wang <fwang@mandriva.org>
    - make it in build step first

* Fri Aug 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1-2mdv2011.0
+ Revision: 567180
- Fix Provides

* Fri Aug 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1-1mdv2011.0
+ Revision: 566511
- import bluedevil


