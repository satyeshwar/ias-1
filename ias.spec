#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ias
Version  : 4.0.14
Release  : 62
URL      : https://github.com/intel/ias/archive/4.0.14.tar.gz
Source0  : https://github.com/intel/ias/archive/4.0.14.tar.gz
Source1  : ias-setup.service
Source2  : ias-test-hmi.path
Source3  : ias-test-hmi.service
Source4  : ias.service
Summary  : Weston Compositor
Group    : Development/Tools
License  : CC-BY-SA-3.0 MIT
Requires: ias-autostart = %{version}-%{release}
Requires: ias-bin = %{version}-%{release}
Requires: ias-data = %{version}-%{release}
Requires: ias-lib = %{version}-%{release}
Requires: ias-libexec = %{version}-%{release}
Requires: ias-license = %{version}-%{release}
Requires: ias-man = %{version}-%{release}
Requires: ias-services = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : doxygen
BuildRequires : lcms2-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-xcb)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(glesv2)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libdrm_intel)
BuildRequires : pkgconfig(libinput)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(libva-drm)
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(mtdev)
BuildRequires : pkgconfig(pango)
BuildRequires : pkgconfig(pangocairo)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-cursor)
BuildRequires : pkgconfig(wayland-egl)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(wayland-scanner)
BuildRequires : pkgconfig(wayland-server)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xcb-composite)
BuildRequires : pkgconfig(xcb-shape)
BuildRequires : pkgconfig(xcb-xfixes)
BuildRequires : pkgconfig(xcb-xkb)
BuildRequires : pkgconfig(xcursor)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : sed
Patch1: 0001-add-example-ias-setup-script.patch

%description
Weston compositor

%package autostart
Summary: autostart components for the ias package.
Group: Default

%description autostart
autostart components for the ias package.


%package bin
Summary: bin components for the ias package.
Group: Binaries
Requires: ias-data = %{version}-%{release}
Requires: ias-libexec = %{version}-%{release}
Requires: ias-license = %{version}-%{release}
Requires: ias-man = %{version}-%{release}
Requires: ias-services = %{version}-%{release}

%description bin
bin components for the ias package.


%package data
Summary: data components for the ias package.
Group: Data

%description data
data components for the ias package.


%package dev
Summary: dev components for the ias package.
Group: Development
Requires: ias-lib = %{version}-%{release}
Requires: ias-bin = %{version}-%{release}
Requires: ias-data = %{version}-%{release}
Provides: ias-devel = %{version}-%{release}

%description dev
dev components for the ias package.


%package doc
Summary: doc components for the ias package.
Group: Documentation
Requires: ias-man = %{version}-%{release}

%description doc
doc components for the ias package.


%package lib
Summary: lib components for the ias package.
Group: Libraries
Requires: ias-data = %{version}-%{release}
Requires: ias-libexec = %{version}-%{release}
Requires: ias-license = %{version}-%{release}

%description lib
lib components for the ias package.


%package libexec
Summary: libexec components for the ias package.
Group: Default
Requires: ias-license = %{version}-%{release}

%description libexec
libexec components for the ias package.


%package license
Summary: license components for the ias package.
Group: Default

%description license
license components for the ias package.


%package man
Summary: man components for the ias package.
Group: Default

%description man
man components for the ias package.


%package services
Summary: services components for the ias package.
Group: Systemd services

%description services
services components for the ias package.


%prep
%setup -q -n ias-4.0.14
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547599758
%autogen --disable-static --disable-setuid-install \
--enable-ias-shell \
--disable-xkbcommon \
--enable-simple-clients \
--enable-clients \
--disable-wayland-compositor \
--disable-libunwind \
--disable-xwayland \
--disable-xwayland-test \
--disable-x11-compositor \
--disable-rpi-compositor \
--enable-ivi-plugin-manager \
--enable-layer-manager-control \
--enable-tracing \
--enable-shadergen \
--enable-demo-clients-install \
--enable-vm \
--enable-vmdisplay
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
:

