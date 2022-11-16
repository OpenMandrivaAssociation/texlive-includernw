Name:		texlive-includernw
Version:	47557
Release:	1
Summary:	Include .Rnw inside .tex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/includernw
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/includernw.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/includernw.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is for including .Rnw (knitr/sweave)-files inside
.tex-files. It requires that you have R and the R-package knitr
installed. Note: This package will probably not work on
Windows. It is tested only on OS X, and will probably also work
on standard Linux distros.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/includernw
%doc %{_texmfdistdir}/doc/latex/includernw

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
