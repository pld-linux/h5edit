Summary:	HDF5 file editor
Summary(pl.UTF-8):	Edytor plików HDF5
Name:		h5edit
Version:	1.2.0
Release:	1
Group:		Applications/File
License:	BSD-like, changed sources must be marked
Source0:	http://www.hdfgroup.org/ftp/HDF5/projects/jpss/h5edit/%{name}-%{version}.tar.gz
# Source0-md5:	33c8648227ea3d1205f84e9252f1f825
URL:		http://www.hdfgroup.org/projects/npoess/h5edit_index.html
BuildRequires:	hdf5-devel >= 1.8.9
BuildRequires:	szip-devel
BuildRequires:	zlib-devel
Requires:	hdf5 >= 1.8.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HDF5 file editor, h5edit, is a tool for editing an HDF5 file. The
tool can read in a command file, written in the h5edit Command
Language, to edit the file accordingly. Commands can also be specified
by command line options. This is intended for simple and short
commands. The h5edit Command Language is defined in the h5edit Command
Language Definition PDF document (included in package).

%description -l pl.UTF-8
h5edit to edytor plików HDF5, narzędzie służące do modyfikowania
plików HDF5. Potrafi wczytać plik poleceń napisany w języku h5edit
Command Language i zmodyfikować odpowiednio plik HDF5. Polecenia można
podawać także poprzez opcje linii poleceń - głównie z myślą o prostych
i krótkich poleceniach. Język edytora jest zdefiniowany w dokumencie
PDF o nazwie h5edit Command Language Definition (dołączonym do
pakietu).

%prep
%setup -q

%build
%configure

%{__make} \
	h5edit_LDADD="-lhdf5_hl -lhdf5"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING doc/{History,RELEASE.txt,H5edit_User_Guide.pdf,h5edit.pdf,h5edit-Command-Language-Defininition.pdf}
%attr(755,root,root) %{_bindir}/h5edit