%install
export SOURCE_DATE_EPOCH=1547599758
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ias
cp COPYING %{buildroot}/usr/share/package-licenses/ias/COPYING
cp data/COPYING %{buildroot}/usr/share/package-licenses/ias/data_COPYING
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/ias-setup.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/ias-test-hmi.path
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system/ias-test-hmi.service
install -m 0644 %{SOURCE4} %{buildroot}/usr/lib/systemd/system/ias.service
## install_append content
mkdir -p %{buildroot}/usr/share/xdg/weston/
install -m 0644 weston.ini.in %{buildroot}/usr/share/xdg/weston/weston.ini
install -m 0644 ias.conf.example %{buildroot}/usr/share/xdg/weston/ias.conf
mkdir -p %{buildroot}/usr/lib/systemd/system/ias.service.wants
mkdir -p %{buildroot}/usr/lib/systemd/system/basic.target.wants
ln -s ../ias-test-hmi.path %{buildroot}/usr/lib/systemd/system/ias.service.wants/ias-test-hmi.path
ln -s ../ias-setup.service %{buildroot}/usr/lib/systemd/system/basic.target.wants/ias-setup.service
install -m 0550 ias-setup %{buildroot}/usr/bin/ias-setup
mv %{buildroot}/usr/lib64/pkgconfig/libweston-4.pc %{buildroot}/usr/lib64/pkgconfig/libias-4.pc
mv %{buildroot}/usr/lib64/pkgconfig/libweston-desktop-4.pc %{buildroot}/usr/lib64/pkgconfig/libias-desktop-4.pc
mv %{buildroot}/usr/lib64/pkgconfig/weston.pc %{buildroot}/usr/lib64/pkgconfig/ias.pc
mv %{buildroot}/usr/include/weston %{buildroot}/usr/include/ias
mv %{buildroot}/usr/share/man/man5/weston.ini.5 %{buildroot}/usr/share/man/man5/ias.ini.5
mv %{buildroot}/usr/share/man/man7/weston-drm.7 %{buildroot}/usr/share/man/man7/ias-weston-drm.7
mv %{buildroot}/usr/share/man/man1/weston.1 %{buildroot}/usr/share/man/man1/ias-weston.1
rm %{buildroot}/usr/libexec/weston*
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/basic.target.wants/ias-setup.service

%files bin
%defattr(-,root,root,-)
/usr/bin/ias-setup
/usr/bin/ias-weston
/usr/bin/ias-weston-launch

