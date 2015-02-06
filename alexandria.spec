Summary:	GNOME application to help you manage your book collection
Name:		alexandria
Version:	0.6.8
Release:	5
URL:		http://alexandria.rubyforge.org/
Source0:	http://files.rubyforge.vm.bytemark.co.uk/alexandria/%name-%version.tar.gz
Patch0:		alexandria-0.6.8-ruby-1.9.1.patch
License:	GPLv2+
Group:		Databases
Requires:	ruby >= 1.8 rubygem(gettext) rubygem(hpricot)
Requires:	ruby-libglade2 ruby-gconf2 ruby-gnome2 >= 0.12.0 rubygem(zoom)
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


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.6.8-2
+ Revision: 774166
- fix build issues with ruby 1.9.1
- mass rebuild of ruby packages against ruby 1.9.1

* Wed Dec 14 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.6.8-1
+ Revision: 741036
- version update 0.6.8

* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 0.6.6-3
+ Revision: 677516
- fix installing
- rebuild to add gconftool-2 as req

* Thu Nov 04 2010 Rémy Clouard <shikamaru@mandriva.org> 0.6.6-2mdv2011.0
+ Revision: 593218
- rebuild for new hpricot

* Mon Oct 04 2010 Funda Wang <fwang@mandriva.org> 0.6.6-1mdv2011.0
+ Revision: 582952
- New version 0.6.6

* Thu Nov 12 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.5-1mdv2010.1
+ Revision: 465372
- update to new version 0.6.5

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.6.4.1-2mdv2010.0
+ Revision: 436637
- rebuild

* Sun Mar 15 2009 Pascal Terjan <pterjan@mandriva.org> 0.6.4.1-1mdv2009.1
+ Revision: 355515
- Update to 0.6.4.1

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.6.3-4mdv2009.0
+ Revision: 266148
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Apr 23 2008 Funda Wang <fwang@mandriva.org> 0.6.3-3mdv2009.0
+ Revision: 196902
- swtich to ubuntu patches, since it works in the more correct way

* Wed Apr 23 2008 Funda Wang <fwang@mandriva.org> 0.6.3-2mdv2009.0
+ Revision: 196901
- add fedora patch to fix bug#40287: crash on starting

* Tue Apr 22 2008 Funda Wang <fwang@mandriva.org> 0.6.3-1mdv2009.0
+ Revision: 196481
- BR rake
- New version 0.6.3

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 0.6.1-8mdv2008.1
+ Revision: 135819
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 02 2007 Pascal Terjan <pterjan@mandriva.org> 0.6.1-8mdv2008.0
+ Revision: 78298
- Use standard ruby macros

  + Emmanuel Andry <eandry@mandriva.org>
    - drop old menu
    - use gconf and scrollkeeper macros


* Fri Aug 25 2006 Pascal Terjan <pterjan@mandriva.org> 0.6.1-7mdv2007.0
- Fix for new gettext (P0)

* Thu Aug 24 2006 Pascal Terjan <pterjan@mandriva.org> 0.6.1-6mdv2007.0
- XDG menu

* Wed Jun 28 2006 Lenny Cartier <lenny@mandriva.com> 0.6.1-5mdv2007.0
- rebuild

* Fri Jan 13 2006 Pascal Terjan <pterjan@mandriva.org> 0.6.1-4mdk
- lib64 fix

* Thu Jan 12 2006 Pascal Terjan <pterjan@mandriva.org> 0.6.1-3mdk
- ship back OSX interface, would be easier for autodeps in fact

* Thu Dec 22 2005 Pascal Terjan <pterjan@mandriva.org> 0.6.1-2mdk
- BuildRequires intltool

* Sun Oct 02 2005 Pascal Terjan <pterjan@mandriva.org> 0.6.1-1mdk
- 0.6.1 (workaround a YAML bug of Ruby 1.8.3)

* Sun Sep 04 2005 Pascal Terjan <pterjan@mandriva.org> 0.6.0-6mdk
- avoid error in post if gconfd is not already running (again)

* Sat Sep 03 2005 Pascal Terjan <pterjan@mandriva.org> 0.6.0-5mdk
- Don't ship OSX interface

* Fri Sep 02 2005 Pascal Terjan <pterjan@mandriva.org> 0.6.0-4mdk
- avoid error in post if gconfd is not already running
- mkrel

* Sun Aug 28 2005 Pascal Terjan <pterjan@mandriva.org> 0.6.0-3mdk
- Requires ruby-zoom

* Thu Aug 25 2005 Pascal Terjan <pterjan@mandriva.org> 0.6.0-2mdk
- Requires scrollkeeper, but don't run it at build time (#10809}
- Disable schemas installation

* Wed Aug 24 2005 Pascal Terjan <pterjan@mandriva.org> 0.6.0-1mdk
- 0.6.0, now with Help

* Sun Mar 27 2005 Pascal Terjan <pterjan@mandrake.org> 0.5.1-2mdk
- Install .desktop

* Sun Mar 27 2005 Pascal Terjan <pterjan@mandrake.org> 0.5.1-1mdk
- 0.5.1

* Sun Mar 13 2005 Pascal Terjan <pterjan@mandrake.org> 0.5.0-1mdk
- 0.5.0

* Sun Nov 07 2004 Pascal Terjan <pterjan@mandrake.org> 0.4.0-2mdk
- Remove fix no longer needed
- Update description

* Sun Nov 07 2004 Pascal Terjan <pterjan@mandrake.org> 0.4.0-1mdk
- 0.4.0

* Sun Jul 11 2004 Franck Villaume <fvill@freesurf.fr> 0.3.1-1mdk
- 0.3.1
- fix Buildrequires

* Sat Jul 03 2004 Pascal Terjan <pterjan@mandrake.org> 0.3.0-1mdk
- 0.3.0
- Drop patch0 (merged upstream)

* Tue Jun 15 2004 Pascal Terjan <pterjan@mandrake.org> 0.2.0-4mdk
- Fix encoding problems

* Mon Jun 14 2004 Pascal Terjan <pterjan@mandrake.org> 0.2.0-3mdk
- Some more BuildRequires

* Mon Jun 14 2004 Pascal Terjan <pterjan@mandrake.org> 0.2.0-2mdk
- Requires ruby-gnome2

* Sun Jun 13 2004 Pascal Terjan <pterjan@mandrake.org> 0.2.0-1mdk
- first mdk release

