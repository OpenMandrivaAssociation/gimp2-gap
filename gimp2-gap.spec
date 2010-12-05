%define version 2.6.0
%define release %mkrel 3

%define req_gimp_version 2.2

%define pkgname gimp-gap

Summary:	GAP (GIMP Animation Package), a video plug-in for GIMP
Name:		gimp2-gap
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Graphics
URL:		http://gimp.org
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Source:		ftp://ftp.gimp.org/pub/gimp/plug-ins/v2.6/gap/%pkgname-%{version}.tar.bz2
Patch2:		gimp-gap-2.6.0-libmpeg3-format-strings.patch
Patch3:		gimp-gap-2.6.0-format-strings.patch
BuildRequires:	intltool >= 0.17
BuildRequires:	glib-gettextize
BuildRequires:	libgimp-devel >= %{req_gimp_version}
BuildRequires:	libjpeg-devel

Requires:	gimp >= %{req_gimp_version}
Requires:	wavplay

%description
The GIMP has some plug-ins supporting animation features based on
layers, with each layer of the image being considered as one frame of
the animation.

GAP is a collection of plug-ins that extend the GIMP's animation
capabilities by supporting the creation of more complex animations. It
was part of the GIMP from 1.1.4 to the 1.2 series, but was split
afterwards.

Additional Informations about the GAP can be found in the GimpUserManual
Chapter Advanced Animation.


%prep
%setup -q -n %pkgname-%{version}
cd extern_libs/
tar xzf libmpeg3.tar.gz
%patch2 -p0
cd ..
%patch3 -p1 -b .format-strings

%build
%define _disable_ld_no_undefined 1
%configure2_5x
make

%install
rm -rf %{buildroot}
%makeinstall libexecdir=%buildroot%_libexecdir/gimp/2.0/plug-ins scriptdatadir=%buildroot%_datadir/gimp/2.0/scripts
#gw the makefile is broken, move the file by hand
mkdir -p %buildroot%_libexecdir/gimp-gap-2.0
mv %buildroot%_libexecdir/gimp/2.0/plug-ins/audioconvert_to_wav.sh %buildroot%_libexecdir/gimp-gap-2.0
rm -f %buildroot%_datadir/gimp/2.0/scripts/*.a
%define gettext_package gimp20-gap
%{find_lang} %{gettext_package}

%clean
rm -rf %{buildroot}

%files -f %{gettext_package}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog* README
%{_libdir}/gimp/2.0/plug-ins/*
%{_libdir}/gimp-gap-2.0
%{_datadir}/gimp/2.0/scripts/*


