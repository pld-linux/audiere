Summary:	Portable audio library
Summary(pl.UTF-8):	Przenośna biblioteka audio
Name:		audiere
Version:	1.9.4
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://dl.sourceforge.net/audiere/%{name}-%{version}.tar.gz
# Source0-md5:	b95dfe6f1e69cfd12371747f22772766
Patch0:		gcc44.patch
URL:		http://audiere.sourceforge.net/
# should be shared to avoid PIC issue
#BuildRequires:	dumb-devel
#BuildRequires:	flac-devel < 1.1.3
BuildRequires:	libcdaudio-devel
BuildRequires:	libogg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
# needs fix (-I, invalid conversion)
#BuildRequires:	speex-devel
#BR: wxWidgets for example player (needs passing WX_CONFIG)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Audiere Audio System is a portable audio library which supports
playing MP3, Ogg Vorbis, WAV, IT, XM, S3M, and MOD files. You can use
it from C, C++, Python, Java, and any language that supports XPCOM
(JavaScript in Mozilla, for example). It currently supports
DirectSound 3, DirectSound 8, and arbitrary DLLs for output in
Windows, and OSS in Linux.

%description -l pl.UTF-8
Audiere Audio System jest przenośną biblioteką obsługującą odtwarzanie
plików MP3, Ogg Vorbis, WAV, IT, XM, S3M oraz MOD. Można jej używać z
poziomu C, C++, Pythona, Javy oraz innych języków obsługujących XPCOM
(jak na przykład JavaScript w Mozilli). Biblioteka jako wyjście
obsługuje obecnie DirectSound 3, DirectSound 8 jak również dowolne
biblioteki DLL dla Windows oraz OSS pod Linuksem.

%package devel
Summary:	Header files for audiere library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki audiere
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcdaudio-devel
Requires:	libogg-devel
Requires:	libstdc++-devel
Requires:	libvorbis-devel

%description devel
Header files for audiere library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki audiere.

%package static
Summary:	Static audiere library
Summary(pl.UTF-8):	Statyczna biblioteka audiere
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static audiere library.

%description static -l pl.UTF-8
Statyczna biblioteka audiere.

%prep
%setup -q
%patch -P0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.txt
%attr(755,root,root) %{_libdir}/libaudiere-%{version}.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/audiere-config
%attr(755,root,root) %{_libdir}/libaudiere.so
%{_libdir}/libaudiere.la
%{_includedir}/audiere.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libaudiere.a
