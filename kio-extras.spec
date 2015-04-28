%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)

Name: kio-extras
Version: 5.2.95
Release: 1
Source0: ftp://ftp.kde.org/pub/kde/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
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
BuildRequires: ninja
Requires: %{mklibname molletnetwork 5} = %{EVRD}

%libpackage molletnetwork 5

%description
KDE 5 I/O Extras.

%prep
%setup -qn %{name}-%{plasmaver}
%apply_patches

%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}
%find_lang kfileaudiopreview5
%find_lang kio_archive
%find_lang kio_bookmarks
%find_lang kio_fish
%find_lang kio_info
%find_lang kio_man
%find_lang kio_mtp
%find_lang kio_nfs
%find_lang kio_recentdocuments
%find_lang kio_sftp
%find_lang kio_smb
%find_lang kio_thumbnail
cat *.lang >all.lang

%files -f all.lang
%{_libdir}/qt5/plugins/*.so
%{_libdir}/qt5/plugins/kf5/kio/*.so
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/mime/packages/kf5_network.xml
%{_datadir}/remoteview
%{_datadir}/kio_bookmarks
%{_datadir}/kio_desktop
%{_datadir}/kio_docfilter
%{_datadir}/kio_info
%{_datadir}/konqsidebartng/virtual_folders/remote/*.desktop
%{_datadir}/konqueror/dirtree/remote/*.desktop
%{_datadir}/kservices5/kded/*.desktop
%{_datadir}/kservices5/*.desktop
%{_datadir}/kservices5/*.protocol
%{_datadir}/kservicetypes5/*.desktop
%{_datadir}/solid/actions/solid_mtp.desktop
%doc %{_docdir}/HTML/*/kioslave5
%doc %{_docdir}/HTML/*/kcontrol/kcmcgi
%doc %{_docdir}/HTML/*/kcontrol/trash
