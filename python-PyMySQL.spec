%global pypi_name PyMySQL

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        4%{?dist}
Summary:        Pure-Python MySQL client library

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}/
Source0:        https://files.pythonhosted.org/packages/a8/b4/3544c8e6ed9b1c6a00e5b302e3d5a646e43a8a0ac5216f5ae8706688706e/PyMySQL-0.8.0.tar.gz

BuildArch:      noarch

# for python2
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

# for python3
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

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

%package -n     python3-%{pypi_name}
Summary:        Pure-Python MySQL client library
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

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
# Remove shebang
for lib in %{buildroot}%{python2_sitelib}/pymysql/tests/thirdparty/test_MySQLdb/*.py; do
  sed -i '1{\@^#!/usr/bin/env python@d}' $lib
done

%py3_install
# Remove shebang
for lib in %{buildroot}%{python3_sitelib}/pymysql/tests/thirdparty/test_MySQLdb/*.py; do
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
* Thu Feb 15 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.8.0-4
- make spec file compatible with epel7
- remove conditionals and always build for Python 3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Dec 27 2017 Julien Enselme <jujens@jujens.eu> - 0.8.0-1
- Update to 0.8.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 07 2017 Julien Enselme <jujens@jujens.eu> - 0.7.11-1
- Update to 0.7.11

* Wed Feb 15 2017 Julien Enselme <jujens@jujens.eu> - 0.7.10-1
- Update to 0.7.10

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.9-3
- Rebuild for Python 3.6

* Wed Nov 23 2016 Damien Ciabrini <dciabrin@redhat.com> - 0.7.9-2
- cherrypick commit 755dfdc upstream to allow bind before connect
  Related: rhbz#1378008

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
