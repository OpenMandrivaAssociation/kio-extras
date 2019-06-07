%define major %(echo %{version} |cut -d. -f1)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)

Name: kio-extras
Version: 19.04.2
Release: 1
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
Source1000: %{name}.rpmlintrc
Patch0: kio-extras-5.1.0.1-link-tirpc-for-nfs.patch
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

Requires: %{mklibname molletnetwork5 %{major}} = %{EVRD}
Obsoletes: %{mklibname molletnetwork5 18} < %{EVRD}
Obsoletes: %{mklibname molletnetwork5 17} < %{EVRD}
Requires: %{mklibname kioarchive 5} = %{EVRD}

%define kioarchive_devel %{mklibname -d kioarchive}

%libpackage molletnetwork5 %{major}
%libpackage kioarchive 5

%description
KDE 5 I/O Extras.

%package -n %{kioarchive_devel}
Summary: Development files for the KIO Archive library
Group: Development/KDE and Qt
Requires: %{mklibname kioarchive 5} = %{EVRD}

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
%{_sysconfdir}/xdg/kio-extras.categories
%{_libdir}/qt5/plugins/*.so
%{_libdir}/qt5/plugins/kf5/kio/*.so
%{_libdir}/qt5/plugins/kf5/kiod/*.so
%{_libdir}/qt5/plugins/kf5/kded/*.so
%{_libdir}/qt5/plugins/kf5/parts/*.so
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/services/*.service
%{_datadir}/mime/packages/kf5_network.xml
%{_datadir}/remoteview
%{_datadir}/kio_bookmarks
%{_datadir}/kio_docfilter
%{_datadir}/kio_info
%{_datadir}/konqsidebartng/virtual_folders/remote/*.desktop
%{_datadir}/konqueror/dirtree/remote/*.desktop
%{_datadir}/kservices5/*.desktop
%{_datadir}/kservices5/*.protocol
%{_datadir}/kservicetypes5/*.desktop
%{_datadir}/solid/actions/solid_mtp.desktop

%files -n %{kioarchive_devel}
%{_includedir}/KF5/*
%{_libdir}/cmake/KioArchive
