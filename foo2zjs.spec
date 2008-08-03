Name:           foo2zjs
Version:        0.20070822
Release:        2%{?dist}
Summary:        Linux printer driver for ZjStream protocol

Group:          System Environment/Libraries
License:        GPL
URL:            http://foo2zjs.rkkda.com/
Source0:        http://foo2zjs.rkkda.com/foo2zjs.tar.gz
Patch0:         foo2zjs-dynamic-jbig.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  jbigkit-devel groff ghostscript
Requires:       lcms

%package -n foo2hp
Summary:        Linux printer driver for HP 1600, HP 2600n
Group:          System Environment/Libraries
Requires:       lcms foo2zjs

%package -n foo2xqx
Summary:        Linux printer driver for HP LaserJet M1005 MFP
Group:          System Environment/Libraries
Requires:       lcms foo2zjs

%package -n foo2lava
Summary:        Linux printer driver for Zenographics LAVAFLOW protocol
Group:          System Environment/Libraries
Requires:       lcms foo2zjs

%package -n foo2qpdl
Summary:        Linux printer driver for Samsung CLP-300, CLP-600, CLP-3160
Group:          System Environment/Libraries
Requires:       lcms foo2zjs

%description
foo2zjs is an open source printer driver for printers that use the
Zenographics ZjStream wire protocol for their print data, such as the
Minolta/QMS magicolor 2300 DL or Konica Minolta magicolor 2430
DL. These printers are often erroneously referred to as winprinters or
GDI printers. However, Microsoft GDI only mandates the API between an
application and the printer driver, not the protocol on the wire
between the printer driver and the printer. In fact, ZjStream printers
are raster printers which happen to use a very efficient wire protocol
which was developed by Zenographics and licensed by most major printer
manufacturers for at least some of their product lines. ZjStream is
just one of many wire protocols that are in use today, such as
Postscript, PCL, Epson, etc.

Users of this package are requested to visit the author's web page at
http://foo2zjs.rkkda.com/ and consider contributing.

%description -n foo2hp
foo2hp is an open source printer driver for printers that use the
Zenographics ZjStream wire protocol for their print data, such as the
HP Color LaserJet 2600n. These printers are often erroneously referred
to as winprinters or GDI printers. However, Microsoft GDI only
mandates the API between an application and the printer driver, not
the protocol on the wire between the printer driver and the
printer. In fact, ZjStream printers are raster printers which happen
to use a very efficient wire protocol which was developed by
Zenographics and licensed by most major printer manufacturers for at
least some of their product lines. ZjStream is just one of many wire
protocols that are in use today, such as Postscript, PCL, Epson, etc.

Users of this package are requested to visit the author's web page at
http://foo2hp.rkkda.com/ and consider contributing.

%description -n foo2xqx 
foo2xqx is an open source printer driver for printers that use the
HP/Software Imaging "XQX" stream wire protocol for their print data,
such as the HP LaserJet M1005 MFP. These printers are often
erroneously referred to as winprinters or GDI printers. However,
Microsoft GDI only mandates the API between an application and the
printer driver, not the protocol on the wire between the printer
driver and the printer. In fact, "XQX" printers are raster printers
which happen to use a very efficient wire protocol which was developed
by HP/Software Imaging. "XQX" is just one of many wire protocols that
are in use today, such as Postscript, PCL, Epson, ZjStream, etc.

Users of this package are requested to visit the author's web page at
http://foo2xqx.rkkda.com/ and consider contributing.

%description -n foo2lava
foo2lava is an open source printer driver for printers that use the
Zenographics LAVAFLOW wire protocol for their print data, such as the
Konica Minolta magicolor 2530 DL or the Konica Minolta magicolor 2490
MF. These printers are often erroneously referred to as winprinters or
GDI printers. However, Microsoft GDI only mandates the API between an
application and the printer driver, not the protocol on the wire
between the printer driver and the printer. In fact, LAVAFLOW printers
are raster printers which happen to use a very efficient wire protocol
which was developed by Zenographics and licensed by most major printer
manufacturers for at least some of their product lines. LAVAFLOW is
just one of many wire protocols that are in use today, such as
Postscript, PCL, Epson, ZjStream, etc.

Users of this package are requested to visit the author's web page at
http://foo2lava.rkkda.com/ and consider contributing.

