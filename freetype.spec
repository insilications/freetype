#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC1A60EACE707FDA5 (wl@gnu.org)
#
%define keepstatic 1
Name     : freetype
Version  : 2.10.2
Release  : 64
URL      : https://download-mirror.savannah.gnu.org/releases/freetype/freetype-2.10.2.tar.gz
Source0  : https://download-mirror.savannah.gnu.org/releases/freetype/freetype-2.10.2.tar.gz
Source1  : https://download-mirror.savannah.gnu.org/releases/freetype/freetype-2.10.2.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : FTL GPL-2.0+ MIT Zlib
Requires: freetype-bin = %{version}-%{release}
Requires: freetype-lib = %{version}-%{release}
Requires: freetype-man = %{version}-%{release}
BuildRequires : brotli-dev
BuildRequires : brotli-dev32
BuildRequires : brotli-staticdev
BuildRequires : brotli-staticdev32
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : bzip2-dev
BuildRequires : bzip2-dev32
BuildRequires : bzip2-staticdev
BuildRequires : findutils
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : harfbuzz-dev
BuildRequires : harfbuzz-dev32
BuildRequires : harfbuzz-staticdev
BuildRequires : libpng-dev
BuildRequires : libpng-dev32
BuildRequires : libpng-staticdev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libbrotlicommon)
BuildRequires : pkgconfig(libbrotlidec)
BuildRequires : pkgconfig(libbrotlienc)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
BuildRequires : zlib-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: debuginfo.patch

%description
FreeType 2.10.2
===============
Homepage: https://www.freetype.org
FreeType is a freely available software library to render fonts.

%package bin
Summary: bin components for the freetype package.
Group: Binaries

%description bin
bin components for the freetype package.


%package dev
Summary: dev components for the freetype package.
Group: Development
Requires: freetype-lib = %{version}-%{release}
Requires: freetype-bin = %{version}-%{release}
Provides: freetype-devel = %{version}-%{release}
Requires: freetype = %{version}-%{release}

%description dev
dev components for the freetype package.


%package dev32
Summary: dev32 components for the freetype package.
Group: Default
Requires: freetype-lib32 = %{version}-%{release}
Requires: freetype-bin = %{version}-%{release}
Requires: freetype-dev = %{version}-%{release}

%description dev32
dev32 components for the freetype package.


%package lib
Summary: lib components for the freetype package.
Group: Libraries

%description lib
lib components for the freetype package.


%package lib32
Summary: lib32 components for the freetype package.
Group: Default

%description lib32
lib32 components for the freetype package.


%package man
Summary: man components for the freetype package.
Group: Default

%description man
man components for the freetype package.


%package staticdev
Summary: staticdev components for the freetype package.
Group: Default
Requires: freetype-dev = %{version}-%{release}

%description staticdev
staticdev components for the freetype package.


%package staticdev32
Summary: staticdev32 components for the freetype package.
Group: Default
Requires: freetype-dev = %{version}-%{release}

%description staticdev32
staticdev32 components for the freetype package.


%prep
%setup -q -n freetype-2.10.2
cd %{_builddir}/freetype-2.10.2
%patch1 -p1
pushd ..
cp -a freetype-2.10.2 build32
popd

%build
## build_prepend content
#find . -type f -name 'configure' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'configure.ac' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#
#echo "AM_MAINTAINER_MODE([disable])" >> configure.ac
## build_prepend end
unset http_proxy
unset https_proxy
unset no_proxy
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1596176047
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe $PGO_GEN"
export FCFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe $PGO_GEN"
export FFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe $PGO_GEN"
export LDFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-common -Wno-error -Wp,-D_REENTRANT
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe $PGO_USE"
export FCFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe $PGO_USE"
export FFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe $PGO_USE"
export CXXFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe $PGO_USE"
export LDFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe $PGO_USE"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#export CCACHE_DISABLE=1
## altflags_pgo end
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
%configure  --enable-shared --enable-static --with-harfbuzz --with-png --with-bzip2 --enable-freetype-config --with-brotli --with-zlib
## make_prepend content
#find . -type f -name 'Makefile' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#
#find . -type f -name 'libtool' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1 RC=

