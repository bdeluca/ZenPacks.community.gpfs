from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class NodeMonitor(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'GPFSNodeMonitor'

    gpfsNodeType = None
    gpfsNodeAdmin = None
    gpfsNodePagePoolL = None
    gpfsNodePagePoolH = None
    gpfsNodePrefetchThreads = None
    gpfsNodeMaxMbps= None
    gpfsNodeMaxFilesToCache= None
    gpfsNodeMaxStatCache= None
    gpfsNodeDmapiEventTimeout= None
    gpfsNodeDmapiMountTimeout= None
    gpfsNodeDmapiSessFailureTimeout= None
    gpfsNodeNsdServerWaitTimeWindowOnMount= None
    gpfsNodeNsdServerWaitTimeForMount= None
    gpfsNodeUnmountOnDiskFail= None
    gpfsNodePlatform = None
    gpfsNodeIP= None
    gpfsNodeStatus= None
    gpfsNodeFailureCount= None
    gpfsNodeHealthy= None
    gpfsNodeDiagnosis= None
    gpfsNodeVersion= None

    #graph
    #gpfsNodeThreadWait 1.3.6.1.4.1.2.6.212.1.4.1.6
    # 1.3.6.1.4.1.2.6.212.1.4.1.5 gpfsNodeFailureCount.


    _properties = ManagedEntity._properties + (
        {'id': 'gpfsNodeType', 'type': 'string'},
        {'id': 'gpfsNodeAdmin', 'type': 'string'},
        {'id': 'gpfsNodeVersion', 'type': 'string'},
        {'id': 'gpfsNodeType', 'type': 'string'},
        )

  

    _relations = ManagedEntity._relations + (
        ('node_monitor', ToOne(ToManyCont,
            'ZenPacks.community.gpfs.GPFSDevice',
            'node_monitors',
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
        return self.node_monitor()

    def getRRDTemplateName(self):
        return 'GPFSNodeMonitor'