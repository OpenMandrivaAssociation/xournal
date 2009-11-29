%define name	xournal
%define version	0.4.5
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Pen-based journal and PDF annotator
Version: 	%{version}
Release: 	%{release}

Source:		http://heanet.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
URL:		http://xournal.sourceforge.net/
License:	GPLv2
Group:		Office
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	imagemagick
BuildRequires:	libgnomecanvas2-devel libgnomeprintui-devel
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

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README html-doc/*
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
