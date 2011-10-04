#specfile originally created for Fedora, modified for Moblin Linux
Summary: Imake source code configuration and build system
Name: imake
Version: 1.0.2
Release: 6
License: MIT/X11
Group: User Interface/X
URL: http://www.x.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0: ftp://ftp.x.org/pub/individual/util/imake-1.0.2.tar.bz2
Source1: ftp://ftp.x.org/pub/individual/util/makedepend-1.0.2.tar.bz2
Source2: ftp://ftp.x.org/pub/individual/util/gccmakedep-1.0.2.tar.bz2
Source3: ftp://ftp.x.org/pub/individual/util/xorg-cf-files-1.0.3.tar.bz2
Source4: ftp://ftp.x.org/pub/individual/util/lndir-1.0.1.tar.bz2
Patch0: xorg-cf-files-1.0.0-misc.patch
Patch1: xorg-cf-files-1.0.0-ProjectRoot.patch
Patch2: xorg-cf-files-1.0.2-redhat.patch
Patch3: xorg-cf-files-1.0.2-xprint.patch
Patch10: imake-1.0.2-find-pedantry.patch

BuildRequires: pkgconfig
BuildRequires: xorg-x11-util-macros
BuildRequires: pkgconfig(xproto)

Provides: ccmakedep cleanlinks gccmakedep lndir makedepend makeg
Provides: mergelib mkdirhier mkhtmlindex revpath xmkmf

%description
Imake is a deprecated source code configuration and build system which
has traditionally been supplied by and used to build the X Window System
in X11R6 and previous releases.  As of the X Window System X11R7 release,
the X Window system has switched to using GNU autotools as the primary
build system, and the Imake system is now deprecated, and should not be
used by new software projects.  Software developers are encouraged to
migrate software to the GNU autotools system.

%prep
%setup -q -c %{name}-%{version} -a1 -a2 -a3 -a4
#%patch0 -p0 -b .imake
#%patch1 -p0 -b .ProjectRoot
%patch2 -p0 -b .redhat
%patch3 -p0 -b .xprint
%patch10 -p0 -b .findpedantry

%build
# Build everything
{
   for pkg in imake makedepend gccmakedep lndir xorg-cf-files ; do
      pushd $pkg-*
      case $pkg in
         imake|xorg-cf-files)
            %configure --with-config-dir=%{_datadir}/X11/config
            ;;
         *)
            %configure
            ;;
      esac
      make
      popd
   done
}

%install
rm -rf $RPM_BUILD_ROOT

# Install everything
{
   for pkg in imake makedepend gccmakedep lndir xorg-cf-files ; do
      pushd $pkg-*
      case $pkg in
#         xorg-cf-files)
#            make install DESTDIR=$RPM_BUILD_ROOT libdir=%{_datadir}
#            ;;
         *)
            make install DESTDIR=$RPM_BUILD_ROOT
            ;;
      esac
      popd
   done
}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
%{_bindir}/ccmakedep
%{_bindir}/cleanlinks
%{_bindir}/gccmakedep
%{_bindir}/imake
%{_bindir}/lndir
%{_bindir}/makedepend
%{_bindir}/makeg
%{_bindir}/mergelib
%{_bindir}/mkdirhier
%{_bindir}/mkhtmlindex
%{_bindir}/revpath
%{_bindir}/xmkmf
%dir %{_datadir}/X11
%dir %{_datadir}/X11/config
%{_datadir}/X11/config/*.cf
%{_datadir}/X11/config/*.def
%{_datadir}/X11/config/*.rules
%{_datadir}/X11/config/*.tmpl
#%dir %{_mandir}/man1x
%doc %{_mandir}/man1/ccmakedep.1x*
%doc %{_mandir}/man1/cleanlinks.1x*
%doc %{_mandir}/man1/gccmakedep.1x*
%doc %{_mandir}/man1/imake.1x*
%doc %{_mandir}/man1/lndir.1x*
%doc %{_mandir}/man1/makedepend.1*
%doc %{_mandir}/man1/makeg.1x*
%doc %{_mandir}/man1/mergelib.1x*
%doc %{_mandir}/man1/mkdirhier.1x*
%doc %{_mandir}/man1/mkhtmlindex.1x*
%doc %{_mandir}/man1/revpath.1x*
%doc %{_mandir}/man1/xmkmf.1x*

