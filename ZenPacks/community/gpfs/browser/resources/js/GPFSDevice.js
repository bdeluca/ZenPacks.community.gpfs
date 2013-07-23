 //js changes to modify summary page
/*
Ext.onReady(function() {
    var DEVICE_OVERVIEW_ID = 'deviceoverviewpanel_summary';
    Ext.ComponentMgr.onAvailable(DEVICE_OVERVIEW_ID, function(){
        var overview = Ext.getCmp(DEVICE_OVERVIEW_ID);
        
        overview.addField({
            name: 'disk_count',
            fieldLabel: _t('Disk Count (LUNs)')
        });
    });
});

*/

(function(){

var ZC = Ext.ns('Zenoss.component');

ZC.registerName(
    'GPFSFileSystemMonitor',
    _t('GPFS File Systems'),
    _t('GPFS File Systems'));

ZC.registerName(
    'GPFSStgPoolMonitor',
    _t('GPFS Stgpools'),
    _t('GPFS Stgpools'));



ZC.GPFSFileSystemMonitorPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'GPFSFileSystemMonitor',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'filesystem_status'},
               
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('File System NameName'),
                sortable: true
            },{
                id: 'filesystem_status',
                dataIndex: 'filesystem_status',
                header: _t('Filesystem Status'),
                sortable: true,
                width: 120
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.GPFSFileSystemMonitorPanel.superclass.constructor.call(
            this, config);
    }
});

Ext.reg('GPFSFileSystemMonitorPanel', ZC.GPFSFileSystemMonitorPanel);



})();
