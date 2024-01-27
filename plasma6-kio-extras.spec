%define major %(echo %{version} |cut -d. -f1)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)

Name: plasma6-kio-extras
Version:	24.01.90
Release:	1
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/kio-extras-%{version}.tar.xz
Source1000: %{name}.rpmlintrc
# https://bugzilla.samba.org/show_bug.cgi?id=12466
Patch1: kio-extras-smb_anon.patch
Summary: KDE 6 I/O Extras
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: gperf
BuildRequires: openslp-devel
BuildRequires: pkgconfig(exiv2)
BuildRequires: pkgconfig(libmtp)
BuildRequires: pkgconfig(libtirpc)
BuildRequires: pkgconfig(OpenEXR)
BuildRequires: pkgconfig(phonon4qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(QCoro6)
BuildRequires: pkgconfig(shared-mime-info)
BuildRequires: pkgconfig(libssh) >= 0.8.6
BuildRequires: pkgconfig(smbclient)
BuildRequires: pkgconfig(taglib)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libimobiledevice-1.0)
BuildRequires: pkgconfig(libplist-2.0)
BuildRequires: pkgconfig(libappimage)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6DNSSD)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6Pty)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(PlasmaActivities)
BuildRequires: cmake(KF6SyntaxHighlighting)
BuildRequires: cmake(PlasmaActivitiesStats)
BuildRequires: cmake(KExiv2Qt6)
BuildRequires: kdsoap-qt6-devel
# There's no point in a separate molletnetwork package.
# This is an internal library that doesn't even ship
# headers or a *.so file, so nothing outside of this
# package can actually depend on it. There is never
# a need for a compat package.
# Kill it.
Obsoletes: %{mklibname molletnetwork6 21} < %{EVRD}
Obsoletes: %{mklibname molletnetwork6 20} < %{EVRD}
Obsoletes: %{mklibname molletnetwork6 19} < %{EVRD}
Obsoletes: %{mklibname molletnetwork6 18} < %{EVRD}
Obsoletes: %{mklibname molletnetwork6 17} < %{EVRD}
Requires: %{mklibname kioarchive} = %{EVRD}
Requires: kio
%rename kio-mtp
%rename kfileaudiopreview
%define kioarchive_devel %{mklibname -d kioarchive}

%libpackage kioarchive 6

%description
KDE 6 I/O Extras.

%package -n %{kioarchive_devel}
Summary: Development files for the KIO Archive library
Group: Development/KDE and Qt
Requires: %{mklibname kioarchive} = %{EVRD}

%description -n %{kioarchive_devel}
Development files for the KIO Archive library

%prep
%autosetup -n kio-extras-%{plasmaver} -p1

%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang all --all-name --with-html

%files -f all.lang
%{_datadir}/qlogging-categories6/kio-extras.categories
%{_libdir}/qt6/plugins/*.so
%{_libdir}/qt6/plugins/kf6/kio/*.so
%{_libdir}/qt6/plugins/kf6/kiod/*.so
%{_libdir}/qt6/plugins/kf6/kded/*.so
%{_libdir}/qt6/plugins/kf6/thumbcreator
%{_datadir}/mime/packages/org.kde.kio.smb.xml
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/dbus-1/services/*.service
%{_datadir}/remoteview
%{_datadir}/kio_bookmarks
%{_datadir}/kio_docfilter
%{_datadir}/kio_info
%{_datadir}/konqueror/dirtree/remote/*.desktop
%{_datadir}/kservices6/*.desktop
%{_datadir}/kservicetypes6/*.desktop
%{_datadir}/solid/actions/solid_mtp.desktop
%{_datadir}/solid/actions/solid_afc.desktop
%{_datadir}/qlogging-categories6/kio-extras.renamecategories
%{_libdir}/qt6/plugins/kf6/kfileitemaction/kactivitymanagerd_fileitem_linking_plugin.so
%{_libdir}/qt6/plugins/kf6/kfileitemaction/forgetfileitemaction.so
%{_libdir}/libexec/kf6/smbnotifier

%files -n %{kioarchive_devel}
%{_includedir}/KioArchive
%{_libdir}/cmake/KioArchive
