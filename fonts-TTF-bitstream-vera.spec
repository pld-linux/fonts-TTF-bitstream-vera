%define tarname ttf-bitstream-vera
Summary:	-
Name:		fonts-ttf-bitstream-vera
Version:	1.10
Release:	0.2
License:	distributable
Group:		X11/Fonts
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{tarname}/1.10/%{tarname}-%{version}.tar.bz2
# Source0-md5:	bb22bd5b4675f5dbe17c6963d8c00ed6
#Source1:	%{name}.Fontmap
PreReq:		fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description

%prep
%setup -q -n %{tarname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ttffontsdir}
install *.ttf $RPM_BUILD_ROOT%{_ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/fontpostinst TTF

%postun 
/usr/bin/fontpostinst TTF

%files
%defattr(644,root,root,755)
# README.TXT is almost empty
%doc COPYRIGHT.TXT RELEASENOTES.TXT
%{_ttffontsdir}/*
