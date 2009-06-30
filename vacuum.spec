Summary:	Fast paced original action game
Summary(pl.UTF-8):	Oryginalna gra akcji z szybkim tempem
Name:		vacuum
Version:	0.12
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/vacuum/%{name}-%{version}.tar.gz
# Source0-md5:	f94eccf4ed6972396951038078c1b17a
Source1:	%{name}.desktop
URL:		http://apocalypse.rulez.org/vacuum/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-SDL
Requires:	perl-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vacuum Magic is a fast-paced action game. The point of the game is
using your magical vacuum field to collect food and defend against
monsters. Food and certain monsters can also be spat out and used as a
projectile against other monsters.

Vacuum Magic can be played by up to six players, either cooperatively,
or against each other.

%description -l pl.UTF-8
Vacuum Magic jest grą akcji, którą cechuje szybkie tempo. Gracz
używa swojej magi w celu zbierania pożywienia i obrony przed
potworami. Pożywienie oraz niektóre potwory mogą być użyte jako
pociski przeciwko innym potworom.

W Vacuum Magic może grać do sześciu graczy, zarówno w trybie
kooperacyjnym, jak również przeciwko sobie.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install data/icon.png $RPM_BUILD_ROOT%{_pixmapsdir}/vacuum.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/vacuum
%{_datadir}/%{name}
%{_desktopdir}/vacuum.desktop
%{_mandir}/man6/vacuum.*
%{_pixmapsdir}/vacuum.png
