# AUTOGENERATED! DO NOT EDIT! File to edit: ../01_components.ipynb.

# %% auto 0
__all__ = ['picocss', 'picolink', 'picocondcss', 'picocondlink', 'named', 'html_attrs', 'hx_attrs', 'show', 'set_pico_cls',
           'xt_html', 'xt_hx', 'A', 'AX', 'Checkbox', 'Card', 'Group', 'Search', 'Grid', 'DialogX', 'Hidden', 'set_val',
           'find_inps', 'fill_form', 'fill_dataclass', 'find_elems', 'Html', 'Head', 'Title', 'Meta', 'Link', 'Style',
           'Body', 'Pre', 'Code', 'Div', 'Span', 'P', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'Strong', 'Em', 'B', 'I', 'U',
           'S', 'Strike', 'Sub', 'Sup', 'Hr', 'Br', 'Img', 'Nav', 'Ul', 'Ol', 'Li', 'Dl', 'Dt', 'Dd', 'Table', 'Thead',
           'Tbody', 'Tfoot', 'Tr', 'Th', 'Td', 'Caption', 'Col', 'Colgroup', 'Form', 'Input', 'Textarea', 'Button',
           'Select', 'Option', 'Label', 'Fieldset', 'Legend', 'Details', 'Dialog', 'Summary', 'Main', 'Header',
           'Footer', 'Section', 'Article', 'Aside', 'Figure', 'Figcaption', 'Mark', 'Small', 'Iframe', 'Object',
           'Embed', 'Param', 'Video', 'Audio', 'Source', 'Canvas', 'Svg', 'Math', 'Script', 'Noscript', 'Template',
           'Slot']

# %% ../01_components.ipynb 2
from html.parser import HTMLParser
from dataclasses import dataclass, asdict

from fastcore.utils import *
from fastcore.xml import *
from fastcore.meta import use_kwargs, delegates

try: from IPython import display
except ImportError: display=None

# %% ../01_components.ipynb 4
def show(xt,*rest):
    if rest: xt = (xt,)+rest
    return display.HTML(to_xml(xt))

# %% ../01_components.ipynb 5
picocss = "https://cdn.jsdelivr.net/npm/@picocss/pico@latest/css/pico.min.css"
picolink = Link(rel="stylesheet", href=picocss)
picocondcss = "https://cdn.jsdelivr.net/npm/@picocss/pico@latest/css/pico.conditional.min.css"
picocondlink = Link(rel="stylesheet", href=picocondcss)

# %% ../01_components.ipynb 8
def set_pico_cls():
    js = """var sel = '.cell-output, .output_area';
document.querySelectorAll(sel).forEach(e => e.classList.add('pico'));

new MutationObserver(ms => {
  ms.forEach(m => {
    m.addedNodes.forEach(n => {
      if (n.nodeType === 1) {
        var nc = n.classList;
        if (nc && (nc.contains('cell-output') || nc.contains('output_area'))) {
          nc.add('pico');
        }
        n.querySelectorAll(sel).forEach(e => e.classList.add('pico'));
      }
    });
  });
}).observe(document.body, { childList: true, subtree: true });"""
    return display.Javascript(js)

# %% ../01_components.ipynb 11
named = set('a button form frame iframe img input map meta object param select textarea'.split())
html_attrs = 'id cls title style'.split()
hx_attrs = 'get post put delete patch trigger target swap include select indicator push_url confirm disable replace_url on'
hx_attrs = html_attrs + [f'hx_{o}' for o in hx_attrs.split()]

# %% ../01_components.ipynb 12
@use_kwargs(html_attrs, keep=True)
def xt_html(tag: str, *c, **kwargs):
    tag,c,kw = xt(tag, *c, **kwargs)
    if tag in named and 'id' in kw and 'name' not in kw: kw['name'] = kw['id']
    return XT([tag,c,kw])

# %% ../01_components.ipynb 13
@use_kwargs(hx_attrs, keep=True)
def xt_hx(tag: str, *c, target_id=None, **kwargs):
    if target_id: kwargs['hx_target'] = '#'+target_id
    return xt_html(tag, *c, **kwargs)

# %% ../01_components.ipynb 14
_g = globals()
_all_ = ['Html', 'Head', 'Title', 'Meta', 'Link', 'Style', 'Body', 'Pre', 'Code',
    'Div', 'Span', 'P', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'Strong', 'Em', 'B',
    'I', 'U', 'S', 'Strike', 'Sub', 'Sup', 'Hr', 'Br', 'Img', 'Link', 'Nav',
    'Ul', 'Ol', 'Li', 'Dl', 'Dt', 'Dd', 'Table', 'Thead', 'Tbody', 'Tfoot', 'Tr',
    'Th', 'Td', 'Caption', 'Col', 'Colgroup', 'Form', 'Input', 'Textarea',
    'Button', 'Select', 'Option', 'Label', 'Fieldset', 'Legend', 'Details', 'Dialog',
    'Summary', 'Main', 'Header', 'Footer', 'Section', 'Article', 'Aside', 'Figure',
    'Figcaption', 'Mark', 'Small', 'Iframe', 'Object', 'Embed', 'Param', 'Video',
    'Audio', 'Source', 'Canvas', 'Svg', 'Math', 'Script', 'Noscript', 'Template', 'Slot']

