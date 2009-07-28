Summary:	A single program for chatting on all famous networks!
Name:		instantbird
Version:	0.1.3.1
Release:	0.1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		Applications/Networking
URL:		http://www.instantbird.com/
Source0:	http://www.instantbird.com/downloads/%{version}/%{name}-%{version}.src.tar.bz2
# Source0-md5:	d9f9a93326d97de14b79d4d0fac09d29
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Instantbird is a multi-protocol Instant Messaging client. Using it,
you can connect to all your different IM accounts.

It uses the Mozilla rendering engine to display IMs, and the Pidgin
libpurple to connect to the different networks.

%prep
%setup -q -n %{name}-%{version}-src

%build
cd mozilla

%{__make} -j1 -f client.mk build \
	STRIP="/bin/true" \
	CC="%{__cc}" \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
