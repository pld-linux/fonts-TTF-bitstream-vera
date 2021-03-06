%define	tarname	ttf-bitstream-vera
Summary:	Bitstream Vera TrueType fonts
Summary(pl.UTF-8):	Fonty TrueType Bitstream Vera
Name:		fonts-TTF-bitstream-vera
Version:	1.10
Release:	7
License:	distributable
Group:		Fonts
Source0:	http://ftp.gnome.org/pub/GNOME/sources/ttf-bitstream-vera/1.10/%{tarname}-%{version}.tar.bz2
# Source0-md5:	bb22bd5b4675f5dbe17c6963d8c00ed6
Source1:	%{name}.fontconfig
URL:		http://www.gnome.org/fonts/
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
Requires:	fontconfig >= 1:2.10.1
Obsoletes:	fonts-ttf-bitstream-vera
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
This package contains Bitstream Vera TrueType fonts (TTF).

%description -l pl.UTF-8
Pakiet ten zawiera fonty TrueType (TTF) Bitstream Vera.

%prep
%setup -q -n %{tarname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ttffontsdir}
install -d $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail
install -d $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

install *.ttf $RPM_BUILD_ROOT%{_ttffontsdir}
install %SOURCE1 $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/60-verdana.conf
ln -s %{_datadir}/fontconfig/conf.avail/60-verdana.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

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
%{_datadir}/fontconfig/conf.avail/60-verdana.conf
%{_sysconfdir}/fonts/conf.d/60-verdana.conf
