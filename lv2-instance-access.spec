Summary:	LV2 Instance Access extension - access to LV2_Handle of a plugin
Summary(pl.UTF-8):	Rozszerzenie LV2 Instance Access - dostęp do LV2_Handle wtyczki
Name:		lv2-instance-access
Version:	1.4
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://lv2plug.in/spec/%{name}-%{version}.tar.bz2
# Source0-md5:	e97c939530619dfca460445096140d8e
URL:		http://lv2plug.in/ns/ext/instance-access/
BuildRequires:	python >= 1:2.6
BuildRequires:	python-modules >= 1:2.6
Requires:	lv2core >= 6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LV2 Instance Access extension defines a method for (e.g.) plugin UIs
to get a direct handle to an LV2 plugin instance (LV2_Handle), if
possible.

%description -l pl.UTF-8
Rozszerzenie LV2 Instance Access definiuje metodę dla (przykładowo)
interfejsów użytkownika wtyczek, pozwalającą (jeśli to możliwe) na
uzyskanie bezpośredniego uchwytu instancji wtyczki LV2 (LV2_Handle).

%package devel
Summary:	Header file for LV2 Instance Access extension
Summary(pl.UTF-8):	Plik nagłówkowy rozszerzenia LV2 Instance Access
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	lv2core-devel >= 6.0

%description devel
Header file for LV2 Instance Access extension.

%description devel -l pl.UTF-8
Plik nagłówkowy rozszerzenia LV2 Instance Access.

%prep
%setup -q

%build
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}

./waf

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%dir %{_libdir}/lv2/instance-access.lv2
%{_libdir}/lv2/instance-access.lv2/instance-access.ttl
%{_libdir}/lv2/instance-access.lv2/manifest.ttl

%files devel
%defattr(644,root,root,755)
%{_libdir}/lv2/instance-access.lv2/instance-access.h
%{_includedir}/lv2/lv2plug.in/ns/ext/instance-access
%{_pkgconfigdir}/lv2-lv2plug.in-ns-ext-instance-access.pc
