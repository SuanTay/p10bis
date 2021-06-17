#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""
    # app :  Fly_me_bot, flymebot
    HOST = os.environ.get("host", 'localhost' )
    PORT  = os.environ.get("port", 3979 )
    APP_ID = os.environ.get("MicrosoftAppId", "7edb707a-eaf5-4a2b-ae9a-440bc2aa9f10") #'096751a9-801e-49c6-bd72-7d35d9d21973' # 
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "wj6f?f%+kB.%(Qj71jUIE{yP>54w>oD") # '16e2ffe5-ce56-4da8-8190-bd8cab2386c2' # 
    LUIS_APP_ID  = os.environ.get("LuisAppId", "bf408bed-468d-4d08-aafd-77e84acd9643")
    LUIS_API_KEY  =os.environ.get("LuisApiKey", "27c8037609e64e908a3cc829433e4437" ) # Authoring key
    LUIS_API_HOST_NAME = os.environ.get("LuisApiHost", "luisflyme02-authoring.cognitiveservices.azure.com") # "westeurope.api.cognitive.microsoft.com"
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get("AppInsights", "27c57565-05cf-4019-9657-9b8b1142693d")
    