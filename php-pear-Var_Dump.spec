%include	/usr/lib/rpm/macros.php
%define		_class		Var_Dump
%define		_status		stable
%define		_pearname	%{_class}
Summary:	%{_pearname} - methods for dumping information about a variable
Summary(pl.UTF-8):	%{_pearname} - metody zrzucania informacji o zmiennych
Name:		php-pear-%{_pearname}
Version:	1.0.3
Release:	3
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	bf987548db4b106d254b086abaa911b4
URL:		http://pear.php.net/package/Var_Dump/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(pcre)
Requires:	php-common >= 3:4.0.4
Requires:	php-pear
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

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

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

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
