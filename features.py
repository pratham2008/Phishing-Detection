import re
import socket
import urllib.parse
import requests
from datetime import datetime
from bs4 import BeautifulSoup

# This function extracts features from a raw URL
def extract_features(url):
    features = {}

    # --- Example feature extraction matching your dataset columns ---
    # UsingIP
    ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
    features['UsingIP'] = 1 if re.search(ip_pattern, url) else -1

    # LongURL (threshold 75 chars)
    features['LongURL'] = 1 if len(url) >= 75 else -1

    # ShortURL (checks for known shorteners)
    shorteners = r"bit\.ly|goo\.gl|tinyurl|ow\.ly|t\.co"
    features['ShortURL'] = 1 if re.search(shorteners, url) else -1

    # Symbol @
    features['Symbol@'] = 1 if "@" in url else -1

    # Redirecting (// in path)
    last_double_slash = url.rfind('//')
    features['Redirecting//'] = 1 if last_double_slash > 6 else -1

    # Prefix-Suffix (- in domain)
    domain = urllib.parse.urlparse(url).netloc
    features['PrefixSuffix-'] = 1 if '-' in domain else -1

    # SubDomains (count dots in domain)
    dot_count = domain.count('.')
    if dot_count == 1:
        features['SubDomains'] = -1
    elif dot_count == 2:
        features['SubDomains'] = 0
    else:
        features['SubDomains'] = 1

    # HTTPS (scheme check)
    features['HTTPS'] = 1 if url.startswith("https") else -1

    # DomainRegLen – dummy (-1 because live WHOIS is complex)
    features['DomainRegLen'] = -1

    # Favicon – dummy
    features['Favicon'] = -1

    # NonStdPort – dummy
    features['NonStdPort'] = -1

    # HTTPSDomainURL – check https inside domain
    features['HTTPSDomainURL'] = 1 if 'https' in domain else -1

    # RequestURL, AnchorURL, LinksInScriptTags – dummy (-1)
    features['RequestURL'] = -1
    features['AnchorURL'] = -1
    features['LinksInScriptTags'] = -1

    # ServerFormHandler – dummy
    features['ServerFormHandler'] = -1

    # InfoEmail
    features['InfoEmail'] = 1 if re.search(r"[^\s]+@[^\s]+\.[^\s]+", url) else -1

    # AbnormalURL – dummy
    features['AbnormalURL'] = -1

    # WebsiteForwarding – dummy
    features['WebsiteForwarding'] = -1

    # StatusBarCust, DisableRightClick, UsingPopupWindow, IframeRedirection
    features['StatusBarCust'] = -1
    features['DisableRightClick'] = -1
    features['UsingPopupWindow'] = -1
    features['IframeRedirection'] = -1

    # AgeofDomain, DNSRecording – dummy
    features['AgeofDomain'] = -1
    features['DNSRecording'] = -1

    # WebsiteTraffic, PageRank, GoogleIndex, LinksPointingToPage, StatsReport
    features['WebsiteTraffic'] = -1
    features['PageRank'] = -1
    features['GoogleIndex'] = -1
    features['LinksPointingToPage'] = -1
    features['StatsReport'] = -1

    return features
