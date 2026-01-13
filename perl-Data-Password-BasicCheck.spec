#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Data
%define		pnam	Password-BasicCheck
Summary:	Data::Password::BasicCheck - Basic password checking
Summary(pl.UTF-8):	Data::Password::BasicCheck - Podstawowe sprawdzanie poprawności hasła
Name:		perl-Data-Password-BasicCheck
Version:	2.01
Release:	4
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Data/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d3a5a3a1ac1263d3178c6785bdf6555b
URL:		http://search.cpan.org/dist/Data-Password-BasicCheck/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::Password::BasicCheck objects will do the following checks on the
given passwords:

- password length is in a defined range that is established at object
  creation;
- there are at least pL symbols in password, where L is password
  length and p is 0 < p =< 1. If not specified at object creation we
  assume p = 2/3 (that is: 0.66666...)
- password contains alphabetic characters, digits and non-alphanumeric
  characters;
- rotations of the password don't match it (e.g.: the password a1&a1&
  matches itself after three rotations)
- after cleaning away digits and symbols, the password, its reverse
  and all possible rotations don't match any personal information given
  (name, surname, city, username)

%description -l pl.UTF-8
Obiekty Data::Password::BasicCheck na podanych hasłach sprawdzą czy:

- długość hasła jest w zakresie podanym przy tworzeniu obiektu;
- w haśle znajduje się przynajmniej pL symboli, gdzie L jest długością
  hasła, a p jest liczbą z zakresu 0 < p =< 1. Jeśli wartość nie
  zostanie podana podczas tworzeniu obiektu, przyjmie wartość domyślną 
  p = 2/3 (czyli: 0.666666...)
- hasło zawiera litery, cyfry i znaki niealfanumeryczne
- rotacje hasła nie pasują do oryginału (n.p.: hasło a1&a1& pasuje do
  samego siebie po trzech rotacjach)
- po usunięciu cyfr i symboli hasło, jego odwrotność oraz wszystkie
  możliwe rotacje nie pasują do którychkolwiek z podanych informacji
  osobistych (imię, nazwisko, miasto, login)

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Data/Password
%{perl_vendorlib}/Data/Password/*.pm
%{_mandir}/man3/*
