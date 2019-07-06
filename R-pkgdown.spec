#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pkgdown
Version  : 1.3.0
Release  : 9
URL      : https://cran.r-project.org/src/contrib/pkgdown_1.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pkgdown_1.3.0.tar.gz
Summary  : Make Static HTML Documentation for a Package
Group    : Development/Tools
License  : MIT
BuildRequires : R-callr
BuildRequires : R-commonmark
BuildRequires : R-desc
BuildRequires : R-devtools
BuildRequires : R-fs
BuildRequires : R-highlight
BuildRequires : R-httr
BuildRequires : R-memoise
BuildRequires : R-openssl
BuildRequires : R-pkgload
BuildRequires : R-purrr
BuildRequires : R-rematch2
BuildRequires : R-rmarkdown
BuildRequires : R-roxygen2
BuildRequires : R-rsconnect
BuildRequires : R-rstudioapi
BuildRequires : R-tibble
BuildRequires : R-usethis
BuildRequires : R-whisker
BuildRequires : R-withr
BuildRequires : R-xml2
BuildRequires : R-yaml
BuildRequires : buildreq-R

%description
# pkgdown <img src="man/figures/logo.png" align="right" alt="" width="120" />
[![Travis-CI build
status](https://travis-ci.org/r-lib/pkgdown.svg?branch=master)](https://travis-ci.org/r-lib/pkgdown)
[![AppVeyor build
status](https://ci.appveyor.com/api/projects/status/github/r-lib/pkgdown?branch=master&svg=true)](https://ci.appveyor.com/project/r-lib/pkgdown)
[![Lifecycle:
maturing](https://img.shields.io/badge/lifecycle-maturing-blue.svg)](https://www.tidyverse.org/lifecycle/#maturing)
[![CRAN
Status](https://www.r-pkg.org/badges/version/pkgdown)](https://cran.r-project.org/package=pkgdown)
[![Codecov test
coverage](https://img.shields.io/codecov/c/github/r-lib/pkgdown/master.svg)](https://codecov.io/github/r-lib/pkgdown?branch=master)

%prep
%setup -q -c -n pkgdown

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552886585

%install
export SOURCE_DATE_EPOCH=1552886585
rm -rf %{buildroot}
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pkgdown
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pkgdown
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pkgdown
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  pkgdown || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pkgdown/DESCRIPTION
/usr/lib64/R/library/pkgdown/INDEX
/usr/lib64/R/library/pkgdown/LICENSE
/usr/lib64/R/library/pkgdown/Meta/Rd.rds
/usr/lib64/R/library/pkgdown/Meta/features.rds
/usr/lib64/R/library/pkgdown/Meta/hsearch.rds
/usr/lib64/R/library/pkgdown/Meta/links.rds
/usr/lib64/R/library/pkgdown/Meta/nsInfo.rds
/usr/lib64/R/library/pkgdown/Meta/package.rds
/usr/lib64/R/library/pkgdown/Meta/vignette.rds
/usr/lib64/R/library/pkgdown/NAMESPACE
/usr/lib64/R/library/pkgdown/NEWS.md
/usr/lib64/R/library/pkgdown/R/pkgdown
/usr/lib64/R/library/pkgdown/R/pkgdown.rdb
/usr/lib64/R/library/pkgdown/R/pkgdown.rdx
/usr/lib64/R/library/pkgdown/assets/docsearch.css
/usr/lib64/R/library/pkgdown/assets/docsearch.js
/usr/lib64/R/library/pkgdown/assets/link.svg
/usr/lib64/R/library/pkgdown/assets/pkgdown.css
/usr/lib64/R/library/pkgdown/assets/pkgdown.js
/usr/lib64/R/library/pkgdown/doc/index.html
/usr/lib64/R/library/pkgdown/doc/pkgdown.Rmd
/usr/lib64/R/library/pkgdown/doc/pkgdown.html
/usr/lib64/R/library/pkgdown/help/AnIndex
/usr/lib64/R/library/pkgdown/help/aliases.rds
/usr/lib64/R/library/pkgdown/help/figures/bacon.jpg
/usr/lib64/R/library/pkgdown/help/figures/logo.png
/usr/lib64/R/library/pkgdown/help/paths.rds
/usr/lib64/R/library/pkgdown/help/pkgdown.rdb
/usr/lib64/R/library/pkgdown/help/pkgdown.rdx
/usr/lib64/R/library/pkgdown/html/00Index.html
/usr/lib64/R/library/pkgdown/html/R.css
/usr/lib64/R/library/pkgdown/rstudio/addins.dcf
/usr/lib64/R/library/pkgdown/templates/config-docsearch.json
/usr/lib64/R/library/pkgdown/templates/content-article-index.html
/usr/lib64/R/library/pkgdown/templates/content-article.html
/usr/lib64/R/library/pkgdown/templates/content-authors.html
/usr/lib64/R/library/pkgdown/templates/content-citation-authors.html
/usr/lib64/R/library/pkgdown/templates/content-home.html
/usr/lib64/R/library/pkgdown/templates/content-news-index.html
/usr/lib64/R/library/pkgdown/templates/content-news.html
/usr/lib64/R/library/pkgdown/templates/content-reference-index.html
/usr/lib64/R/library/pkgdown/templates/content-reference-topic.html
/usr/lib64/R/library/pkgdown/templates/content-title-body.html
/usr/lib64/R/library/pkgdown/templates/content-tutorial-index.html
/usr/lib64/R/library/pkgdown/templates/content-tutorial.html
/usr/lib64/R/library/pkgdown/templates/docsearch.html
/usr/lib64/R/library/pkgdown/templates/footer.html
/usr/lib64/R/library/pkgdown/templates/head.html
/usr/lib64/R/library/pkgdown/templates/header.html
/usr/lib64/R/library/pkgdown/templates/layout.html
/usr/lib64/R/library/pkgdown/templates/navbar.html
/usr/lib64/R/library/pkgdown/tests/testthat.R
/usr/lib64/R/library/pkgdown/tests/testthat/assets/autolink.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/autolink.html
/usr/lib64/R/library/pkgdown/tests/testthat/assets/cname/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/cname/_pkgdown.yml
/usr/lib64/R/library/pkgdown/tests/testthat/assets/figure/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/figure/_pkgdown.yml
/usr/lib64/R/library/pkgdown/tests/testthat/assets/figure/man/figure.Rd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/figure/vignettes/figures.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/home-empty-readme-md/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/home-empty-readme-md/README.md
/usr/lib64/R/library/pkgdown/tests/testthat/assets/home-index-rmd/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/home-index-rmd/index.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/home-links.html
/usr/lib64/R/library/pkgdown/tests/testthat/assets/home-old-skool/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/home-old-skool/NAMESPACE
/usr/lib64/R/library/pkgdown/tests/testthat/assets/home-page-header.html
/usr/lib64/R/library/pkgdown/tests/testthat/assets/home-readme-rmd/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/home-readme-rmd/NAMESPACE
/usr/lib64/R/library/pkgdown/tests/testthat/assets/home-readme-rmd/README.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/home-readme-rmd/README.md
/usr/lib64/R/library/pkgdown/tests/testthat/assets/init-extra-1/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/init-extra-1/README.md
/usr/lib64/R/library/pkgdown/tests/testthat/assets/init-extra-1/pkgdown/extra.css
/usr/lib64/R/library/pkgdown/tests/testthat/assets/init-extra-2/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/init-extra-2/README.md
/usr/lib64/R/library/pkgdown/tests/testthat/assets/init-extra-2/pkgdown/extra.css
/usr/lib64/R/library/pkgdown/tests/testthat/assets/init-extra-2/pkgdown/extra.js
/usr/lib64/R/library/pkgdown/tests/testthat/assets/news-bad-nesting/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/news-bad-nesting/NEWS.md
/usr/lib64/R/library/pkgdown/tests/testthat/assets/news-github-links/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/news-github-links/NEWS.md
/usr/lib64/R/library/pkgdown/tests/testthat/assets/news-multi-page/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/news-multi-page/NEWS.md
/usr/lib64/R/library/pkgdown/tests/testthat/assets/news-multi-page/_pkgdown.yml
/usr/lib64/R/library/pkgdown/tests/testthat/assets/news/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/news/NEWS.md
/usr/lib64/R/library/pkgdown/tests/testthat/assets/open-graph/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/open-graph/NAMESPACE
/usr/lib64/R/library/pkgdown/tests/testthat/assets/open-graph/R/f.R
/usr/lib64/R/library/pkgdown/tests/testthat/assets/open-graph/_pkgdown.yml
/usr/lib64/R/library/pkgdown/tests/testthat/assets/open-graph/logo.png
/usr/lib64/R/library/pkgdown/tests/testthat/assets/open-graph/man/f.Rd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/open-graph/vignettes/open-graph.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/search-site/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/search-site/_pkgdown.yml
/usr/lib64/R/library/pkgdown/tests/testthat/assets/search-site/docs/CNAME
/usr/lib64/R/library/pkgdown/tests/testthat/assets/search-site/sitemaps-schema-0.9.xsd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/site-dot-github/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/site-dot-github/README.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/site-empty/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/site-empty/NAMESPACE
/usr/lib64/R/library/pkgdown/tests/testthat/assets/site-orcid/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/tutorials-inst/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/tutorials-inst/inst/tutorials/test-1/test-1.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/tutorials-inst/inst/tutorials/test-1/tutorial-test-1.dcf
/usr/lib64/R/library/pkgdown/tests/testthat/assets/tutorials-vignettes/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/tutorials-vignettes/vignettes/tutorials/test-1/test-1.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/tweak-anchor.html
/usr/lib64/R/library/pkgdown/tests/testthat/assets/vignette-with-img.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/test-autolink_html.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-citation-authors.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-cname.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-home-authors.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-home-index.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-home-license.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-news.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-search-docs.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build.r
/usr/lib64/R/library/pkgdown/tests/testthat/test-build_article.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build_home.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build_site.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-development.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-figure.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-github.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-highlight.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-html-build.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-html-tweak.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-init.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-link-href.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-link-packages.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-metadata.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-rd-html.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-replay-html.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-template-content.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-topics.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-tutorials.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-usage.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-utils.R
