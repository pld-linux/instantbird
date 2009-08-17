Summary:	A single program for chatting on all famous networks!
Name:		instantbird
Version:	0.1.3.1
Release:	0.1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		Applications/Networking
URL:		http://www.instantbird.com/
Source0:	http://www.instantbird.com/downloads/%{version}/%{name}-%{version}.src.tar.bz2
Patch0:		mozilla-ac.patch
Patch1:		syslibs.patch
Patch2:		nocross.patch
# Source0-md5:	d9f9a93326d97de14b79d4d0fac09d29
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing

%description
Instantbird is a multi-protocol Instant Messaging client. Using it,
you can connect to all your different IM accounts.

It uses the Mozilla rendering engine to display IMs, and the Pidgin
libpurple to connect to the different networks.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p0
%patch2 -p0
%patch1 -p0

%build
cd mozilla
cp -f %{_datadir}/automake/config.* build/autoconf
%{__aclocal} -I build/autoconf
%{__autoconf}

cat << 'EOF' > .mozconfig
. $topsrcdir/xulrunner/config/mozconfig

# Options for 'configure' (same as command-line options).
ac_add_options --prefix=%{_prefix}
ac_add_options --exec-prefix=%{_exec_prefix}
ac_add_options --bindir=%{_bindir}
ac_add_options --sbindir=%{_sbindir}
ac_add_options --sysconfdir=%{_sysconfdir}
ac_add_options --datadir=%{_datadir}
ac_add_options --includedir=%{_includedir}
ac_add_options --libdir=%{_libdir}
ac_add_options --libexecdir=%{_libexecdir}
ac_add_options --localstatedir=%{_localstatedir}
ac_add_options --sharedstatedir=%{_sharedstatedir}
ac_add_options --mandir=%{_mandir}
ac_add_options --infodir=%{_infodir}
%if %{?debug:1}0
ac_add_options --disable-optimize
ac_add_options --enable-debug
ac_add_options --enable-debug-modules
ac_add_options --enable-debugger-info-modules
ac_add_options --enable-crash-on-assert
%else
ac_add_options --disable-debug
ac_add_options --disable-logging
ac_add_options --enable-optimize="%{rpmcflags}"
%endif
ac_add_options --disable-strip
ac_add_options --disable-strip-libs
%if %{with tests}
ac_add_options --enable-tests
%else
ac_add_options --disable-tests
%endif

ac_add_options --with-distribution-id=org.pld-linux
ac_add_options --with-system-bz2
ac_add_options --with-system-jpeg
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-png
ac_add_options --with-system-zlib
ac_add_options --with-default-mozilla-five-home=%{_libdir}/%{name}

ac_add_options --enable-option-checking=fatal
EOF


%{__make} -j1 -f client.mk build \
	AUTOCONF=autoconf \
	STRIP="/bin/true" \
	CC="%{__cc}" \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
