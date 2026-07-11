%global tl_name includernw
%global tl_revision 47557

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1.0
Release:	%{tl_revision}.1
Summary:	Include .Rnw inside .tex
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/includernw
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/includernw.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/includernw.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is for including .Rnw (knitr/sweave)-files inside .tex-
files. It requires that you have R and the R-package knitr installed.
Note: This package will probably not work on Windows. It is tested only
on OS X, and will probably also work on standard Linux distros.

