%define name	xournal
%define version	0.4.7
%define release 1

Name: 	 	%{name}
Summary: 	Pen-based journal and PDF annotator
Version: 	%{version}
Release: 	%{release}

Source0:	http://heanet.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
URL:		http://xournal.sourceforge.net/
License:	GPLv2
Group:		Office
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(libgnomecanvas-2.0)
BuildRequires:	libpoppler-glib-devel
# For pdftoppm: see http://forum.mandriva.com/viewtopic.php?t=92135
Requires:	poppler

%description
Xournal is an application for notetaking, sketching, keeping a journal using a
stylus.  It is similar to Microsoft Windows Journal or to other alternatives
such as Jarnal, Gournal, and NoteLab.

%prep
%setup -q

%build
./autogen.sh
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
%makeinstall

# menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Xournal
Comment=%summary
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;GTK;Office;
EOF

# icons
mkdir -p %{buildroot}%{_liconsdir}
convert -size 48x48 pixmaps/%{name}.png %{buildroot}/%{_liconsdir}/%{name}.png
mkdir -p %{buildroot}/%{_iconsdir}
convert -size 32x32 pixmaps/%{name}.png %{buildroot}/%{_iconsdir}/%{name}.png
mkdir -p %{buildroot}/%{_miconsdir}
convert -size 16x16 pixmaps/%{name}.png %{buildroot}/%{_miconsdir}/%{name}.png

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README html-doc/*
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png


%changelog
* Fri Jul 06 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.4.7-1
+ Revision: 808340
- version update 0.4.7

* Thu Dec 30 2010 Funda Wang <fwang@mandriva.org> 0.4.5-2mdv2011.0
+ Revision: 626170
- rebuild for new poppler

* Sun Nov 29 2009 Jérôme Brenier <incubusss@mandriva.org> 0.4.5-1mdv2011.0
+ Revision: 471383
- BuildRequires : libpoppler-glib-devel
- new version 0.4.5
- fix license tag
- cosmetic changes (specfile policy)

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 0.4.2.1-5mdv2010.0
+ Revision: 446262
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.4.2.1-4mdv2009.1
+ Revision: 350056
- 2009.1 rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Mon Aug 11 2008 Adam Williamson <awilliamson@mandriva.org> 0.4.2.1-3mdv2009.0
+ Revision: 270892
- requires poppler (for pdftoppm)

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 0.4.2.1-2mdv2009.0
+ Revision: 269806
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jun 11 2008 Austin Acton <austin@mandriva.org> 0.4.2.1-1mdv2009.0
+ Revision: 217827
- sync
- new version

* Mon Mar 03 2008 Austin Acton <austin@mandriva.org> 0.4.1-2mdv2008.1
+ Revision: 178071
- improve menu entry

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 30 2007 Funda Wang <fwang@mandriva.org> 0.4.1-1mdv2008.1
+ Revision: 103805
- New version 0.4.1

* Tue Sep 04 2007 Funda Wang <fwang@mandriva.org> 0.4.0.1-1mdv2008.0
+ Revision: 78966
- New version 0.4.0.1

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Wed Aug 22 2007 Austin Acton <austin@mandriva.org> 0.4-1mdv2008.0
+ Revision: 68810
- Import xournal