for o in _all_: _g[o] = partial(xt_hx, o.lower())

# %% ../01_components.ipynb 17
@delegates(xt_hx, keep=True)
def A(*c, hx_get=None, target_id=None, hx_swap=None, href='#', **kwargs):
    return xt_hx('a', *c, href=href, hx_get=hx_get, target_id=target_id, hx_swap=hx_swap, **kwargs)

# %% ../01_components.ipynb 19
@delegates(xt_hx, keep=True)
def AX(txt, hx_get=None, target_id=None, hx_swap=None, href='#', **kwargs):
    return xt_hx('a', txt, href=href, hx_get=hx_get, target_id=target_id, hx_swap=hx_swap, **kwargs)

# %% ../01_components.ipynb 21
@delegates(xt_hx, keep=True)
def Checkbox(checked:bool=False, label=None, **kwargs):
    if not checked: checked=None
    res = Input(type="checkbox", checked=checked, **kwargs)
    if label: res = Label(res, label)
    return res

# %% ../01_components.ipynb 23
@delegates(xt_hx, keep=True)
def Card(*c, header=None, footer=None, **kwargs):
    if header: c = (Header(header),) + c
    if footer: c += (Footer(footer),)
    return Article(*c, **kwargs)

# %% ../01_components.ipynb 25
@delegates(xt_hx, keep=True)
def Group(*c, **kwargs):
    return Fieldset(*c, role="group", **kwargs)

# %% ../01_components.ipynb 27
@delegates(xt_hx, keep=True)
def Search(*c, **kwargs):
    return Form(*c, role="search", **kwargs)

# %% ../01_components.ipynb 29
@delegates(xt_hx, keep=True)
def Grid(*c, cls='grid', **kwargs):
    c = tuple(o if isinstance(o,list) else Div(o) for o in c)
    return xt_hx('div', *c, cls=cls, **kwargs)

# %% ../01_components.ipynb 31
@delegates(xt_hx, keep=True)
def DialogX(*c, open=None, header=None, footer=None, id=None, **kwargs):
    card = Card(*c, header=header, footer=footer, **kwargs)
    return Dialog(card, open=open, id=id)

# %% ../01_components.ipynb 33
@delegates(xt_hx, keep=True)
def Hidden(value:str="", **kwargs):
    return Input(type="hidden", value=value, **kwargs)

# %% ../01_components.ipynb 34
def set_val(tag, attr, val):
    if attr.get('type', '') in ('checkbox','radio'):
        if val: attr['checked'] = '1'
        else: attr.pop('checked', '')
    else: attr['value'] = val

# %% ../01_components.ipynb 35
def find_inps(html):
    if not html: return []
    tag,cs,attrs = html
    if tag == 'input': return [html]
    res = []
    for c in cs:
        if isinstance(c, list): res.extend(find_inps(c))
    return res

# %% ../01_components.ipynb 36
def fill_form(form, obj):
    "Modifies form in-place and returns it"
    inps = find_inps(form)
    inps = {attrs['id']:(tag,attrs) for tag,c,attrs in inps if 'id' in attrs}
    for nm,val in asdict(obj).items():
        if nm in inps:
            tag,attr = inps[nm]
            set_val(tag, attr, val)
    return form

# %% ../01_components.ipynb 38
def fill_dataclass(src, dest):
    "Modifies dataclass in-place and returns it"
    for nm,val in asdict(src).items(): setattr(dest, nm, val)
    return dest

# %% ../01_components.ipynb 40
class _FindElems(HTMLParser):
    def __init__(self, tag=None, attr=None, **props):
        super().__init__()
        self.tag,self.attr,self.props = tag,attr,props
        self.res = []

    def handle_starttag(self, tag, attrs):
        if self.tag and tag!=self.tag: return
        d = dict(attrs)
        if [k for k,v in self.props.items() if d.get(k,None)==v]:
            self.res.append(d.get(self.attr, None) if self.attr else d)

# %% ../01_components.ipynb 41
def find_elems(s:XT|str, tag=None, attr=None, **props):
    "Find elements in `s` with `tag` (if supplied) and `props`, returning `attr`"
    o = _FindElems(tag, attr, **props)
    o.feed(to_xml(s))
    return o.res
