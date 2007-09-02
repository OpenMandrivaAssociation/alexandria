%define	name	alexandria
%define	version	0.6.1
%define	release	%mkrel 8

Summary:	GNOME application to help you manage your book collection
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://alexandria.rubyforge.org/
Source0:	http://rubyforge.org/frs/download.php/746/%{name}-%{version}.tar.bz2
Patch0:		alexandria-0.6.1-gettext.patch
License:	GPL
Group:		Databases
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	ruby >= 1.8 ruby-amazon >= 0.8.3 ruby-gettext >= 0.6.1
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
%patch0 -p0

# Don't run scrollkeeper-update in install
rm -f data/omf/alexandria/post-install.rb

%build
ruby install.rb config
ruby install.rb setup

%install
rm -rf %buildroot
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 ruby install.rb install --prefix=%buildroot

mkdir -p %buildroot%{_sysconfdir}/gconf/schemas/
cp -a schemas/alexandria.schemas %buildroot%{_sysconfdir}/gconf/schemas/

%find_lang %name --all-name 

#menu

install -m 755 -d %buildroot%{_datadir}/applications/
cp -a %{name}.desktop %buildroot%{_datadir}/applications/

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="GNOME" \
  --add-category="X-MandrivaLinux-MoreApplications-Databases" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

# icon
install -m 755 -d %buildroot{%{_miconsdir},%{_liconsdir}}
cp -a data/alexandria/icons/alexandria_small.png %buildroot%_miconsdir/%{name}.png
cp -a data/alexandria/icons/alexandria_small.png %buildroot%_iconsdir/%{name}.png
cp -a data/alexandria/icons/alexandria_small.png %buildroot%_liconsdir/%{name}.png


%post
%update_scrollkeeper
%update_menus
%post_install_gconf_schemas %{name}

%preun
%preun_uninstall_gconf_schemas %{name}

%postun
%clean_scrollkeeper
%clean_menus

%clean
rm -rf %buildroot

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

%doc README AUTHORS ChangeLog HACKING TODO

