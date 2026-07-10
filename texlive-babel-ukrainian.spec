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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides support for use of babel in documents written in
Ukrainian. The support is adapted for use under legacy TeX engines as
well as XeTeX and LuaTeX.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/source/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/babel-ukrainian
%dir %{_datadir}/texmf-dist/source/generic/babel-ukrainian
%dir %{_datadir}/texmf-dist/tex/generic/babel-ukrainian
%doc %{_datadir}/texmf-dist/doc/generic/babel-ukrainian/README.md
%doc %{_datadir}/texmf-dist/doc/generic/babel-ukrainian/ukraineb.pdf
%doc %{_datadir}/texmf-dist/source/generic/babel-ukrainian/ukraineb.dtx
%doc %{_datadir}/texmf-dist/source/generic/babel-ukrainian/ukraineb.ins
%{_datadir}/texmf-dist/tex/generic/babel-ukrainian/ukraineb.ldf
