# This file is the conventional place for "Info" adapters. Info adapters are
# a crucial part of the Zenoss API and therefore the web interface for any
# custom classes delivered by your ZenPack. Examples of custom classes that
# will almost certainly need info adapters include datasources, custom device
# classes and custom device component classes.

# Mappings of interfaces (interfaces.py) to concrete classes and the factory
# (these info adapter classes) used to create info objects for them are managed
# in the configure.zcml file.

from zope.component import adapts
from zope.interface import implements

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.device import DeviceInfo
from Products.Zuul.infos.component import ComponentInfo

from ZenPacks.community.gpfs.interfaces import (INetGPFSDeviceInfo,
                                                IGPFSFileSystemMonitorInfo,
                                                IGPFSStgPoolMonitorInfo,
                                                IGPFSDiskMonitorInfo,
                                                )


class GPFSDeviceInfo(DeviceInfo):
    """
    Defines API access for this datasource.
    """

    implements(INetGPFSDeviceInfo)

    disk_count = ProxyProperty('disk_count')


class GPFSFileSystemInfo(ComponentInfo):
    implements(IGPFSFileSystemMonitorInfo)
    filesystem_status = ProxyProperty('filesystem_status')


class GPFSStgPoolInfo(ComponentInfo):
    implements(IGPFSStgPoolMonitorInfo)
    num_disks = ProxyProperty('num_disks')

class GPFSDiskInfo(ComponentInfo):
    implements(IGPFSDiskMonitorInfo)
    gpfsDiskFSName = ProxyProperty('fs_name')
    gpfsDiskStgPoolName = ProxyProperty('stgpool_name')
    gpfsDiskMetadata = ProxyProperty('has_metadata')
    gpfsDiskData = ProxyProperty('has_data')


# class ExampleComponentInfo(ComponentInfo):
#     implements(IExampleComponentInfo)
#     adapts(ExampleComponent)

#     attributeOne = ProxyProperty("attributeOne")
#     attributeTwo = ProxyProperty("attributeTwo")