VERBOSE=1 V=1 make -j16 check
make clean
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%configure  --enable-shared --enable-static --with-harfbuzz --with-png --with-bzip2 --enable-freetype-config --with-brotli --with-zlib
## make_prepend content
#find . -type f -name 'Makefile' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#
#find . -type f -name 'libtool' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1 RC=

pushd ../build32/
## build_prepend content
#find . -type f -name 'configure' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'configure.ac' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#
#echo "AM_MAINTAINER_MODE([disable])" >> configure.ac
## build_prepend end
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure  --enable-shared --enable-static --with-harfbuzz --with-png --with-bzip2 --enable-freetype-config --with-brotli --with-zlib   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
## make_prepend content
#find . -type f -name 'Makefile' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#
#find . -type f -name 'libtool' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1 RC=
popd

%install
export SOURCE_DATE_EPOCH=1596176047
rm -rf %{buildroot}
pushd ../build32/
%make_install32 V=1 VERBOSE=1 RC=
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install V=1 VERBOSE=1 RC=

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/freetype-config

%files dev
%defattr(-,root,root,-)
/usr/include/freetype2/freetype/config/ftconfig.h
/usr/include/freetype2/freetype/config/ftheader.h
/usr/include/freetype2/freetype/config/ftmodule.h
/usr/include/freetype2/freetype/config/ftoption.h
/usr/include/freetype2/freetype/config/ftstdlib.h
/usr/include/freetype2/freetype/freetype.h
/usr/include/freetype2/freetype/ftadvanc.h
/usr/include/freetype2/freetype/ftbbox.h
/usr/include/freetype2/freetype/ftbdf.h
/usr/include/freetype2/freetype/ftbitmap.h
/usr/include/freetype2/freetype/ftbzip2.h
/usr/include/freetype2/freetype/ftcache.h
/usr/include/freetype2/freetype/ftchapters.h
/usr/include/freetype2/freetype/ftcid.h
/usr/include/freetype2/freetype/ftcolor.h
/usr/include/freetype2/freetype/ftdriver.h
/usr/include/freetype2/freetype/fterrdef.h
/usr/include/freetype2/freetype/fterrors.h
/usr/include/freetype2/freetype/ftfntfmt.h
/usr/include/freetype2/freetype/ftgasp.h
/usr/include/freetype2/freetype/ftglyph.h
/usr/include/freetype2/freetype/ftgxval.h
/usr/include/freetype2/freetype/ftgzip.h
/usr/include/freetype2/freetype/ftimage.h
/usr/include/freetype2/freetype/ftincrem.h
/usr/include/freetype2/freetype/ftlcdfil.h
/usr/include/freetype2/freetype/ftlist.h
/usr/include/freetype2/freetype/ftlzw.h
/usr/include/freetype2/freetype/ftmac.h
/usr/include/freetype2/freetype/ftmm.h
/usr/include/freetype2/freetype/ftmodapi.h
/usr/include/freetype2/freetype/ftmoderr.h
/usr/include/freetype2/freetype/ftotval.h
/usr/include/freetype2/freetype/ftoutln.h
/usr/include/freetype2/freetype/ftparams.h
/usr/include/freetype2/freetype/ftpfr.h
/usr/include/freetype2/freetype/ftrender.h
/usr/include/freetype2/freetype/ftsizes.h
/usr/include/freetype2/freetype/ftsnames.h
/usr/include/freetype2/freetype/ftstroke.h
/usr/include/freetype2/freetype/ftsynth.h
/usr/include/freetype2/freetype/ftsystem.h
/usr/include/freetype2/freetype/fttrigon.h
/usr/include/freetype2/freetype/fttypes.h
/usr/include/freetype2/freetype/ftwinfnt.h
/usr/include/freetype2/freetype/t1tables.h
/usr/include/freetype2/freetype/ttnameid.h
/usr/include/freetype2/freetype/tttables.h
/usr/include/freetype2/freetype/tttags.h
/usr/include/freetype2/ft2build.h
/usr/lib64/libfreetype.so
/usr/lib64/pkgconfig/freetype2.pc
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libfreetype.so
/usr/lib32/pkgconfig/32freetype2.pc
/usr/lib32/pkgconfig/freetype2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfreetype.so.6
/usr/lib64/libfreetype.so.6.17.2

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libfreetype.so.6
/usr/lib32/libfreetype.so.6.17.2

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/freetype-config.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libfreetype.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libfreetype.a
