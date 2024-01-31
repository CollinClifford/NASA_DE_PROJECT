import os

# This function just returns the path to the JSON within the datalake folder.

def return_path(web_service, project_directory):
    if web_service == 'planetary/apod':
        return os.path.join(project_directory, 'data_lake_storage/apod/apod.json')
    elif web_service == 'neo/rest/v1/feed':
        return os.path.join(project_directory, 'data_lake_storage/neows/neows.json')
    elif web_service == 'DONKI/CME':
        return os.path.join(project_directory, 'data_lake_storage/donki/cme/cme.json')
    elif web_service == 'DONKI/CMEAnalysis':
        return os.path.join(project_directory, 'data_lake_storage/donki/cmeanalysis/cmeanalysis.json') 
    elif web_service == 'DONKI/GST':
        return os.path.join(project_directory, 'data_lake_storage/donki/gst/gst.json') 
    elif web_service == 'DONKI/HSS':
        return os.path.join(project_directory, 'data_lake_storage/donki/hss/hss.json') 
    elif web_service == 'DONKI/IPS':
        return os.path.join(project_directory, 'data_lake_storage/donki/ips/ips.json') 
    elif web_service == 'DONKI/MPC':
        return os.path.join(project_directory, 'data_lake_storage/donki/mpc/mpc.json') 
    elif web_service == 'DONKI/notifications':
        return os.path.join(project_directory, 'data_lake_storage/donki/notifications/notifications.json')
    elif web_service == 'DONKI/RBE':
        return os.path.join(project_directory, 'data_lake_storage/donki/rbe/rbe.json')
    elif web_service == 'DONKI/SEP':
        return os.path.join(project_directory, 'data_lake_storage/donki/sep/sep.json')
    elif web_service == 'DONKI/WSAEnlilSimulations':
        return os.path.join(project_directory, 'data_lake_storage/donki/wsaenlilsimulations/wsaenlilsimulations.json')
    elif web_service == 'EPIC/api/natural/date/':
        return os.path.join(project_directory, 'data_lake_storage/epic/enhanced/epic_enhanced.json')
    elif web_service == 'EPIC/api/enhanced/date/':
        return os.path.join(project_directory, 'data_lake_storage/epic/natural/epic_natural.json')
    elif web_service == 'mars-photos/api/v1/rovers/curiosity/photos':
        return os.path.join(project_directory, 'data_lake_storage/mars_rover_photos/curiosity/curiosity.json')
    elif web_service == 'mars-photos/api/v1/rovers/opportunity/photos':
        return os.path.join(project_directory, 'data_lake_storage/mars_rover_photos/opportunity/opportunity.json')
    elif web_service == 'mars-photos/api/v1/rovers/perseverance/photos':
        return os.path.join(project_directory, 'data_lake_storage/mars_rover_photos/perseverance/perseverance.json')
    elif web_service == 'mars-photos/api/v1/rovers/spirit/photos':
        return os.path.join(project_directory, 'data_lake_storage/mars_rover_photos/spirit/spirit.json')
    elif web_service == 'planetary/earth/assets':
        return os.path.join(project_directory, 'data_lake_storage/earth/earth.json')
    else:
        return None