#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-sentinels
Version  : 1.0.0
Release  : 5
URL      : https://files.pythonhosted.org/packages/ac/b7/1af07a98390aba07da31807f3723e7bbd003d6441b4b3d67b20d97702b23/sentinels-1.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ac/b7/1af07a98390aba07da31807f3723e7bbd003d6441b4b3d67b20d97702b23/sentinels-1.0.0.tar.gz
Summary  : Various objects to denote special meanings in python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-sentinels-license = %{version}-%{release}
Requires: pypi-sentinels-python = %{version}-%{release}
Requires: pypi-sentinels-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
Overview
--------
The sentinels module is a small utility providing the Sentinel class, along with useful instances.

%package license
Summary: license components for the pypi-sentinels package.
Group: Default

%description license
license components for the pypi-sentinels package.


%package python
Summary: python components for the pypi-sentinels package.
Group: Default
Requires: pypi-sentinels-python3 = %{version}-%{release}

%description python
python components for the pypi-sentinels package.


%package python3
Summary: python3 components for the pypi-sentinels package.
Group: Default
Requires: python3-core
Provides: pypi(sentinels)

%description python3
python3 components for the pypi-sentinels package.


%prep
%setup -q -n sentinels-1.0.0
cd %{_builddir}/sentinels-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649701223
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sentinels
cp %{_builddir}/sentinels-1.0.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sentinels/c37e9e0ecb1d7bab2168531c171b0f2e92ddceba
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sentinels/c37e9e0ecb1d7bab2168531c171b0f2e92ddceba

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
