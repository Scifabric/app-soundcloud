# -*- coding: utf-8 -*-

# This file is part of PyBOSSA.
#
# PyBOSSA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBOSSA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBOSSA.  If not, see <http://www.gnu.org/licenses/>.


import soundcloud


def get_soundcloud_clips():
    """
    Gets public soundcloud clips
    """
    client = soundcloud.Client(client_id="APP-KEY")
    #tracks = client.get('/tracks', tags='hip-hop, pop, rock', license='cc-by-sa')
    tracks = client.get('/tracks', tags='hip-hop, pop, rock')
    html = []
    n = 0
    for t in tracks:
        if n < 10:
            print t.permalink_url
            e = client.get('/oembed', url=t.permalink_url)
            html.append(e.html)
            n = n + 1;
        else:
            break
    return html
