%define	oname	rst2pdf

Name:		python-%{oname}
Version:	0.103.1
Release:	1
Summary:	Convert restructured text to PDF via reportlab
Source0:	https://files.pythonhosted.org/packages/source/r/rst2pdf/rst2pdf-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/rst2pdf
BuildArch:	noarch

BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	git-core

%patchlist
rst2pdf-allow-newer-docutils.patch

%description
The usual way of creating PDF from reStructuredText is by going through LaTeX. 
This tool provides an alternative by producing PDF directly using the ReportLab
library.

%prep -a
# Make setuptools-scm happy
git init
git add .
git config user.name "OpenMandriva Builder"
git config user.email info@openmandriva.org
git commit -am "Import %{version}"
git tag -a %{version} -m %{version}

%install -a
chmod +x %{buildroot}%{py_puresitedir}/rst2pdf/{findfonts,dumpstyle}.py

%files
%{_bindir}/rst2pdf 
%{py_puresitedir}/rst2pdf
%{py_puresitedir}/rst2pdf-%{version}.dist-info
