# -*- coding: utf-8 -*- #
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The command group for the Access Context Manager CLI."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class AccessContextManagerAlpha(base.Group):
  """Manage Access Context Manager resources.

  Policy API for configuring context aware access features and access zones.
  """


@base.ReleaseTracks(base.ReleaseTrack.BETA)
class AccessContextManagerBeta(base.Group):
  """Manage Access Context Manager resources.

  Policy API for configuring context aware access features and access zones.
  """
