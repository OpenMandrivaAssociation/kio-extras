%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)

Name: kio-extras
Version:	16.08.2
Release:	1
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
Source1000: %{name}.rpmlintrc
Patch0: kio-extras-5.1.0.1-link-tirpc-for-nfs.patch
Summary: KDE 5 I/O Extras
URL: http://kde.org/
License: GPL
Group: System/Libraries
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
BuildRequires: pkgconfig(libssh) >= 0.6.0
BuildRequires: pkgconfig(smbclient)
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

Requires: %{mklibname molletnetwork5 5} = %{EVRD}

%libpackage molletnetwork5 5

%description
KDE 5 I/O Extras.

%prep
%setup -qn %{name}-%{plasmaver}
%apply_patches

%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_libdir}/qt5/plugins/*.so
%{_libdir}/qt5/plugins/kf5/kio/*.so
%{_libdir}/qt5/plugins/kf5/kded/*.so
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/dbus-1/interfaces/*.xml
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
%doc %{_docdir}/HTML/*/kioslave5
%doc %{_docdir}/HTML/*/kcontrol/trash
