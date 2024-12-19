%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-turtlebot4-gz-bringup
Version:        2.0.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS turtlebot4_gz_bringup package

License:        Apache 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jazzy-geometry-msgs
Requires:       ros-jazzy-irobot-create-common-bringup
Requires:       ros-jazzy-irobot-create-description
Requires:       ros-jazzy-irobot-create-gz-bringup
Requires:       ros-jazzy-irobot-create-gz-plugins
Requires:       ros-jazzy-irobot-create-gz-toolbox
Requires:       ros-jazzy-irobot-create-msgs
Requires:       ros-jazzy-irobot-create-nodes
Requires:       ros-jazzy-irobot-create-toolbox
Requires:       ros-jazzy-ros-gz-interfaces
Requires:       ros-jazzy-ros-gz-sim
Requires:       ros-jazzy-std-msgs
Requires:       ros-jazzy-turtlebot4-description
Requires:       ros-jazzy-turtlebot4-gz-gui-plugins
Requires:       ros-jazzy-turtlebot4-gz-toolbox
Requires:       ros-jazzy-turtlebot4-msgs
Requires:       ros-jazzy-turtlebot4-navigation
Requires:       ros-jazzy-turtlebot4-node
Requires:       ros-jazzy-turtlebot4-viz
Requires:       ros-jazzy-ros-workspace
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-geometry-msgs
BuildRequires:  ros-jazzy-irobot-create-common-bringup
BuildRequires:  ros-jazzy-irobot-create-description
BuildRequires:  ros-jazzy-irobot-create-gz-bringup
BuildRequires:  ros-jazzy-irobot-create-gz-plugins
BuildRequires:  ros-jazzy-irobot-create-gz-toolbox
BuildRequires:  ros-jazzy-irobot-create-msgs
BuildRequires:  ros-jazzy-irobot-create-nodes
BuildRequires:  ros-jazzy-irobot-create-toolbox
BuildRequires:  ros-jazzy-ros-gz-interfaces
BuildRequires:  ros-jazzy-ros-gz-sim
BuildRequires:  ros-jazzy-std-msgs
BuildRequires:  ros-jazzy-turtlebot4-description
BuildRequires:  ros-jazzy-turtlebot4-gz-gui-plugins
BuildRequires:  ros-jazzy-turtlebot4-gz-toolbox
BuildRequires:  ros-jazzy-turtlebot4-msgs
BuildRequires:  ros-jazzy-turtlebot4-navigation
BuildRequires:  ros-jazzy-turtlebot4-node
BuildRequires:  ros-jazzy-turtlebot4-viz
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-jazzy-ament-lint-auto
BuildRequires:  ros-jazzy-ament-lint-common
%endif

%description
TurtleBot 4 Gazebo Simulator bringup

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Thu Dec 19 2024 rkreinin <rkreinin@clearpathrobotics.com> - 2.0.2-1
- Autogenerated by Bloom

* Fri Sep 27 2024 rkreinin <rkreinin@clearpathrobotics.com> - 2.0.1-1
- Autogenerated by Bloom

