let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/repos/finance-app/backend
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +109 ~/repos/finance-app/backend/README.md
badd +1 ~/repos/finance-app/backend/tests/api/routes/__init__.py
badd +15 ~/repos/finance-app/backend/tests/api/routes/test_items.py
badd +2 ~/repos/finance-app/backend/tests/api/routes/test_login.py
badd +1 ~/repos/finance-app/backend/tests/api/routes/test_private.py
badd +1 ~/repos/finance-app/backend/tests/api/__init__.py
badd +15 ~/repos/finance-app/backend/tests/crud/test_user.py
badd +68 ~/repos/finance-app/backend/app/crud.py
badd +1 ~/repos/finance-app/backend/app/initial_data.py
badd +1 ~/repos/finance-app/backend/app/main.py
badd +106 ~/repos/finance-app/backend/app/models.py
badd +1 ~/repos/finance-app/backend/app/tests_pre_start.py
badd +116 ~/repos/finance-app/backend/app/utils.py
badd +1 ~/repos/finance-app/backend/app/core/__init__.py
badd +119 ~/repos/finance-app/backend/app/core/config.py
badd +1 ~/repos/finance-app/.venv/lib/python3.12/site-packages/pydantic/networks.py
badd +1 app/api/routes/items.py
badd +36 ~/repos/finance-app/backend/app/core/security.py
badd +57 ~/repos/finance-app/backend/app/api/deps.py
argglobal
%argdel
$argadd .
edit app/api/routes/items.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 14 + 91) / 183)
exe 'vert 2resize ' . ((&columns * 168 + 91) / 183)
argglobal
enew
setlocal foldmethod=manual
setlocal foldexpr=0
setlocal foldmarker={{{,}}}
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldenable
wincmd w
argglobal
balt ~/repos/finance-app/backend/app/models.py
setlocal foldmethod=manual
setlocal foldexpr=0
setlocal foldmarker={{{,}}}
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldenable
silent! normal! zE
let &fdl = &fdl
let s:l = 1 - ((0 * winheight(0) + 23) / 47)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 05|
wincmd w
2wincmd w
exe 'vert 1resize ' . ((&columns * 14 + 91) / 183)
exe 'vert 2resize ' . ((&columns * 168 + 91) / 183)
tabnext 1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let &winminheight = s:save_winminheight
let &winminwidth = s:save_winminwidth
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
set hlsearch
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
