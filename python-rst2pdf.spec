%define	oname	rst2pdf

Name:		python-%{oname}
Version:	0.93
Release:	1
Summary:	Convert restructured text to PDF via reportlab
Source0:	https://rst2pdf.googlecode.com/files/%{oname}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://rst2pdf.googlecode.com
BuildArch:	noarch
BuildRequires:	pythonegg(setuptools)
BuildRequires:	pkgconfig(python)

Requires:  pythonegg(docutils) 
Requires:  pythonegg(pdfrw) 
Requires:  pythonegg(pygments) 
Requires:  pythonegg(reportlab) >= 2.4 
Requires:  pythonegg(setuptools)

%description
The usual way of creating PDF from reStructuredText is by going through LaTeX. 
This tool provides an alternative by producing PDF directly using the ReportLab
library.

%prep
%setup -q -n %{oname}-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

chmod +x %{buildroot}%{py_puresitedir}/rst2pdf/{smartypants,findfonts,dumpstyle}.py


%check
# reportlab-2.7 will crash the tests
#python setup.py test

%files
%doc README.txt LICENSE.txt CHANGES.txt
%{_bindir}/rst2pdf 
%{py_puresitedir}/rst2pdf/*.py*
%{py_puresitedir}/rst2pdf/images/*
%{py_puresitedir}/rst2pdf/styles/*
%{py_puresitedir}/rst2pdf/templates/*
%{py_puresitedir}/rst2pdf/extensions/*.py*
%{py_puresitedir}/rst2pdf*.egg-info



