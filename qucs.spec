Summary:	An integrated circuit simulator
Summary(de):	Ein Schaltungs Simulator
Summary(pl):	Symulator uk�ad�w elektronicznych
Name:		qucs
Version:	0.0.9
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qucs/%{name}-%{version}.tar.gz
# Source0-md5:	863eba475f35d006325f9d49671a2031
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

%description -l de
Qucs liefert ein GUI dass auf Qt basiert und simuliert elektronische
Schaltkreise, die es erm�glichen kleine und grosse Signale und
St�rger�usche auf Mikro Chips zu simulieren. Die Resultate k�nnen in
der Form von Pr�sentationen in diversen Formaten dargestellt werden.

%description -l pl
Qucs dostarczas GUI oparte o bibliotek� Qt do symulacji uk�ad�w
elektronicznych, kt�re umo�liwiaj� symulowanie r�nych sygna��w i
szum�w w uk�adach scalonych. Wyniki mog� by� obrazowane jako specjalne
prezentacje w r�nych formatach.

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
