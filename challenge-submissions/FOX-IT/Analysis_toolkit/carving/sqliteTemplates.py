import datetime;

SQL_TYPE_INT = 1;
SQL_TYPE_TEXT = 2;
SQL_TYPE_FLOAT = 4;
SQL_TYPE_BLOB = 8;
SQL_TYPE_NULL = 16;

OVERFLOW_STRING = "**overflow**"
	

'''Predefined sqlite table templates'''
browserCachedPositionsTemplate = (("latitude", SQL_TYPE_FLOAT | SQL_TYPE_INT), 
						  ("longitude", SQL_TYPE_FLOAT | SQL_TYPE_INT), 
						  ("altitude", SQL_TYPE_FLOAT, SQL_TYPE_NULL | SQL_TYPE_INT), 
						  ("accuracy", SQL_TYPE_FLOAT | SQL_TYPE_INT), 
						  ("altitudeAccuracy", SQL_TYPE_FLOAT | SQL_TYPE_NULL | SQL_TYPE_INT), 
						  ("heading", SQL_TYPE_FLOAT | SQL_TYPE_NULL | SQL_TYPE_INT), 
						  ("speed", SQL_TYPE_NULL | SQL_TYPE_FLOAT | SQL_TYPE_INT), 
						  ("timestamp", SQL_TYPE_FLOAT | SQL_TYPE_INT));

