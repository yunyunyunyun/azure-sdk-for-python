# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Location(Model):
    """
    Location information.

    :param str id: Gets or sets the ID of the resource
     (/subscriptions/SubscriptionId).
    :param str subscription_id: Gets or sets the subscription Id.
    :param str name: Gets or sets the location name
    :param str display_name: Gets or sets the display name of the location
    :param str latitude: Gets or sets the latitude of the location
    :param str longitude: Gets or sets the longitude of the location
    """

    _required = []

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'latitude': {'key': 'latitude', 'type': 'str'},
        'longitude': {'key': 'longitude', 'type': 'str'},
    }

    def __init__(self, id=None, subscription_id=None, name=None, display_name=None, latitude=None, longitude=None):
        self.id = id
        self.subscription_id = subscription_id
        self.name = name
        self.display_name = display_name
        self.latitude = latitude
        self.longitude = longitude
