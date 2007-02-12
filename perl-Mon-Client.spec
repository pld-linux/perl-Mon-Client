#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		_rc		pre2
%define		_realname	mon-client
Summary:	Perl modules for interfacing with the mon package
Summary(pl.UTF-8):	Moduły Perla do współpracy z pakietem mon
Name:		perl-Mon-Client
Version:	1.0.0
Release:	0.%{_rc}.0.2
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	ftp://ftp.kernel.org/pub/software/admin/mon/devel/%{_realname}-%{version}%{_rc}.tar.bz2
# Source0-md5:	fecf57b02fd35bddcd242c5f4a303359
URL:		http://www.kernel.org/software/mon/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Perl5 module for interfacing with the Mon system
monitoring package. Currently only the client interface is
implemented, but more things like special logging routines and
persistent monitors are being considered.

"mon" is a tool for monitoring the availability of services. More
information can be found at <http://www.kernel.org/software/mon/> and
<https://sourceforge.net/projects/mon/>.

%description -l pl.UTF-8
To jest moduł Perla 5 do współpracy z pakietem monitorowania systemu
Mon. Aktualnie zaimplementowany jest tylko interfejs kliencki, ale pod
uwagę brane jest więcej elementów, takich jak procedury do specjalnego
logowania czy stałe monitory.

"mon" to narzędzei do monitorowania dostępności usług. Więcej
informacji pożna znaleźć pod <http://www.kernel.org/software/mon/>
oraz <https://sourceforge.net/projects/mon/>.

%prep
%setup -q -n %{_realname}-%{version}%{_rc}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Mon/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{perl_vendorlib}/Mon
%{perl_vendorlib}/Mon/Client.pm
%{perl_vendorlib}/Mon/Config.pm
%{perl_vendorlib}/Mon/Protocol.pm
%{perl_vendorlib}/Mon/SNMP.pm
%{_mandir}/man3/Mon::Client.3pm*
%{_mandir}/man3/Mon::Config.3pm*
%{_mandir}/man3/Mon::Protocol.3pm*
%{_mandir}/man3/Mon::SNMP.3pm*
