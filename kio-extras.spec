%define major %(echo %{version} |cut -d. -f1)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)

Name: kio-extras
Version:	23.08.0
Release:	1
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Source1000: %{name}.rpmlintrc
# https://bugzilla.samba.org/show_bug.cgi?id=12456
Patch1: kio-extras-smb_anon.patch
Summary: KDE 5 I/O Extras
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: gperf
BuildRequires: openslp-devel
BuildRequires: pkgconfig(exiv2)
BuildRequires: pkgconfig(libmtp)
BuildRequires: pkgconfig(libtirpc)
BuildRequires: pkgconfig(OpenEXR)
BuildRequires: pkgconfig(phonon4qt5)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Sql)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(shared-mime-info)
BuildRequires: pkgconfig(libssh) >= 0.8.5
BuildRequires: pkgconfig(smbclient)
BuildRequires: pkgconfig(taglib)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libimobiledevice-1.0)
BuildRequires: pkgconfig(libplist-2.0)
BuildRequires: pkgconfig(libappimage)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5DNSSD)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5KHtml)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5Pty)
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5SyntaxHighlighting)
BuildRequires: cmake(KDSoap)
BuildRequires: cmake(KF5ActivitiesStats)
BuildRequires: cmake(KF5KExiv2)
# There's no point in a separate molletnetwork package.
# This is an internal library that doesn't even ship
# headers or a *.so file, so nothing outside of this
# package can actually depend on it. There is never
# a need for a compat package.
# Kill it.
Obsoletes: %{mklibname molletnetwork5 21} < %{EVRD}
Obsoletes: %{mklibname molletnetwork5 20} < %{EVRD}
Obsoletes: %{mklibname molletnetwork5 19} < %{EVRD}
Obsoletes: %{mklibname molletnetwork5 18} < %{EVRD}
Obsoletes: %{mklibname molletnetwork5 17} < %{EVRD}
Requires: %{mklibname kioarchive} = %{EVRD}
Requires: kio
%rename kio-mtp
%rename kfileaudiopreview
%define kioarchive_devel %{mklibname -d kioarchive}

%libpackage kioarchive 5

%description
KDE 5 I/O Extras.

%package -n %{kioarchive_devel}
Summary: Development files for the KIO Archive library
Group: Development/KDE and Qt
Requires: %{mklibname kioarchive} = %{EVRD}

%description -n %{kioarchive_devel}
Development files for the KIO Archive library

%prep
%autosetup -n %{name}-%{plasmaver} -p1

%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang all --all-name --with-html

%files -f all.lang
%{_datadir}/qlogging-categories5/kio-extras.categories
%{_libdir}/qt5/plugins/*.so
%{_libdir}/qt5/plugins/kf5/kio/*.so
%{_libdir}/qt5/plugins/kf5/kiod/*.so
%{_libdir}/qt5/plugins/kf5/kded/*.so
%{_libdir}/qt5/plugins/kf5/thumbcreator
%{_datadir}/mime/packages/org.kde.kio.smb.xml
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/dbus-1/services/*.service
%{_datadir}/remoteview
%{_datadir}/kio_bookmarks
%{_datadir}/kio_docfilter
%{_datadir}/kio_info
%{_datadir}/konqueror/dirtree/remote/*.desktop
%{_datadir}/kservices5/*.desktop
%{_datadir}/kservicetypes5/*.desktop
%{_datadir}/solid/actions/solid_mtp.desktop
%{_datadir}/solid/actions/solid_afc.desktop
%{_datadir}/qlogging-categories5/kio-extras.renamecategories
%{_libdir}/qt5/plugins/kf5/kfileitemaction/kactivitymanagerd_fileitem_linking_plugin.so
%{_libdir}/qt5/plugins/kf5/kfileitemaction/forgetfileitemaction.so
%{_libdir}/libexec/kf5/smbnotifier

%files -n %{kioarchive_devel}
%{_includedir}/KioArchive
%{_libdir}/cmake/KioArchive
