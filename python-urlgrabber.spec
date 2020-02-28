Name:          python-urlgrabber
Version:       4.0.0
Release:       1
Summary:       Cross-protocol urlgrabber
License:       LGPLv2+
Url:           http://urlgrabber.baseurl.org/
Source0:       http://urlgrabber.baseurl.org/download/urlgrabber-%{version}.tar.gz

Patch0001:     0001-urlgrabber-ext-down-another-python-3-compat.patch
Patch0002:     0002-Revert-Simplify-mirror-conversion-to-utf8.patch
Patch0003:     0003-urlgrabber-ext-down-convert-url-into-bytes.patch

BuildArch:     noarch

%global _description\
It is a urlgrabber.We can use it to fetch data in three ways.Urlgrab copies\
files to the local filesystem,urlopen opens the remote file and returns a\
file object,urlread returns contents of files as string.It is easy to install\
and use this package.

%description %_description

%package -n python2-urlgrabber
Summary:       %summary
BuildRequires: python2-devel python2dist(setuptools) python2dist(pycurl) python2dist(six)
%{?python_provide:%python_provide python2-urlgrabber}

%description -n python2-urlgrabber %_description

%package -n python3-urlgrabber
Summary:       %summary
Provides:      urlgrabber = %{version}-%{release}
BuildRequires: python3-devel python3dist(setuptools) python3dist(pycurl) python3dist(six)
%{?python_provide:%python_provide python3-urlgrabber}

%description -n python3-urlgrabber %_description

%prep
%autosetup -n urlgrabber-%{version} -p1

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install
sed -e "s|/usr/bin/python|%{__python3}|" -i $RPM_BUILD_ROOT/%{_libexecdir}/*
rm -rf $RPM_BUILD_ROOT/%{_docdir}/urlgrabber-%{version}

%files -n python2-urlgrabber
%license LICENSE
%doc README ChangeLog TODO
%{python2_sitelib}/urlgrabber
%{python2_sitelib}/urlgrabber-%{version}-py?.?.egg-info

%files -n python3-urlgrabber
%license LICENSE
%doc README ChangeLog TODO
%{_bindir}/urlgrabber
%{_libexecdir}/urlgrabber-ext-down
%{python3_sitelib}/urlgrabber
%{python3_sitelib}/urlgrabber-%{version}-py?.?.egg-info

%changelog
* Fri Feb 28 2020 lingsheng <lingsheng@huawei.com> - 4.0.0-1
- update version to 4.0.0

* Fri Feb 14 2020 Jiangping Hu <hujp1985@foxmail.com> - 3.10.1-18
- Package init
