Name:           ros-lunar-avt-vimba-camera
Version:        0.0.10
Release:        0%{?dist}
Summary:        ROS avt_vimba_camera package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/avt_vimba_ros
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-camera-info-manager
Requires:       ros-lunar-diagnostic-updater
Requires:       ros-lunar-dynamic-reconfigure
Requires:       ros-lunar-image-geometry
Requires:       ros-lunar-image-transport
Requires:       ros-lunar-message-filters
Requires:       ros-lunar-polled-camera
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-sensor-msgs
Requires:       ros-lunar-std-msgs
BuildRequires:  ros-lunar-camera-info-manager
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-diagnostic-updater
BuildRequires:  ros-lunar-dynamic-reconfigure
BuildRequires:  ros-lunar-image-geometry
BuildRequires:  ros-lunar-image-transport
BuildRequires:  ros-lunar-message-filters
BuildRequires:  ros-lunar-polled-camera
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-sensor-msgs
BuildRequires:  ros-lunar-std-msgs

%description
Wrapper of the Allied Vision Technologies (AVT) VIMBA Ethernet and Firewire SDK.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Wed Aug 16 2017 Miquel Massot <miquel.massot@uib.cat> - 0.0.10-0
- Autogenerated by Bloom