%description -n foo2qpdl
foo2qpdl is an open source printer driver for printers that use the
QPDL wire protocol for their print data, such as the Samsung CLP-300
or the Samsung CLP-600 or the Xerox Phaser 6110. These printers are
often erroneously referred to as winprinters or GDI printers. However,
Microsoft GDI only mandates the API between an application and the
printer driver, not the protocol on the wire between the printer
driver and the printer. In fact, QPDL printers are raster printers
which happen to use a very efficient wire protocol. QPDL is just one
of many wire protocols that are in use today, such as Postscript, PCL,
Epson, ZjStream, etc.

Users of this package are requested to visit the author's web page at
http://foo2lava.rkkda.com/ and consider contributing.


%prep
%setup -q -n foo2zjs
%patch0 -p1
sed -i -e s/foo2zjs-icc2ps/icc2ps/g *wrapper*
sed -i -e s/775/755/ Makefile
chmod -x COPYING

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/foomatic/db/source/driver
mkdir -p $RPM_BUILD_ROOT%{_datadir}/foomatic/db/source/printer
mkdir -p $RPM_BUILD_ROOT%{_datadir}/foomatic/db/source/opt
mkdir -p $RPM_BUILD_ROOT%{_datadir}/cups/model

make PREFIX=$RPM_BUILD_ROOT%{_prefix} BINPROGS= install-prog \
     FOODB=$RPM_BUILD_ROOT%{_datadir}/foomatic/db/source \
     MODEL=$RPM_BUILD_ROOT/usr/share/cups/model \
     PPD=$RPM_BUILD_ROOT/usr/share/ppd \
     install-extra install-crd install-man install-foo install-ppd 


