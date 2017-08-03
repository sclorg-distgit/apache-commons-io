%{?scl:%scl_package apache-commons-io}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}apache-commons-io
Version:        2.5
Release:        2.2%{?dist}
Epoch:          1
Summary:        Utilities to assist with developing IO functionality
License:        ASL 2.0
URL:            http://commons.apache.org/io
Source0:        http://archive.apache.org/dist/commons/io/source/commons-io-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(junit:junit)
BuildRequires:  %{?scl_prefix}mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-antrun-plugin)

%description
Commons-IO contains utility classes, stream implementations,
file filters, and endian classes. It is a library of utilities
to assist with developing IO functionality.

%package javadoc
Summary:        API documentation for %{pkg_name}

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n commons-io-%{version}-src
sed -i 's/\r//' *.txt

%build
%mvn_file  : commons-io %{pkg_name}
%mvn_alias : org.apache.commons:

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 1:2.5-2.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 1:2.5-2.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 23 2016 Michael Simacek <msimacek@redhat.com> - 1:2.5-1
- Update to upstream version 2.5

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-13
- Remove legacy Obsoletes/Provides for jakarta-commons

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:2.4-11
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Michal Srb <msrb@redhat.com> - 1:2.4-9
- Rebuild

* Mon Apr 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-8
- Update to current packaging guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1:2.4-6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan  9 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-5
- Bump release tag

* Tue Jan  8 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-4
- Build with xmvn

* Mon Nov 19 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-3
- Add Provides/Obsoletes for jakarta-commons-io

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-1
- Updae to 2.4

* Mon Apr 16 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.3-1
- Update to 2.3

* Wed Apr 4 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.2-1
- Update to 2.2
- Remove rpm bug workaround
- Finalize renaming from jakarta-comons-io

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 7 2011 Alexander Kurtakov <akurtako@redhat.com> 1:2.1-1
- Update to latest upstream (2.1).

* Thu Jun 23 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:2.0.1-3
- Fix build with maven3
- Use new add_maven_depmap macro

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:2.0.1-1
- Update to 2.0.1
- Versionless jars & javadocs
- Use maven 3 to build
- Use apache-commons-parent for BR

* Fri Oct 22 2010 Chris Spike <chris.spike@arcor.de> 1:2.0-1
- Updated to 2.0
- Cleaned up BRs

* Thu Jul  8 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:1.4-6
- Add license to javadoc subpackage

* Fri May 21 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:1.4-5
- Correct depmap filename for backward compatibility

* Mon May 17 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:1.4-4
- Fix maven depmap JPP name to short_name

* Wed May 12 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:1.4-3
- Add obsoletes to javadoc sub-package

* Wed May 12 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:1.4-2
- Add symlink to short_name.jar
- Fix mavendepmapfragdir wildcard

* Tue May 11 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:1.4-1
- Rename and rebase of jakarta-commons-io
- Clean up whole spec
