Name: 	 	xournal
Summary: 	Pen-based journal and PDF annotator
Version: 	0.4.8.2016
Release: 	1

Source0:	http://heanet.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
URL:		https://xournal.sourceforge.net/
License:	GPLv2
Group:		Office
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(libgnomecanvas-2.0)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(x11)
BuildRequires:	pkgconfig(poppler-glib)
# For pdftoppm: see http://forum.mandriva.com/viewtopic.php?t=92135
Requires:	poppler

%description
Xournal is an application for notetaking, sketching, keeping a journal using a
stylus.  It is similar to Microsoft Windows Journal or to other alternatives
such as Jarnal, Gournal, and NoteLab.

%prep
%setup -q

%build
%configure
%make_build
										
%install
%make_install

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


