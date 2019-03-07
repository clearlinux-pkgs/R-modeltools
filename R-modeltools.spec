#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-modeltools
Version  : 0.2.22
Release  : 14
URL      : https://cran.r-project.org/src/contrib/modeltools_0.2-22.tar.gz
Source0  : https://cran.r-project.org/src/contrib/modeltools_0.2-22.tar.gz
Summary  : Tools and Classes for Statistical Models
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : clr-R-helpers

%description
The functionality is experimental and the user interface is likely to
  change in the future. The documentation is rather terse, but packages `coin'
  and `party' have some working examples. However, if you find the
  implemented ideas interesting we would be very interested in a discussion
  of this proposal. Contributions are more than welcome!

%prep
%setup -q -c -n modeltools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1531797053

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1531797053
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library modeltools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library modeltools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library modeltools
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library modeltools|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/modeltools/DESCRIPTION
/usr/lib64/R/library/modeltools/INDEX
/usr/lib64/R/library/modeltools/Meta/Rd.rds
/usr/lib64/R/library/modeltools/Meta/features.rds
/usr/lib64/R/library/modeltools/Meta/hsearch.rds
/usr/lib64/R/library/modeltools/Meta/links.rds
/usr/lib64/R/library/modeltools/Meta/nsInfo.rds
/usr/lib64/R/library/modeltools/Meta/package.rds
/usr/lib64/R/library/modeltools/NAMESPACE
/usr/lib64/R/library/modeltools/NEWS
/usr/lib64/R/library/modeltools/R/modeltools
/usr/lib64/R/library/modeltools/R/modeltools.rdb
/usr/lib64/R/library/modeltools/R/modeltools.rdx
/usr/lib64/R/library/modeltools/help/AnIndex
/usr/lib64/R/library/modeltools/help/aliases.rds
/usr/lib64/R/library/modeltools/help/modeltools.rdb
/usr/lib64/R/library/modeltools/help/modeltools.rdx
/usr/lib64/R/library/modeltools/help/paths.rds
/usr/lib64/R/library/modeltools/html/00Index.html
/usr/lib64/R/library/modeltools/html/R.css
