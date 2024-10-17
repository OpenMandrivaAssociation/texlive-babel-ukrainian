Name:		texlive-babel-ukrainian
Version:	56674
Release:	2
Summary:	Babel support for Ukrainian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-ukrainian
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-ukrainian.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-ukrainian.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-ukrainian.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides support for use of babel in documents
written in Ukrainian. The support is adapted for use under
legacy TeX engines as well as XeTeX and LuaTeX.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/babel-ukrainian
%{_texmfdistdir}/tex/generic/babel-ukrainian
%doc %{_texmfdistdir}/doc/generic/babel-ukrainian

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
