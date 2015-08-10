%global pypi_name PyMySQL

Name:           python-%{pypi_name}
Version:        0.6.6
Release:        4%{?dist}
Summary:        Pure-Python MySQL client library

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}/
Source0:        https://pypi.python.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools


%description
This package contains a pure-Python MySQL client library. The goal of PyMySQL is
to be a drop-in replacement for MySQLdb and work on CPython, PyPy, IronPython
and Jython.


%package -n     python2-%{pypi_name}
Requires:       mariadb
Summary:        Pure-Python MySQL client library
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
This package contains a pure-Python MySQL client library. The goal of PyMySQL is
to be a drop-in replacement for MySQLdb and work on CPython, PyPy, IronPython
and Jython.


%package -n     python3-%{pypi_name}
Summary:        Pure-Python MySQL client library
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       mariadb
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This package contains a pure-Python MySQL client library. The goal of PyMySQL is
to be a drop-in replacement for MySQLdb and work on CPython, PyPy, IronPython
and Jython.


%prep
%setup -qn %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info


%build
%py2_build
%py3_build


%install
%py2_install
%py3_install

# Remove shebang
for lib in %{buildroot}%{python3_sitelib}/pymysql/tests/thirdparty/test_MySQLdb/*.py; do
  sed -i '1{\@^#!/usr/bin/env python@d}' $lib
done

# Remove shebang
for lib in %{buildroot}%{python2_sitelib}/pymysql/tests/thirdparty/test_MySQLdb/*.py; do
  sed -i '1{\@^#!/usr/bin/env python@d}' $lib
done


%check
# Tests cannot be launch on koji, they require a mysqldb running.


%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{pypi_name}-%{version}-py%{python2_version}.egg-info/
%{python2_sitelib}/pymysql/

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/pymysql/

%changelog
* Thu Aug 6 2015 Julien Enselme <jujens@jujens.eu> - 0.6.6-4
- Use %%license in %%files

* Wed Aug 5 2015 Julien Enselme <jujens@jujens.eu> - 0.6.6-3
- Move python2 package in its own subpackage
- Add provides

* Fri Jul 31 2015 Julien Enselme <jujens@jujens.eu> - 0.6.6-2
- Add Provides: python2-PyMySQL
- Remove usage of %%py3dir

* Sun May 31 2015 Julien Enselme <jujens@jujens.eu> - 0.6.6-1
- Update to 0.6.6

* Wed Nov 26 2014 Julien Enselme <jujens@jujens.eu> - 0.6.2-1
- Initial packaging
