%define req_gimp_version 2.2
%define pkgname gimp-gap

Summary:	GAP (GIMP Animation Package), a video plug-in for GIMP
Name:		gimp2-gap
Version:	2.6.0
Release:	5
License:	GPLv2+
Group:		Graphics
URL:		http://gimp.org

Source0:	ftp://ftp.gimp.org/pub/gimp/plug-ins/v2.6/gap/%pkgname-%{version}.tar.bz2
Patch2:		gimp-gap-2.6.0-libmpeg3-format-strings.patch
Patch3:		gimp-gap-2.6.0-format-strings.patch
Patch4:		gimp-gap-2.6.0-fix-linking.patch
BuildRequires:	intltool >= 0.17
BuildRequires:	glib-gettextize
BuildRequires:	gimp-devel >= %{req_gimp_version}
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
%patch4 -p1

autoreconf -fi

%build
%define _disable_ld_no_undefined 1
%configure2_5x
make

%install
%makeinstall libexecdir=%buildroot%_libexecdir/gimp/2.0/plug-ins scriptdatadir=%buildroot%_datadir/gimp/2.0/scripts
#gw the makefile is broken, move the file by hand
mkdir -p %buildroot%_libexecdir/gimp-gap-2.0
mv %buildroot%_libexecdir/gimp/2.0/plug-ins/audioconvert_to_wav.sh %buildroot%_libexecdir/gimp-gap-2.0
rm -f %buildroot%_datadir/gimp/2.0/scripts/*.a
%define gettext_package gimp20-gap
%{find_lang} %{gettext_package}

%files -f %{gettext_package}.lang
%doc AUTHORS ChangeLog* README
%{_libdir}/gimp/2.0/plug-ins/*
%{_libdir}/gimp-gap-2.0
%{_datadir}/gimp/2.0/scripts/*




%changelog
* Tue Dec 06 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.6.0-4mdv2012.0
+ Revision: 738276
- fix linking
- yearly rebuild

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.6.0-3mdv2011.0
+ Revision: 610854
- rebuild

* Sun Aug 16 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.6.0-2mdv2010.0
+ Revision: 416906
- rebuild for new libjpeg

* Thu Jul 09 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.6.0-1mdv2010.0
+ Revision: 393927
- new version
- update license
- update source URL
- drop patch 0
- fix format strings

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.4.0-3mdv2009.0
+ Revision: 246156
- rebuild

* Mon Feb 04 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.4.0-1mdv2008.1
+ Revision: 162471
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.2.2-1mdv2008.0
+ Revision: 72689
- new version


* Thu Jan 11 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.2.1-1mdv2007.0
+ Revision: 107537
- Import gimp2-gap

* Thu Jan 11 2007 Götz Waschk <waschk@mandriva.org> 2.2.1-1mdv2007.1
- unpack patch
- New version 2.2.1

* Wed May 31 2006 Götz Waschk <waschk@mandriva.org> 2.2.0-3mdv2007.0
- fix build on x86_64

* Tue May 30 2006 Götz Waschk <waschk@mandriva.org> 2.2.0-2mdv2007.0
- fix buildrequires

* Mon May 29 2006 Götz Waschk <waschk@mandriva.org> 2.2.0-1mdv2007.0
- new version

* Thu May 26 2005 Götz Waschk <waschk@mandriva.org> 2.0.2-3mdk
- Rebuild

* Sat May 22 2004 Götz Waschk <waschk@linux-mandrake.com> 2.0.2-2mdk
- improve description

* Sat May 22 2004 Götz Waschk <waschk@linux-mandrake.com> 2.0.2-1mdk
- fix URLs
- New release 2.0.2

* Thu Apr 15 2004 Götz Waschk <waschk@linux-mandrake.com> 2.0.0-1mdk
- new version

* Fri Mar 26 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.0-0.1pre1_mdk
- new release

* Thu Mar 25 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.3.25-3mdk
- rebuild for gimp2

* Wed Feb 11 2004 Götz Waschk <waschk@linux-mandrake.com> 1.3.25-2mdk
- rebuild

* Sat Jan 31 2004 Götz Waschk <waschk@linux-mandrake.com> 1.3.25-1mdk
- fix installation
- drop patch
- new version

