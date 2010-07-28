%define upstream_name    Class-ISA
%define upstream_version 0.36

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Report the search path thru an ISA tree
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(if)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_mandir}/man3/*
%perl_vendorlib/*
