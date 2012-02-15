Summary:	GNOME application to help you manage your book collection
Name:		alexandria
Version:	0.6.8
Release:	2
URL:		http://alexandria.rubyforge.org/
Source0:	http://files.rubyforge.vm.bytemark.co.uk/alexandria/%name-%version.tar.gz
Patch0:		alexandria-0.6.8-ruby-1.9.1.patch
License:	GPLv2+
Group:		Databases
Requires:	ruby >= 1.8 ruby-gettext >= 0.6.1 rubygem(hpricot)
Requires:	ruby-libglade2 ruby-gconf2 ruby-gnome2 >= 0.12.0 ruby-zoom
Requires(post):	scrollkeeper
Requires(postun):	scrollkeeper
BuildRequires:	ruby-devel gettext GConf2 intltool
BuildRequires:	desktop-file-utils
BuildArch: noarch

%description
Alexandria is a GNOME application to help you manage your book collection.

Alexandria:
  * retrieves and displays book information (including cover pictures)
    from several online libraries, such as Amazon, Proxis, Barnes and
    Noble, and the Spanish Ministry of Culture ;
  * allows books to be added and updated by hand ;
  * enables searches either by EAN/ISBN, title, authors or keyword ;
  * saves data using the YAML format ;
  * can import and export data into ONIX, Tellico and EAN/ISBN-list
    formats ;
  * generates from your libraries XHTML web pages themable with CSS ;
  * allows marking your books as loaned, each with the loan-date and the
    name of the person who has borrowed them ;
  * features a HIG-compliant user interface ;
  * shows books in different views (standard list or icons list), that
    can be either filtered or sorted ;
  * handles book rating and notes ;
  * supports CueCat (R) barcode readers ;
  * includes translations for several languages.

%prep
%setup -q
%patch0 -p1 -b .ruby19~

%build
rake --trace build

%install
rake install_package_staging \
	DESTDIR=$RPM_BUILD_ROOT \
	RUBYLIBDIR=%{ruby_sitelibdir}

mkdir -p %buildroot%{_sysconfdir}/gconf/schemas/
cp -a schemas/alexandria.schemas %buildroot%{_sysconfdir}/gconf/schemas/

%find_lang %name --all-name 

#menu
rm -f %buildroot%_datadir/menu/alexandria
install -m 755 -d %buildroot%{_datadir}/applications/
cp -a %{name}.desktop %buildroot%{_datadir}/applications/

desktop-file-install --vendor="" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

rm -f %buildroot%{_datadir}/gconf/schemas/alexandria.schemas

# icon
install -m 755 -d %buildroot{%{_miconsdir},%{_liconsdir}}
cp -a data/alexandria/icons/alexandria_small.png %buildroot%_miconsdir/%{name}.png
cp -a data/alexandria/icons/alexandria_small.png %buildroot%_iconsdir/%{name}.png
cp -a data/alexandria/icons/alexandria_small.png %buildroot%_liconsdir/%{name}.png

%files -f %name.lang
%defattr(-,root,root)
%{_bindir}/*
%{ruby_sitelibdir}/%{name}*
%{_datadir}/%{name}
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_datadir}/applications/%{name}.desktop
%{_datadir}/gnome/help/%{name}
%{_datadir}/omf/%{name}
%{_datadir}/sounds/%{name}
%{_datadir}/pixmaps/alexandria.xpm
%_iconsdir/hicolor/*/apps/*
%_mandir/man1/*
%doc README ChangeLog TODO
