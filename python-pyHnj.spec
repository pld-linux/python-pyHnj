
%define 	module	pyHnj

Summary:	pyHnj - a Python wrapper for libhnj library
Summary(pl.UTF-8):	pyHnj - pythonowy wrapper dla biblioteki libhnj
Name:		python-%{module}
Version:	0.6
Release:	2
License:	GPL v2
Group:		Libraries/Python
Source0:	http://hkn.eecs.berkeley.edu/~dyoo/python/pyHnj/%{module}-%{version}.tar.gz
# Source0-md5:	1e777539150c5b6a853dce3a10e64398
URL:		http://hkn.eecs.berkeley.edu/~dyoo/python/pyHnj/
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyHnj is an extension wrapper for the libhnj hyphenation library.

%description -l pl.UTF-8
pyHnj jest pythonowym wrapperem do biblioteki libhnj.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

python setup.py install \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.txt
%attr(755,root,root) %{py_sitedir}/*.so
%{_datadir}/pyHnj/hyphen.mashed