talkMessagesTemplate = (("_id", SQL_TYPE_NULL),
						("thread_id", SQL_TYPE_INT | SQL_TYPE_NULL), 
						("nickname", SQL_TYPE_TEXT | SQL_TYPE_NULL), 
						("body", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
						("date", SQL_TYPE_INT), 
						("real_date", SQL_TYPE_INT), 
						("type", SQL_TYPE_INT), 
						("packet_id", SQL_TYPE_TEXT), 
						("err_code", SQL_TYPE_INT), 
						("err_msg", SQL_TYPE_TEXT | SQL_TYPE_NULL), 
						("is_muc", SQL_TYPE_INT | SQL_TYPE_NULL), 
						("show_ts", SQL_TYPE_INT | SQL_TYPE_NULL));

talkContactsTemplate = 	(("_id", SQL_TYPE_NULL), 
						 ("username", SQL_TYPE_TEXT), 
						 ("nickname", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
						 ("provider", SQL_TYPE_INT), 
						 ("account", SQL_TYPE_INT), 
						 ("contactList", SQL_TYPE_INT), 
						 ("type", SQL_TYPE_INT), 
						 ("subscriptionStatus", SQL_TYPE_INT), 
						 ("subscriptionType", SQL_TYPE_INT), 
						 ("qc", SQL_TYPE_INT), 
						 ("rejected", SQL_TYPE_INT), 
						 ("otr", SQL_TYPE_INT));
						
destinationHistoryTemplate = (("time", SQL_TYPE_NULL), 
							  ("dest_lat", SQL_TYPE_INT | SQL_TYPE_NULL), 
							  ("dest_lng", SQL_TYPE_INT | SQL_TYPE_NULL), 
							  ("dest_title", SQL_TYPE_TEXT | SQL_TYPE_NULL), 
							  ("dest_address", SQL_TYPE_TEXT | SQL_TYPE_NULL), 
							  ("dest_token", SQL_TYPE_TEXT | SQL_TYPE_NULL), 
							  ("source_lat", SQL_TYPE_INT), 
							  ("source_lng", SQL_TYPE_INT), 
							  ("day_of_week", SQL_TYPE_INT | SQL_TYPE_NULL), 
							  ("hour_of_day", SQL_TYPE_INT | SQL_TYPE_NULL)); 
						
mapsSearchHistoryTemplate = (("_id", SQL_TYPE_NULL), 
							 ("type", SQL_TYPE_INT), 
							 ("data1", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
							 ("data2", SQL_TYPE_NULL | SQL_TYPE_TEXT));
							 
mapsSuggestionTemplate = (("_id", SQL_TYPE_NULL), 
						  ("data1", SQL_TYPE_TEXT | SQL_TYPE_NULL), 
						  ("singleResult", SQL_TYPE_INT | SQL_TYPE_NULL), 
						  ("displayQuery", SQL_TYPE_NULL | SQL_TYPE_TEXT));
						
smsTemplate = (("_id", SQL_TYPE_NULL),
			   ("Thread_id", SQL_TYPE_INT),
			   ("Address", SQL_TYPE_TEXT | SQL_TYPE_NULL),
			   ("Person", SQL_TYPE_INT | SQL_TYPE_NULL), 
			   ("Date", SQL_TYPE_INT),
			   ("Protocol", SQL_TYPE_INT | SQL_TYPE_NULL),
			   ("Read", SQL_TYPE_INT),
			   ("status", SQL_TYPE_INT),
			   ("type", SQL_TYPE_INT),
			   ("Reply_path_present", SQL_TYPE_INT | SQL_TYPE_NULL),
			   ("subject", SQL_TYPE_TEXT | SQL_TYPE_NULL),
			   ("body", SQL_TYPE_TEXT | SQL_TYPE_NULL),
			   ("service_center", SQL_TYPE_TEXT | SQL_TYPE_NULL),
			   ("locked",  SQL_TYPE_INT))

callsTemplate =  (("_id", SQL_TYPE_NULL),
				  ("number", SQL_TYPE_TEXT | SQL_TYPE_NULL),
				  ("date", SQL_TYPE_INT),
				  ("duration", SQL_TYPE_INT),
				  ("type", SQL_TYPE_INT),
				  ("new", SQL_TYPE_INT),
				  ("name", SQL_TYPE_TEXT | SQL_TYPE_NULL),
				  ("numbertype", SQL_TYPE_INT),
				  ("numberlabel", SQL_TYPE_TEXT | SQL_TYPE_NULL));
	  
gmailMsgTemplate = (("_id", SQL_TYPE_NULL), 
					("messageId", SQL_TYPE_INT),
					("conversation", SQL_TYPE_INT),
					("fromAddress", SQL_TYPE_TEXT | SQL_TYPE_NULL),
					("toAddress", SQL_TYPE_TEXT | SQL_TYPE_NULL), 
					("ccAddress", SQL_TYPE_TEXT | SQL_TYPE_NULL),
					("bccAddress", SQL_TYPE_TEXT | SQL_TYPE_NULL),
					("replyToAddress", SQL_TYPE_TEXT | SQL_TYPE_NULL),
					("dateSentMs", SQL_TYPE_INT | SQL_TYPE_NULL),
					("dateReceivedMs", SQL_TYPE_INT | SQL_TYPE_NULL),
					("subject", SQL_TYPE_TEXT | SQL_TYPE_NULL),
					("snippet", SQL_TYPE_TEXT | SQL_TYPE_NULL),
					("listInfo", SQL_TYPE_TEXT | SQL_TYPE_NULL),
					("personalLevel", SQL_TYPE_INT | SQL_TYPE_NULL),
					("body", SQL_TYPE_TEXT | SQL_TYPE_NULL),
					("bodyEmbedsExternalResources", SQL_TYPE_INT | SQL_TYPE_NULL),
					("joinedAttachmentsInfo", SQL_TYPE_TEXT | SQL_TYPE_NULL),
					("synced", SQL_TYPE_INT | SQL_TYPE_NULL),
					("error", SQL_TYPE_TEXT | SQL_TYPE_NULL),
					("clientCreated", SQL_TYPE_INT | SQL_TYPE_NULL),
					("refMessageId", SQL_TYPE_INT));

contactsRContactsTemplate = (("_id", SQL_TYPE_NULL), 
					   ("is_restricted", SQL_TYPE_INT | SQL_TYPE_NULL),
					   ("account_name", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
					   ("account_type", SQL_TYPE_TEXT | SQL_TYPE_NULL),
					   ("sourceid", SQL_TYPE_TEXT | SQL_TYPE_NULL),
					   ("version", SQL_TYPE_INT), 
					   ("dirty", SQL_TYPE_INT),
					   ("deleted", SQL_TYPE_INT),
					   ("contact_id", SQL_TYPE_INT | SQL_TYPE_NULL), 
					   ("aggregation_mode", SQL_TYPE_INT),
					   ("aggregation_needed", SQL_TYPE_INT), 
					   ("custom_ringtone", SQL_TYPE_TEXT | SQL_TYPE_NULL), 
					   ("send_to_voicemail", SQL_TYPE_INT), 
					   ("times_contacted", SQL_TYPE_INT), 
					   ("last_time_contacted", SQL_TYPE_INT | SQL_TYPE_NULL), 
					   ("starred", SQL_TYPE_INT), 
					   ("display_name", SQL_TYPE_TEXT | SQL_TYPE_NULL), 
					   ("display_name_source", SQL_TYPE_INT | SQL_TYPE_NULL), 
					   ("sync1",SQL_TYPE_TEXT | SQL_TYPE_NULL),
					   ("sync2",SQL_TYPE_TEXT | SQL_TYPE_NULL),
					   ("sync3",SQL_TYPE_TEXT | SQL_TYPE_NULL),
					   ("sync4",SQL_TYPE_TEXT | SQL_TYPE_NULL))
					   
contactsDataTemplate = (("_id", SQL_TYPE_NULL), 
				("package_id", SQL_TYPE_INT | SQL_TYPE_NULL), 
				("mimetype_id", SQL_TYPE_INT),
				("raw_contact_id", SQL_TYPE_INT), 
				("is_primary", SQL_TYPE_INT), 
				("is_super_primary", SQL_TYPE_INT), 
				("data_version", SQL_TYPE_INT), 
				("data1", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
				("data2", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
				("data3", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
				("data4", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
				("data5", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
				("data6", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
				("data7", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
				("data8", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
				("data9", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
				("data10", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
				("data11", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
				("data12", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
				("data13", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
				("data14", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
				("data15", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
				("data_sync1", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
				("data_sync2", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
				("data_sync3", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
				("data_sync4", SQL_TYPE_NULL | SQL_TYPE_TEXT));

browserBookmarksTemplate = (("_id", SQL_TYPE_NULL), 
						   ("title", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
						   ("url", SQL_TYPE_TEXT), 
						   ("visits", SQL_TYPE_INT), 
						   ("date", SQL_TYPE_INT | SQL_TYPE_NULL), 
						   ("created", SQL_TYPE_INT), 
						   ("description", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
						   ("bookmark", SQL_TYPE_INT), 
						   ("favicon", SQL_TYPE_BLOB | SQL_TYPE_NULL), 
						   ("thumbnail", SQL_TYPE_BLOB | SQL_TYPE_NULL), 
						   ("touch_icon", SQL_TYPE_BLOB | SQL_TYPE_NULL));

webviewPasswordTemplate = (("_id", SQL_TYPE_NULL), 
						   ("host", SQL_TYPE_TEXT), 
						   ("username", SQL_TYPE_TEXT), 
						   ("password", SQL_TYPE_TEXT));
						   
webviewHttpAuthTemplate = (("_id", SQL_TYPE_NULL), 
						   ("host", SQL_TYPE_TEXT), 
						   ("realm", SQL_TYPE_TEXT | SQL_TYPE_NULL), 
						   ("username", SQL_TYPE_TEXT), 
						   ("password", SQL_TYPE_TEXT));

downloadsDownloadsTemplate = (("_id", SQL_TYPE_NULL), 
							  ("uri", SQL_TYPE_TEXT | SQL_TYPE_NULL), 
							  ("method", SQL_TYPE_INT | SQL_TYPE_NULL), 
							  ("entity", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
							  ("no_integrity", SQL_TYPE_NULL | SQL_TYPE_INT), 
							  ("hint", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
							  ("otaupdate", SQL_TYPE_NULL | SQL_TYPE_INT), 
							  ("_data", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
							  ("mimetype", SQL_TYPE_TEXT | SQL_TYPE_NULL), 
							  ("destination", SQL_TYPE_NULL | SQL_TYPE_INT), 
							  ("no_system", SQL_TYPE_NULL | SQL_TYPE_INT), 
							  ("visibility", SQL_TYPE_INT | SQL_TYPE_NULL), 
							  ("control", SQL_TYPE_INT | SQL_TYPE_NULL), 
							  ("status", SQL_TYPE_NULL | SQL_TYPE_INT), 
							  ("numfailed", SQL_TYPE_NULL | SQL_TYPE_INT), 
							  ("lastmod", SQL_TYPE_INT | SQL_TYPE_NULL), 
							  ("notificationpackage", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
							  ("notificationclass", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
							  ("notificationextras", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
							  ("cookiedata", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
							  ("useragent", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
							  ("referer", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
							  ("total_bytes", SQL_TYPE_INT | SQL_TYPE_NULL), 
							  ("current_bytes", SQL_TYPE_NULL | SQL_TYPE_INT), 
							  ("etag", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
							  ("uid", SQL_TYPE_INT | SQL_TYPE_NULL), 
							  ("otheruid", SQL_TYPE_INT | SQL_TYPE_NULL), 
							  ("title", SQL_TYPE_TEXT | SQL_TYPE_NULL), 
							  ("description", SQL_TYPE_NULL | SQL_TYPE_TEXT), 
							  ("scanned", SQL_TYPE_NULL | SQL_TYPE_TEXT));
						   
templates = {"MMSSMS.DB-sms": smsTemplate, 
			"CONTACTS2.DB-calls": callsTemplate, 
			"MAILSTORE.*@GMAIL.COM.DB-messages": gmailMsgTemplate,
			"CONTACTS2.DB-data": contactsDataTemplate,
			"CONTACTS2.DB-raw_contacts": contactsRContactsTemplate,
			"BROWSER.DB-bookmarks": browserBookmarksTemplate,
			"WEBVIEW.DB-password": webviewPasswordTemplate, 
			"WEBVIEW.DB-httpauth": webviewHttpAuthTemplate,
			"DA_DESTINATION_HISTORY-destination_history":destinationHistoryTemplate,
			"SEARCH_HISTORY.DB-history":mapsSearchHistoryTemplate,
			"SEARCH_HISTORY.DB-suggestions":mapsSuggestionTemplate, 
			"TALK.DB-messages":talkMessagesTemplate, 
			"TALK.DB-contacts":talkContactsTemplate,
			"CACHEDPOSITIONS.DB-cachedpositions": browserCachedPositionsTemplate, 
			"DOWNLOADS.DB-downloads":downloadsDownloadsTemplate
			};

primKeyPositions = {"MMSSMS.DB-sms": 0, 
			"CONTACTS2.DB-calls": 0, 
			"MAILSTORE.*@GMAIL.COM.DB-messages": 0,
			"CONTACTS2.DB-data": 0,
			"CONTACTS2.DB-raw_contacts": 0, 
			"BROWSER.DB-bookmarks": 0,
			"WEBVIEW.DB-password": 0, 
			"WEBVIEW.DB-httpauth": 0,
			"DA_DESTINATION_HISTORY-destination_history":0,
			"SEARCH_HISTORY.DB-history":0,
			"SEARCH_HISTORY.DB-suggestions":0,
			"TALK.DB-messages":0,
			"TALK.DB-contacts":0, 
			"CACHEDPOSITIONS.DB-cachedpositions":-1, 
			"DOWNLOADS.DB-downloads":0
			};
