#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-commons-io
Version  : 1.4
Release  : 3
URL      : https://repo1.maven.org/maven2/commons-io/commons-io/1.4/commons-io-1.4.jar
Source0  : https://repo1.maven.org/maven2/commons-io/commons-io/1.4/commons-io-1.4.jar
Source1  : https://repo1.maven.org/maven2/commons-io/commons-io/1.4/commons-io-1.4.pom
Source2  : https://repo1.maven.org/maven2/commons-io/commons-io/2.1/commons-io-2.1.pom
Source3  : https://repo1.maven.org/maven2/commons-io/commons-io/2.2/commons-io-2.2.jar
Source4  : https://repo1.maven.org/maven2/commons-io/commons-io/2.2/commons-io-2.2.pom
Source5  : https://repo1.maven.org/maven2/commons-io/commons-io/2.4/commons-io-2.4.jar
Source6  : https://repo1.maven.org/maven2/commons-io/commons-io/2.4/commons-io-2.4.pom
Source7  : https://repo1.maven.org/maven2/commons-io/commons-io/2.5/commons-io-2.5.jar
Source8  : https://repo1.maven.org/maven2/commons-io/commons-io/2.5/commons-io-2.5.pom
Source9  : https://repo1.maven.org/maven2/commons-io/commons-io/2.6/commons-io-2.6.jar
Source10  : https://repo1.maven.org/maven2/commons-io/commons-io/2.6/commons-io-2.6.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-commons-io-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-commons-io package.
Group: Data

%description data
data components for the mvn-commons-io package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-io/commons-io/1.4
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/commons-io/commons-io/1.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-io/commons-io/1.4
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/commons-io/commons-io/1.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-io/commons-io/2.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/commons-io/commons-io/2.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-io/commons-io/2.2
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/commons-io/commons-io/2.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-io/commons-io/2.2
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/commons-io/commons-io/2.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-io/commons-io/2.4
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/commons-io/commons-io/2.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-io/commons-io/2.4
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/commons-io/commons-io/2.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-io/commons-io/2.5
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/commons-io/commons-io/2.5

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-io/commons-io/2.5
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/commons-io/commons-io/2.5

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-io/commons-io/2.6
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/commons-io/commons-io/2.6

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-io/commons-io/2.6
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/commons-io/commons-io/2.6


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/commons-io/commons-io/1.4/commons-io-1.4.jar
/usr/share/java/.m2/repository/commons-io/commons-io/1.4/commons-io-1.4.pom
/usr/share/java/.m2/repository/commons-io/commons-io/2.1/commons-io-2.1.pom
/usr/share/java/.m2/repository/commons-io/commons-io/2.2/commons-io-2.2.jar
/usr/share/java/.m2/repository/commons-io/commons-io/2.2/commons-io-2.2.pom
/usr/share/java/.m2/repository/commons-io/commons-io/2.4/commons-io-2.4.jar
/usr/share/java/.m2/repository/commons-io/commons-io/2.4/commons-io-2.4.pom
/usr/share/java/.m2/repository/commons-io/commons-io/2.5/commons-io-2.5.jar
/usr/share/java/.m2/repository/commons-io/commons-io/2.5/commons-io-2.5.pom
/usr/share/java/.m2/repository/commons-io/commons-io/2.6/commons-io-2.6.jar
/usr/share/java/.m2/repository/commons-io/commons-io/2.6/commons-io-2.6.pom
