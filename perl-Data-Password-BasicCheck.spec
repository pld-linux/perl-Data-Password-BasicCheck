#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Data
%define		pnam	Password-BasicCheck
Summary:	Data::Password - Basic password checking
Summary(pl):	Data::Password - Podstawowe sprawdzanie poprawno¶ci has³a
Name:		perl-%{pdir}-%{pnam}
Version:	2.01
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
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

%description -l pl
Obiekty Data::Password::BasicCheck na podanych has³ach sprawdz± czy:

- d³ugo¶æ has³a jest w zakresie podanym przy tworzeniu obiektu;
- w ha¶le znajduje siê przynajmniej pL symboli, gdzie L jest d³ugo¶ci±
  has³a, a p jest liczb± z zakresu 0 < p =< 1. Je¶li warto¶æ nie
  zostanie podana podczas tworzeniu obiektu, przyjmie warto¶æ domy¶ln± 
  p = 2/3 (czyli: 0.666666...)
- has³o zawiera litery, cyfry i znaki niealfanumeryczne
- rotacje has³a nie pasuj± do orygina³u (n.p.: has³o a1&a1& pasuje do
  samego siebie po trzech rotacjach)
- po usuniêciu cyfr i symboli has³o, jego odwrotno¶æ oraz wszystkie
  mo¿liwe rotacje nie pasuj± do którychkolwiek z podanych informacji
  osobistych (imiê, nazwisko, miasto, login)

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
%{perl_vendorlib}/Data/Password/*.pm
%{_mandir}/man3/*
