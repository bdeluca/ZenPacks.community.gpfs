from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class GPFSDevice(Device):
    #file_system_count = None
    disk_count = None

    _properties = Device._properties + (
            { 
            #'id': 'file_system_count',
            #             'type': 'int',
            'id': 'disk_count',
                         'type': 'int',
        
            },
        )

    _relations = Device._relations + (
            ('filesystem_monitors', ToManyCont(ToOne,
                'ZenPacks.community.gpfs.FileSystemMonitor',
                'filesystem_monitor',
                )),
            ('stgpool_monitors', ToManyCont(ToOne,
                'ZenPacks.community.gpfs.StgPoolMonitor',
                'stgpool_monitor',
                )),
            ('disk_monitors', ToManyCont(ToOne,
                'ZenPacks.community.gpfs.DiskMonitor',
                'disk_monitor',
                )),


             )
           
