# ISC License
# Copyright (c) 2018, obermann
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.


import eg


eg.RegisterPlugin(
	name = "Skaitvardis",
	author = "obermann",
	version = "1.0.1",
	kind = "other",
	canMultiLoad = True,
	description = (
		"Plugin for spelling numbers in Lithuanian."
	),
	url="https://github.com/obermann/SkaitvardisPlugin",
	guid="{1A0AC1A1-7E02-40FE-AB2C-9DF9845EBC00}"
)


import skaitvardisplius


class SkaitvardisPlugin(eg.PluginClass):
	def __init__(self):
		self.AddAction(Spell)


class Spell(eg.ActionBase):
	name = "Spell Number in Lithuanian"
	description = "Spell the integer, float, fraction (str of numerator/denumerator) number in Lithuanian."
	def __call__(self,
		group="CARDINAL",
		gender="MASCULINE",
		number="SINGULAR",
		case="NOMINATIVE"
		):
		return " ".join(skaitvardisplius.spellUnit(eg.result, set([
			getattr(skaitvardisplius.M, group),
			getattr(skaitvardisplius.M, gender),
			getattr(skaitvardisplius.M, number),
			getattr(skaitvardisplius.M, case)
			])))

	def Configure(self,
		group="CARDINAL",
		gender="MASCULINE",
		number="SINGULAR",
		case="NOMINATIVE"
		):
		argnames=["group", "gender", "number", "case"]
		lists=[[skaitvardisplius.M.getName(i) for i in sorted(getattr(skaitvardisplius, k.capitalize()).toList(), reverse=True)] for k in argnames]
		values=[lists[i].index(locals()[argnames[i]]) for i in range(len(argnames))]
		panel = eg.ConfigPanel()
		windows=[panel.Choice(values[i], lists[i]) for i in range(len(argnames))]
		eg.EqualizeWidths(windows)
		for i in windows: panel.AddCtrl(i)
		while panel.Affirmed():
			panel.SetResult(*[i.GetString(i.GetValue()) for i in windows])

