%include	/usr/lib/rpm/macros.php
%define		_class		Var_Dump
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - methods for dumping information about a variable
Summary(pl):	%{_pearname} - metody zrzucania informacji o zmiennych
Name:		php-pear-%{_pearname}
Version:	1.0.2
Release:	1.2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	68e55d06868baf3189442d0eb5ee1401
URL:		http://pear.php.net/package/Var_Dump/
BuildRequires:	rpm-php-pearprov >= 4.4.2-10.2
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

%description -l pl
Wy¶wietla graficznie informacje o warto¶ciach zmiennych:
- je¿eli dana jest prosta zmienna (string, integer, double, resource),
  sama warto¶æ jest wypisywana,
- je¿eli dana jest tablica, przeszukiwana jest rekursywnie i warto¶ci
  s± prezentowane w formacie, który pokazuje klucze i elementy,
- je¿eli dany jest obiekt, informacje o obiekcie i klasie s±
  wy¶wietlane.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

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
