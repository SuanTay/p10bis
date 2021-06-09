#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""
    # app :  Fly_me_bot, flymebot
    PORT = 3979
    APP_ID = "9cd88225-f5d8-4ef0-af35-28cb24f3c735"
    APP_PASSWORD = "*O!R|z8fKX7b%!;_iG$&^nWZ[hSyx"
    LUIS_APP_ID = "b2d6732c-ebad-44f7-b3d3-acc41d969ee3"
    LUIS_API_KEY = "27c8037609e64e908a3cc829433e4437" # Authoring key
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = "westeurope.api.cognitive.microsoft.com"
    APPINSIGHTS_INSTRUMENTATION_KEY ="a3f1f698-5b10-4d5b-966d-0a2fa2006c3c"
    
