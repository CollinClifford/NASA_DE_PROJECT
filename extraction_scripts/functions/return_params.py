def return_params(web_service, start_date, end_date, api_key):
    
        if web_service == "planetary/apod":
            return {'start_date': start_date, 'end_date': end_date, 'api_key': api_key, 'thumbs': 'True'}
        elif web_service == 'neo/rest/v1/feed':
            return {'start_date': start_date, 'end_date': end_date, 'api_key': api_key}
        elif web_service == 'DONKI/CME':
            return {'startDate': start_date, 'endDate': end_date, 'api_key': api_key}
        elif web_service == 'DONKI/CMEAnalysis':
            return {'startDate': start_date, 'endDate': end_date, 'api_key': api_key}
        elif web_service == 'DONKI/GST':
            return {'startDate': start_date, 'endDate': end_date, 'api_key': api_key}
        elif web_service == 'DONKI/HSS':
            return {'startDate': start_date, 'endDate': end_date, 'api_key': api_key}
        elif web_service == 'DONKI/IPS':
            return {'startDate': start_date, 'endDate': end_date, 'api_key': api_key}
        elif web_service == 'DONKI/MPC':
            return {'startDate': start_date, 'endDate': end_date, 'api_key': api_key}
        elif web_service == 'DONKI/notifications':
            return {'startDate': start_date, 'endDate': end_date, 'api_key': api_key}
        elif web_service == 'DONKI/RBE':
            return {'startDate': start_date, 'endDate': end_date, 'api_key': api_key}
        elif web_service == 'DONKI/SEP':
            return {'startDate': start_date, 'endDate': end_date, 'api_key': api_key}
        elif web_service == 'DONKI/WSAEnlilSimulations':
            return {'startDate': start_date, 'endDate': end_date, 'api_key': api_key}
        elif web_service == 'EPIC/api/natural/date/':
            return {'api_key': api_key}
        elif web_service == 'EPIC/api/enhanced/date/':
            return {'api_key': api_key}
        elif web_service == 'mars-photos/api/v1/rovers/perseverance/photos':
            return {'earth_date': start_date, 'api_key': api_key}
        elif web_service == 'mars-photos/api/v1/rovers/curiosity/photos':
            return {'earth_date': start_date, 'api_key': api_key}
        elif web_service == 'mars-photos/api/v1/rovers/opportunity/photos':
            return {'earth_date': start_date, 'api_key': api_key}
        elif web_service == 'mars-photos/api/v1/rovers/spirit/photos':
            return {'earth_date': start_date, 'api_key': api_key}
        else:
            return None