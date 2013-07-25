from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class FileSystemMonitor(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'GPFSFileSystemMonitor'

    filesystem_status = None
    

    _properties = ManagedEntity._properties + (
        {'id': 'filesystem_status', 'type': 'string'},
       
        )

    _relations = ManagedEntity._relations + (
        ('filesystem_monitor', ToOne(ToManyCont,
            'ZenPacks.community.gpfs.GPFSDevice',
            'filesystem_monitors',
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
        return self.filesystem_monitor()

    def getRRDTemplateName(self):
        return 'GPFSFileSystemMonitor'