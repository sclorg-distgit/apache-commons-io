%global pkg_name apache-commons-io
%{?scl:%scl_package %{pkg_name}}
%{?java_common_find_provides_and_requires}

%global base_name       io
%global short_name      commons-%{base_name}

Name:           %{?scl_prefix}%{pkg_name}
Version:        2.4
Release:        12.11%{?dist}
Epoch:          1
Summary:        Utilities to assist with developing IO functionality
License:        ASL 2.0
URL:            http://commons.apache.org/%{base_name}
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix_maven}apache-commons-parent >= 26-7


%description
Commons-IO contains utility classes, stream implementations,
file filters, and endian classes. It is a library of utilities
to assist with developing IO functionality.

%package javadoc
Summary:        API documentation for %{pkg_name}

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
sed -i 's/\r//' *.txt
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_file  : %{short_name} %{pkg_name}
%mvn_alias : org.apache.commons:
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1:2.4-12.11
- Mass rebuild 2015-01-13

* Fri Jan 09 2015 Michal Srb <msrb@redhat.com> - 1:2.4-12.10
- Mass rebuild 2015-01-09

* Tue Dec 16 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-12.9
- Migrate requires and build-requires to rh-java-common

* Mon Dec 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-12.8
- Mass rebuild 2014-12-15

* Mon Dec 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-12.7
- Rebuild for rh-java-common collection

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-12.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-12.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-12.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-12.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-12.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-12.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1:2.4-12
- Mass rebuild 2013-12-27

* Fri Sep 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-11
- Add BuildRequires on apache-commons-parent >= 26-7

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-10
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

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
