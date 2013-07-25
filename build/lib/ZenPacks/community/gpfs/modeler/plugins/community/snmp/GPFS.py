from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )

from Products.DataCollector.plugins.DataMaps import ObjectMap, RelationshipMap

class GPFS(SnmpPlugin):
    #relname = 'filesystem_monitors'
    #modname = 'ZenPacks.community.gpfs.FileSystemMonitor'
    snmpGetTableMaps = (
        GetTableMap(
            'disk_table', '.1.3.6.1.4.1.2.6.212.1.9.1', {
                '.1': 'diskId',
                '.2': 'filesystemId',
                '.3': 'poolname',
                '.4': 'state',
                '.5': 'Working',
                '.6': 'totalSpaceH',
                '.7': 'totalSpaceL',
                '.8': 'freeSpaceH',
                '.9': 'freeSpaceL',
                '.10': 'blockFreeSpaceH',
                '.11': 'blockFreeSpaceL',
                
                }
            ),

        GetTableMap(
        'disk_config_table', '.1.3.6.1.4.1.2.6.212.1.10.1', {
                '.1': 'diskId',
                '.2': 'fsname',
                '.3': 'stgpool',
                '.4': 'metadata',
                '.5': 'data',
                }
            ),


            
        GetTableMap(
            'filesystem_table', '.1.3.6.1.4.1.2.6.212.1.6.1', {
                '.1': 'gpfsFileSystemName',
                '.2': 'gpfsFileSystemStatus',
                '.3': 'gpfsFileSystemXstatus',
                '.4': 'gpfsFileSystemTotalSpaceL',
                '.5': 'gpfsFileSystemTotalSpaceH',
                '.6': 'gpfsFileSystemNumTotalInodesL',
                '.7': 'gpfsFileSystemNumTotalInodesH',
                '.8': 'gpfsFileSystemFreeSpaceL',
                '.9': 'gpfsFileSystemFreeSpaceH',
                '.10': 'gpfsFileSystemNumFreeInodesL',
                '.11': 'gpfsFileSystemNumFreeInodesH',
                
                }
            ),

        GetTableMap(
            'stgpool_table', '.1.3.6.1.4.1.2.6.212.1.8.1', {
                '.1': 'gpfsStgPoolName',
                '.2': 'gpfsStgPoolFSName',
                '.3': 'gpfsStgPoolTotalSpaceL',
                '.4': 'gpfsStgPoolTotalSpaceH',
                '.5': 'gpfsStgPoolFreeSpaceL',
                '.6': 'gpfsStgPoolFreeSpaceH',
                '.7': 'gpfsStgPoolNumDisks',
                }
            ),

        GetTableMap(
            'node_status_table', '.1.3.6.1.4.1.2.6.212.1.4.1', {
                '.1': 'gpfsNodeName',
                '.9': 'gpfsNodeVersion',
               
                }
            ),

        GetTableMap(
            'node_config_table', '.1.3.6.1.4.1.2.6.212.1.5.1', {
                '.1': 'gpfsNodeName',
                '.2': 'gpfsNodeType',
                '.3': 'gpfsNodeAdmin',
               
                }
            ),
        )

    def process(self, device, results, log):
        #import pdb; 
        #pdb.set_trace()
        filesystem_table = results[1].get('filesystem_table', {})
        stgpool_table = results[1].get('stgpool_table', {})
        disk_config_table = results[1].get('disk_config_table', {})
        node_status_table = results[1].get('node_status_table', {})
        node_config_table = results[1].get('node_config_table', {})
        
        rms = []
        
        objs = []
        for snmpindex, row in stgpool_table.items():
            name = "%s:%s" % (row.get('gpfsStgPoolFSName'), row.get('gpfsStgPoolName'))
            if not name:
                log.warn('Skipping stgpool sensor with no name')
                continue

            objs.append(ObjectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                'num_disks': row.get('gpfsStgPoolNumDisks'),
                }))

        rms.append(RelationshipMap(
           relname="stgpool_monitors",
           modname='ZenPacks.community.gpfs.StgPoolMonitor',
           objmaps=objs))
        
        objs = []
        for snmpindex, row in disk_config_table.items():
            name = row.get('diskId')
            if not name:
                log.warn('skipping disk sensor with no name')
                continue

            objs.append(ObjectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                'gpfsDiskFSName': row.get('fsname'),
                'gpfsDiskStgPoolName': row.get('stgpool'),
                'gpfsDiskMetadata': row.get('metadata'),
                'gpfsDiskData': row.get('data'),
                 
                }))

        
        rms.append(RelationshipMap(
             relname="disk_monitors",
             modname='ZenPacks.community.gpfs.DiskMonitor',
             objmaps=objs))
        

        objs = []
        for snmpindex, row in filesystem_table.items():
            name = row.get('gpfsFileSystemName')
            if not name:
                log.warn('skipping disk sensor with no name')
                continue

            objs.append(ObjectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                'filesystem_status': row.get('gpfsFileSystemStatus'),
                #'port': row.get('tempSensorPortId'),
                }))
        rms.append(RelationshipMap(
             relname="filesystem_monitors",
             modname='ZenPacks.community.gpfs.FileSystemMonitor',
             objmaps=objs))

        objs = []
        for snmpindex, row in node_status_table.items():
            name = row.get('gpfsNodeName')
            print row.get('gpfsNodeVersion')
            if not name:
                log.warn('skipping node sensor with no name')
                continue
            objs.append(ObjectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                'gpfsNodeVersion': row.get('gpfsNodeVersion'),
                #'port': row.get('tempSensorPortId'),
                }))
        rms.append(RelationshipMap(
             relname="node_monitors",
             modname='ZenPacks.community.gpfs.NodeMonitor',
             objmaps=objs))
        
        #for x in  rms:
        #    print x
        return rms

