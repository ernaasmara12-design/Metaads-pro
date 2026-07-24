"""
Ad Set Enums
"""

# Optimization Goal
OPTIMIZATION_GOALS = {
    "Conversions": "OFFSITE_CONVERSIONS",
    "Link Clicks": "LINK_CLICKS",
    "Landing Page Views": "LANDING_PAGE_VIEWS",
    "Reach": "REACH",
    "Impressions": "IMPRESSIONS",
    "Post Engagement": "POST_ENGAGEMENT",
    "Video Views": "THRUPLAY",
}

# Billing Event
BILLING_EVENTS = {
    "Impressions": "IMPRESSIONS",
    "Link Clicks": "LINK_CLICKS",
}

# Conversion Location
CONVERSION_LOCATION = {
    "Website": "WEBSITE",
    "App": "APP",
    "Messenger": "MESSENGER",
    "WhatsApp": "WHATSAPP",
}

# Dynamic Creative
DYNAMIC_CREATIVE = {
    "On": True,
    "Off": False,
}
