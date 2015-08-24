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
import config
import json


def get_soundcloud_clips():
    """
    Gets public soundcloud clips
    """
    client = soundcloud.Client(client_id=config.client_id)
    #tracks = client.get('/tracks', tags='hip-hop, pop, rock', license='cc-by-sa')
    tracks = client.get('/tracks', tags='hip-hop, pop, rock')
    tasks = []
    n = 0
    for t in tracks:
        if n < 10:
            e = client.get('/oembed', url=t.permalink_url)
            task_info = {'question': 'Is this a hip-hop song?', 'embed': e.html}
            tasks.append(dict(info=task_info))
            n = n + 1
        else:
            break
    return tasks


if __name__ == '__main__':
    file = open('soundcloud_tasks.json', 'w')
    clips = get_soundcloud_clips()
    file.write(json.dumps(clips))
    file.close()
