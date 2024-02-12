def drop_view(cursor, schema):
    drop_query=f"""
        drop view if exists donki.cme_cme_analyses_vw;
        drop view if exists donki.cme_instruments_vw;
        drop view if exists donki.wsaenlilsimulations_impact_list_vw;
        drop view if exists donki.wsaenlilsimulations_cme_inputs_vw;
        drop view if exists donki.sep_linked_events_vw;
        drop view if exists donki.sep_instruments_vw;
        drop view if exists donki.rbe_linked_events_vw;
        drop view if exists donki.rbe_instruments_vw;
        drop view if exists donki.mpc_linked_events_vw;
        drop view if exists donki.mpc_instruments_vw;
        drop view if exists donki.ips_instruments_vw;
        drop view if exists donki.hss_linked_events_vw;
        drop view if exists donki.hss_instruments_vw;
        drop view if exists donki.gst_linked_events_vw;
        drop view if exists donki.cme_linked_events_vw;
        drop view if exists donki.gst_all_kp_index_vw;
        """
    
    cursor.execute(drop_query)