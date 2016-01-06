##############################################################
## NOTE: Please be careful about running this script.  When
## I run it, I have OpenDNS set at the highest levels of blocking
## filtering.  Would highly recommend you do something similar
## if you intend on actually running this.
##
import requests
import time
import pandas as pd

# Read into pandas dataframe
cols = ['dt', 'tm', 'time_taken', 'c_ip', 'cs_username', 'cs_auth_group', 'x_exc
eption_id', 'sc_filter_result', 'cs_categories', 'csReferer', 'sc_status', 's_ac
tion', 'cs_method', 'rsContentType', 'cs_uri_scheme', 'cs_host','cs_uri_port', '
cs_uri_path', 'cs_uri_query', 'cs_uri_extension', 'csUserAgent', 's_ip', 'sc_byt
es', 'cs_bytes', 'x_virus_id']
sgos = pd.read_csv('./cleaned_sgos.csv', names=cols)

urls = sgos[['csReferer', 'cs_host']]

# RESTART at ROW 70311 
start  = 70311
end = len(urls)
read_timeout = 10.0
#end = 10
for i in range(start, end):
    refr = urls.loc[i, 'csReferer'] 
    host = urls.loc[i, 'cs_host']
    print i
    print '  refr =', refr[7:]
    print '  host = ', host
    try:
        if refr[0] in ['h', 'H']:
            rr = requests.get(refr, timeout=(1, read_timeout))
            print '   refr Status Code', rr.status_code
    except:
        print 'EXCEPTION with: ', refr

    try:
        if host[0] not in ['-', '']:      
            rh = requests.get('http://' + host, timeout=(1, read_timeout))
            print '   host Status Code', rh.status_code
    except:
        print "EXCEPTION with: %s" % host
