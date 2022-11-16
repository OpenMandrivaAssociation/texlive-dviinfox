Name:		texlive-dviinfox
Version:	59216
Release:	1
Summary:	Perl script to print DVI meta information
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dviinfox
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dviinfox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dviinfox.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a perl script which prints information
about a DVI file. It also supports XeTeX XDV format.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/scripts/dviinfox
%doc %{_texmfdistdir}/texmf-dist/doc/latex/dviinfox

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
