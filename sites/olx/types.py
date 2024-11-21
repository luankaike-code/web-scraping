from typing import TypedDict, Literal

type UFs = Literal['', 'ac',	'al',	'ap',	'am',	'ba',	'ce',	'df',	'es',	'go',	'ma',	'mt',	'ms',	'mg',	'pa',	'pb',	'pr',	'pe',	'pi',	'rj',	'rn',	'rs',	'ro',	'rr',	'sc',	'sp',	'se',	'to']
type CategorysOlx = Literal['', 'imoveis']

class XPaths:
	btn_view_grid = '//*[@id="main-content"]/div[5]/div/div[2]/button[2]',
	items_conteiner = '//*[@id="main-content"]/div[7]'

class ParamsUrlOlx(TypedDict):
	f: Literal[None, 'p', 'c']
	ps: None | int
	pe: None | int
	sf: Literal[None, 1]
	sp: Literal[None, 1, 5]