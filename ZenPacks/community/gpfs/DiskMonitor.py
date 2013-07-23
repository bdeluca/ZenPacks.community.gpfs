from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class DiskMonitor(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'GPFSDiskMonitor'

    gpfsDiskFSName = None
    gpfsDiskStgPoolName = None
    gpfsDiskMetadata = None
    gpfsDiskData = None
    

    _properties = ManagedEntity._properties + (
        {'id': 'gpfsDiskFSName', 'type': 'string'},
        {'id': 'gpfsDiskStgPoolName', 'type': 'string'},
        {'id': 'gpfsDiskMetadata', 'type': 'string'},
        {'id': 'gpfsDiskData', 'type': 'string'},
        )

    _relations = ManagedEntity._relations + (
        ('disk_monitor', ToOne(ToManyCont,
            'ZenPacks.community.gpfs.GPFSDevice',
            'disk_monitors',
            )),
        )

    factory_type_information = ({
        'actions': ({
            'id': 'perfConf',
            'name': 'Template',
            'action': 'objTemplates',
            'permissions': (ZEN_CHANGE_DEVICE,),
            },),
        },)

    def device(self):
        return self.disk_monitor()

    def getRRDTemplateName(self):
        return 'GPFSDiskMonitor'