%global tl_name babel-ukrainian
%global tl_revision 79184

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5a
Release:	%{tl_revision}.1
Summary:	Babel support for Ukrainian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/ukrainian
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-ukrainian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-ukrainian.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-ukrainian.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides support for use of babel in documents written in
Ukrainian. The support is adapted for use under legacy TeX engines as
well as XeTeX and LuaTeX.

