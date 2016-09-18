%global pypi_name PyMySQL
%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        0.7.9
Release:        1%{?dist}
Summary:        Pure-Python MySQL client library

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}/
Source0:        https://pypi.python.org/packages/a4/c4/c15457f261fda9839637de044eca9b6da8f55503183fe887523801b85701/PyMySQL-0.7.9.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools


%description
This package contains a pure-Python MySQL client library. The goal of PyMySQL is
to be a drop-in replacement for MySQLdb and work on CPython, PyPy, IronPython
and Jython.


%package -n     python2-%{pypi_name}
Summary:        Pure-Python MySQL client library
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
This package contains a pure-Python MySQL client library. The goal of PyMySQL is
to be a drop-in replacement for MySQLdb and work on CPython, PyPy, IronPython
and Jython.

%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        Pure-Python MySQL client library
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This package contains a pure-Python MySQL client library. The goal of PyMySQL is
to be a drop-in replacement for MySQLdb and work on CPython, PyPy, IronPython
and Jython.
%endif

%prep
%setup -qn %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
# Remove shebang
for lib in %{buildroot}%{python2_sitelib}/pymysql/tests/thirdparty/test_MySQLdb/*.py; do
  sed -i '1{\@^#!/usr/bin/env python@d}' $lib
done

%if 0%{?with_python3}
%py3_install
# Remove shebang
for lib in %{buildroot}%{python3_sitelib}/pymysql/tests/thirdparty/test_MySQLdb/*.py; do
  sed -i '1{\@^#!/usr/bin/env python@d}' $lib
done
%endif

%check
# Tests cannot be launch on koji, they require a mysqldb running.


%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{pypi_name}-%{version}-py%{python2_version}.egg-info/
%{python2_sitelib}/pymysql/

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/pymysql/
%endif

%changelog
* Sun Sep 18 2016 Julien Enselme <jujens@jujens.eu> - 0.7.9-1
- Update to 0.7.9

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 4 2016 Julien Enselme <jujens@jujens.eu> - 0.6.7-4
- Correct installation problems due to Requires: mariadb

* Thu Nov 5 2015 Julien Enselme <jujens@jujens.eu> - 0.6.7-3
- Rebuilt for python 3.5

* Wed Nov  4 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 0.6.7-2
- Drop unnecessary mariadb requirement
- Add python3 conditionals in order to rebuild it in EL7

* Thu Oct 1 2015 Julien Enselme <jujens@jujens.eu> - 0.6.7-1
- Update to 0.6.7

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
