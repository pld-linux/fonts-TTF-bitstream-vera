%define tarname ttf-bitstream-vera
Summary:	Bitstream Vera True Type fonts
Summary(pl):	Fonty True Type Bitstream Vera
Name:		fonts-ttf-bitstream-vera
Version:	1.10
Release:	1
License:	distributable
Group:		X11/Fonts
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{tarname}/1.10/%{tarname}-%{version}.tar.bz2
# Source0-md5:	bb22bd5b4675f5dbe17c6963d8c00ed6
#Source1:	%{name}.Fontmap
URL:		http://www.gnome.org/fonts/
Requires(post,postun):	fontpostinst
Requires:       %{_fontsdir}/TTF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
This package contains Bitstream Vera True Type fonts (TTF).

%description -l pl
Pakiet ten zawiera fonty True Type (TTF) Bitstream Vera.

%prep
%setup -q -n %{tarname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ttffontsdir}
install *.ttf $RPM_BUILD_ROOT%{_ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun 
fontpostinst TTF

%files
%defattr(644,root,root,755)
# README.TXT is almost empty
%doc COPYRIGHT.TXT RELEASENOTES.TXT
%{_ttffontsdir}/*
