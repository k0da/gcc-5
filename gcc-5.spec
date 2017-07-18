#
# spec file for package gcc-5
#
# Copyright (c) specCURRENT_YEAR SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gcc-5
Version:        0.1
Release:        0
Summary:        GCC5 wrapper over scl devtoolset-4 from scl
License:        MIT 
Group:          Development
Url:            http://github/gooddata/gcc-5.git
Source:         README 
BuildRequires:  devtoolset-4-runtime
BuildRequires:  setup
Provides:       gcc5-c++
Provides:       gcc5
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description

%prep
cp %{SOURCE0} ./

%build

%install
install -d %{buildroot}/etc/profile.d/
ls -la ../ 
ln -s /opt/rh/devtoolset-4/enable %{buildroot}/etc/profile.d/z-devtoolset4.sh

%files
%defattr(-,root,root)
%doc README 
/etc/profile.d/z-devtoolset4.sh

%changelog
* Tue Jul 18 2017 Dinar Valeev <dinar.valeev@gooddata.com>
- initial release
