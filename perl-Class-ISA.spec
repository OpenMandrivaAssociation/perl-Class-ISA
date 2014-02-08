%define upstream_name    Class-ISA
%define upstream_version 0.36

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Report the search path thru an ISA tree
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Suppose you have a class (like Food::Fish::Fishstick) that is derived, via
its @ISA, from one or more superclasses (as Food::Fish::Fishstick is from
Food::Fish, Life::Fungus, and Chemicals), and some of those superclasses
may themselves each be derived, via its @ISA, from one or more superclasses
(as above).

When, then, you call a method in that class ($fishstick->calories), Perl
first searches there for that method, but if it's not there, it goes
searching in its superclasses, and so on, in a depth-first (or maybe
"height-first" is the word) search. In the above example, it'd first look
in Food::Fish, then Food, then Matter, then Life::Fungus, then Life, then
Chemicals.

This library, Class::ISA, provides functions that return that list -- the
list (in order) of names of classes Perl would search to find a method,
with no duplicates.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README ChangeLog
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.360.0-3mdv2011.0
+ Revision: 653556
- rebuild for updated spec-helper

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.360.0-2mdv2011.0
+ Revision: 562530
- rebuild
- rebuild

* Sun Dec 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.360.0-1mdv2011.0
+ Revision: 474212
- import perl-Class-ISA


* Sun Dec 06 2009 cpan2dist 0.36-1mdv
- initial mdv release, generated with cpan2dist
