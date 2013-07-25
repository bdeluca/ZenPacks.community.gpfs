from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class StgPoolMonitor(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'GPFSStgPoolMonitor'

    num_disks = None
    

    _properties = ManagedEntity._properties + (
        {'id': 'num_disks', 'type': 'string'},
       
        )

    _relations = ManagedEntity._relations + (
        ('stgpool_monitor', ToOne(ToManyCont,
            'ZenPacks.community.gpfs.GPFSDevice',
            'stgpool_monitors',
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
        return self.stgpool_monitor()

    def getRRDTemplateName(self):
        return 'GPFSStgPoolMonitor'