%files data
%defattr(-,root,root,-)
/usr/share/ias/background.png
/usr/share/ias/border.png
/usr/share/ias/examples/eglinfo
/usr/share/ias/examples/extension_test_client
/usr/share/ias/examples/inputctrl
/usr/share/ias/examples/layoutctrl
/usr/share/ias/examples/surfctrl
/usr/share/ias/examples/traceinfo
/usr/share/ias/examples/wcap-decode
/usr/share/ias/examples/weston-calibrator
/usr/share/ias/examples/weston-clickdot
/usr/share/ias/examples/weston-cliptest
/usr/share/ias/examples/weston-confine
/usr/share/ias/examples/weston-dnd
/usr/share/ias/examples/weston-editor
/usr/share/ias/examples/weston-es2gears
/usr/share/ias/examples/weston-eventdemo
/usr/share/ias/examples/weston-flower
/usr/share/ias/examples/weston-fullscreen
/usr/share/ias/examples/weston-image
/usr/share/ias/examples/weston-info
/usr/share/ias/examples/weston-multi-resource
/usr/share/ias/examples/weston-presentation-shm
/usr/share/ias/examples/weston-resizor
/usr/share/ias/examples/weston-scaler
/usr/share/ias/examples/weston-simple-clock
/usr/share/ias/examples/weston-simple-damage
/usr/share/ias/examples/weston-simple-dmabuf-drm
/usr/share/ias/examples/weston-simple-dmabuf-v4l
/usr/share/ias/examples/weston-simple-egl
/usr/share/ias/examples/weston-simple-egl-ms
/usr/share/ias/examples/weston-simple-shm
/usr/share/ias/examples/weston-simple-touch
/usr/share/ias/examples/weston-smoke
/usr/share/ias/examples/weston-stacking
/usr/share/ias/examples/weston-subsurfaces
/usr/share/ias/examples/weston-terminal
/usr/share/ias/examples/weston-transformed
/usr/share/ias/examples/wrandr
/usr/share/ias/fullscreen.png
/usr/share/ias/home.png
/usr/share/ias/icon_editor.png
/usr/share/ias/icon_flower.png
/usr/share/ias/icon_ivi_clickdot.png
/usr/share/ias/icon_ivi_flower.png
/usr/share/ias/icon_ivi_simple-egl.png
/usr/share/ias/icon_ivi_simple-shm.png
/usr/share/ias/icon_ivi_smoke.png
/usr/share/ias/icon_terminal.png
/usr/share/ias/icon_window.png
/usr/share/ias/intel.png
/usr/share/ias/panel.png
/usr/share/ias/pattern.png
/usr/share/ias/random.png
/usr/share/ias/sidebyside.png
/usr/share/ias/sign_close.png
/usr/share/ias/sign_maximize.png
/usr/share/ias/sign_minimize.png
/usr/share/ias/terminal.png
/usr/share/ias/tiling.png
/usr/share/ias/wayland.png
/usr/share/ias/wayland.svg
/usr/share/wayland-sessions/ias-weston.desktop
/usr/share/xdg/weston/ias.conf
/usr/share/xdg/weston/weston.ini

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/ias/ivi-layout-export.h
/usr/include/ias/weston.h
/usr/include/libias-4/compositor-drm.h
/usr/include/libias-4/compositor-fbdev.h
/usr/include/libias-4/compositor-headless.h
/usr/include/libias-4/compositor-ias.h
/usr/include/libias-4/compositor-rdp.h
/usr/include/libias-4/compositor-wayland.h
/usr/include/libias-4/compositor-x11.h
/usr/include/libias-4/compositor.h
/usr/include/libias-4/config-parser.h
/usr/include/libias-4/ias-common.h
/usr/include/libias-4/ias-plugin-framework-definitions.h
/usr/include/libias-4/ias-spug.h
/usr/include/libias-4/libweston-desktop.h
/usr/include/libias-4/matrix.h
/usr/include/libias-4/platform.h
/usr/include/libias-4/plugin-registry.h
/usr/include/libias-4/timeline-object.h
/usr/include/libias-4/version.h
/usr/include/libias-4/weston-egl-ext.h
/usr/include/libias-4/windowed-output-api.h
/usr/include/libias-4/zalloc.h
/usr/lib64/libias-4.so
/usr/lib64/libias-desktop-4.so
/usr/lib64/pkgconfig/ias.pc
/usr/lib64/pkgconfig/libias-4.pc
/usr/lib64/pkgconfig/libias-desktop-4.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/ias/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/ias/cms-static.so
/usr/lib64/ias/cpp_example.so
/usr/lib64/ias/cpp_example.so.0
/usr/lib64/ias/cpp_example.so.0.0.0
/usr/lib64/ias/desktop-shell.so
/usr/lib64/ias/extension_sample.so
/usr/lib64/ias/extension_sample.so.0
/usr/lib64/ias/extension_sample.so.0.0.0
/usr/lib64/ias/fullscreen-shell.so
/usr/lib64/ias/grid_layout.so
/usr/lib64/ias/grid_layout.so.0
/usr/lib64/ias/grid_layout.so.0.0.0
/usr/lib64/ias/hmi-controller.so
/usr/lib64/ias/ias-shell-protocol.so
/usr/lib64/ias/ias-shell.so
/usr/lib64/ias/ias_plugin_framework.so
/usr/lib64/ias/input.so
/usr/lib64/ias/input.so.0
/usr/lib64/ias/input.so.0.0.0
/usr/lib64/ias/ivi-shell.so
/usr/lib64/ias/ivi_plugin_framework.so
/usr/lib64/ias/libias_hmi.so
/usr/lib64/ias/libwl_base.so
/usr/lib64/ias/libwl_disp.so
/usr/lib64/ias/sprite_example.so
/usr/lib64/ias/sprite_example.so.0
/usr/lib64/ias/sprite_example.so.0.0.0
/usr/lib64/ias/surface_gbc_control.so
/usr/lib64/ias/surface_gbc_control.so.0
/usr/lib64/ias/surface_gbc_control.so.0.0.0
/usr/lib64/ias/thumbnail_layout.so
/usr/lib64/ias/thumbnail_layout.so.0
/usr/lib64/ias/thumbnail_layout.so.0.0.0
/usr/lib64/ias/trace-reporter.so
/usr/lib64/ias/vm-comm-network.so
/usr/lib64/libias-4.so.0
/usr/lib64/libias-4.so.0.0.2
/usr/lib64/libias-4/drm-backend.so
/usr/lib64/libias-4/fbdev-backend.so
/usr/lib64/libias-4/gl-renderer.so
/usr/lib64/libias-4/headless-backend.so
/usr/lib64/libias-4/ias-backend.so
/usr/lib64/libias-desktop-4.so.0
/usr/lib64/libias-desktop-4.so.0.0.2

%files libexec
%defattr(-,root,root,-)
/usr/libexec/ias-test-hmi
/usr/libexec/vmdisplay-input
/usr/libexec/vmdisplay-server
/usr/libexec/vmdisplay-wayland

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ias/COPYING
/usr/share/package-licenses/ias/data_COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ias-weston.1
/usr/share/man/man5/ias.ini.5
/usr/share/man/man7/ias-weston-drm.7

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/basic.target.wants/ias-setup.service
/usr/lib/systemd/system/ias-setup.service
/usr/lib/systemd/system/ias-test-hmi.path
/usr/lib/systemd/system/ias-test-hmi.service
/usr/lib/systemd/system/ias.service
/usr/lib/systemd/system/ias.service.wants/ias-test-hmi.path
