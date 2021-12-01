#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pkgdown
Version  : 2.0.0
Release  : 30
URL      : https://cran.r-project.org/src/contrib/pkgdown_2.0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pkgdown_2.0.0.tar.gz
Summary  : Make Static HTML Documentation for a Package
Group    : Development/Tools
License  : MIT
Requires: R-bslib
Requires: R-callr
Requires: R-crayon
Requires: R-desc
Requires: R-digest
Requires: R-downlit
Requires: R-fs
Requires: R-httr
Requires: R-jsonlite
Requires: R-magrittr
Requires: R-memoise
Requires: R-purrr
Requires: R-ragg
Requires: R-rlang
Requires: R-rmarkdown
Requires: R-tibble
Requires: R-whisker
Requires: R-withr
Requires: R-xml2
Requires: R-yaml
BuildRequires : R-bslib
BuildRequires : R-callr
BuildRequires : R-crayon
BuildRequires : R-desc
BuildRequires : R-digest
BuildRequires : R-downlit
BuildRequires : R-fs
BuildRequires : R-httr
BuildRequires : R-jsonlite
BuildRequires : R-magrittr
BuildRequires : R-memoise
BuildRequires : R-purrr
BuildRequires : R-ragg
BuildRequires : R-rlang
BuildRequires : R-rmarkdown
BuildRequires : R-tibble
BuildRequires : R-whisker
BuildRequires : R-withr
BuildRequires : R-xml2
BuildRequires : R-yaml
BuildRequires : buildreq-R

%description
package.  'pkgdown' converts your documentation, vignettes, 'README',
    and more to 'HTML' making it easy to share information about your
    package online.

%prep
%setup -q -c -n pkgdown
cd %{_builddir}/pkgdown

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1638370395

