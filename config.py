#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""
    # app :  Fly_me_bot, flymebot
    PORT  = os.environ.get("port", 3979 )
    APP_ID = os.environ.get("MicrosoftAppId", "7edb707a-eaf5-4a2b-ae9a-440bc2aa9f10")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "wj6f?f%+kB.%(Qj71jUIE{yP>54w>oD")
    LUIS_APP_ID  = os.environ.get("LuisAppId", "22dace73-c035-4def-a5c0-072306b41258")
    LUIS_API_KEY  = os.environ.get("LuisApiKey", "27c8037609e64e908a3cc829433e4437" ) # Authoring key
    LUIS_API_HOST_NAME ="https://luisflyme02-authoring.cognitiveservices.azure.com/" # "westeurope.api.cognitive.microsoft.com"
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get("AppInsights", "9e7124b9-929c-40a4-8dcf-59cb037148ef")
    
