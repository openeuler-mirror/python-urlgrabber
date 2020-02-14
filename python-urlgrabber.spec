Name:          python-urlgrabber
Version:       3.10.1
Release:       18
Summary:       Cross-protocol urlgrabber
License:       LGPLv2+
Url:           http://urlgrabber.baseurl.org/
Source0:       http://urlgrabber.baseurl.org/download/urlgrabber-%{version}.tar.gz
Patch1:        BZ-1051554-speed-on-404-mirror.patch

BuildArch:     noarch
BuildRequires: python2-pycurl python2-devel

%global _description\
It is a urlgrabber.We can use it to fetch data in three ways.Urlgrab copies\
files to the local filesystem,urlopen opens the remote file and returns a\
file object,urlread returns contents of files as string.It is easy to install\
and use this package.

%description %_description

%global _package_python2 python2-urlgrabber

%package -n %_package_python2
Summary:       %summary
Provides:      urlgrabber = %{version}-%{release}
Requires:      python2-pycurl
%{?python_provide:%python_provide python2-urlgrabber}

%description -n %_package_python2 %_description

%prep
%setup -q -n urlgrabber-%{version}
%patch1 -p1

%build
%py2_build

%install
%py2_install
rm -rf $RPM_BUILD_ROOT/%{_docdir}/urlgrabber-%{version}

%files -n %_package_python2
%license LICENSE
%doc README ChangeLog TODO
%{_bindir}/urlgrabber
%{python2_sitelib}/urlgrabber*
%attr(0755,root,root) %{_libexecdir}/urlgrabber-ext-down

%changelog
* Fri Feb 14 2020 Jiangping Hu <hujp1985@foxmail.com> - 3.10.1-18
- Package init
