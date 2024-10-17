%define upstream_name    Catalyst-Plugin-Authentication-CDBI
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	CDBI Authentication for Catalyst
License:	Artistic/GPL
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst)
BuildRequires:	perl(Catalyst::Plugin::Authentication)
BuildArch:	noarch

%description
This plugin allows you to authenticate your web users using
database tables accessed through Class::DBI classes.
Note that this plugin requires a session plugin such as
Catalyst::Plugin::Session::FastMmap.
This module is now well past the teatime of it's lifespan,
and no new features will be added. For new applications,
you probably want to look at Catalyst::Plugin::Authentication
and friends instead

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Catalyst/Plugin/Authentication/*
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2mdv2011.0
+ Revision: 680729
- mass rebuild

* Thu Jul 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 398819
- rebuild
- using %%perl_convert_version
- fixed source field

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.10-4mdv2009.0
+ Revision: 241159
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-2mdv2008.0
+ Revision: 85990
- rebuild


* Sat Apr 08 2006 Arnaud de Lorbeau <devel@mandriva.com> 0.10-1mdk
- Initial MDV RPM

