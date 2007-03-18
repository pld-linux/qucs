Summary:	An integrated circuit simulator
Summary(de.UTF-8):	Ein Schaltungs Simulator
Summary(pl.UTF-8):	Symulator układów elektronicznych
Name:		qucs
Version:	0.0.11
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qucs/%{name}-%{version}.tar.gz
# Source0-md5:	2bc139dd30d4d9e83760bafb497f1654
Source1:	%{name}.desktop
URL:		http://www.kde-apps.org/content/show.php?content=21644
BuildRequires:	qt-devel >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qucs provides a GUI based on Qt for setting up electronical circuits,
simulator, which is able to simulate the small- and large signal and
noise behaviour of microwave circuits. The results can be shown on as
pecial presentation page in different formats (rect, polar, smith,
tabular).

%description -l de.UTF-8
Qucs liefert ein GUI dass auf Qt basiert und simuliert elektronische
Schaltkreise, die es ermöglichen kleine und grosse Signale und
Störgeräusche auf Mikro Chips zu simulieren. Die Resultate können in
der Form von Präsentationen in diversen Formaten dargestellt werden.

%description -l pl.UTF-8
Qucs dostarczas GUI oparte o bibliotekę Qt do symulacji układów
elektronicznych, które umożliwiają symulowanie różnych sygnałów i
szumów w układach scalonych. Wyniki mogą być obrazowane jako specjalne
prezentacje w różnych formatach.

%prep
%setup -q

%build
export QTDIR="%{_prefix}"
%configure

%{__make} \
        CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install qucs/bitmaps/biast.png $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc RELEASE README THANKS TODO AUTHORS NEWS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man?/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/biast.png
