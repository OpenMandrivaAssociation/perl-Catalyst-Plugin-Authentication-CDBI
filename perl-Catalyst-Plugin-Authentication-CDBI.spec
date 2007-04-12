%define realname Catalyst-Plugin-Authentication-CDBI
%define name perl-%{realname}
%define version 0.10
%define release %mkrel 1

Summary:	CDBI Authentication for Catalyst
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		/%{realname}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-Catalyst
BuildRequires:	perl-Catalyst-Plugin-Authentication
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-root

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
%setup -q -n %{realname}-%{version}

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