# Remove remnants of GPL-violating foo2oak stuff.
rm -f $RPM_BUILD_ROOT%{_bindir}/*oak*
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/*oak*.1
rm -f $RPM_BUILD_ROOT%{_datadir}/foomatic/db/source/opt/foo2oak*
rm -f $RPM_BUILD_ROOT%{_datadir}/foomatic/db/source/driver/foo2oak.xml
rm -f $RPM_BUILD_ROOT%{_datadir}/foomatic/db/source/printer/Generic-OAKT_Printer.xml
rm -f $RPM_BUILD_ROOT%{_datadir}/foomatic/db/source/printer/HP-Color_LaserJet_1500.xml
rm -f $RPM_BUILD_ROOT/usr/share/cups/model/Generic-OAKT_Printer.ppd.gz
rm -f $RPM_BUILD_ROOT/usr/share/cups/model/HP-Color_LaserJet_1500.ppd.gz



%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/*zjs*
%{_datadir}/foo2zjs
%{_mandir}/man1/*zjs*
%{_datadir}/foomatic/db/source/driver/foo2zjs.xml
%{_datadir}/foomatic/db/source/opt/foo2zjs*.xml
%{_datadir}/foomatic/db/source/printer/Generic-ZjStream_Printer.xml
%{_datadir}/foomatic/db/source/printer/HP-LaserJet_1000.xml
%{_datadir}/foomatic/db/source/printer/HP-LaserJet_1005.xml
%{_datadir}/foomatic/db/source/printer/HP-LaserJet_1018.xml
%{_datadir}/foomatic/db/source/printer/HP-LaserJet_1020.xml
%{_datadir}/foomatic/db/source/printer/HP-LaserJet_1022.xml
%{_datadir}/foomatic/db/source/printer/Minolta-Color_PageWorks_Pro_L.xml
%{_datadir}/foomatic/db/source/printer/Minolta-magicolor_2200_DL.xml
%{_datadir}/foomatic/db/source/printer/Minolta-magicolor_2300_DL.xml
%{_datadir}/foomatic/db/source/printer/Minolta-magicolor_2430_DL.xml
%{_datadir}/cups/model/Generic-ZjStream_Printer.ppd.gz
%{_datadir}/cups/model/HP-LaserJet_1000.ppd.gz
%{_datadir}/cups/model/HP-LaserJet_1005.ppd.gz
%{_datadir}/cups/model/HP-LaserJet_1018.ppd.gz
%{_datadir}/cups/model/HP-LaserJet_1020.ppd.gz
%{_datadir}/cups/model/HP-LaserJet_1022.ppd.gz
%{_datadir}/cups/model/Minolta-Color_PageWorks_Pro_L.ppd.gz
%{_datadir}/cups/model/Minolta-magicolor_2200_DL.ppd.gz
%{_datadir}/cups/model/Minolta-magicolor_2300_DL.ppd.gz
%{_datadir}/cups/model/Minolta-magicolor_2430_DL.ppd.gz

%files -n foo2hp
%{_bindir}/*hp*
%{_mandir}/man1/*hp*
%{_datadir}/foomatic/db/source/driver/foo2hp.xml
%{_datadir}/foomatic/db/source/opt/foo2hp*.xml
%{_datadir}/foomatic/db/source/printer/HP-Color_LaserJet_1600.xml
%{_datadir}/foomatic/db/source/printer/HP-Color_LaserJet_2600n.xml
%{_datadir}/cups/model/HP-Color_LaserJet_1600.ppd.gz
%{_datadir}/cups/model/HP-Color_LaserJet_2600n.ppd.gz

%files -n foo2xqx
%{_bindir}/*xqx*
%{_mandir}/man1/*xqx*
%{_datadir}/foomatic/db/source/driver/foo2xqx.xml
%{_datadir}/foomatic/db/source/opt/foo2xqx*.xml
%{_datadir}/foomatic/db/source/printer/HP-LaserJet_M1005_MFP.xml
%{_datadir}/cups/model/HP-LaserJet_M1005_MFP.ppd.gz

%files -n foo2lava
%{_bindir}/*lava*
%{_bindir}/opldecode
%{_mandir}/man1/*lava*
%{_mandir}/man1/opldecode.1.gz
%{_datadir}/foomatic/db/source/driver/foo2lava.xml
%{_datadir}/foomatic/db/source/opt/foo2lava*.xml
%{_datadir}/foomatic/db/source/printer/KonicaMinolta-magicolor_2480_MF.xml
%{_datadir}/foomatic/db/source/printer/KonicaMinolta-magicolor_2490_MF.xml
%{_datadir}/foomatic/db/source/printer/KonicaMinolta-magicolor_2530_DL.xml
%{_datadir}/cups/model/KonicaMinolta-magicolor_2480_MF.ppd.gz
%{_datadir}/cups/model/KonicaMinolta-magicolor_2490_MF.ppd.gz
%{_datadir}/cups/model/KonicaMinolta-magicolor_2530_DL.ppd.gz

%files -n foo2qpdl
%{_bindir}/*qpdl*
%{_mandir}/man1/*qpdl*
%{_datadir}/foomatic/db/source/driver/foo2qpdl.xml
%{_datadir}/foomatic/db/source/opt/foo2qpdl*.xml
%{_datadir}/foomatic/db/source/printer/Samsung-CL*.xml
%{_datadir}/foomatic/db/source/printer/Xerox-Phaser-611*.xml
%{_datadir}/cups/model/Samsung-CL*.ppd.gz
%{_datadir}/cups/model/Xerox-Phaser-611*.ppd.gz
%{_datadir}/foo2qpdl/crd/

%doc COPYING ChangeLog INSTALL README manual.pdf

%post
/bin/rm -f /var/cache/foomatic/*

%post -n foo2hp
/bin/rm -f /var/cache/foomatic/*

%post -n foo2xqx
/bin/rm -f /var/cache/foomatic/*

%post -n foo2lava
/bin/rm -f /var/cache/foomatic/*

%post -n foo2qpdl
/bin/rm -f /var/cache/foomatic/*

%changelog
* Sun Aug 03 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.20070822-2
- rebuild

* Wed Aug 29 2007 David Woodhouse <dwmw2@infradead.org> 0.20070822-1
- Update to 2007-08-22 release
- Add foo2qpdl subpackage
- Add %%post script to remove foomatic cache

* Mon Jan 29 2007 David Woodhouse <dwmw2@infradead.org> 0.20070128-1
- Update to 2007-01-28 release

* Mon Jan 29 2007 David Woodhouse <dwmw2@infradead.org> 0.20070127-1
- Update to 2007-01-27 release
- Add foo2xqx, foo2lava subpackages
- Include foomatic files which are now absent from Fedora foomatic

* Wed Sep 13 2006 David Woodhouse <dwmw2@infradead.org> 0.20060929-1
- Review fixes

* Wed Sep 13 2006 David Woodhouse <dwmw2@infradead.org> 0.20060911-1
- Initial build.
