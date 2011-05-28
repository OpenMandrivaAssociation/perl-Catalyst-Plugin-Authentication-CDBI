%define upstream_name    Catalyst-Plugin-Authentication-CDBI
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2

Summary:	CDBI Authentication for Catalyst
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(Catalyst)
BuildRequires:	perl(Catalyst::Plugin::Authentication)
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}
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
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Catalyst/Plugin/Authentication/*
%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

