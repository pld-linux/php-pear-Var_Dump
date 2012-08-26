%define		_class		Var_Dump
%define		_status		stable
%define		_pearname	Var_Dump
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - methods for dumping information about a variable
Summary(pl.UTF-8):	%{_pearname} - metody zrzucania informacji o zmiennych
Name:		php-pear-%{_pearname}
Version:	1.0.4
Release:	5
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	321be257dc68f515b64bb92ee0b9a1bb
URL:		http://pear.php.net/package/Var_Dump/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.0.4
Requires:	php(pcre)
Requires:	php(pcre)
Requires:	php-pear
Obsoletes:	php-pear-Var_Dump-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Displays informations about the values of variables on a graphical
way:
- If given a simple variable (string, integer, double, ressource), the
  value itself is printed,
- If given an array, it is explored recursively and values are
  presented in a format that shows keys and elements,
- If given an object, informations about the object and the class are
  printed.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Wyświetla graficznie informacje o wartościach zmiennych:
- jeżeli dana jest prosta zmienna (string, integer, double, resource),
  sama wartość jest wypisywana,
- jeżeli dana jest tablica, przeszukiwana jest rekursywnie i wartości
  są prezentowane w formacie, który pokazuje klucze i elementy,
- jeżeli dany jest obiekt, informacje o obiekcie i klasie są
  wyświetlane.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_pearname}

%{php_pear_dir}/data/%{_pearname}
