%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]")}

Name:           python-paste-script
Version:        1.7.3
Release:        4%{?dist}
Summary:        A pluggable command-line frontend
Group:          System Environment/Libraries
# paste/script/wsgiserver/ is BSD licensed from CherryPy
# paste/script/util/subprocess24.py is MIT or Python
# string24.py may also be MIT or Python: apart from the top two lines, it is
# python 2.4.3's string.py
# The rest of the code is MIT.
License: MIT and BSD and (MIT or Python)
URL:            http://pythonpaste.org/script
Source0:        http://pypi.python.org/packages/source/P/PasteScript/PasteScript-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools-devel
BuildRequires:  python-paste-deploy
Requires:       python-paste >= 1.3
Requires:       python-paste-deploy
Requires:       python-cheetah
Requires:       python-setuptools
Requires:       pyOpenSSL

%description
Paster is pluggable command-line frontend, including commands to setup package
file layouts

Built-in features:

 * Creating file layouts for packages.
   For instance a setuptools-ready file layout.
 * Serving up web applications, with configuration based on paste.deploy


%prep
%setup -q -n PasteScript-%{version}
find docs -type f -exec chmod 0644 \{\} \;

%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root=%{buildroot} 

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc docs/*
%{python_sitelib}/*
%{_bindir}/paster


%changelog
* Wed Jul 14 2010 David Malcolm <dmalcolm@redhat.com> - 1.7.3-4
- add requirement on pyOpenSSL
- fix license tag
- specfile cleanups
Resolves: rhbz#613189

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.7.3-3.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Luke Macken <lmacken@redhat.com> - 1.7.3-1
- Update to 1.7.3
- Remove copydir_re_fix.patch

* Tue Dec  9 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.6.3-5
- Add patch for copydir re error
-   (http://trac.pythonpaste.org/pythonpaste/ticket/313)

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.6.3-4
- Rebuild for Python 2.6

* Mon Oct 6 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 1.6.3-3
- Require python-setuptools
- BuildRequire python-paste-deploy

* Sat Jun 14 2008 Luke Macken <lmacken@redhat.com> - 1.6.3-1
- Update to Paste 1.6.3

* Mon Mar 10 2008 Luke Macken <lmacken@redhat.com> - 1.6.2-2
- Require python-paste >= 1.3

* Thu Feb 28 2008 Luke Macken <lmacken@redhat.com> - 1.6.2-1
- Update to 1.6.2

* Wed Oct  3 2007 Luke Macken <lmacken@redhat.com> - 1.3.6-1
- 1.3.6

* Sun Sep  2 2007 Luke Macken <lmacken@redhat.com> - 1.3.5-2
- Update for python-setuptools changes in rawhide

* Sun Jul  8 2007 Luke Macken <lmacken@redhat.com> - 1.3.5-1
- 1.3.5

* Sat Mar  3 2007 Luke Macken <lmacken@redhat.com> - 1.1-1
- 1.1

* Sat Dec  9 2006 Luke Macken <lmacken@redhat.com> - 1.0-4
- Add python-devel to BuildRequires
- Python 2.5 fixes
- 1.0

* Sun Sep 17 2006 Luke Macken <lmacken@redhat.com> - 0.9.8-1
- 0.9.8

* Sun Sep  3 2006 Luke Macken <lmacken@redhat.com> - 0.9-5
- Rebuild for FC6

* Mon Aug 21 2006 Luke Macken <lmacken@redhat.com> - 0.9-4
- Include .pyo files instead of ghosting them.

* Sat Jul 29 2006 Luke Macken <lmacken@redhat.com> - 0.9-3
- Require python-paste-deploy

* Wed Jul 26 2006 Luke Macken <lmacken@redhat.com> - 0.9-2
- Rename to python-paste-script
- Use consistent buildroot variables
- Fix docs inclusion

* Mon Jul 10 2006 Luke Macken <lmacken@redhat.com> - 0.9-1
- Initial package
