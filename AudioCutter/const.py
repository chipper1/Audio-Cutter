"""
Your favorite Audio Cutter.
Author : Bilal Elmoussaoui (bil.elmoussaoui@gmail.com)
Artist : Alfredo Hernández
Website : https://github.com/bil-elmoussaoui/Audio-Cutter
Licence : The script is released under GPL, uses a modified script
     form Chromium project released under BSD license
This file is part of AudioCutter.
AudioCutter is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
AudioCutter is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with AudioCutter. If not, see <http://www.gnu.org/licenses/>.
"""

from gettext import gettext as _

AUDIO_MIMES = {
    "audio/ogg": _("OGG Audio"),
    "audio/midi": _("MIDI"),
    "audio/x-wav": _("Waveform Audio Format"),
    "audio/aac": _("AAC Audio"),
    "audio/mpeg": _("MP3 Audio"),
    "audio/3gpp": _("3GPP Audio Container"),
    "audio/3gpp2": _("3GPP2 Audio Container"),
    "audio/webm": _("WEBM Audio")
}