%install
export SOURCE_DATE_EPOCH=1638370395
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pkgdown
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pkgdown
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pkgdown
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc pkgdown || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pkgdown/BS3/assets/bootstrap-toc.css
/usr/lib64/R/library/pkgdown/BS3/assets/bootstrap-toc.js
/usr/lib64/R/library/pkgdown/BS3/assets/docsearch.css
/usr/lib64/R/library/pkgdown/BS3/assets/docsearch.js
/usr/lib64/R/library/pkgdown/BS3/assets/link.svg
/usr/lib64/R/library/pkgdown/BS3/assets/pkgdown.css
/usr/lib64/R/library/pkgdown/BS3/assets/pkgdown.js
/usr/lib64/R/library/pkgdown/BS3/templates/after-body.html
/usr/lib64/R/library/pkgdown/BS3/templates/before-body.html
/usr/lib64/R/library/pkgdown/BS3/templates/config-docsearch.json
/usr/lib64/R/library/pkgdown/BS3/templates/content-article-index.html
/usr/lib64/R/library/pkgdown/BS3/templates/content-article.html
/usr/lib64/R/library/pkgdown/BS3/templates/content-citation-authors.html
/usr/lib64/R/library/pkgdown/BS3/templates/content-home.html
/usr/lib64/R/library/pkgdown/BS3/templates/content-news-index.html
/usr/lib64/R/library/pkgdown/BS3/templates/content-news.html
/usr/lib64/R/library/pkgdown/BS3/templates/content-reference-index.html
/usr/lib64/R/library/pkgdown/BS3/templates/content-reference-topic.html
/usr/lib64/R/library/pkgdown/BS3/templates/content-title-body.html
/usr/lib64/R/library/pkgdown/BS3/templates/content-tutorial-index.html
/usr/lib64/R/library/pkgdown/BS3/templates/content-tutorial.html
/usr/lib64/R/library/pkgdown/BS3/templates/docsearch.html
/usr/lib64/R/library/pkgdown/BS3/templates/footer.html
/usr/lib64/R/library/pkgdown/BS3/templates/head.html
/usr/lib64/R/library/pkgdown/BS3/templates/header.html
/usr/lib64/R/library/pkgdown/BS3/templates/in-header.html
/usr/lib64/R/library/pkgdown/BS3/templates/layout-redirect.html
/usr/lib64/R/library/pkgdown/BS3/templates/layout.html
/usr/lib64/R/library/pkgdown/BS3/templates/navbar.html
/usr/lib64/R/library/pkgdown/BS5/assets/link.svg
/usr/lib64/R/library/pkgdown/BS5/assets/pkgdown.js
/usr/lib64/R/library/pkgdown/BS5/assets/pkgdown.scss
/usr/lib64/R/library/pkgdown/BS5/assets/syntax-highlighting.scss
/usr/lib64/R/library/pkgdown/BS5/templates/after-body.html
/usr/lib64/R/library/pkgdown/BS5/templates/before-body.html
/usr/lib64/R/library/pkgdown/BS5/templates/config-docsearch.json
/usr/lib64/R/library/pkgdown/BS5/templates/content-article-index.html
/usr/lib64/R/library/pkgdown/BS5/templates/content-article.html
/usr/lib64/R/library/pkgdown/BS5/templates/content-authors.html
/usr/lib64/R/library/pkgdown/BS5/templates/content-citation-authors.html
/usr/lib64/R/library/pkgdown/BS5/templates/content-home.html
/usr/lib64/R/library/pkgdown/BS5/templates/content-news-index.html
/usr/lib64/R/library/pkgdown/BS5/templates/content-news.html
/usr/lib64/R/library/pkgdown/BS5/templates/content-reference-index.html
/usr/lib64/R/library/pkgdown/BS5/templates/content-reference-topic.html
/usr/lib64/R/library/pkgdown/BS5/templates/content-title-body.html
/usr/lib64/R/library/pkgdown/BS5/templates/content-tutorial-index.html
/usr/lib64/R/library/pkgdown/BS5/templates/content-tutorial.html
/usr/lib64/R/library/pkgdown/BS5/templates/footer.html
/usr/lib64/R/library/pkgdown/BS5/templates/head.html
/usr/lib64/R/library/pkgdown/BS5/templates/header.html
/usr/lib64/R/library/pkgdown/BS5/templates/in-header.html
/usr/lib64/R/library/pkgdown/BS5/templates/layout-redirect.html
/usr/lib64/R/library/pkgdown/BS5/templates/layout.html
/usr/lib64/R/library/pkgdown/BS5/templates/navbar.html
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
/usr/lib64/R/library/pkgdown/doc/customise.R
/usr/lib64/R/library/pkgdown/doc/customise.Rmd
/usr/lib64/R/library/pkgdown/doc/customise.html
/usr/lib64/R/library/pkgdown/doc/index.html
/usr/lib64/R/library/pkgdown/doc/linking.R
/usr/lib64/R/library/pkgdown/doc/linking.Rmd
/usr/lib64/R/library/pkgdown/doc/linking.html
/usr/lib64/R/library/pkgdown/doc/metadata.R
/usr/lib64/R/library/pkgdown/doc/metadata.Rmd
/usr/lib64/R/library/pkgdown/doc/metadata.html
/usr/lib64/R/library/pkgdown/doc/pkgdown.R
/usr/lib64/R/library/pkgdown/doc/pkgdown.Rmd
/usr/lib64/R/library/pkgdown/doc/pkgdown.html
/usr/lib64/R/library/pkgdown/doc/search.R
/usr/lib64/R/library/pkgdown/doc/search.Rmd
/usr/lib64/R/library/pkgdown/doc/search.html
/usr/lib64/R/library/pkgdown/help/AnIndex
/usr/lib64/R/library/pkgdown/help/aliases.rds
/usr/lib64/R/library/pkgdown/help/figures/bacon.jpg
/usr/lib64/R/library/pkgdown/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/pkgdown/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/pkgdown/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/pkgdown/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/pkgdown/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/pkgdown/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/pkgdown/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/pkgdown/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/pkgdown/help/figures/logo.png
/usr/lib64/R/library/pkgdown/help/paths.rds
/usr/lib64/R/library/pkgdown/help/pkgdown.rdb
/usr/lib64/R/library/pkgdown/help/pkgdown.rdx
/usr/lib64/R/library/pkgdown/highlight-styles/arrow-dark.scss
/usr/lib64/R/library/pkgdown/highlight-styles/arrow-light.scss
/usr/lib64/R/library/pkgdown/highlight-styles/atom-one-dark.scss
/usr/lib64/R/library/pkgdown/highlight-styles/atom-one-light.scss
/usr/lib64/R/library/pkgdown/highlight-styles/ayu-dark.scss
/usr/lib64/R/library/pkgdown/highlight-styles/ayu-light.scss
/usr/lib64/R/library/pkgdown/highlight-styles/ayu-mirage.scss
/usr/lib64/R/library/pkgdown/highlight-styles/breeze-dark.scss
/usr/lib64/R/library/pkgdown/highlight-styles/breeze-light.scss
/usr/lib64/R/library/pkgdown/highlight-styles/breezedark.scss
/usr/lib64/R/library/pkgdown/highlight-styles/dracula.scss
/usr/lib64/R/library/pkgdown/highlight-styles/espresso.scss
/usr/lib64/R/library/pkgdown/highlight-styles/github-dark.scss
/usr/lib64/R/library/pkgdown/highlight-styles/github-light.scss
/usr/lib64/R/library/pkgdown/highlight-styles/gruvbox-dark.scss
/usr/lib64/R/library/pkgdown/highlight-styles/gruvbox-light.scss
/usr/lib64/R/library/pkgdown/highlight-styles/haddock.scss
/usr/lib64/R/library/pkgdown/highlight-styles/kate.scss
/usr/lib64/R/library/pkgdown/highlight-styles/monochrome.scss
/usr/lib64/R/library/pkgdown/highlight-styles/monokai.scss
/usr/lib64/R/library/pkgdown/highlight-styles/nord.scss
/usr/lib64/R/library/pkgdown/highlight-styles/oblivion.scss
/usr/lib64/R/library/pkgdown/highlight-styles/printing.scss
/usr/lib64/R/library/pkgdown/highlight-styles/pygments.scss
/usr/lib64/R/library/pkgdown/highlight-styles/radical.scss
/usr/lib64/R/library/pkgdown/highlight-styles/solarized-dark.scss
/usr/lib64/R/library/pkgdown/highlight-styles/solarized-light.scss
/usr/lib64/R/library/pkgdown/highlight-styles/tango.scss
/usr/lib64/R/library/pkgdown/highlight-styles/vim-dark.scss
/usr/lib64/R/library/pkgdown/highlight-styles/zenburn.scss
/usr/lib64/R/library/pkgdown/html/00Index.html
/usr/lib64/R/library/pkgdown/html/R.css
/usr/lib64/R/library/pkgdown/po/de/LC_MESSAGES/R-pkgdown.mo
/usr/lib64/R/library/pkgdown/po/es/LC_MESSAGES/R-pkgdown.mo
/usr/lib64/R/library/pkgdown/po/fr/LC_MESSAGES/R-pkgdown.mo
/usr/lib64/R/library/pkgdown/po/pt/LC_MESSAGES/R-pkgdown.mo
/usr/lib64/R/library/pkgdown/po/tr/LC_MESSAGES/R-pkgdown.mo
/usr/lib64/R/library/pkgdown/po/zh_CN/LC_MESSAGES/R-pkgdown.mo
/usr/lib64/R/library/pkgdown/rstudio/addins.dcf
/usr/lib64/R/library/pkgdown/tests/testthat.R
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/build-articles.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/build-favicons.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/build-footer.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/build-home-authors.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/build-home-citation.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/build-home-community.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/build-home-index.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/build-home.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/build-logo.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/build-news.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/build-redirects.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/build-reference-index.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/build-reference.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/build-search-docs/search-no-url.json
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/build-search-docs/search.json
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/development.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/highlight.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/init.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/markdown.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/navbar.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/package.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/rd-html.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/render.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/repo.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/rmarkdown.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/sitrep.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/topics.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/tweak-tabset.md
/usr/lib64/R/library/pkgdown/tests/testthat/_snaps/tweak-tags.md
/usr/lib64/R/library/pkgdown/tests/testthat/assets/articles-resources/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/articles-resources/vignettes/external.png
/usr/lib64/R/library/pkgdown/tests/testthat/assets/articles-resources/vignettes/resources.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/articles/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/articles/vignettes/articles/nested.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/articles/vignettes/html-document.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/articles/vignettes/html-vignette.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/articles/vignettes/standard.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/articles/vignettes/toc-false.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/articles/vignettes/widget.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/articles/vignettes/width.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/bad-images/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/bad-images/README.md
/usr/lib64/R/library/pkgdown/tests/testthat/assets/bad-images/vignettes/html-vignette.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/cname/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/cname/_pkgdown.yml
/usr/lib64/R/library/pkgdown/tests/testthat/assets/figure/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/figure/_pkgdown.yml
/usr/lib64/R/library/pkgdown/tests/testthat/assets/figure/man/figure.Rd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/figure/vignettes/figures.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/home-index-rmd/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/home-index-rmd/index.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/home-old-skool/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/home-old-skool/NAMESPACE
/usr/lib64/R/library/pkgdown/tests/testthat/assets/home-readme-rmd/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/home-readme-rmd/NAMESPACE
/usr/lib64/R/library/pkgdown/tests/testthat/assets/home-readme-rmd/README.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/home-readme-rmd/README.md
/usr/lib64/R/library/pkgdown/tests/testthat/assets/init-asset-subdirs/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/init-asset-subdirs/README.md
/usr/lib64/R/library/pkgdown/tests/testthat/assets/init-asset-subdirs/pkgdown/_pkgdown.yml
/usr/lib64/R/library/pkgdown/tests/testthat/assets/init-asset-subdirs/pkgdown/assets/subdir1/file1.txt
/usr/lib64/R/library/pkgdown/tests/testthat/assets/init-asset-subdirs/pkgdown/assets/subdir1/subdir2/file2.txt
/usr/lib64/R/library/pkgdown/tests/testthat/assets/init-extra-1/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/init-extra-1/README.md
/usr/lib64/R/library/pkgdown/tests/testthat/assets/init-extra-1/pkgdown/extra.css
/usr/lib64/R/library/pkgdown/tests/testthat/assets/init-extra-2/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/init-extra-2/README.md
/usr/lib64/R/library/pkgdown/tests/testthat/assets/init-extra-2/pkgdown/extra.css
/usr/lib64/R/library/pkgdown/tests/testthat/assets/init-extra-2/pkgdown/extra.js
/usr/lib64/R/library/pkgdown/tests/testthat/assets/man-figures/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/man-figures/README.md
/usr/lib64/R/library/pkgdown/tests/testthat/assets/man-figures/_pkgdown.yml
/usr/lib64/R/library/pkgdown/tests/testthat/assets/man-figures/man/figures/kitten.jpg
/usr/lib64/R/library/pkgdown/tests/testthat/assets/man-figures/man/kitten.Rd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/man-figures/vignettes/another-kitten.jpg
/usr/lib64/R/library/pkgdown/tests/testthat/assets/man-figures/vignettes/kitten.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/news-bad-nesting/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/news-bad-nesting/NEWS.md
/usr/lib64/R/library/pkgdown/tests/testthat/assets/news-github-links/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/news-github-links/NEWS.md
/usr/lib64/R/library/pkgdown/tests/testthat/assets/news-multi-page/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/news-multi-page/NEWS.md
/usr/lib64/R/library/pkgdown/tests/testthat/assets/news-multi-page/_pkgdown.yml
/usr/lib64/R/library/pkgdown/tests/testthat/assets/news/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/news/NEWS.md
/usr/lib64/R/library/pkgdown/tests/testthat/assets/news/README.md
/usr/lib64/R/library/pkgdown/tests/testthat/assets/open-graph-customized/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/open-graph-customized/NAMESPACE
/usr/lib64/R/library/pkgdown/tests/testthat/assets/open-graph-customized/R/f.R
/usr/lib64/R/library/pkgdown/tests/testthat/assets/open-graph-customized/_pkgdown.yml
/usr/lib64/R/library/pkgdown/tests/testthat/assets/open-graph-customized/man/f.Rd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/open-graph-customized/man/figures/card.png
/usr/lib64/R/library/pkgdown/tests/testthat/assets/open-graph-customized/vignettes/no-description.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/open-graph-customized/vignettes/open-graph.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/open-graph/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/open-graph/NAMESPACE
/usr/lib64/R/library/pkgdown/tests/testthat/assets/open-graph/R/f.R
/usr/lib64/R/library/pkgdown/tests/testthat/assets/open-graph/_pkgdown.yml
/usr/lib64/R/library/pkgdown/tests/testthat/assets/open-graph/logo.png
/usr/lib64/R/library/pkgdown/tests/testthat/assets/open-graph/man/f.Rd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/open-graph/vignettes/open-graph.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/pandoc-fail.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/reference-fail/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/reference-fail/NAMESPACE
/usr/lib64/R/library/pkgdown/tests/testthat/assets/reference-fail/R/f.R
/usr/lib64/R/library/pkgdown/tests/testthat/assets/reference-fail/man/f.Rd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/reference-pre-post/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/reference-pre-post/pkgdown/post-reference.R
/usr/lib64/R/library/pkgdown/tests/testthat/assets/reference-pre-post/pkgdown/pre-reference.R
/usr/lib64/R/library/pkgdown/tests/testthat/assets/reference/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/reference/NAMESPACE
/usr/lib64/R/library/pkgdown/tests/testthat/assets/reference/R/funs.R
/usr/lib64/R/library/pkgdown/tests/testthat/assets/reference/_pkgdown.yml
/usr/lib64/R/library/pkgdown/tests/testthat/assets/reference/man/a.Rd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/reference/man/b.Rd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/reference/man/c.Rd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/reference/man/help.Rd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/search-site/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/search-site/_pkgdown.yml
/usr/lib64/R/library/pkgdown/tests/testthat/assets/search-site/sitemaps-schema-0.9.xsd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/sidebar-comment/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/sidebar/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/sidebar/README.md
/usr/lib64/R/library/pkgdown/tests/testthat/assets/sidebar/_pkgdown.yml
/usr/lib64/R/library/pkgdown/tests/testthat/assets/sidebar/sidebar.html
/usr/lib64/R/library/pkgdown/tests/testthat/assets/site-bad-logo/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/site-bad-logo/_pkgdown.yml
/usr/lib64/R/library/pkgdown/tests/testthat/assets/site-bad-logo/logo.png
/usr/lib64/R/library/pkgdown/tests/testthat/assets/site-dot-github/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/site-dot-github/README.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/site-empty/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/site-empty/NAMESPACE
/usr/lib64/R/library/pkgdown/tests/testthat/assets/site-favicons/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/site-favicons/logo.png
/usr/lib64/R/library/pkgdown/tests/testthat/assets/site-favicons/pkgdown/favicon/favicon.ico
/usr/lib64/R/library/pkgdown/tests/testthat/assets/templates-local/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/templates-local/pkgdown/templates/content-article.html
/usr/lib64/R/library/pkgdown/tests/testthat/assets/templates-local/pkgdown/templates/footer-article.html
/usr/lib64/R/library/pkgdown/tests/testthat/assets/tutorials/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/tutorials/vignettes/tutorials/test-1/test-1.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/tutorials/vignettes/tutorials/test-1/tutorial-test-1.dcf
/usr/lib64/R/library/pkgdown/tests/testthat/assets/version-formatting/DESCRIPTION
/usr/lib64/R/library/pkgdown/tests/testthat/assets/vignette-with-crayon.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/assets/vignette-with-img.Rmd
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-articles.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-favicons.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-footer.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-github.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-home-authors.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-home-citation.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-home-community.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-home-index.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-home-license.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-home.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-logo.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-news.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-redirects.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-reference-index.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-reference.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-search-docs.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build-tutorials.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-build.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-deploy-site.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-development.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-figure.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-highlight.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-html-build.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-init.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-markdown.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-navbar.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-package.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-pkgdown_print.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-rd-data.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-rd-example.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-rd-html.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-render.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-repo.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-rmarkdown.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-sitrep.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-templates.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-topics.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-tweak-badges.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-tweak-navbar.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-tweak-page.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-tweak-reference.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-tweak-tabset.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-tweak-tags.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-usage.R
/usr/lib64/R/library/pkgdown/tests/testthat/test-utils.R
